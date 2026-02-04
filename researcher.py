import os
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import SYSTEM_INSTRUCTION

# Load environment variables from .env
load_dotenv()

# FIX: In the new google-genai SDK, timeouts are set in HttpOptions during Client init.
# Note: Timeout is in milliseconds (600,000ms = 10 minutes).
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options=types.HttpOptions(timeout=600000) 
)

def generate_executive_brief(topic="Major AI market shifts in the last 24 hours"):
    print(f"🔍 Lighthouse 3 is investigating: {topic}...")
    
    model_id = "gemini-3-pro-preview"
    
    try:
        # We removed the 'request_options' from here to fix the AttributeError
        response = client.models.generate_content(
            model=model_id,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                tools=[types.Tool(google_search=types.GoogleSearch())],
                thinking_config=types.ThinkingConfig(
                    thinking_level=types.ThinkingLevel.HIGH,
                    include_thoughts=True 
                ),
                temperature=1.0
            ),
            contents=topic
        )
        return response
    except Exception as e:
        print(f"❌ API Error: {e}")
        return None

def save_report_to_md(result, topic):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    filename = f"brief_{timestamp}.md"
    
    print(f"💾 Saving report to {filename}...")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# 🗼 Lighthouse 3: Strategy Briefing\n")
        f.write(f"**Research Topic:** {topic}\n")
        f.write(f"**Generated on:** {datetime.now().strftime('%B %d, %Y at %I:%M %p')}\n\n")
        f.write("---\n\n")
        f.write(result.text)
        f.write("\n\n---\n## 🧠 INTERNAL REASONING (THOUGHT SIGNATURE)\n")
        
        found_thoughts = False
        for part in result.candidates[0].content.parts:
            if part.thought:
                f.write(f"{part.text}\n\n")
                found_thoughts = True
        
        if not found_thoughts:
            f.write("No internal reasoning was returned for this specific hunt.")
            
    print(f"✅ Success! Report exported.")

if __name__ == "__main__":
    current_topic = "Major AI market shifts in the last 24 hours"
    result = generate_executive_brief(current_topic)
    
    if result:
        save_report_to_md(result, current_topic)
    else:
        print("Failed to generate report.")