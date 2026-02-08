import os

# قائمة القنوات والافلام (الاسم، معرف الفيديو من يوتيوب)
channels = [
    ("Bein Sport News Ar", "2lJZPT6OljI"),
    ("Bein Sport Haber Tr", "9xVXWLwT0vA"),
    ("فيلم كلب بلدي", "kvfmomTgDkU")
]

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for name, vid_id in channels:
        # جلب الرابط المباشر
        stream_url = os.popen(f"yt-dlp -g https://www.youtube.com/watch?v={vid_id}").read().strip()
        if stream_url:
            f.write(f'#EXTINF:-1, {name}\n{stream_url}\n')
