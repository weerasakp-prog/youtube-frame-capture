# YouTube Frame Capture

This Python script allows you to automatically download a YouTube video and extract frames at regular intervals (e.g., every 30 seconds).

## Features

- Download videos from YouTube using the video URL
- Extract frames at specified time intervals (default: 30 seconds)
- Save frames as JPEG images with timestamps in the filename
- Option to keep or delete the downloaded video after processing

## Requirements

- Python 3.6+
- pytube
- OpenCV (cv2)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/weerasakp-prog/youtube-frame-capture.git
cd youtube-frame-capture
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage with default settings (extract frames every 30 seconds):
```bash
python youtube_frame_capture.py https://www.youtube.com/watch?v=VIDEO_ID
```

Specify a custom interval (e.g., every 5 seconds):
```bash
python youtube_frame_capture.py https://www.youtube.com/watch?v=VIDEO_ID -i 5
```

Specify a custom output folder:
```bash
python youtube_frame_capture.py https://www.youtube.com/watch?v=VIDEO_ID -o my_frames
```

Keep the downloaded video file after processing:
```bash
python youtube_frame_capture.py https://www.youtube.com/watch?v=VIDEO_ID -k
```

### Full Command-line Options

```
usage: youtube_frame_capture.py [-h] [-i INTERVAL] [-o OUTPUT] [-k] url

Extract frames from a YouTube video at regular intervals.

positional arguments:
  url                   YouTube video URL

optional arguments:
  -h, --help            show this help message and exit
  -i INTERVAL, --interval INTERVAL
                        Interval between frames in seconds (default: 30)
  -o OUTPUT, --output OUTPUT
                        Output folder for frames (default: 'frames')
  -k, --keep-video      Keep the downloaded video file
```

## How It Works

1. The script downloads the highest quality progressive MP4 video from the provided YouTube URL.
2. It then uses OpenCV to open the video and extracts frames at the specified intervals.
3. Each frame is saved as a JPEG image with a filename format of `frame_XXXX_HH:MM:SS.jpg`, where:
   - `XXXX` is a sequential frame number
   - `HH:MM:SS` is the timestamp in the video
4. By default, the downloaded video is deleted after processing to save disk space.

## Example

For the video at https://www.youtube.com/watch?v=rvtygG4n6ew, running:

```bash
python youtube_frame_capture.py https://www.youtube.com/watch?v=rvtygG4n6ew
```

Will generate frames every 30 seconds in the "frames" directory.

## License

This project is open source and available under the MIT License.
