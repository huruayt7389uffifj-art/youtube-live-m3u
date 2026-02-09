channels = [
    ("beIN SPORTS News", "2lJZPT6OljI"),
    ("beIN SPORTS Live", "kvfmomTgDkU"),
    ("beIN SPORTS HABER", "9xVXWLwT0vA")
]

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for name, vid_id in channels:
        # استخدام رابط خارجي لجلب البث المباشر يتخطى حظر المناطق
        stream_url = f"https://www.youtube.com/watch?v={vid_id}"
        # هنا سنضع الرابط بصيغة تقبلها معظم مشغلات IPTV مباشرة
        f.write(f'#EXTINF:-1, {name}\n{stream_url}\n')

print("تم تحديث القائمة بنجاح!")
