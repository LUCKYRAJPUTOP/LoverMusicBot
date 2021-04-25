# LoverMusicBot TELEGRAM VC MUSIC BOT - This Is A Pyrogram Bot Based On Pytgcalls For Playing Songs Or Audio Files In Telegram Group Voice Chat
[![LoverMusicBot logo](https://telegra.ph/file/175cc1e0ac37172565528.jpg)](https://t.me/LoverNetwork)


-It is inspired from su music project and hamkercat's telegram voice bot.
Neither su music project , nor pytgcalls are stable


<p align="center">
<a href="https://app.codacy.com/gh/LuckyRajputOP/LoverMusicBot?utm_source=github.com&utm_medium=referral&utm_content=LuckyRajputOP/LoverMusicBot&utm_campaign=Badge_Grade_Settings" alt="Codacy Badge">
<img src="https://api.codacy.com/project/badge/Grade/6141417ceaf84545bab6bd671503df51" /> </a>
<a href="https://github.com/LuckyRajputOP/LoverMusicBot" alt="Libraries.io dependency status for GitHub repo"> <img src="https://img.shields.io/librariesio/github/LuckyRajputOP/LoverMusicBot" /> </a>
<a href="http://hits.dwyl.com/LuckyRajputOP/LovetMusicBot" alt="HitCount"> <img src="http://hits.dwyl.com/LuckyRajputOP/LoverMusicBot.svg" /> </a>
</p>
<p align="center">
<a href="https://github.com/LuckyRajputOP/LoverMusicBot" alt="GitHub closed issues"> <img src="https://img.shields.io/github/issues-closed-raw/LuckyRajputOP/LoverMusicBot?style=flat&logo=github&color=success" /> </a>
<a href="https://github.com/LuckyRajputOP/LoverMusicBot" alt="GitHub commit activity"> <img src="https://img.shields.io/github/commit-activity/m/LuckyRajputOP/LoverMusicBot" /> </a>
<a href="https://github.com/LuckyRajputOP/LoverMusicBot/graphs/contributors" alt="GitHub contributors"> <img src="https://img.shields.io/github/contributors/LuckyRajputOP/LoverMusicBot?style=flat&logo=github" /> </a>
<a href="https://github.com/LuckyRajputOP/LoverMusicBot/network/members" alt="GitHub forks"> <img src="https://img.shields.io/github/forks/LuckyRajputOP/LoverMusicBot?label=Forks&logo=github" /> </a>
<a href="https://github.com/LuckyRajputOP/LoverMusicBot" alt="GitHub closed pull requests"> <img src="https://img.shields.io/github/issues-pr-closed-raw/LuckyRajputOP/LoverMusicBot?color=success" /> </a>
<a href="https://github.com/LuckyRajputOP/LoverMusicBot" alt="GitHub issues"> <img src="https://img.shields.io/github/issues-raw/LuckyRajputOP/LoverMusicBot?style=flat&logo=github&color=yellow" /> </a>
</p>
<p align="center">
<a href="https://github.com/LuckyRajputOP/LoverMusicBot" alt="GitHub release (latest by date including pre-releases)"> <img src="https://img.shields.io/github/v/release/LuckyRajputOP/LoverMusicBot?include_prereleases?style=flat&logo=github" /> </a>
<a href="https://www.python.org/" alt="made-with-python"> <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=flat&logo=python&color=blue" /> </a>
<a href="https://github.com/LuckyRajputOP/LoverMusicBot" alt="Docker!"> <img src="https://aleen42.github.io/badges/src/docker.svg" /> </a>
<a href="https://github.com/LuckyRajputOP/LoverMusicBot" alt="GitHub repo size"> <img src="https://img.shields.io/github/repo-size/LuckyRajputOP/LoverMusicBot" /> </a>
<a href="https://github.com/LuckyRajputOP/LoverMusicBot/blob/master/LICENSE" alt="GPLv3 license"> <img src="https://img.shields.io/badge/License-GPLv3-blue.svg" /> </a>
</p>
<p align="center">
<a href="https://t.me/LoverOwner" alt="Telegram!"> <img src="https://aleen42.github.io/badges/src/telegram.svg" /> </a>
<a href="https://github.com/LuckyRajputOP/LoverMusicBot/graphs/commit-activity" alt="Maintenance"> <img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" /> </a>
<a href="https://makeapullrequest.com" alt="PRs Welcome"> <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" /> </a>
</p>


## Requirements

- FFmpeg
- NodeJS [nodesource.com](https://nodesource.com/)
- Python 3.7+
- [PyTgCalls](https://github.com/pytgcalls/pytgcalls)

## Deployment

### Config

Copy `example.env` to `.env` and fill it with your credentials.

### Without Docker

1. Install Python requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run:
   ```bash
   python main.py
   ```

### Using Docker

1. Build:
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```

### Heroku
 [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/LuckyRajputOP/LoverMusicBot.git)

### StringSession

[![GenerateString](https://img.shields.io/badge/repl.it-generateString-yellowgreen)](https://replit.com/@LuckyRajputOP/AuraXVCBot) 

## Commands
-The commands and there use is explained here-:
- `/saavn` To search song on jio saavan and play the first result 
- `/ytt` To search the song on Youtube and play the first matching result.
- `/deezer` To search song on deezer and play good quality stream.
- `/song` To download a song from youtube.
- `/play` Reply this in response to a link or any telegram audio file it will be played 
- `/skip` to skip current song 
- `/stop` to stop the streaming of song 
- `/pause` to pause the stream 
- `/resume` to resume the playback. 
- Inline search is also supported.

* Bot Link:  <a href="https://t.me/LoverMusicBot" alt="LoverMusicBot"> <img src="https://img.shields.io/badge/%F0%9F%A4%96%20-LoverMusicBot-blue" /> </a>
* News channel: <a  href="https://t.me/LoverUpdates" alt="LoverMusicBot Updates"> <img  src="https://img.shields.io/badge/%F0%9F%92%A1-LoverMusicBot%20Updates-9cf" /> </a>

## Support
- [Channel](https://t.me/LoverNetwork)
- [Group](https://t.me/LoverNetwork)

## Credits
- [hamker cat](https://github.com/thehamkercat/Telegram_VC_Bot)
- [Roj](https://github.com/rojserbest)
- [Marvin](https://github.com/BlackStoneReborn)
- [Laky](https://github.com/Laky-64) & [Andrew](https://github.com/AndrewLaneX): PyTgCalls

