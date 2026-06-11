from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://www.facebook.com/login")
    
    print(">>> Login FB manual di browser yang muncul")
    print(">>> Setelah login berhasil, balik ke terminal ini dan tekan ENTER")
    input()
    
    context.storage_state(path="session.json")
    print(">>> session.json tersimpan!")
    
    browser.close()
