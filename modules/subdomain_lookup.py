import requests

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=30)
        data = response.json()

        subdomains = set()
        for entry in data:
            name = entry.get("name_value", "")
            for line in name.split("\n"):
                subdomains.add(line.strip())

        return sorted(subdomains)
    except Exception as e:
        return [f"Error: {e}"]


if __name__ == "__main__":
    for sub in get_subdomains("softwarica.edu.np"):
        print(sub)