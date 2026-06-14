# OSINT Recon Dashboard

An AI-powered OSINT (Open Source Intelligence) dashboard built with Python and Streamlit. Given a domain, it gathers publicly available intelligence — WHOIS records, DNS records, IP geolocation, subdomains, breach status, and username footprint — and uses Google's Gemini AI to generate a structured digital footprint summary and risk assessment.

## Features

- **WHOIS lookup** — registrar, creation/expiry dates, name servers
- **DNS records** — A, MX, NS, TXT records
- **IP & Geolocation** — resolves domain to IP and geolocates it
- **Subdomain enumeration** — via crt.sh certificate transparency logs
- **Breach check** — checks an email against known data breaches (via XposedOrNot, free API)
- **Username search** — checks for account existence across GitHub, Reddit, Instagram, X
- **AI risk assessment** — Gemini analyzes all collected data and produces a summary, risk flags, and a risk score (1-10)
- **Scan history** — all scans saved to a local SQLite database, viewable later

## Tech Stack

- Python 3
- Streamlit (dashboard UI)
- `python-whois`, `dnspython`, `requests` (data gathering)
- Google Gemini API (`google-genai`) for AI analysis
- SQLite (scan history storage)

## Setup & Running

1. Clone this repository.
2. Create a virtual environment and activate it:
python -m venv venv

venv\Scripts\activate
3. Install dependencies:
pip install -r requirements.txt
4. Create a `.env` file in the project root with:
GEMINI_API_KEY=your_key_here
   (Get a free key from https://aistudio.google.com)
5. Run the dashboard:
streamlit run app.py

## Project Structure
osint_dashboard/

├── app.py                  # Main Streamlit dashboard

├── modules/

│   ├── whois_lookup.py

│   ├── dns_lookup.py

│   ├── ip_lookup.py

│   ├── subdomain_lookup.py

│   ├── breach_check.py

│   ├── username_check.py

│   ├── ai_summary.py

│   └── db.py

├── requirements.txt

└── scan_history.db          # created automatically on first run

## Known Limitations

- **WHOIS coverage**: Country-code TLDs (e.g. `.np`) often return no WHOIS data, as the underlying `python-whois` library primarily supports gTLDs (`.com`, `.net`, `.org`). The dashboard detects and reports this clearly rather than failing.
- **crt.sh reliability**: The free crt.sh service used for subdomain enumeration occasionally times out under load, especially for high-traffic domains. This is handled gracefully with error messages.
- **Free-tier API limits**: Both the breach-check API (XposedOrNot) and Gemini API are used on free tiers, which have rate limits suitable for individual/educational use but not high-volume production use.

## Ethical Use & Legal Considerations

This tool is built strictly for **educational and authorized OSINT/reconnaissance purposes**, as part of a BSc Ethical Hacking & Cybersecurity coursework project. All data sources used (WHOIS, DNS, crt.sh, IP geolocation, breach databases) are **publicly accessible** and do not require unauthorized access to any system.

Key considerations:
- **No active exploitation**: This tool performs only passive reconnaissance — it does not scan, probe, or attempt to access any target system.
- **Privacy awareness**: The breach-check and username-search features process user-supplied identifiers (emails/usernames). Users should only check identifiers they own or have explicit permission to investigate, in line with the Computer Misuse Act 1990 and GDPR/Data Protection Act 2018 principles around lawful processing of personal data.
- **Responsible disclosure**: If this tool is ever used to identify a real security weakness (e.g. an exposed subdomain), findings should be reported responsibly to the affected organization, not exploited.
- **Intended audience**: Security researchers, students, and organizations conducting authorized assessments of their own digital footprint.

## Author

Saksham — BSc Ethical Hacking & Cybersecurity, Softwarica College (Coventry University), Semester 1 Project