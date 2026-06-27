import requests

def lookup_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    return response.json()

def main():
    ip = input("IP address (blank for your own): ").strip()
    data = lookup_ip(ip)
    if data.get("status") == "fail":
        print(f"Lookup failed: {data.get('message')}")
        return
    print(f"IP: {data['query']}")
    print(f"Country: {data['country']}")
    print(f"Region: {data['regionName']}")
    print(f"City: {data['city']}")
    print(f"ISP: {data['isp']}")

if __name__ == "__main__":
    main()
