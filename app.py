import streamlit as st
from PIL import Image
from main import generate_story_from_images, narrate_story, get_gemini_voices

LANG_OPTIONS = {
    "English (US)": "en-US",
    "English (India)": "en-IN",
    "Hindi (India)": "hi-IN",
    "Bengali (Bangladesh)": "bn-BD",
    "Tamil (India)": "ta-IN",
    "Telugu (India)": "te-IN",
}

EMOTION_OPTIONS = ["neutral", "cheerful", "excited", "sad", "angry", "serious"]

st.title("AI Story Generator from Images")
st.markdown("""
Upload 1 to 10 images, select story style, language, narrator voice, and emotion.
Let Gemini write and narrate your story!
""")

with st.sidebar:
    st.header("🎨 AI NarrativeFlow")

    uploaded_files = st.file_uploader(
        "Upload your images",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True
    )

    story_style = st.selectbox(
        "Choose a story style",
        ("Comedy", "Thriller", "Fairy Tale", "Sci-Fi", "Mystery", "Adventure", "Morale")
    )

    selected_language = st.selectbox(
        "Choose story & narration language",
        list(LANG_OPTIONS.keys())
    )
    lang_code = LANG_OPTIONS[selected_language]

    voices = get_gemini_voices(lang_code)
    if not voices:
        st.error("No Gemini voices available for this language. Please select another language.")
    voice_names = [v["name"] for v in voices]
    selected_voice_idx = st.selectbox("Choose narrator voice", range(len(voices)), format_func=lambda i: voice_names[i])
    selected_voice = voices[selected_voice_idx]["id"]

    emotion = st.selectbox("Narration emotion/tone", EMOTION_OPTIONS)

    generate_button = st.button("Generate Story and Narration", type="primary")

if generate_button:
    if not uploaded_files:
        st.warning("Please upload at least 1 image.")
    elif len(uploaded_files) > 10:
        st.warning("Please upload a maximum of 10 images.")
    else:
        with st.spinner("Writing and narrating your story..."):
            try:
                pil_images = [Image.open(f) for f in uploaded_files]

                st.subheader("Your Visual Inspiration:")
                columns = st.columns(len(pil_images))
                for idx, img in enumerate(pil_images):
                    with columns[idx]:
                        st.image(img, use_container_width=True)

                story = generate_story_from_images(pil_images, story_style, lang_code, emotion)
                if "Error" in story or "failed" in story or "API key" in story:
                    st.error(story)
                else:
                    st.subheader(f"Your {story_style} Story:")
                    st.success(story)

                    st.subheader("Listen to your story:")
                    audio_file = narrate_story(story, lang_code, selected_voice, emotion)
                    if isinstance(audio_file, str) and audio_file.lower().startswith("error"):
                        st.error(audio_file)
                    else:
                        st.audio(audio_file, format="audio/wav")
            except Exception as e:
                st.error(f"An error occurred: {e}")
