import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# read .env file
load_dotenv()

# OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# AI instructions
SYSTEM_PROMPT = """
You are a cinematic short video script writer.

Return ONLY valid JSON.

Format:
{
  "title": "Video Title",
  "scenes": [
    {
      "narration": "Narration text",
      "visual_prompt": "Detailed cinematic image description",
      "duration_sec": 5
    }
  ]
}

Rules:
- Create exactly 4 scenes
- Make narration emotional and cinematic
- Make visual prompts detailed
- Total duration around 30 seconds
"""

# function
def generate_script(prompt: str):

    response = client.chat.completions.create(

        model="openai/gpt-3.5-turbo",

        response_format={"type": "json_object"},

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content

    content = content.replace("```json", "")
    content = content.replace("```", "")

    content = content.strip()

    script_data = json.loads(content)

    return script_data