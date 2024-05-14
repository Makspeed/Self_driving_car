import picamera
import time

# Initialize the camera
camera = picamera.PiCamera()

try:
    # Start recording video
    camera.start_recording('my_video.h264')
    
    # Record video for 10 seconds (adjust as needed)
    camera.wait_recording(10)
    
    # Stop recording
    camera.stop_recording()
    
    print("Video saved as 'my_video.h264'")
    
except Exception as e:
    print(f"Error: {e}")

finally:
    # Clean up resources
    camera.close()
