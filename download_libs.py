#!/usr/bin/env python3
"""ดาวน์โหลดไลบรารีลงโฟลเดอร์ lib (ค่าเริ่มต้น ./lib) ใช้ทั้งบนเครื่องและใน GitHub Actions
ใช้: python3 download_libs.py [โฟลเดอร์ปลายทาง]"""
import os, sys, urllib.request
OUT = sys.argv[1] if len(sys.argv) > 1 else "lib"
LIBS = {
 "jszip.min.js": "https://cdn.jsdelivr.net/npm/jszip@3.10.1/dist/jszip.min.js",
 "exif-reader.js": "https://cdn.jsdelivr.net/npm/exifreader@4.23.3/dist/exif-reader.js",
 "mp4-muxer.js": "https://cdn.jsdelivr.net/npm/mp4-muxer@5.1.3/build/mp4-muxer.js",
 "opencv.js": "https://cdn.jsdelivr.net/npm/@techstark/opencv-js@4.10.0-release.1/dist/opencv.js",
}
os.makedirs(OUT, exist_ok=True)
for n, u in LIBS.items():
    p = os.path.join(OUT, n)
    if os.path.exists(p) and os.path.getsize(p) > 1000: continue
    print("ดาวน์โหลด", n)
    urllib.request.urlretrieve(u, p)
    if os.path.getsize(p) < 1000: raise SystemExit("ไฟล์ผิดปกติ: " + n)
print("เสร็จแล้ว")
