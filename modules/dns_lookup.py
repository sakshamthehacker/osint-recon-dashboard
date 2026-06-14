import dns.resolver

def get_dns_records(domain):
    records = {}
    record_types = ["A", "MX", "NS", "TXT"]

    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            records[rtype] = [str(rdata) for rdata in answers]
        except Exception as e:
            records[rtype] = f"No {rtype} record found or error: {e}"

    return records


if __name__ == "__main__":
    result = get_dns_records("google.com")
    for rtype, values in result.items():
        print(f"{rtype}: {values}")