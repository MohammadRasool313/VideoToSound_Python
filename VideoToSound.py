from moviepy.editor import VideoFileClip
import os
import argparse

def extract_audio(video_path, output_audio_path):
    try:
        # Load video file
        video = VideoFileClip(video_path)
        
        # Check if video has audio
        if not video.audio:
            raise ValueError("The video file contains no audio track")
            
        # Extract audio
        audio = video.audio
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_audio_path), exist_ok=True)
        
        # Save audio as WAV file
        audio.write_audiofile(output_audio_path, verbose=False)
        
        print(f"\nSuccess! Audio extracted to: {output_audio_path}")
        return True
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Extract audio from video files')
    parser.add_argument('-i', '--input', required=True, help='Path to input video file')
    parser.add_argument('-o', '--output', default='output.wav', 
                      help='Path to output audio file (default: output.wav)')
    
    args = parser.parse_args()
    
    # Ensure output has .wav extension
    if not args.output.endswith('.wav'):
        args.output += '.wav'
    
    # Process the file
    success = extract_audio(args.input, args.output)
    
    if success:
        input("Press Enter to exit...")

if __name__ == '__main__':
    main()