# AI NarrativeFlow
 - Multilingual Image-to-Story & Voice Narrator (Powered by Google Gemini 2.5)


> **Transform your images into emotionally expressive, multilingual narrated stories using Google Gemini 2.5 Voice AI.**

---

## Overview

**AI NarrativeFlow** is an interactive web app that converts a series of uploaded images into a **cohesive, culturally rich story**, then narrates it in a **selected voice, emotion, and language** — powered by **Google Gemini 2.5 multimodal and TTS APIs**.

This project blends **visual storytelling**, **emotion-driven narration**, and **multilingual capabilities**, showcasing the potential of **Generative AI for creative applications** such as:
- Digital storytelling
- Interactive learning content
- AI narrators for regional languages
- Creative writing assistance

---

## Key Features

✅ **Multimodal Story Generation** – Generates complete, connected stories based on multiple uploaded images.  
✅ **Emotion-Aware Narration** – Speaks with emotional tones like *cheerful, excited, sad, serious, or angry*.  
✅ **Multilingual Support** – Supports English, Hindi, Bengali, Tamil, and Telugu.  
✅ **Voice Selection** – Choose from multiple Gemini 2.5 narrator voices (Zephyr, Kore, Puck, etc.).  
✅ **Cultural Context Awareness** – Generates stories with Indian names, places, and moral or twist endings depending on the style.  
✅ **Streamlit UI** – Simple, elegant web interface for uploading images and controlling story parameters.  

---

## How It Works

1. **Upload Images** – Provide 1–10 images as visual inspiration.
2. **Select Style** – Choose from genres like *Comedy, Thriller, Fairy Tale, Sci-Fi, Mystery, Adventure,* or *Morale*.
3. **Set Language & Emotion** – Select storytelling language and narration tone.
4. **Gemini 2.5 Magic ✨** –  
   - `gemini-2.5-flash-lite` generates the story from the visual and textual prompt.  
   - `gemini-2.5-flash-preview-tts` narrates it in your chosen voice and emotional tone.
5. **Listen & Enjoy** – The app plays your narrated story instantly.

---
## 🛠️ Pipeline Blueprint

![pipeline](https://github.com/arushssingh/AI-NarrativeFlow/blob/main/assets/pipeline.png)

| Layer                     | Components                     | Description                                       |
| ------------------------- | ------------------------------ | ------------------------------------------------- |
| **User Layer**            | Streamlit App                  | User uploads, selects controls                    |
| **Prompt Layer**          | `create_advanced_prompt()`     | Creates language, emotion, and style-aware prompt |
| **Story Model Layer**     | `gemini-2.5-flash-lite`        | Generates contextual story text from images       |
| **Narration Model Layer** | `gemini-2.5-flash-preview-tts` | Converts story text into emotional audio          |
| **Output Layer**          | Streamlit Renderer             | Displays text and plays back audio                |

---
## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| **Generative AI** | Google Gemini 2.5 (Flash Lite + TTS) |
| **Frontend** | Streamlit |
| **Languages** | Python |
| **Environment** | `.env` (for storing API key) |
| **Libraries** | `google-genai`, `PIL`, `streamlit`, `dotenv`, `wave`, `base64`, `io` |

---

## 🏗️ Project Structure
```bash
AI-NarrativeFlow/
│
├─ main.py    # Core backend functions
├─ app.py     # Streamlit frontend for user interaction
├── assets/                        
│   ├── appInterface_1.png            # e.g., image upload + user choice filling  
│   ├── appInterface_2.png            # e.g., output story with audio 
│   └── pipeline.png                  # working pipeline
├─ requirements.txt # Python dependencies
└─ README.md # Project documentation

```
---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SannidhyaDas/AI-NarrativeFlow.git
cd AI-NarrativeFlow
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment

Create a .env file in the root folder and add your Google API key:
```ini
GOOGLE_API_KEY=your_google_api_key_here
```

### 4️⃣ Run the App
```bash
streamlit run app.py
```

## 🌍 Supported Languages & Voices

| Language             | Gemini Voice Options       |
| -------------------- | -------------------------- |
| English (US)         | Zephyr, Puck, Charon, Kore |
| Hindi (India)        | Kore, Puck                 |
| Bengali (Bangladesh) | Zephyr, Puck               |
| Tamil (India)        | Kore, Puck                 |
| Telugu (India)       | Kore, Puck                 |

## 🎭 Supported Emotions

- neutral
- cheerful
- excited
- sad
- angry
- serious
---
## 💡 Real-World Impact & Use Cases

📚 **AI Storytelling Companion** – Empowers users and creators to turn simple visuals into emotionally rich, multilingual stories — perfect for digital media, education, and entertainment platforms.

🎧 **Language Learning Assistant** – Enhances regional language fluency through story-based listening and contextual narration, supporting India's multilingual learning ecosystem.

🎬 **Creative Script Generator** – Assists writers, filmmakers, and ad creators in ideating scripts or storyboards from visual inspiration — reducing pre-production time and boosting creativity.

🌐 **Inclusive Voice Narration Platform** – Brings stories to life with expressive, emotion-aware voiceovers in multiple Indian languages — making storytelling accessible for all audiences.

🎨 **Content Personalization Engine** – Demonstrates how multimodal GenAI can tailor content to user emotions, language, and context — a use case for personalized media and edtech experiences.

---
## 🏁 Future Enhancements

🎙️ Add custom voice cloning for personalized narration

🖼️ Integrate background music generation

🧠 Add memory to continue stories across sessions

🌐 Extend to more regional languages 
