from playwright.sync_api import sync_playwright

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        page.on("console", lambda msg: print(f"BROWSER LOG: {msg.text}"))
        
        print("Navigating to http://127.0.0.1:5000...")
        page.goto("http://127.0.0.1:5000")
        
        page.on("dialog", lambda dialog: print(f"ALERT TRIGGERED: {dialog.message}") or dialog.accept())
        
        print("Clicking scrape button...")
        page.locator("#btnScrape").click()
        
        print("Waiting for scrape to finish...")
        try:
            page.wait_for_function('''() => {
                const live = document.getElementById('liveStatus').style.display;
                const table = document.getElementById('tableWrapper').style.display;
                return live === 'none' || table === 'block';
            }''', timeout=60000)
        except Exception as e:
            print(f"Wait timeout or error: {e}")
            
        table_display = page.evaluate("document.getElementById('tableWrapper').style.display")
        live_status = page.evaluate("document.getElementById('liveStatus').style.display")
        live_text = page.evaluate("document.getElementById('liveStatusText').textContent")
        
        print(f"Table display: {table_display}")
        print(f"LiveStatus display: {live_status}")
        print(f"LiveStatus Text: {live_text}")
        
        html = page.evaluate("document.getElementById('tableBody').innerHTML")
        print(f"Table HTML: {html[:200]}")
        
        browser.close()

if __name__ == "__main__":
    run_test()
