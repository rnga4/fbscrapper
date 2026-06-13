from flask import Flask, render_template, request, jsonify, send_file
from playwright.sync_api import sync_playwright
import json, csv, time, os, random, threading
from datetime import datetime

app = Flask(__name__)
JOBS = {}

# Mapping kota → FB Marketplace city ID
CITY_MAP = {
    "jakarta":    "jakarta",
    "surabaya":   "surabaya",
    "bandung":    "bandung",
    "medan":      "medan",
    "semarang":   "semarang",
    "makassar":   "makassar",
    "palembang":  "palembang",
    "tangerang":  "tangerang",
    "depok":      "depok",
    "bekasi":     "bekasi",
    "bogor":      "bogor",
    "yogyakarta": "yogyakarta",
    "malang":     "malang",
    "batam":      "batam",
    "pekanbaru":  "pekanbaru",
    "denpasar":   "denpasar",
}

def do_scrape(job_id, keyword, max_scroll, city, radius):
    JOBS[job_id] = {"status": "running", "log": [], "data": []}

    def log(msg):
        JOBS[job_id]["log"].append(msg)

    try:
        with sync_playwright() as p:
            # Gunakan path relatif dari file main.py ini
            current_dir = os.path.dirname(os.path.abspath(__file__))
            project_dir = os.path.dirname(current_dir)
            session_path = os.path.join(project_dir, "session.json")
            
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(storage_state=session_path)
            page = context.new_page()

            # Build URL dengan lokasi & radius kalau ada
            if city and city in CITY_MAP:
                url = (f"https://www.facebook.com/marketplace/{CITY_MAP[city]}/search"
                       f"?query={keyword}&radius={radius}&deliveryMethod=local_pick_up")
                log(f"Lokasi: {city} | Radius: {radius} km")
            else:
                url = f"https://www.facebook.com/marketplace/search?query={keyword}"
                log("Lokasi: Semua")

            log(f"Membuka {url}")
            page.goto(url, wait_until="domcontentloaded")
            time.sleep(random.uniform(2.5, 4.0))

            prev_count = 0
            for i in range(int(max_scroll)):
                page.evaluate("window.scrollBy(0, 2000)")
                time.sleep(random.uniform(1.0, 2.5))
                count = page.eval_on_selector_all(
                    "a[href*='/marketplace/item/']",
                    "els => new Set(els.map(e => e.href.split('?')[0])).size"
                )
                log(f"Scroll {i+1}/{max_scroll} — {count} listing")
                if count == prev_count:
                    log("Tidak ada listing baru, stop scroll")
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
                        const FB_BADGES = new Set(["terlaris","baru","featured","cepat terjual","dijual cepat","sold","terjual","unggulan"]);
                        const isPrice    = t => t.startsWith("Rp") || t.toLowerCase() === "gratis";
                        const isLocation = t => t.includes(",");
                        const isBadge    = t => FB_BADGES.has(t.toLowerCase());
                        const isValidTitle = t => t.length > 3 && !isPrice(t) && !isLocation(t) && !isBadge(t);
                        const price    = spans.find(isPrice) || "N/A";
                        const title    = spans.find(isValidTitle) || spans.find(t => !isPrice(t) && !isLocation(t)) || "N/A";
                        const location = spans.filter(t => !isPrice(t) && t.toLowerCase() !== "gratis").pop() || "N/A";
                        data.push({ title, price, location, url: href });
                    }
                    return data;
                }
            """)
            browser.close()

            ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
            slug = keyword.replace(" ", "_")
            output_dir = os.path.join(project_dir, "output")
            base = os.path.join(output_dir, f"{slug}_{ts}")
            os.makedirs(output_dir, exist_ok=True)

            with open(f"{base}.json", "w", encoding="utf-8") as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            with open(f"{base}.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["title","price","location","url"])
                writer.writeheader()
                writer.writerows(results)

            JOBS[job_id]["data"]   = results
            JOBS[job_id]["csv"]    = f"{base}.csv"
            JOBS[job_id]["status"] = "done"
            log(f"Selesai! {len(results)} listing ditemukan")

    except Exception as e:
        JOBS[job_id]["status"] = "error"
        JOBS[job_id]["log"].append(f"ERROR: {str(e)}")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scrape", methods=["POST"])
def scrape():
    body       = request.json
    keyword    = body.get("keyword", "wifi only")
    max_scroll = body.get("max_scroll", 15)
    city       = body.get("city", "")
    radius     = body.get("radius", 400)
    job_id     = datetime.now().strftime("%Y%m%d%H%M%S%f")
    t = threading.Thread(target=do_scrape, args=(job_id, keyword, max_scroll, city, radius))
    t.start()
    return jsonify({"job_id": job_id})

@app.route("/status/<job_id>")
def status(job_id):
    return jsonify(JOBS.get(job_id, {"status": "not_found"}))

@app.route("/download/<job_id>")
def download(job_id):
    job = JOBS.get(job_id)
    if job and "csv" in job:
        return send_file(job["csv"], as_attachment=True)
    return "Not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
