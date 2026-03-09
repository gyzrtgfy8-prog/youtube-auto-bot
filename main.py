from moviepy.editor import TextClip, CompositeVideoClip
from gtts import gTTS
import os

text = "Welcome to my AI channel"

# create voice
tts = gTTS(text)
tts.save("voice.mp3")

# create video
clip = TextClip(text, fontsize=70, color='white', size=(1080,1920))
clip = clip.set_duration(5)

video = CompositeVideoClip([clip])
video.write_videofile("video.mp4", fps=24)

print("Video created")
