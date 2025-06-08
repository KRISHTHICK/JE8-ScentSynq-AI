# JE8-ScentSynq-AI
GenAi

Great! Here's a brand new AI project topic that’s different from previous fashion or tradition-based ideas. This one focuses on personalized scent recommendations, which can be applied to fashion, wellness, or luxury retail.

---

## 🧪🕯️ **ScentSynq AI – Personalized Perfume & Aroma Matchmaker**

### 🧠 **Project Idea**:

**ScentSynq AI** is an interactive AI-powered aroma stylist that recommends personalized perfume blends and home fragrance combinations based on user mood, event, season, or even outfit type. Using a combination of a local LLM (via **Ollama**), **Python**, and **Streamlit**, it creates a sensory style guide.

It is designed to run locally in **VS Code** and can be deployed via **GitHub Pages** or Streamlit Cloud.

---

### 🌟 **Key Features**:

| Feature                                | Description                                                         |
| -------------------------------------- | ------------------------------------------------------------------- |
| 🌺 **Mood-Based Scent Generator**      | Generates perfume or diffuser recommendations based on user mood    |
| 👗 **Outfit & Occasion Sync**          | Matches scent with attire, event, and personality                   |
| 🧪 **Custom Fragrance Composer**       | Suggests blendable scent profiles (e.g., base, middle, top notes)   |
| 📅 **Seasonal & Time-of-Day Adjuster** | Recommends different aromas for summer evenings vs. winter mornings |
| 💬 **Aroma Advisor Agent (Ollama)**    | Chat with an agent for lifestyle-based aroma suggestions            |
| 📝 **Caption & Name Generator**        | Generates poetic scent names and social captions for perfumes       |

---

### 🗂️ **Folder Structure**

```
ScentSynq-AI/
├── app.py
├── scent_agent.py
├── aroma_utils.py
├── assets/
│   └── sample_perfumes/
├── requirements.txt
└── README.md
```

---

### 📄 `requirements.txt`

```
streamlit
ollama
Pillow
```

---

### ▶️ `app.py`

```python
import streamlit as st
from PIL import Image
from aroma_utils import suggest_scents, generate_blend
from scent_agent import chat_with_agent

st.set_page_config(page_title="ScentSynq AI", layout="wide")

st.title("🧪🕯️ ScentSynq AI – Personalized Perfume & Aroma Stylist")
st.markdown("Tell us your mood, event, or upload your outfit. We'll find your signature scent.")

mood = st.selectbox("🌈 What's your current mood?", ["Romantic", "Adventurous", "Calm", "Energized"])
event = st.text_input("🎉 What's the occasion?", "Evening Gala")

st.subheader("🔮 Recommended Scent Profiles:")
scent_suggestions = suggest_scents(mood, event)
st.markdown(scent_suggestions)

st.subheader("🧪 Your Custom Blend:")
blend = generate_blend(mood)
st.success(f"Top Note: {blend['top']} | Middle: {blend['middle']} | Base: {blend['base']}")

st.subheader("💬 Ask the Aroma AI Agent:")
prompt = st.text_input("Type your lifestyle or scent preference...")
if prompt:
    response = chat_with_agent(prompt)
    st.markdown(response)
```

---

### 🤖 `scent_agent.py`

```python
import subprocess

def chat_with_agent(prompt):
    user_input = f"Suggest a custom scent or perfume idea for: {prompt}"
    result = subprocess.run(["ollama", "run", "tinyllama", user_input], capture_output=True, text=True)
    return result.stdout.strip()
```

---

### 🌺 `aroma_utils.py`

```python
import random

def suggest_scents(mood, event):
    mood_map = {
        "Romantic": "Rose, Jasmine, Sandalwood",
        "Adventurous": "Cedarwood, Vetiver, Citrus Zest",
        "Calm": "Lavender, Chamomile, Musk",
        "Energized": "Lemon, Mint, Green Tea"
    }
    return f"For a **{mood}** mood and **{event}**, try: {mood_map.get(mood)}"

def generate_blend(mood):
    top_notes = ["Lemon", "Bergamot", "Mint", "Ylang-Ylang"]
    middle_notes = ["Jasmine", "Rose", "Cinnamon", "Green Tea"]
    base_notes = ["Musk", "Sandalwood", "Amber", "Vanilla"]

    return {
        "top": random.choice(top_notes),
        "middle": random.choice(middle_notes),
        "base": random.choice(base_notes)
    }
```

---

### 🧾 `README.md`

````markdown
# 🧪🕯️ ScentSynq AI

ScentSynq AI is a personalized AI aroma stylist built with Streamlit and Ollama. It suggests fragrance profiles based on mood, event, or outfit.

## 🚀 How to Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
````

2. **Run the app**:

   ```bash
   streamlit run app.py
   ```

3. **Ensure Ollama is installed**:

   * Start Ollama server
   * Use a local LLM like TinyLLaMA

## 🧠 Features

* Mood & event-based scent suggestions
* Custom fragrance blend generator
* AI-based aroma advisor
* Captions for social media perfume branding

```

---

Would you like this deployed setup connected with GitHub Pages or Streamlit Cloud instructions next?
```
