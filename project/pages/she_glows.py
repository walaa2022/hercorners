import streamlit as st
import google.generativeai as genai
from datetime import datetime
import os
from dotenv import load_dotenv

# Initialize Gemini
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Learning paths focused on modern skills
LEARNING_PATHS = {
    "💰 Money Queen": {
        "emoji": "💰",
        "color": "#98FB98",
        "description": "Master your money! From budgeting to investing, get that bag! 💅",
        "modules": [
            {
                "title": "Budget Like a Boss",
                "topics": ["Personal budgeting", "Saving strategies", "Money mindset"],
                "prompt": "You're teaching teen girls about {topic}. Use Gen Z language, be encouraging, and give practical examples they can relate to."
            },
            {
                "title": "Investing 101",
                "topics": ["Stock market basics", "Investment apps", "Long-term planning"],
                "prompt": "Explain {topic} to teen girls using Gen Z language. Make investing concepts fun and relatable."
            },
            {
                "title": "Side Hustle Era",
                "topics": ["Online business ideas", "Digital marketing", "Pricing strategies"],
                "prompt": "Share practical advice about {topic} for teen entrepreneurs. Use trendy language and real examples."
            }
        ]
    },
    "🤖 AI & Tech Bestie": {
        "emoji": "🤖",
        "color": "#FFB6C1",
        "description": "Slay the AI game! Learn to use AI tools like a pro! ✨",
        "modules": [
            {
                "title": "AI Tools Mastery",
                "topics": ["Gemini basics", "ChatGPT tips", "Prompt writing"],
                "prompt": "Teach teen girls how to use {topic}. Include practical examples and creative ways to use AI tools."
            },
            {
                "title": "Content Creation",
                "topics": ["AI writing tools", "Image generation", "Video editing AI"],
                "prompt": "Explain how to use {topic} for content creation. Include trendy examples and creative ideas."
            },
            {
                "title": "AI Business Ideas",
                "topics": ["AI services", "Online tutoring", "Digital products"],
                "prompt": "Share ideas for {topic} that teen girls can start. Make it practical and achievable."
            }
        ]
    },
    "👑 Business Queen": {
        "emoji": "👑",
        "color": "#DDA0DD",
        "description": "Build your empire! Learn business & marketing secrets! 💫",
        "modules": [
            {
                "title": "Business Basics",
                "topics": ["Business planning", "Market research", "Branding"],
                "prompt": "Explain {topic} in Gen Z language. Use examples relevant to teen entrepreneurs."
            },
            {
                "title": "Social Media Empire",
                "topics": ["Content strategy", "Growth hacks", "Monetization"],
                "prompt": "Share practical tips for {topic}. Include trending platforms and strategies."
            },
            {
                "title": "Customer Queen",
                "topics": ["Customer service", "Community building", "Brand loyalty"],
                "prompt": "Teach about {topic} using relatable examples for teen business owners."
            }
        ]
    }
}

def get_ai_lesson(path, module, topic):
    """Get personalized lesson from Gemini"""
    try:
        prompt = f"{LEARNING_PATHS[path]['modules'][module]['prompt'].format(topic=topic)}\n\nProvide a fun, interactive lesson with:\n1. Key points\n2. Real examples\n3. Action steps\n4. Pro tips"
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "Oops! Let's try that lesson again bestie! 💕"

def create_practice_task(path, module, topic):
    """Generate practice task using Gemini"""
    try:
        prompt = f"""Create a practical task for teen girls learning about {topic}.
        Make it:
        1. Fun and engaging
        2. Actually doable
        3. Related to real life
        4. Something they can complete in 15-30 minutes
        Use Gen Z language and emojis!"""
        
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "Let's try another task bestie! 💕"

def show_page():
    st.markdown("""
        <h1 style='text-align: center;'>✨ She Glows ✨</h1>
        <p style='text-align: center;'>Level up your skills & secure that bag! 💅</p>
    """, unsafe_allow_html=True)

    # Initialize session state
    if 'current_path' not in st.session_state:
        st.session_state.current_path = None
    if 'progress' not in st.session_state:
        st.session_state.progress = {}
    if 'achievements' not in st.session_state:
        st.session_state.achievements = []

    # Create columns
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### Choose Your Glow Up ✨")
        
        # Path selection buttons
        for path, info in LEARNING_PATHS.items():
            if st.button(
                f"{info['emoji']} {path}",
                key=f"path_{path}",
                use_container_width=True
            ):
                st.session_state.current_path = path
                st.rerun()

        # Show achievements
        if st.session_state.achievements:
            st.markdown("### Your Achievements 🏆")
            for achievement in st.session_state.achievements:
                st.markdown(f"- {achievement['emoji']} {achievement['title']}")

    with col2:
        if st.session_state.current_path:
            path = st.session_state.current_path
            path_info = LEARNING_PATHS[path]

            # Display path info
            st.markdown(f"""
                <div style='background-color: {path_info['color']}30; 
                         padding: 20px; border-radius: 15px; margin-bottom: 20px;'>
                    <h3>{path_info['emoji']} {path}</h3>
                    <p>{path_info['description']}</p>
                </div>
            """, unsafe_allow_html=True)

            # Show modules
            st.markdown("### Your Modules 📚")
            for i, module in enumerate(path_info['modules']):
                with st.expander(f"{module['title']} ✨"):
                    # Topics in module
                    for topic in module['topics']:
                        st.markdown(f"#### {topic}")
                        
                        # Get lesson
                        if st.button(f"Learn about {topic} 📚", key=f"learn_{topic}"):
                            lesson = get_ai_lesson(path, i, topic)
                            st.markdown(lesson)
                            
                            # Practice task
                            st.markdown("### Practice Time! 💪")
                            task = create_practice_task(path, i, topic)
                            st.info(task)
                            
                            # Complete button
                            if st.button("I've completed this! ✅", key=f"complete_{topic}"):
                                # Add achievement
                                achievement = {
                                    'title': f"Mastered {topic}",
                                    'emoji': "🌟",
                                    'date': datetime.now().strftime("%B %d, %Y")
                                }
                                st.session_state.achievements.append(achievement)
                                st.balloons()
                                st.success("Yass queen! Keep slaying! 👑")
                                st.rerun()

        else:
            st.markdown("""
                ### Welcome to Your Glow Up Journey! ✨
                
                Choose your path to start:
                - 💰 Money Queen: Master your finances
                - 🤖 AI & Tech Bestie: Learn AI tools
                - 👑 Business Queen: Start your empire
                
                Let's level up together! 💅
            """)