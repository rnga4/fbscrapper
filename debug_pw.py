from playwright.sync_api import sync_playwright
import os

def test_scrape():
    with sync_playwright() as p:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        session_path = os.path.join(current_dir, "session.json")
        
        browser = p.chromium.launch(headless=True)
        if os.path.exists(session_path):
            context = browser.new_context(storage_state=session_path)
        else:
            context = browser.new_context()
            
        page = context.new_page()
        page.goto("https://www.facebook.com/marketplace/search?query=macbook")
        page.wait_for_timeout(5000)
        
        html = page.content()
        with open("debug_page.html", "w", encoding="utf-8") as f:
            f.write(html)
            
        browser.close()

if __name__ == "__main__":
    test_scrape()
