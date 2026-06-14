from modules.whois_lookup import get_whois_info
from modules.dns_lookup import get_dns_records
from modules.ip_lookup import resolve_ip, geolocate_ip

def run_report(domain):
    print(f"\n===== OSINT REPORT: {domain} =====\n")

    print("--- WHOIS ---")
    whois_data = get_whois_info(domain)
    for k, v in whois_data.items():
        print(f"{k}: {v}")

    print("\n--- DNS RECORDS ---")
    dns_data = get_dns_records(domain)
    for k, v in dns_data.items():
        print(f"{k}: {v}")

    print("\n--- IP & GEOLOCATION ---")
    ip = resolve_ip(domain)
    print(f"IP: {ip}")
    geo = geolocate_ip(ip)
    for k, v in geo.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    run_report("google.com")