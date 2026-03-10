import google.generativeai as genai

API_KEY = "AIzaSyBK0mtPEDtdtBF7voTlk4I-iXmO12DmBvU"

def refresh_model():
    if API_KEY:
        genai.configure(api_key=API_KEY)

        try:
            model = genai.GenerativeModel("models/gemini-flash-latest")
        except:
            model = genai.GenerativeModel("models/gemini-pro-latest")
    else:
        model = None
    return model
def generate_message(context):
    model = refresh_model()
    try:
        if model is None:
            return "AI not configured (no API key)."

        response = model.generate_content(
            f"User gesture: {context}. Reply in one short friendly sentence, only reply for current gesture."
        )

        return response.text.strip()

    except Exception as e:
        return "AI error: " + str(e)
