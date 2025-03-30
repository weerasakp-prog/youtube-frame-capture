#!/usr/bin/env python3
import os
import argparse
import cv2
from pytube import YouTube
import time
from datetime import timedelta

def download_youtube_video(url, output_path="downloads"):
    """
    Download a YouTube video to the specified output path.
    
    Args:
        url (str): The YouTube URL
        output_path (str): Directory to save the video
        
    Returns:
        str: Path to the downloaded video file
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Create a YouTube object
    print(f"Fetching video from {url}...")
    yt = YouTube(url)
    
    # Get the highest resolution mp4 stream with progressive=True
    # (progressive=True means audio and video are combined)
    print(f"Downloading: {yt.title}")
    video = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
    
    # Download the video
    video_path = video.download(output_path)
    print(f"Downloaded to: {video_path}")
    
    return video_path

def extract_frames(video_path, output_folder="frames", interval_seconds=30):
    """
    Extract frames from a video at specified intervals.
    
    Args:
        video_path (str): Path to the video file
        output_folder (str): Directory to save the frames
        interval_seconds (int): Interval between frames in seconds
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps
    
    print(f"Video FPS: {fps}")
    print(f"Total frames: {total_frames}")
    print(f"Duration: {timedelta(seconds=int(duration))}")
    
    # Calculate frame intervals
    frame_interval = int(fps * interval_seconds)
    
    # Initialize frame counter
    count = 0
    frame_number = 0
    
    print(f"Extracting frames every {interval_seconds} seconds...")
    
    while True:
        # Read the next frame
        success, frame = cap.read()
        
        # Break the loop if we've reached the end of the video
        if not success:
            break
        
        # If we're at a desired interval, save the frame
        if count % frame_interval == 0:
            # Format the timestamp as HH:MM:SS
            timestamp = timedelta(seconds=int(count/fps))
            
            # Save the frame with a descriptive filename
            filename = f"frame_{frame_number:04d}_{timestamp}.jpg"
            output_path = os.path.join(output_folder, filename)
            
            cv2.imwrite(output_path, frame)
            print(f"Saved: {output_path}")
            
            frame_number += 1
        
        # Increment the frame counter
        count += 1
    
    # Release the video capture object
    cap.release()
    
    print(f"Extracted {frame_number} frames in total.")

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Extract frames from a YouTube video at regular intervals.")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("-i", "--interval", type=int, default=30, help="Interval between frames in seconds (default: 30)")
    parser.add_argument("-o", "--output", default="frames", help="Output folder for frames (default: 'frames')")
    parser.add_argument("-k", "--keep-video", action="store_true", help="Keep the downloaded video file")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Download the YouTube video
    video_path = download_youtube_video(args.url)
    
    # Extract frames
    extract_frames(video_path, args.output, args.interval)
    
    # Delete the video file if not keeping it
    if not args.keep_video and os.path.exists(video_path):
        print(f"Deleting downloaded video: {video_path}")
        os.remove(video_path)

if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Process completed in {timedelta(seconds=int(elapsed_time))}")
