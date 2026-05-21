# video-to-gif

> Конвертер відеофайлів в анімований GIF за допомогою OpenCV та Pillow.

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=flat&logo=opencv&logoColor=white)](https://opencv.org)

## Можливості

- Витягує перші N кадрів з відео (налаштовується)
- Зменшує розмір до 320×240 для оптимізації файлу
- Регульована швидкість відтворення GIF
- Підтримка MP4, AVI, MOV та інших форматів через OpenCV

## Встановлення

```bash
git clone https://github.com/yyvolovyk-1983-edu/video-to-gif
cd video-to-gif
pip install opencv-python pillow
```

## Використання

```python
from video_to_gif import video_frame_img

# Базове використання
video_frame_img("path/to/video.mp4", "output.gif")

# З параметрами (кількість кадрів, розмір, fps)
video_frame_img("video.mp4", "output.gif", max_frames=30, size=(640, 480), fps=15)
```

## Приклад

```bash
python video_to_gif.py --input example_video.mp4 --output result.gif --frames 20
```

## Залежності

```
opencv-python
pillow
```

## Структура

```
video-to-gif/
├── video_to_gif.py     # основний скрипт
├── example_video.mp4   # приклад відео
└── README.md
```
