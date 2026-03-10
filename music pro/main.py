import cv2
import mediapipe as mp
import time

from gesture_recognition import count_fingers
from music_controller import perform_action
from ai_generator import generate_message

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

last_display_text = ""
display_timer = 0

last_ai_time = 0
AI_COOLDOWN = 4      # prevents 429
AI_COOLDOWN_SKIP=2  # faster for skip adjustments

# prevents repeating the same gesture while hand is held
gesture_locked = False
vol_locked = False
# gesture smoothing (must be stable for a bit)
stable_gesture = None
stable_frames = 0
REQUIRED_STABLE_FRAMES = 6     # ~0.2–0.3 seconds


while True:
    ok, img = cap.read()
    if not ok:
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            fingers = count_fingers(hand_landmarks)
            total = fingers.count(True)
            now = time.time()

            # ---- stability filter ----
            if total == stable_gesture:
                stable_frames += 1
            else:
                stable_gesture = total
                stable_frames = 0

            if stable_frames < REQUIRED_STABLE_FRAMES:
                continue

            # ---- only trigger once until hand leaves ----
            if not gesture_locked:

                # PLAY
                if total == 5:
                    perform_action("PLAY")
                    gesture_locked = True

                    if now - last_ai_time > AI_COOLDOWN:
                        try:
                            last_display_text = generate_message("play music")
                        except:
                            last_display_text = "AI busy — continuing manually"
                        last_ai_time = now

                # PAUSE
                elif total == 0:
                    perform_action("PAUSE")
                    gesture_locked = True

                    if now - last_ai_time > AI_COOLDOWN:
                        try:
                            last_display_text = generate_message("pause music")
                        except:
                            last_display_text = "AI busy — continuing manually"
                        last_ai_time = now

                # NEXT
                elif total == 1:
                    perform_action("NEXT")
                    gesture_locked = True

                    if now - last_ai_time > AI_COOLDOWN_SKIP:
                        try:
                            last_display_text = generate_message("next song")
                        except:
                            last_display_text = "AI busy — continuing manually"
                        last_ai_time = now

                # PREVIOUS
                elif total == 2:
                    perform_action("PREVIOUS")
                    gesture_locked = True

                    if now - last_ai_time > AI_COOLDOWN_SKIP:
                        try:
                            last_display_text = generate_message("previous song")
                        except:
                            last_display_text = "AI busy — continuing manually"
                        last_ai_time = now

                # VOLUME UP (continuous)
                elif total == 3:
                    perform_action("VOL_UP")


                    if now - last_ai_time > AI_COOLDOWN and not vol_locked:
                        try:
                            last_display_text = generate_message("Volume Up")
                        except:
                            last_display_text = "AI busy — continuing manually"
                        last_ai_time = now
                        vol_locked = True

                # VOLUME DOWN (continuous)
                elif total == 4:
                    perform_action("VOL_DOWN")
                    

                    if now - last_ai_time > AI_COOLDOWN and not vol_locked:
                        try:
                            last_display_text = generate_message("Volume Down")
                        except:
                            last_display_text = "AI busy — continuing manually"
                        last_ai_time = now
                        vol_locked = True

                display_timer = 1000

    else:
        # hand removed -> unlock new gestures
        gesture_locked = False
        stable_gesture = None
        vol_locked=False
        stable_frames = 0

    # ---- AI banner ----
    if display_timer > 0:
        cv2.rectangle(img, (0, 0), (640, 60), (0, 0, 0), -1)
        cv2.putText(img, last_display_text, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        display_timer -= 1

    cv2.imshow("Gesture Music Controller", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
