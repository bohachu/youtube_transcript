# Youtube Transcript Downloader
Youtube Transcript Downloader 是一個 Python 套件，它可以簡單地從 YouTube 影片下載字幕。此工具可以透過 Python 庫的方式使用，也可以在命令列界面運行。

## 安裝
使用以下命令安裝 Youtube Transcript Downloader：
```sh
python3 -m pip install youtube-transcript
```

## 套件用法
在 Python 程式可以透過以下方式匯入並使用 Youtube Transcript Downloader：

```python
from youtube_transcript import youtube_transcript

# 下載字幕
youtube_transcript.download_transcript(url, username, output_folder)
```

其中，`url` 是您要下載字幕的 Youtube 影片網址，`username` 是您的使用者名稱，`output_folder` 是存放輸出目錄的路徑。
## 命令列界面用法
在命令列界面，可以直接運行模組：
```sh
python3 -m youtube_transcript
```

命令列界面提供以下參數：
- `urls`: Youtube 影片網址（必充）
- `username`: 使用者名稱（可選，預設為 "cbh@cameo.tw"）
- `folder`: 輸出目錄的路徑（可選）

範例：
```sh
python3 -m youtube_transcript "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -u "cbh@cameo.tw" -f "/path/to/output/folder"
```

## 本文件生成prompt
* 請撰寫完整 README.md
* 要包含安裝 python3 -m pip install youtube-transcript
* 要包含套件用法 from youtube_transcript import youtube_transcript
* 要包含cli用法 python3 -m youtube_transcript
* 用繁體中文寫

## 程式碼生成prompt
```
-- 我要寫一個 .py
檔名: youtube_transcript.py
目的: 我要做一個可以抓取youtube字幕的抓取工具，儲存變成文字json檔案
用法: 同時要支援 cli 可以參數運用
用法: 同時要支援 import 套件可以運用呼叫
輸入參數: 一個或多個 youtube 網址
輸入參數: 使用者名稱，預設是 cbh@cameo.tw
輸入參數: 輸出檔案群.json要放到哪個folder, 預設放在 data/users/[使用者名稱]/youtube_transcript/[日期]/*.json
輸出檔案群: 根據輸入的 youtube 網址輸出類似這樣的多個 json 內容檔案
{
  "user": "cbh@cameo.tw",
  "type": "youtube_transcript",
  "time": "2023-05-21T04:21:18Z",
  "id": "23b9242f-2f62-42e8-bdbe-f65241d2ac5a",
  "file_path": "data/users/cbh_cameo_tw/youtube_transcript/2023-05-21/type_youtube_transcript_time_2023-05-21T04_21_18Z_id_23b9242f-2f62-42e8-bdbe-f65241d2ac5a.json",
  "url":"https://www.youtube.com/watch?v=HEquaCEckwg",
  "transcript": "0:00
summary of finish big by bill birlingham
0:04
written by lee schullery in quick read
0:06
narrated
0:07
by alex smith introduction
0:11
the truth is that every entrepreneur
...
"
}
例外: 如果其中一個影片URL抓不到 transcript 也沒有關係，印出抓不到的訊息，就可以忽略就好，不要跳出離開程式碼
```

## Release notes
- python3 -m to_pip -n youtube-transcript -v 1.0.4 youtube_transcript.py
  - 2023-05-21 14:19 Bowen 改成可以 setup.py 用 github 安裝的方法，避免pypi當站
  - python3 -m pip install git+https://github.com/bohachu/youtube_transcript.git
- python3 -m to_pip -n youtube_transcript -v 1.0.3 youtube_transcript.py
  - 2023-05-21 13:28
  - 改名字從 youtube_transcript_downloader to youtube_transcript 避免撞名 pypi
- python3 -m to_pip -n youtube_transcript -v 1.0.2 youtube_transcript.py
  - 2023-05-21 13:21 Bowen
  - 新增加 README.md 完整說明
