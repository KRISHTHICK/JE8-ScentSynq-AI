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
