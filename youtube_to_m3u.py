channels = [
    ("beIN SPORTS News", "2lJZPT6OljI"),
    ("beIN SPORTS Live", "kvfmomTgDkU"),
    ("beIN SPORTS HABER", "9xVXWLwT0vA")
]

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for name, vid_id in channels:
        # استخدام بوابة (Gateway) لتحويل رابط اليوتيوب إلى m3u8 مباشر
        m3u8_link = f"https://c.v-it.top/live/{vid_id}/index.m3u8"
        f.write(f'#EXTINF:-1, {name}\n{m3u8_link}\n')

print("تم إنشاء روابط m3u8 بنجاح!")
