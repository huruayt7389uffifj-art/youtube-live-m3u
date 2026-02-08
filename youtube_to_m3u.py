import os

# قائمة الأفلام والقنوات التي طلبتها
channels = [
    ("فيلم كلب بلدي", "https://youtu.be/F_-IZrZ6wZM"),
    ("فيلم لا تراجع ولا استسلام", "https://youtu.be/F_-IZrZ6wZM"),
    ("فيلم معلش احنا بنتبهدل", "https://youtu.be/4PVzaqu5avY"),
    ("beIN SPORTS HABER", "https://youtu.be/9xVXWLwT0vA")
]

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for name, url in channels:
        # السكريبت يستخدم yt-dlp لجلب الرابط المباشر لكل فيديو
        print(f"جاري معالجة: {name}...")
        os.system(f"yt-dlp -g {url} > temp_url.txt")
        if os.path.exists("temp_url.txt"):
            with open("temp_url.txt", "r") as t:
                stream_url = t.read().strip()
            if stream_url:
                f.write(f'#EXTINF:-1, {name}\n{stream_url}\n')

# حذف الملف المؤقت بعد الانتهاء
if os.path.exists("temp_url.txt"):
    os.remove("temp_url.txt")
