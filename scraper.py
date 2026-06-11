from playwright.sync_api import sync_playwright
import json, csv, time, os, sys, random
from datetime import datetime

KEYWORD    = sys.argv[1] if len(sys.argv) > 1 else "wifi only"
HEADLESS   = "--headless" in sys.argv
MAX_SCROLL = 15

def scrape_marketplace(keyword):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        context = browser.new_context(storage_state="session.json")
        page = context.new_page()

        url = f"https://www.facebook.com/marketplace/search?query={keyword}"
        print(f">>> Keyword  : {keyword}")
        print(f">>> Headless : {HEADLESS}")
        print(f">>> URL      : {url}\n")
        page.goto(url, wait_until="domcontentloaded")
        time.sleep(random.uniform(2.5, 4.0))

        print(">>> Scrolling...")
        prev_count = 0
        for i in range(MAX_SCROLL):
            page.evaluate("window.scrollBy(0, 2000)")
            time.sleep(random.uniform(1.0, 2.5))
            count = page.eval_on_selector_all(
                "a[href*='/marketplace/item/']",
                "els => new Set(els.map(e => e.href.split('?')[0])).size"
            )
            print(f"    scroll {i+1}/{MAX_SCROLL} — {count} listing")
            if count == prev_count:
                print("    tidak ada listing baru, stop\n")
                break
            prev_count = count

        results = page.evaluate("""
            () => {
                const cards = [...document.querySelectorAll("a[href*='/marketplace/item/']")];
                const seen = new Set();
                const data = [];
                for (const card of cards) {
                    const href = card.href.split('?')[0];
                    if (seen.has(href)) continue;
                    seen.add(href);
                    const spans = [...card.querySelectorAll("span")]
                        .map(s => s.innerText.trim())
                        .filter(t => t.length > 0);
                    const price = spans.find(t => t.startsWith("Rp") || t.toLowerCase() === "gratis") || "N/A";
                    const title = spans.reduce((a, b) =>
                        (b.length > a.length && !b.startsWith("Rp") && b.toLowerCase() !== "gratis") ? b : a
                    , "");
                    const location = spans.filter(t => !t.startsWith("Rp") && t.toLowerCase() !== "gratis").pop() || "N/A";
                    data.push({ title, price, location, url: href });
                }
                return data;
            }
        """)

        browser.close()
        return results

os.makedirs("output", exist_ok=True)
data = scrape_marketplace(KEYWORD)

ts           = datetime.now().strftime("%Y%m%d_%H%M%S")
keyword_slug = KEYWORD.replace(" ", "_")
base         = f"output/{keyword_slug}_{ts}"

with open(f"{base}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with open(f"{base}.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price", "location", "url"])
    writer.writeheader()
    writer.writerows(data)

print(f"{'─'*60}")
for i, item in enumerate(data):
    print(f"  [{i+1}/{len(data)}] {item['title']}")
    print(f"  Harga  : {item['price']}")
    print(f"  Lokasi : {item['location']}")
    print(f"  URL    : {item['url']}")
    print()

print(f"{'─'*60}")
print(f">>> Selesai! {len(data)} listing")
print(f">>> JSON : {base}.json")
print(f">>> CSV  : {base}.csv")
