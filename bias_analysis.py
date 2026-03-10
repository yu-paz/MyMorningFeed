import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def analyze_bias(articles):
    # format headlines into a readable prompt
    headlines_text = ""
    for article in articles:
        source = article["source"]["name"]
        title = article["title"].split(" - ")[0]
        description = article["description"] or "No description available"
        headlines_text += f"Source: {source}\nHeadline: {title}\nSummary: {description}\n\n"

    prompt = f"""
    Below are news headlines and summaries from different sources covering today's top stories.
    
    {headlines_text}
    
    Please do the following:
    1. Identify the 2-3 biggest stories covered across multiple sources
    2. For each story compare how different sources framed it
    3. try to make a conclusion about what is going on and the truth of the matter based on the information provided
    4. Note any major differences in tone, emphasis, or bias between sources
    
    Keep the analysis concise, clear, and factual.
    """

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content