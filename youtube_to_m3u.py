import subprocess

channels = [
    ("beIN SPORTS News", "https://www.youtube.com/watch?v=2lJZPT6OljI"),
    ("beIN SPORTS Live", "https://www.youtube.com/watch?v=kvfmomTgDkU"),
    ("beIN SPORTS HABER", "https://www.youtube.com/watch?v=9xVXWLwT0vA")
]

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for name, url in channels:
        try:
            stream_url = subprocess.check_output(['yt-dlp', '-g', url]).decode('utf-8').strip()
            f.write(f'#EXTINF:-1, {name}\n{stream_url}\n')
            print(f"Added: {name}")
        except:
            print(f"Failed: {name}")
