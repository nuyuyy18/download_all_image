import os
import requests

# Daftar URL gambar
urls = [
    "https://picsum.photos/id/0/5000/3333",
    "https://picsum.photos/id/1/5000/3333",
    "https://picsum.photos/id/9/5000/INVALID",  
    "https://picsum.photos/id/2/5000/3333",
    "https://picsum.photos/id/3/5000/3333",
    "https://picsum.photos/id/4/5000/3333",
    "https://picsum.photos/id/5/5000/3334",
    "https://picsum.photos/id/6/5000/3333",
    "https://picsum.photos/id/7/4728/3168",
    "https://picsum.photos/id/8/5000/3333"
]

os.makedirs("dw_img", exist_ok=True)

for url in urls:
    try:
        file_id = url.split("/")[4]
        filename = f"{file_id}.jpg"
        path = os.path.join("dw_img", filename)

        print(f"Mengunduh {filename}...")
        r = requests.get(url, timeout=10)

        # Skip kalau invalid
        if not r.ok or "text/html" in r.headers.get("Content-Type", ""):
            print(f"❌ Invalid: {filename}"); continue  

        with open(path, "wb") as f: f.write(r.content)
        print(f"✅ Sukses: {filename}")

    except Exception as e:
        print(f"⚠️ Error {url}: {e}")

print("Selesai semua 🚀")
