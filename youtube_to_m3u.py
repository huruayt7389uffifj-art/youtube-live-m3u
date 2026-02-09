import subprocess

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

def get_live_m3u8(video_id):
    try:
        url = f"https://www.youtube.com/watch?v={video_id}"
        # جلب رابط الـ m3u8 الأصلي مباشرة من خوادم يوتيوب
        cmd = ['yt-dlp', '--quiet', '--no-warnings', '-g', url]
        result = subprocess.check_output(cmd).decode('utf-8').strip()
        return result
    except:
        return None

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for name, vid_id in channels:
        print(f"Fetching: {name}")
        stream = get_live_m3u8(vid_id)
        if stream:
            f.write(f'#EXTINF:-1, {name}\n{stream}\n')

print("Done! Check your playlist.m3u now.")
