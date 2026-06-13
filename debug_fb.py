import requests

def check_fb():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    res = requests.get("https://www.facebook.com/marketplace/search?query=macbook", headers=headers)
    
    html = res.text
    if "/marketplace/item/" in html:
        print("FOUND: /marketplace/item/")
    else:
        print("NOT FOUND: /marketplace/item/")
        print("Found marketplace links:", [line for line in html.split('"') if "/marketplace" in line][:10])

if __name__ == "__main__":
    check_fb()
