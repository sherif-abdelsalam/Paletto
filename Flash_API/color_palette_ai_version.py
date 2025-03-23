import google.generativeai as genai
import os
genai.configure(api_key=os.getenv("gemini_api_key"))
def generate_response(input_string: str) -> str:
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(input_string)
    return response.text