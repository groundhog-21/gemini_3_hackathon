import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def inspect_video(youtube_url, query="Summarize the key technical breakthroughs shown in this video."):
    print(f"🎥 Lighthouse 3 is watching the video: {youtube_url}...")
    
    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        config=types.GenerateContentConfig(
            # Using 'LOW' thinking for speed, since the video is the context
            thinking_config=types.ThinkingConfig(thinking_level=types.ThinkingLevel.LOW),
            temperature=1.0
        ),
        contents=[
            types.Part.from_uri(file_uri=youtube_url, mime_type="video/mp4"),
            query
        ]
    )
    return response.text

if __name__ == "__main__":
    # Test with a known AI keynote or demo video
    test_url = "https://www.youtube.com/watch?v=HcyUUvxkykE" # Replace with a real AI demo!
    analysis = inspect_video(test_url)
    print("\n--- VIDEO ANALYSIS ---")
    print(analysis)