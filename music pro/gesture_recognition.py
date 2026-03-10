def count_fingers(hand_landmarks):
    tips = [4, 8, 12, 16, 20]
    fingers = []

    # thumb
    fingers.append(
        hand_landmarks.landmark[tips[0]].x <
        hand_landmarks.landmark[tips[0] - 1].x
    )

    # other fingers
    for i in range(1, 5):
        fingers.append(
            hand_landmarks.landmark[tips[i]].y <
            hand_landmarks.landmark[tips[i] - 2].y
        )

    return fingers
