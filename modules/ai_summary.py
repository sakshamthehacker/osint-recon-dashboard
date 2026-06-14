import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def summarize_findings(data):
    prompt = f"""You are a cybersecurity analyst reviewing OSINT scan results for a domain.
Here is the raw data collected:

{data}

Based on this data, provide:
1. A short summary (2-3 sentences) of this target's digital footprint.
2. Any potential security risks or concerns you notice (e.g. exposed subdomains, expiring domain, breached email, unusual DNS entries). List as bullet points.
3. An overall risk score from 1 (very low risk) to 10 (very high risk), with one sentence justifying the score.

Keep the entire response concise and well-organized with clear headings."""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text


if __name__ == "__main__":
    sample_data = {
        "domain": "example.com",
        "whois": {"registrar": "Example Registrar", "expiration_date": "2024-01-01"},
        "subdomains": ["mail.example.com", "admin.example.com", "test.example.com"],
        "breach_check": {"breached": True, "breach_count": 3}
    }
    print(summarize_findings(sample_data))