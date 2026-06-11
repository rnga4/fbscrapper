# fbscrapper
fb marketplace scarpper, proyek iseng aja, barangkali ada yang mau nambahin fitur silahkan.

## Setup Session (Login Facebook)

Sebelum menjalankan scraper, kamu perlu login Facebook terlebih dahulu untuk generate `session.json`.

### Langkah-langkah:

1. **Install Playwright di lokal (bukan Docker)**
```bash
pip install playwright
playwright install chromium
```

2. **Jalankan script login**
```bash
python3 save_session.py
```

3. **Browser Chrome akan terbuka** — login Facebook seperti biasa

4. **Setelah berhasil login**, `session.json` akan tersimpan otomatis

5. **Jalankan Docker**
```bash
docker-compose up -d
```

6. **Akses aplikasi** di `http://localhost:5010`

> ⚠️ **Penting:** Jangan pernah share atau commit `session.json` ke GitHub karena berisi credentials login kamu.
