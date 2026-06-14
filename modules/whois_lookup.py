import whois

def get_whois_info(domain):
    try:
        data = whois.whois(domain)

        # Detect if we got a real result or a useless disclaimer
        if data.registrar is None and data.creation_date is None:
            return {"domain": domain, "error": "No WHOIS data available for this domain (often happens with country-specific TLDs like .np)"}

        return {
            "domain": domain,
            "registrar": data.registrar,
            "creation_date": data.creation_date,
            "expiration_date": data.expiration_date,
            "name_servers": data.name_servers,
            "status": data.status
        }
    except Exception as e:
        return {"domain": domain, "error": str(e)}


if __name__ == "__main__":
    for d in ["google.com", "softwarica.edu.np", "thisdomaindoesnotexist12345.com"]:
        print(f"\n--- {d} ---")
        result = get_whois_info(d)
        for key, value in result.items():
            print(f"{key}: {value}")