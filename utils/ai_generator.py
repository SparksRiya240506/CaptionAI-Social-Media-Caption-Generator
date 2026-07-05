import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_content(description, platform, tone):

    prompt = f"""
You are a professional social media marketing expert.

Generate:

1. Three unique captions for {platform}.
2. Ten relevant hashtags.
3. Three call-to-action phrases.

Description:
{description}

Tone:
{tone}

Return the output exactly in this format:

CAPTIONS:
1.
2.
3.

HASHTAGS:
#tag1 #tag2 #tag3

CTAS:
1.
2.
3.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content

    captions = ""
    hashtags = ""
    ctas = ""

    current_section = None

    for line in content.split("\n"):

        line = line.strip()

        if "CAPTIONS" in line.upper():
            current_section = "captions"
            continue

        elif "HASHTAGS" in line.upper():
            current_section = "hashtags"
            continue

        elif "CTAS" in line.upper():
            current_section = "ctas"
            continue

        if current_section == "captions":
            captions += line + "\n"

        elif current_section == "hashtags":
            hashtags += line + "\n"

        elif current_section == "ctas":
            ctas += line + "\n"

    return captions, hashtags, ctas