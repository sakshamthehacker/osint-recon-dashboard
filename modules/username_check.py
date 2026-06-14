import requests

def check_username(username):
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "X (Twitter)": f"https://x.com/{username}"
    }

    results = {}
    headers = {"User-Agent": "Mozilla/5.0"}

    for platform, url in platforms.items():
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                results[platform] = {"exists": True, "url": url}
            else:
                results[platform] = {"exists": False, "url": url}
        except Exception as e:
            results[platform] = {"exists": "error", "error": str(e)}

    return results


if __name__ == "__main__":
    for platform, info in check_username("github").items():
        print(f"{platform}: {info}")