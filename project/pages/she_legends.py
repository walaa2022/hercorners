import streamlit as st
from elevenlabs import generate, set_api_key, Voice
import google.generativeai as genai
from datetime import datetime
import os
from PIL import Image
from dotenv import load_dotenv
import sys
from pathlib import Path

# Add the root directory to Python path
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

from config import MENTORS

# Load environment variables
load_dotenv()

# Configure APIs
set_api_key(os.getenv('ELEVEN_LABS_API_KEY'))
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def load_mentor_image(mentor_name):
    """Load mentor image from path"""
    try:
        image_path = os.path.join(root_dir, MENTORS[mentor_name]["image"])
        return Image.open(image_path)
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return None

def get_ai_response(mentor, message, conversation_history):
    """Get AI response using Gemini"""
    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"{MENTORS[mentor]['prompt']}\n\nPrevious conversation:\n{conversation_history}\n\nUser: {message}\nYou:"
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
        return "Sorry bestie, I'm having a moment! Let's try again? ✨"

def get_voice_response(text, mentor):
    """Generate voice response using ElevenLabs"""
    try:
        # Debug print to check voice ID
        print(f"Using voice ID for {mentor}: {MENTORS[mentor]['voice_id']}")
        
        # Generate audio with direct voice ID
        audio = generate(
            text=text,
            voice=MENTORS[mentor]["voice_id"],  # Use voice ID directly
            model="eleven_monolingual_v1"  # Specify model explicitly
        )
        
        if audio:
            print(f"Successfully generated voice for {mentor}")
            return audio
        else:
            st.error(f"No audio generated for {mentor}")
            return None
            
    except Exception as e:
        st.error(f"Error generating voice for {mentor}: {str(e)}")
        print(f"Voice generation error details: {str(e)}")
        return None

def show_page():
    st.title("👑 She Legends")
    st.write("Spill the tea with your fave mentors! They've been through it all and are here to share their wisdom!")

    # Initialize session states
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'current_mentor' not in st.session_state:
        st.session_state.current_mentor = None

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### Choose Your Mentor ✨")
        for mentor in MENTORS:
            if st.button(
                f"{mentor}\n{MENTORS[mentor]['role']}",
                key=f"select_{mentor}",
                use_container_width=True
            ):
                st.session_state.current_mentor = mentor
                st.session_state.messages = []
                st.rerun()

    with col2:
        if st.session_state.current_mentor:
            mentor = st.session_state.current_mentor
            mentor_info = MENTORS[mentor]

            # Display mentor card with image
            col_img, col_info = st.columns([1, 2])
            with col_img:
                image = load_mentor_image(mentor)
                if image:
                    st.image(image, use_container_width=True)
            
            with col_info:
                st.markdown(f"""
                    <div style='background-color: {mentor_info["background"]}; padding: 20px; border-radius: 15px;'>
                        <h2>{mentor}</h2>
                        <p><strong>{mentor_info['role']}</strong></p>
                        <p><em>"{mentor_info['quote']}"</em></p>
                        <p>{mentor_info['description']}</p>
                    </div>
                """, unsafe_allow_html=True)

            # Chat interface
            st.markdown("### 💭 Chat Space")
            
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.write(message["content"])
                    if message["role"] == "assistant" and "audio" in message:
                        st.audio(message["audio"])

            # Chat input
            user_message = st.chat_input(f"Ask {mentor} anything...")
            if user_message:
                # Add user message
                st.session_state.messages.append({
                    "role": "user",
                    "content": user_message,
                    "timestamp": datetime.now().strftime("%I:%M %p")
                })

                # Get AI response
                conversation_history = "\n".join([
                    f"{'User' if m['role']=='user' else 'You'}: {m['content']}"
                    for m in st.session_state.messages[-5:]
                ])
                
                ai_response = get_ai_response(mentor, user_message, conversation_history)
                audio = get_voice_response(ai_response, mentor)

                # Add mentor response
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": ai_response,
                    "audio": audio,
                    "timestamp": datetime.now().strftime("%I:%M %p")
                })
                
                st.rerun()

        else:
            st.markdown("""
                ### Hey Bestie! 👋
                Choose your fave mentor from the left to start chatting!
                Each queen brings their own unique vibe and wisdom! ✨
            """)

            # Preview all mentors with images
            for mentor, info in MENTORS.items():
                col_img, col_info = st.columns([1, 3])
                with col_img:
                    image = load_mentor_image(mentor)
                    if image:
                        st.image(image, use_container_width=True)
                
                with col_info:
                    st.markdown(f"""
                        <div style='background-color: {info["background"]}40; padding: 20px; border-radius: 15px;'>
                            <h3>{mentor}</h3>
                            <p>{info['role']}</p>
                            <p><em>"{info['quote']}"</em></p>
                        </div>
                    """, unsafe_allow_html=True)