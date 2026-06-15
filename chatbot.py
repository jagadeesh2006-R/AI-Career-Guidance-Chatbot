from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def get_career_guidance(user_question):

    prompt = f"""
    You are an expert Career Counselor.

    Student Question:
    {user_question}

    Provide:

    1. Career Suggestions
    2. Required Skills
    3. Learning Roadmap
    4. Recommended Projects
    5. Certifications
    6. Interview Preparation Tips

    Give detailed and structured answers.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text