import requests

def check_breach(email):
    url = f"https://api.xposedornot.com/v1/check-email/{email}"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if "breaches" in data and data["breaches"]:
            breach_list = data["breaches"][0]  # unwrap the nested list
            return {"email": email, "breached": True, "breach_count": len(breach_list), "breaches": breach_list}
        else:
            return {"email": email, "breached": False, "breach_count": 0, "breaches": []}

    except Exception as e:
        return {"email": email, "error": str(e)}


if __name__ == "__main__":
    print(check_breach("test@example.com"))
    print(check_breach("thisisaveryrandomunlikelyemail12345@nowhere.com"))