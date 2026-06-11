from playwright.sync_api import sync_playwright
import time

# Ambil satu URL listing dari hasil sebelumnya
TEST_URL = "https://www.facebook.com/marketplace/item/1015507104578372/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state="session.json")
    page = context.new_page()
    
    page.goto(TEST_URL, wait_until="domcontentloaded")
    time.sleep(5)  # tunggu lebih lama
    
    # Dump semua h1, h2 yang ada
    print("=== H1 ===")
    for el in page.query_selector_all("h1"):
        print(repr(el.inner_text().strip()))
    
    print("\n=== Links /user/ atau /profile ===")
    for el in page.query_selector_all("a[href*='/user/'], a[href*='/profile.php']"):
        href = el.get_attribute("href")
        text = el.inner_text().strip()[:60]
        print(f"  href={href[:60]} | text={repr(text)}")
    
    print("\n=== Spans dengan Rp ===")
    for el in page.query_selector_all("span"):
        txt = el.inner_text().strip()
        if txt.startswith("Rp"):
            print(repr(txt))
            break
    
    input("\n>>> Tekan ENTER untuk tutup...")
    browser.close()
