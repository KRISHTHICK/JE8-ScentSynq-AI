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
