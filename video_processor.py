import subprocess

def convert_video(input_file: str, output_file: str):
    """
    Reconversión para compatibilidad con YouTube/TikTok/Facebook.
    """
    cmd = [
        "ffmpeg", "-i", input_file,
        "-c:v", "libx264", "-c:a", "aac",
        "-movflags", "+faststart", output_file
    ]
    subprocess.run(cmd, check=True)
