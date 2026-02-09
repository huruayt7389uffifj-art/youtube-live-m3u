channels = [
    ("Tom and Jerry in NY", "rEKifG2XUZg"),
    ("Gumball", "W8a4yXFozs0"),
    ("Mr. Bean Cartoon S1", "3hvLr9a5vns"),
    ("Baby Looney Tunes", "XfZetbS9084"),
    ("Cartoonito 1", "rJU6YjyUbbE"),
    ("Cartoonito 2", "400k2SKoeh4"),
    ("Adventure Time", "uZkaJ3e9nfY"),
    ("PAW Patrol", "P9pDG_quB9U"),
    ("Mr Bean World", "o-c7MuNavZY"),
    ("Bluey", "NeH-ENJt2n8")و
    ("beIN SPORTS News", "2lJZPT6OljI"),
    ("beIN SPORTS Live", "kvfmomTgDkU"),
    ("beIN SPORTS HABER", "9xVXWLwT0vA")
]

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for name, vid_id in channels:
        # استخدام بوابة tlive المستقرة لتحويل يوتيوب إلى m3u8
        m3u8_link = f"https://raw.githubusercontent.com/t-live/live/main/yt.php?id={vid_id}"
        # أو الرابط المباشر الأكثر قوة:
        final_link = f"https://www.youtube.com/watch?v={vid_id}"
        
        # سنعتمد صيغة البث المباشر التي تحول الرابط تلقائياً
        f.write(f'#EXTINF:-1, {name}\nhttps://vid.priv.au/api/v1/playlists/{vid_id}/index.m3u8\n')

print("تم التحديث بروابط m3u8 جديدة")
