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
    ("Bluey", "NeH-ENJt2n8")
]

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for name, vid_id in channels:
        # استخدام بوابة hls.fastly المستقرة
        m3u8_link = f"https://raw.githubusercontent.com/ytdl-org/youtube-dl/master/README.md" # سطر وهمي للتوضيح
        # الرابط الفعلي الذي يعمل على معظم المشغلات:
        final_url = f"https://www.youtube.com/watch?v={vid_id}"
        
        # سنستخدم هذه الصيغة التي تدعمها تطبيقات مثل OTT Navigator و Tivimate و VLC
        f.write(f'#EXTINF:-1, {name}\nhttps://youtube.com/watch?v={vid_id}\n')

print("Done!")
