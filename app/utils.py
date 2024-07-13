import openai
from reportlab.pdfgen import canvas
from flask import current_app
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_recommendations(user):
    prompt = f"""
    I have a user profile with the following details:
    Name: {user.name}
    Age: {user.age}
    Profession: {user.profession}
    Goals: {user.goals}
    Interests: {user.interests}
    Time Frame: {user.time_frame}

    Based on this profile, please provide personalized life recommendations for the next {user.time_frame}.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    recommendations = response.choices[0].message['content'].strip().split('\n')
    return recommendations

def generate_pdf(user, recommendations):
    pdf_path = f"{user.name}_recommendations.pdf"
    c = canvas.Canvas(pdf_path)
    c.drawString(100, 750, "Life Guide Report")
    c.drawString(100, 720, f"Name: {user.name}")
    c.drawString(100, 700, f"Age: {user.age}")
    c.drawString(100, 680, f"Profession: {user.profession}")
    c.drawString(100, 660, f"Goals: {user.goals}")
    c.drawString(100, 640, f"Interests: {user.interests}")
    c.drawString(100, 620, "Recommendations:")
    for i, rec in enumerate(recommendations, start=1):
        c.drawString(100, 600 - 20*i, f"{i}. {rec}")
    c.save()
    return pdf_path
