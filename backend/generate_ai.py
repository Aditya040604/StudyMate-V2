import requests

def generate_response(prompt, api_key):
    """
    Sends a request to the Gemini AI API to generate a response.
    Args:
        text (str): Input text.
        api_key (str): Your Gemini AI API key.
    Returns:
        str: Generated response.
    """
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

