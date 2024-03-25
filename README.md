# Video Conversion Script for Upload

This Python script is designed to convert video files in the current directory to formats suitable for uploading to various platforms. It provides options to adjust the resolution, audio settings, and bitrate of the output videos.

## Features

- Converts all `.mp4` files in the current directory to the specified format
- Supports optional low resolution output (720p)
- Allows encoding without audio
- Provides an option for low bitrate audio
- Offers a high video bitrate setting for YouTube uploads
- Resizes the video to the specified resolution and sets the frame rate to 30 fps
- Saves the converted files in a `converted` directory

## Requirements

- Python 3.x
- MoviePy library

## Installation

1. Clone the repository or download the script file.
2. Install the required dependencies by running the following command:
   ```
   pip install moviepy
   ```
   
   
Sure! Here's a brief installation guide for FFmpeg that you can add to the README:

### FFmpeg Installation

The script relies on FFmpeg for video processing. Make sure you have FFmpeg installed on your system before running the script.

#### Windows

1. Download the latest FFmpeg binaries from the [official website](https://ffmpeg.org/download.html#build-windows).
2. Extract the downloaded archive to a directory of your choice.
3. Add the `bin` directory of the extracted FFmpeg directory to your system's PATH environment variable.

#### macOS

1. Install FFmpeg using Homebrew by running the following command in the terminal:
   ```
   brew install ffmpeg
   ```

#### Linux

1. Install FFmpeg using your distribution's package manager. For example:
   - Ubuntu or Debian:
     ```
     sudo apt-get update
     sudo apt-get install ffmpeg
     ```
   - Fedora or CentOS:
     ```
     sudo dnf install ffmpeg
     ```
   - Arch Linux:
     ```
     sudo pacman -S ffmpeg
     ```

## Usage

To use the script, open a terminal or command prompt and navigate to the directory containing the script and the video files you want to convert. Then, run the script with the desired options:

```
python convert_for_upload.py [--lowres] [--noaudio] [--lowaudio] [--yt]
```

### Options

- `--lowres`: Enable low resolution output (720p).
- `--noaudio`: Encode without audio, only video.
- `--lowaudio`: Use a low bitrate for audio.
- `--yt`: Use a high video bitrate, ready for YouTube.

## Examples

1. Convert videos to low resolution (720p):
   ```
   python convert_for_upload.py --lowres
   ```

2. Convert videos without audio:
   ```
   python convert_for_upload.py --noaudio
   ```

3. Convert videos with low bitrate audio:
   ```
   python convert_for_upload.py --lowaudio
   ```

4. Convert videos with high video bitrate for YouTube:
   ```
   python convert_for_upload.py --yt
   ```

## Output

The converted video files will be saved in the `converted` directory within the current directory. The script will create the `converted` directory if it doesn't already exist.

The output file names will be modified based on the selected options:
- `--lowres`: The file name will have ` - low res` appended before the `.mp4` extension.
- `--noaudio`: The file name will have ` - no audio` appended before the `.mp4` extension.
- `--lowaudio`: The file name will have ` - low bitrate audio` appended before the `.mp4` extension.
- `--yt`: The file name will have ` - yt` appended before the `.mp4` extension.

## Contributing

I welcome contributions to enhance the functionality and usability of this script. If you have any ideas, suggestions, or bug reports, please feel free to open an issue or submit a pull request on the GitHub repository.

I appreciate your feedback and look forward to collaborating with the community to make this script even better!