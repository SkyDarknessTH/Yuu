// Service Worker: แคชไฟล์ทั้งหมดหลังเปิดครั้งแรก เพื่อใช้งานออฟไลน์ได้ (รวมบน iPhone)
const C='tls-v2';
self.addEventListener('install',e=>{self.skipWaiting();e.waitUntil(caches.open(C).then(c=>c.addAll(['./','index.html','lib/jszip.min.js','lib/exif-reader.js','lib/mp4-muxer.js','lib/opencv.js']).catch(()=>{})))});
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==C).map(k=>caches.delete(k)))).then(()=>clients.claim())));
self.addEventListener('fetch',e=>{
 if(e.request.method!=='GET'||new URL(e.request.url).origin!==location.origin)return;
 e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request).then(n=>{const k=n.clone();caches.open(C).then(c=>c.put(e.request,k));return n})));
});
