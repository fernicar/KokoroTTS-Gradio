import gradio as gr
import os
import subprocess
import datetime

# Hardcoded voice menu mapping (voice name and corresponding language)
voice_menu = {
    # US Voices
    "af_alloy (en)": {"name": "af_alloy", "lang": "en-us"},
    "af_aoede (en)": {"name": "af_aoede", "lang": "en-us"},
    "af_bella (en)": {"name": "af_bella", "lang": "en-us"},
    "af_heart (en)": {"name": "af_heart", "lang": "en-us"},
    "af_jessica (en)": {"name": "af_jessica", "lang": "en-us"},
    "af_kore (en)": {"name": "af_kore", "lang": "en-us"},
    "af_nicole (en)": {"name": "af_nicole", "lang": "en-us"},
    "af_nova (en)": {"name": "af_nova", "lang": "en-us"},
    "af_river (en)": {"name": "af_river", "lang": "en-us"},
    "af_sarah (en)": {"name": "af_sarah", "lang": "en-us"},
    "af_sky (en)": {"name": "af_sky", "lang": "en-us"},

    "am_adam (en)": {"name": "am_adam", "lang": "en-us"},
    "am_echo (en)": {"name": "am_echo", "lang": "en-us"},
    "am_eric (en)": {"name": "am_eric", "lang": "en-us"},
    "am_fenrir (en)": {"name": "am_fenrir", "lang": "en-us"},
    "am_liam (en)": {"name": "am_liam", "lang": "en-us"},
    "am_michael (en)": {"name": "am_michael", "lang": "en-us"},
    "am_onyx (en)": {"name": "am_onyx", "lang": "en-us"},
    "am_puck (en)": {"name": "am_puck", "lang": "en-us"},

    # GB Voices
    "bf_alice (en)": {"name": "bf_alice", "lang": "en-gb"},
    "bf_emma (en)": {"name": "bf_emma", "lang": "en-gb"},
    "bf_isabella (en)": {"name": "bf_isabella", "lang": "en-gb"},
    "bf_lily (en)": {"name": "bf_lily", "lang": "en-gb"},
    "bm_daniel (en)": {"name": "bm_daniel", "lang": "en-gb"},
    "bm_fable (en)": {"name": "bm_fable", "lang": "en-gb"},
    "bm_george (en)": {"name": "bm_george", "lang": "en-gb"},
    "bm_lewis (en)": {"name": "bm_lewis", "lang": "en-gb"},

    # FR Voices
    "ff_siwis (fr)": {"name": "ff_siwis", "lang": "fr-fr"},

    # IT Voices
    "if_sara (it)": {"name": "if_sara", "lang": "it"},
    "im_nicola (it)": {"name": "im_nicola", "lang": "it"},

    # JP Voices
    "jf_alpha (ja)": {"name": "jf_alpha", "lang": "ja"},
    "jf_gongitsune (ja)": {"name": "jf_gongitsune", "lang": "ja"},
    "jf_nezumi (ja)": {"name": "jf_nezumi", "lang": "ja"},
    "jf_tebukuro (ja)": {"name": "jf_tebukuro", "lang": "ja"},
    "jm_kumo (ja)": {"name": "jm_kumo", "lang": "ja"},

    # CN Voices
    "zf_xiaobei (cmn)": {"name": "zf_xiaobei", "lang": "cmn"},
    "zf_xiaoni (cmn)": {"name": "zf_xiaoni", "lang": "cmn"},
    "zf_xiaoxiao (cmn)": {"name": "zf_xiaoxiao", "lang": "cmn"},
    "zf_xiaoyi (cmn)": {"name": "zf_xiaoyi", "lang": "cmn"},
    "zm_yunjian (cmn)": {"name": "zm_yunjian", "lang": "cmn"},
    "zm_yunxi (cmn)": {"name": "zm_yunxi", "lang": "cmn"},
    "zm_yunxia (cmn)": {"name": "zm_yunxia", "lang": "cmn"},
    "zm_yunyang (cmn)": {"name": "zm_yunyang", "lang": "cmn"}
}

def tts(text, speed, voice_choice):
    selected_voice = voice_menu.get(voice_choice)
    if not selected_voice:
        return "Selected voice not found.", None
    voice_name = selected_voice["name"]
    lang = selected_voice["lang"]

    # Prepare environment variables for the TTS process
    env = os.environ.copy()
    env["TEXT"] = text
    env["SPEED"] = str(speed)
    env["VOICE"] = voice_name
    env["LANG"] = lang

    # Execute the command that generates audio.wav using the kokoro TTS model
    process = subprocess.run(["uv", "run", "hello.py"], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if process.returncode != 0:
        return f"Error during TTS generation: {process.stderr}", None

    # Check if audio.wav was generated
    if not os.path.exists("audio.wav"):
        return "audio.wav was not generated.", None

    # Create output folder if it doesn't exist and rename audio.wav with a timestamp
    os.makedirs("output", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    new_filename = os.path.join("output", f"audio_{timestamp}.wav")
    try:
        os.rename("audio.wav", new_filename)
    except Exception as e:
        return f"Error renaming audio file: {e}", None

    return f"Audio file saved as {new_filename}", new_filename

# Build Gradio interface in local mode only
iface = gr.Interface(
    fn=tts,
    inputs=[
        gr.Textbox(label="Text", placeholder="Enter text here"),
        gr.Slider(minimum=0.5, maximum=2.0, value=1.0, step=0.1, label="Speed"),
        gr.Dropdown(choices=list(voice_menu.keys()), label="Voice")
    ],
    outputs=["text", "audio"],
    title="Kokoro TTS Gradio Interface",
    allow_flagging="never"
)

iface.launch(server_name="127.0.0.1", share=False)
