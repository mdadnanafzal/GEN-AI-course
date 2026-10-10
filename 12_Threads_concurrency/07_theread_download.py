import threading
import requests 
import time 

def downlad(url):
    print(f"starting download from {url}")
    resp = requests.get(url)
    print(f"finished downlaoding form {url}, size: {len(resp.content)} bytes")


urls = [
    "https://plus.unsplash.com/premium_photo-1790059278261-e9f80f565619?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
    "https://images.unsplash.com/photo-1790106078526-ce7cfa2c6c2a?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
]

start = time.time()
threads = []

for url in urls:
     t= threading.Thread(target=downlad, args = (url, ))
     t.start()
     threads.append(t)
for thread in threads:
    t.join()

end = time.time()

print(f"all downloads done in {end - start:.2f} seconds")
