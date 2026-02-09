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
        # سيرفر yewtu.be هو الأكثر موثوقية لتخطي حماية يوتيوب حالياً
        m3u8_link = f"https://yewtu.be/latest_version?id={vid_id}&itag=96"
        f.write(f'#EXTINF:-1, {name}\n{m3u8_link}\n')

print("Update successful.")
