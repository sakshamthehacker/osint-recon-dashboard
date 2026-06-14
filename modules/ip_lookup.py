import socket
import requests

def resolve_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except Exception as e:
        return f"Error: {e}"

def geolocate_ip(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        return response.json()
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    ip = resolve_ip("google.com")
    print(f"IP: {ip}")
    print(geolocate_ip(ip))