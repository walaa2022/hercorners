import streamlit as st
from datetime import datetime
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Define categories with their properties
CATEGORIES = {
    "💔 Heartbreak Hotel": {
        "color": "#FFB6C1",
        "prompt": "You are an empathetic friend helping with heartbreak. Use gentle, supportive, Gen Z language.",
        "description": "Share your heart feels & get support 💕"
    },
    "🏠 Family Tea": {
        "color": "#E6E6FA",
        "prompt": "You are a wise friend helping with family issues. Use understanding, Gen Z language.",
        "description": "Spill the family tea & get advice 🫂"
    },
    "📚 School Stress": {
        "color": "#98FB98",
        "prompt": "You are a supportive friend helping with school stress. Use encouraging, Gen Z language.",
        "description": "Academic pressure? Let's talk it out 📝"
    },
    "🧠 Mental Health": {
        "color": "#DDA0DD",
        "prompt": "You are a caring friend helping with mental health. Use gentle, supportive Gen Z language.",
        "description": "Safe space for mental health chat 💭"
    }
}

def get_ai_response(message, category):
    """Get supportive response from Gemini"""
    try:
        prompt = f"{CATEGORIES[category]['prompt']}\nUser: {message}\nRespond with empathy and support:"
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "I'm here for you bestie! Let's try chatting again? 💕"

def show_page():
    st.title("💧 She Melted Mascara")
    st.write("Your safe space to let it all out! No filter needed here bestie 💕")

    # Initialize session state
    if 'current_category' not in st.session_state:
        st.session_state.current_category = None
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = {}
        for category in CATEGORIES:
            st.session_state.chat_messages[category] = []
    if 'community_posts' not in st.session_state:
        st.session_state.community_posts = []

    # Layout
    col1, col2 = st.columns([1, 2])

    # Category Selection (Left Column)
    with col1:
        st.markdown("### Choose Your Space 💕")
        
        # Create buttons for each category
        for category in CATEGORIES:
            if st.button(
                category + "\n" + CATEGORIES[category]['description'],
                key=f"cat_{category}",
                use_container_width=True,
            ):
                st.session_state.current_category = category
                st.session_state.reload = not st.session_state.get('reload', False)  # Toggle reload

        # Add Community Board button
        if st.button(
            "✨ Community Board\nSee what others are sharing",
            use_container_width=True,
            key="community_board"
        ):
            st.session_state.current_category = "community"
            st.session_state.reload = not st.session_state.get('reload', False)  # Toggle reload

    # Main Content (Right Column)
    with col2:
        if st.session_state.current_category == "community":
            # Community Board View
            st.markdown("### ✨ Community Board")
            
            # Filter options
            filter_cat = st.selectbox(
                "Filter by category",
                ["All"] + list(CATEGORIES.keys())
            )
            
            # Initialize hug and support counts if missing
            for post in st.session_state.community_posts:
                if "hugs" not in post:
                    post["hugs"] = 0
                if "support" not in post:
                    post["support"] = 0
            
            # Display posts
            for idx, post in enumerate(st.session_state.community_posts):
                if filter_cat == "All" or filter_cat == post["category"]:
                    with st.container():
                        st.markdown(f"""
                            <div style='background-color: {CATEGORIES[post["category"]]["color"]}40; 
                                         padding: 15px; border-radius: 10px; margin: 10px 0;'>
                                <p style='color: #666; font-size: 0.9em;'>
                                    {post["category"]} • Anonymous • {post["timestamp"]}
                                </p>
                                <p>{post["content"]}</p>
                                <p>🫂 Hugs: {post["hugs"]} | 💕 Support: {post["support"]}</p>
                            </div>
                        """, unsafe_allow_html=True)
                        
                        col1, col2 = st.columns([1, 3])
                        with col1:
                            if st.button("🫂 Send Hug", key=f"hug_{post['timestamp']}_{idx}"):
                                post["hugs"] += 1  # Increment hug count
                                st.session_state.reload = not st.session_state.get('reload', False)  # Toggle reload

                        with col2:
                            if st.button("💕 Send Support", key=f"support_{post['timestamp']}_{idx}"):
                                post["support"] += 1  # Increment support count
                                st.session_state.reload = not st.session_state.get('reload', False)  # Toggle reload

        elif st.session_state.current_category:
            # Chat Interface for Selected Category
            category = st.session_state.current_category
            
            # Category Header
            st.markdown(f"""
                <div style='background-color: {CATEGORIES[category]["color"]}40; 
                         padding: 15px; border-radius: 10px; margin-bottom: 20px;'>
                    <h3>{category}</h3>
                    <p>{CATEGORIES[category]["description"]}</p>
                </div>
            """, unsafe_allow_html=True)

            # Chat History
            chat_container = st.container()
            with chat_container:
                for message in st.session_state.chat_messages[category]:
                    with st.chat_message(message["role"]):
                        st.write(message["content"])

            # Share options
            share_type = st.radio(
                "How would you like to share?",
                ["💭 Private Chat", "✨ Share with Community"],
                horizontal=True
            )

            if share_type == "💭 Private Chat":
                # Chat input
                if prompt := st.chat_input("Tell me what's on your mind..."):
                    # Add user message
                    st.session_state.chat_messages[category].append({
                        "role": "user",
                        "content": prompt
                    })
                    
                    # Get and add AI response
                    response = get_ai_response(prompt, category)
                    st.session_state.chat_messages[category].append({
                        "role": "assistant",
                        "content": response
                    })
                    st.session_state.reload = not st.session_state.get('reload', False)  # Toggle reload

            else:
                # Community share form
                with st.form(f"share_form_{category}"):
                    share_text = st.text_area(
                        "Share with the community...",
                        placeholder="Your story matters! Share it here 💕"
                    )
                    
                    if st.form_submit_button("Share Anonymously 💝"):
                        if share_text:
                            # Add to community posts
                            st.session_state.community_posts.insert(0, {
                                "category": category,
                                "content": share_text,
                                "timestamp": datetime.now().strftime("%I:%M %p"),
                                "hugs": 0,
                                "support": 0
                            })
                            
                            # Get and show AI support
                            support = get_ai_response(share_text, category)
                            st.success("Thanks for sharing, bestie! You're so brave! 💕")
                            st.info(f"Support Message: {support}")
                            st.session_state.reload = not st.session_state.get('reload', False)  # Toggle reload

        else:
            # Welcome Screen
            st.markdown("""
                ### Welcome to Your Safe Space! 💕
                
                Choose a category from the left to:
                - Chat privately with our AI bestie
                - Share with the community
                - Give and receive support
                
                Remember: You're never alone here! 🫂
            """)