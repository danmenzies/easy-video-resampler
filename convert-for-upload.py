import os
import argparse
from moviepy.editor import VideoFileClip

def convert_for_upload(lowres, noaudio, lowaudio, yt):
    # Source and destination directories
    source_dir = './'
    dest_dir = './converted'

    # Check if destination directory exists, if not, create it
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Resolution settings based on lowres flag
    resolution = 720 if lowres else 1080
    video_bitrate = "1000k" if lowres else "2000k"
    video_bitrate = video_bitrate if not yt else '8000k'    

    # Audio settings based on noaudio flag
    audio_codec = 'aac' if not noaudio else None
    audio_bitrate = '320k' if not lowaudio else '192k'
    audio_bitrate = audio_bitrate if not noaudio else '0k'    
    
    print("Building clips")
    print(f'resolution: {resolution}')
    print(f'video_bitrate: {video_bitrate}')
    print(f'audio_codec: {audio_codec}')
    print(f'audio_bitrate: {audio_bitrate}')
    print(f'--------------------------------------')

    # Iterate through each file in the source directory
    for filename in os.listdir(source_dir):
        # Check if file is an mp4
        if filename.endswith('.mp4'):
            # Create video clip
            clip = VideoFileClip(os.path.join(source_dir, filename))

            # Conditionally modify the clip for no audio
            if noaudio:
                clip = clip.without_audio()

            # Resize the clip based on the lowres flag and set frame rate to 30 fps
            resized_clip = clip.resize(height=resolution).set_fps(30)
            
            # Tweak the name of the file if needed
            destination_filename = filename
            
            if yt:
                destination_filename = filename.replace('.mp4', ' - yt.mp4')
                
            elif lowres:
                destination_filename = filename.replace('.mp4', ' - low res.mp4')    
                
            elif lowaudio:
                destination_filename = filename.replace('.mp4', ' - low bitrate audio.mp4')  
                
            elif noaudio:
                destination_filename = filename.replace('.mp4', ' - no audio.mp4')            

            # Write to file with specified settings, adjusting for audio
            resized_clip.write_videofile(
                os.path.join(dest_dir, destination_filename),
                audio_codec=audio_codec,
                audio_bitrate=audio_bitrate,
                bitrate=video_bitrate
            )

def main():
    # Setup argparse for command line flags
    parser = argparse.ArgumentParser(description='Convert videos for upload, with optional settings for low resolution and no audio.')
    parser.add_argument('--lowres', action='store_true', help='Enable low resolution output.')
    parser.add_argument('--noaudio', action='store_true', help='Encode without audio, only video.')
    parser.add_argument('--lowaudio', action='store_true', help='Use a low bitrate for audio.')
    parser.add_argument('--yt', action='store_true', help='Use a high video bit rate, ready for YouTube.')
    args = parser.parse_args()

    # Call the conversion function with the flags
    convert_for_upload(args.lowres, args.noaudio, args.lowaudio, args.yt)

if __name__ == '__main__':
    main()
