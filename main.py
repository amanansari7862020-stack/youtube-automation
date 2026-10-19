import os
import google.generativeai as genai
# Configure Gemini API Key from GitHub Secrets
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def generate_video_idea():
    model = genai.GenerativeModel("gemini-3.8-flash")
    response = model.generate_content("Give me a trendy faceless YouTube channel idea.")
    print("Video Idea:", response.text)

if __name__ == "__main__":
    generate_video_idea()
