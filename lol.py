from __future__ import unicode_literals
import youtube_dl
ydl_opts = {
    'proxy': 'socks5://127.0.0.1:1080',
}
link = "https://youtu.be/vMHs7CRyVDA"
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
