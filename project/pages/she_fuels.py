import streamlit as st
import google.generativeai as genai
from datetime import datetime
import os
from dotenv import load_dotenv

def show_page():
    # Configure Gemini
    load_dotenv()
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

    # Page title
    st.title("🔥 She Fuels")
    st.write("Share your wins & get support! ✨")

    # Initialize session state for posts
    if 'posts' not in st.session_state:
        st.session_state.posts = []

    # Two columns layout
    col1, col2 = st.columns([1, 2])

    with col1:
        # Simple share form
        st.markdown("### Share Your Win ✨")
        
        # Category selection
        category = st.selectbox(
            "Type of win:",
            ["✨ Achievement", "💪 Challenge Overcome", "💡 Advice to Share"]
        )
        
        # Share story
        story = st.text_area(
            "What's your win?",
            placeholder="Share something you're proud of..."
        )
        
        if st.button("Share ✨"):
            if story:
                try:
                    # Get AI support response
                    model = genai.GenerativeModel('gemini-pro')
                    prompt = f"""As a supportive friend, respond to this achievement using Gen Z language and emojis:
                    Category: {category}
                    Story: {story}
                    Keep it encouraging and specific to their achievement!"""
                    
                    response = model.generate_content(prompt)
                    
                    # Add post
                    new_post = {
                        'category': category,
                        'content': story,
                        'support': response.text,
                        'time': datetime.now().strftime("%I:%M %p"),
                        'likes': 0
                    }
                    st.session_state.posts.insert(0, new_post)
                    st.success("Posted! Thanks for sharing! ✨")
                    st.rerun()
                    
                except Exception as e:
                    st.error("Oops! Try sharing again! 💕")

    with col2:
        # Display posts
        st.markdown("### Community Wins ✨")
        
        for post in st.session_state.posts:
            with st.container():
                # Post content with styling
                st.markdown(f"""
                    <div style='
                        background-color: #FFE4E1;
                        padding: 15px;
                        border-radius: 10px;
                        margin: 10px 0;'>
                        <p style='color: #666; font-size: 0.9em;'>
                            {post['category']} • {post['time']}
                        </p>
                        <p>{post['content']}</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # AI support message
                st.info(post['support'])
                
                # Simple interaction
                if st.button(f"✨ Send Support ({post['likes']})", key=f"like_{post['time']}"):
                    post['likes'] += 1
                    st.balloons()
                    st.rerun()
        
        if not st.session_state.posts:
            st.markdown("""
                ### Share Your First Win! ✨
                Be the first to inspire others! 💫
            """)