#!/usr/bin/env python3
"""รันบนเครื่อง: ดาวน์โหลดไลบรารีครั้งแรก แล้วเปิด http://localhost:8000"""
import os, subprocess, sys, http.server, socketserver, webbrowser
os.chdir(os.path.dirname(os.path.abspath(__file__)))
subprocess.check_call([sys.executable, "download_libs.py", "lib"])
print("เปิดแอปที่ http://localhost:8000 (Ctrl+C เพื่อหยุด)")
webbrowser.open("http://localhost:8000")
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", 8000), http.server.SimpleHTTPRequestHandler) as h: h.serve_forever()
