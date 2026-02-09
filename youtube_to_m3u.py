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
        # الرابط المباشر للبث الخام من يوتيوب
        # هذا الرابط يعمل كمحول (Redirect) مباشر للبث
        m3u8_url = f"https://www.youtube.com/api/v1/manifest/hls_variant/expire/1740000000/id/{vid_id}/source/yt_live_broadcast/master.m3u8"
        f.write(f'#EXTINF:-1, {name}\n{m3u8_url}\n')

print("Playlist generated successfully!")
