import subprocess

# قائمة الأفلام والقنوات
channels = [
    ("فيلم كلب بلدي", "https://www.youtube.com/watch?v=F_-IZrZ6wZM"),
    ("فيلم لا تراجع ولا استسلام", "https://www.youtube.com/watch?v=F_-IZrZ6wZM"),
    ("فيلم معلش احنا بنتبهدل", "https://www.youtube.com/watch?v=4PVzaqu5avY"),
    ("beIN SPORTS HABER", "https://www.youtube.com/watch?v=9xVXWLwT0vA")
]

def get_url(youtube_url):
    try:
        # استخدام subprocess بدلاً من os.system لضمان جلب الرابط بدقة
        result = subprocess.check_output(['yt-dlp', '-g', youtube_url], stderr=subprocess.STDOUT).decode('utf-8').strip()
        return result
    except:
        return None

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for name, url in channels:
        print(f"Processing: {name}")
        stream_url = get_url(url)
        if stream_url:
            f.write(f'#EXTINF:-1, {name}\n{stream_url}\n')
            print(f"Success: {name}")
        else:
            print(f"Failed: {name}")
