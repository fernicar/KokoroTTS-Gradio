"""
pip install kokoro-onnx soundfile

wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
python examples/save.py
"""

import soundfile as sf
from kokoro_onnx import Kokoro

kokoro = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")
import os
import soundfile as sf
from kokoro_onnx import Kokoro

# Retrieve parameters from environment variables
text = os.environ.get("TEXT", "hello, i am speaking")
speed = float(os.environ.get("SPEED", "1.0"))
voice = os.environ.get("VOICE", "af_nicole")
lang = os.environ.get("LANG", "en-us")

kokoro = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")
samples, sample_rate = kokoro.create(
    text, voice=voice, speed=speed, lang=lang
)
sf.write("audio.wav", samples, sample_rate)
print("Created audio.wav")
