import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from io import BytesIO
import io
import wave
import base64

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found")
client = genai.Client(api_key=api_key)

# Official Gemini 2.5 voice names (style-based), update as needed
GEMINI_VOICE_MAP = {
    "en-US": [
        {"id": "zephyr", "name": "Zephyr (Bright)"},
        {"id": "puck", "name": "Puck (Upbeat)"},
        {"id": "charon", "name": "Charon (Informative)"},
        {"id": "kore", "name": "Kore (Firm)"},
        # Add more English (US) voices as needed
    ],
    "hi-IN": [
        # Voices are style-based; can use English voices with hi-IN language text
        {"id": "kore", "name": "Kore (Firm)"},
        {"id": "puck", "name": "Puck (Upbeat)"},
    ],
    "bn-BD": [
        {"id": "zephyr", "name": "Zephyr (Bright)"},
        {"id": "puck", "name": "Puck (Upbeat)"},
    ],
    "ta-IN": [
        {"id": "kore", "name": "Kore (Firm)"},
        {"id": "puck", "name": "Puck (Upbeat)"},
    ],
    "te-IN": [
        {"id": "kore", "name": "Kore (Firm)"},
        {"id": "puck", "name": "Puck (Upbeat)"},
    ],
}

def get_gemini_voices(lang_code):
    return GEMINI_VOICE_MAP.get(lang_code, GEMINI_VOICE_MAP.get("en-US", []))

def create_advanced_prompt(style, lang_code, emotion):
    lang_name = {
        "en-US": "English (US)",
        "hi-IN": "Hindi (India)",
        "bn-BD": "Bengali (Bangladesh)",
        "ta-IN": "Tamil (India)",
        "te-IN": "Telugu (India)"
    }.get(lang_code, "English (US)")
    
    prompt = f"""
    Your persona: Friendly Indian storyteller.
    Language: {lang_name}
    Emotion/tone: {emotion}
    Style: {style}

    Instructions:
    - Specify suitable title for the story.
    - Write a continuous, well-structured story connecting all images.
    - Write the story entirely in {lang_name}, **without mixing languages**.
    - Do NOT describe the image metadata, visual code, or non-narrative text.
    - Do NOT include raw image descriptions or technical details.
    - Use Indian names, places, and cultural context only.
    - Story must be 4-5 paragraphs with a clear beginning, middle, and end.
    """
    if style == "Morale":
        prompt += "[MORAL]: Add a one-sentence moral at the end.\n"
    elif style == "Mystery":
        prompt += "[SOLUTION]: Reveal culprit and key clue at the end.\n"
    elif style == "Thriller":
        prompt += "[TWIST]: Reveal a twist ending.\n"
    return prompt

def generate_story_from_images(images, style, lang_code, emotion):
    prompt = create_advanced_prompt(style, lang_code, emotion)
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=[images, prompt]
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

def pcm_to_wav_bytes(pcm_bytes, sample_rate=24000, num_channels=1, sample_width=2):
    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wav_file:
        wav_file.setnchannels(num_channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(pcm_bytes)
    buffer.seek(0)
    return buffer

def narrate_story(story_text, lang_code, voice_name, emotion):
    style_prompt = f"Please narrate the following story in a {emotion} tone: {story_text}"
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-tts",
            contents=style_prompt,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=voice_name)
                    )
                )
            )
        )
        audio_data = response.candidates[0].content.parts[0].inline_data.data

        # Decode if base64 encoded string
        if isinstance(audio_data, str):
            audio_bytes = base64.b64decode(audio_data)
        else:
            audio_bytes = audio_data

        # Check first bytes to guess format
        header = audio_bytes[:4]
        if header == b'RIFF':
            # WAV format, no wrapping needed
            audio_stream = io.BytesIO(audio_bytes)
        else:
            # Wrap raw pcm into wav container
            audio_stream = pcm_to_wav_bytes(audio_bytes)

        return audio_stream

    except Exception as e:
        return f"Error: {e}"

