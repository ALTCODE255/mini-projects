@echo off
set /p audio="Enter AUDIO file name (including extension): "
set /p img="Enter BG image file name (including extension): "
set /p output="Enter OUTPUT VIDEO file name (no extension): "
ffmpeg -loop 1 -i %img% -i %audio% -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest %output%.mp4