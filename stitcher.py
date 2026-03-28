import os
from moviepy import VideoFileClip, concatenate_videoclips

def stitch_space_videos():
    input_folder = "raw_clips"
    output_file = "final_output/storm_sage_final.mp4"
    
    # Folder se saari mp4 files uthao
    clips_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.mp4')]
    clips_files.sort() # Taaki sequence sahi rahe
    
    if not clips_files:
        print("Error: raw_clips folder khali hai! Pehle Gemini se video download karo.")
        return

    print(f"Stitching {len(clips_files)} clips...")
    
    clips = [VideoFileClip(c) for c in clips_files]
    
    # Clips ko jodo
    final_clip = concatenate_videoclips(clips, method="compose")
    
    # Video export karo (YouTube optimized)
    final_clip.write_videofile(output_file, fps=24, codec="libx264", audio_codec="aac")
    print(f"Success! Video save ho gayi: {output_file}")

if __name__ == "__main__":
    stitch_space_videos()