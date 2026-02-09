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

def get_url(v_id):
    try:
        url = f"https://www.youtube.com/watch?v={v_id}"
        # إضافة إعدادات متقدمة لتخطي الحظر الجغرافي وحظر البوتات
        cmd = [
            'yt-dlp',
            '--quiet',
            '--no-warnings',
            '--format', 'best',
            '--extractor-args', 'youtube:player_client=android', # محاكاة تطبيق أندرويد لتجنب الحظر
            '-g',
            url
        ]
        return subprocess.check_output(cmd).decode('utf-8').strip()
    except Exception as e:
        return None

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for name, vid_id in channels:
        print(f"Fetching: {name}")
        stream_link = get_url(vid_id)
        if stream_link:
            f.write(f'#EXTINF:-1, {name}\n{stream_link}\n')
        else:
            # رابط احتياطي في حال فشل الاستخراج
            f.write(f'#EXTINF:-1, {name} (Backup)\nhttps://www.youtube.com/watch?v={vid_id}\n')

print("Done!")
