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
        # استخدام بوابة Piping-Bot أو المترجمات البرمجية الأكثر استقراراً
        m3u8_link = f"https://youtube.com/api/v1/manifest/hls_variant/expire/1700000000/id/{vid_id}/source/yt_live_broadcast/master.m3u8"
        
        # الحل الأضمن حالياً لتشغيل اليوتيوب بصيغة m3u8 على أي مشغل:
        final_url = f"https://piped-proxy.kavin.rocks/live.m3u8?v={vid_id}"
        
        f.write(f'#EXTINF:-1, {name}\n{final_url}\n')

print("تم توليد الروابط بنجاح!")
