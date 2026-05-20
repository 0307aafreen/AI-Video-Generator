import os
from gtts import gTTS

# function to generate voice audio
def generate_voice(text):

    # create outputs folder
    os.makedirs("outputs", exist_ok=True)

    # audio save path
    audio_path = "outputs/voice.mp3"

    # convert text to speech
    tts = gTTS(
        text=text,
        lang="en"
    )

    # save audio file
    tts.save(audio_path)

    # return audio path
    return audio_path