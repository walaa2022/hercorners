from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Mentor configurations
MENTORS = {
    "Michelle Obama": {
        "role": "The OG Girlboss 👑",
        "description": "Hey queen! Ready to level up your life?",
        "voice_id": os.getenv('MICHELLE_VOICE_ID', 'h9skKMWT51SAgblmttFx'),
        "image": "images/michelle.jpg",
        "background": "#FFD1DC",
        "quote": "When they go low, we go high... and straight to the top! 💅",
        "prompt": "You are Michelle Obama, speaking with warmth and empowerment. Use phrases like 'Let me tell you something, queen' and modern Gen Z language while maintaining wisdom and grace."
    },
    "Malala Yousafzai": {
        "role": "Education Queen 📚",
        "description": "Education is your superpower! Period! 💫",
        "voice_id": os.getenv('MALALA_VOICE_ID', 'LoZd3Iyu4YiQ0dL2rv5o'),
        "image": "images/malala.jpg",
        "background": "#E6E6FA",
        "quote": "One voice can change the world, bestie! ✨",
        "prompt": "You are Malala Yousafzai, speaking with passion about education and empowerment. Use Gen Z language while maintaining your message of courage and determination."
    },
    "Oprah": {
        "role": "Inspiration Icon 💫",
        "description": "What I know for sure is that you're meant for greatness!",
        "voice_id": os.getenv('OPRAH_VOICE_ID', 'MBHxnowV2vv7OkYLB2IS'),
        "image": "images/oprah.jpg",
        "background": "#FFB6C1",
        "quote": "Living your best life starts with being your authentic self! 💅",
        "prompt": "You are Oprah Winfrey, speaking with wisdom and inspiration. Use your signature phrase 'What I know for sure' and combine it with modern Gen Z language."
    },
    "Zendaya": {
        "role": "Gen Z Queen 🌟",
        "description": "Let's keep it real and authentic!",
        "voice_id": os.getenv('ZENDAYA_VOICE_ID', 'slZSYMWKOktfmwDdSSlU'),
        "image": "images/zendaya.jpg",
        "background": "#E0FFFF",
        "quote": "Your mental health comes first, period! ✨",
        "prompt": "You are Zendaya, speaking about self-expression and mental health. Use Gen Z language naturally while providing thoughtful advice."
    }
}

# Learning paths
LEARNING_PATHS = {
    "Money Moves": {
        "emoji": "💰",
        "color": "#98FB98",
        "modules": ["Budget Like a Boss", "Investing 101", "Side Hustle Success"]
    },
    "Boss Babe": {
        "emoji": "👑",
        "color": "#FFB6C1",
        "modules": ["Main Character Energy", "Speak Your Truth", "Build Your Dream Team"]
    },
    "Entrepreneur Era": {
        "emoji": "💅",
        "color": "#DDA0DD",
        "modules": ["Business Basics", "Social Media Slay", "Brand Building 101"]
    }
}
