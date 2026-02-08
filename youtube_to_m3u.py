import subprocess

import os



# الروابط الجديدة التي أرسلتها (بث مباشر)

channels = [

    ("beIN SPORTS News", "https://www.youtube.com/live/2lJZPT6OljI?si=OCQVbDnpzT6sKoWy"),

    ("beIN SPORTS Live", "https://www.youtube.com/live/kvfmomTgDkU?si=46wjd6i_bsE7w2pe"),

    ("beIN SPORTS HABER", "https://www.youtube.com/live/9xVXWLwT0vA?si=R7pXYwsHu4HMg9fN")

]



def get_url(youtube_url):

    try:

        # استخدام yt-dlp لجلب الرابط المباشر

        result = subprocess.check_output(['yt-dlp', '-g', youtube_url], stderr=subprocess.STDOUT).decode('utf-8').strip()

        return result

    except Exception as e:

        print(f"Error fetching {youtube_url}: {e}")

        return None



# إنشاء ملف القائمة

with open("playlist.m3u", "w", encoding="utf-8") as f:

    f.write("#EXTM3U\n")

    for name, url in channels:

        print(f"جاري معالجة: {name}")

        stream_url = get_url(url)

        if stream_url:

            f.write(f'#EXTINF:-1, {name}\n{stream_url}\n')

            print(f"تم بنجاح: {name}")

        else:

            print(f"فشل جلب رابط: {name}")
