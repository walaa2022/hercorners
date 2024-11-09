import streamlit as st
from datetime import datetime
import os
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
import io

# Load environment variables
load_dotenv()
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
        "prompt": """You are a caring friend and art therapist helping with mental health. 
        Use gentle, supportive Gen Z language. Focus on validation, understanding, 
        and providing resources when appropriate.""",
        "description": "Safe space for mental health chat & art sharing 💭"
    }
}

def get_art_analysis(image_data):
    """Get art analysis from Gemini Vision"""
    try:
        # Convert PIL Image to bytes
        if isinstance(image_data, Image.Image):
            img_byte_arr = io.BytesIO()
            image_data.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
        else:
            img_byte_arr = image_data

        # Create vision model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Prepare the image for analysis
        image_parts = [
            {
                "mime_type": "image/png",
                "data": img_byte_arr
            }
        ]
        
        prompt = """You are an empathetic art therapist analyzing artwork. 
        Provide a detailed, caring analysis using Gen Z language and emojis.
        
        Please analyze:
        1. 🎨 Colors & Vibes
        - What emotions do the colors give off?
        - What's the overall mood?
        
        2. 💫 Art Elements
        - What catches your eye?
        - What might these elements mean emotionally?
        
        3. 💕 Emotional Support
        - Validate the feelings you see
        - Share some encouraging words
        
        4. 🌟 Growth & Reflection
        - Ask a gentle question about their feelings
        - Suggest a supportive activity
        
        Use caring, relatable language that teens connect with."""

        # Generate content
        response = model.generate_content([prompt, image_parts[0]])
        
        return response.text

    except Exception as e:
        print(f"Error in art analysis: {str(e)}")
        return """I couldn't fully analyze your art bestie, but I'm here to support you! 💕
                Would you like to tell me more about what you created? I'm all ears! ✨"""
                
# Add this function alongside your existing get_art_analysis function
def get_art_analysis(image_data):
    """Get art analysis from Gemini Vision"""
    try:
        # Convert PIL Image to bytes
        if isinstance(image_data, Image.Image):
            img_byte_arr = io.BytesIO()
            image_data.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
        else:
            img_byte_arr = image_data

        # Create vision model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Prepare the image for analysis
        image_parts = [
            {
                "mime_type": "image/png",
                "data": img_byte_arr
            }
        ]
        
        prompt = """You are an empathetic art therapist analyzing artwork. 
        Provide a caring analysis using Gen Z language and emojis.
        
        🎨 Art Analysis:
        - What emotions and mood do you see in this art?
        - What catches your eye and what might it mean?
        - Share some supportive and encouraging words
        
        Keep your response caring and supportive, using language teens can relate to."""

        # Generate content
        response = model.generate_content([prompt, image_parts[0]])
        
        return response.text

    except Exception as e:
        print(f"Error in art analysis: {str(e)}")
        return """I couldn't fully analyze your art bestie, but I'm here to support you! 💕
                Would you like to tell me more about what you created? I'm all ears! ✨"""
def get_ai_response(message, category, image=None):
    """Get supportive response from Gemini"""
    try:
        if image:
            # If image is provided, use art analysis instead
            return get_art_analysis(image)
        else:
            # Regular chat response
            model = genai.GenerativeModel('gemini-pro')  # Note: Using stable version
            prompt = f"{CATEGORIES[category]['prompt']}\nUser: {message}\nRespond with empathy and support:"
            response = model.generate_content(prompt)
            return response.text
    except Exception as e:
        print(f"Error in get_ai_response: {str(e)}")
        return "I'm here for you bestie! Let's try chatting again? 💕"
    
def show_page():
    st.title("💧 She Melted Mascara")
    st.write("Your safe space to let it all out! No filter needed here bestie 💕")

    # Initialize session states
    if 'current_category' not in st.session_state:
        st.session_state.current_category = None
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = {}
        for category in CATEGORIES:
            st.session_state.chat_history[category] = []
    if 'community_posts' not in st.session_state:
        st.session_state.community_posts = []
    if 'view' not in st.session_state:
        st.session_state.view = 'categories'
        # Layout
    col1, col2 = st.columns([1, 2])

    # Left Column Navigation
    with col1:
        st.markdown("### Choose Your Space 💕")
        
        # Category buttons
        for category in CATEGORIES:
            if st.button(
                f"{category}\n{CATEGORIES[category]['description']}",
                key=f"cat_{category}",
                use_container_width=True
            ):
                st.session_state.current_category = category
                st.session_state.view = 'chat'
                st.rerun()

        # Community button
        if st.button("💕 Community Board\nSee shared stories & support others", 
                    key="community", use_container_width=True):
            st.session_state.view = 'community'
            st.rerun()

    # Right Column Content
    with col2:
        if st.session_state.view == 'chat' and st.session_state.current_category:
            category = st.session_state.current_category
            
            # Category Header
            st.markdown(f"""
                <div style='background-color: {CATEGORIES[category]["color"]}40; 
                         padding: 15px; border-radius: 10px; margin-bottom: 20px;'>
                    <h3>{category}</h3>
                    <p>{CATEGORIES[category]["description"]}</p>
                </div>
            """, unsafe_allow_html=True)

            # Chat mode selection
            chat_mode = st.radio(
                "Choose your chat mode:",
                ["💭 Private Chat", "✨ Public Share"],
                horizontal=True
            )

            if chat_mode == "💭 Private Chat":
                # Mental Health category special features
                if category == "🧠 Mental Health":
                    tab1, tab2 = st.tabs(["💭 Chat", "🎨 Art Expression"])
                    
                    with tab1:
                        # Display chat history
                        for message in st.session_state.chat_history[category]:
                            with st.chat_message(message["role"]):
                                st.write(message["content"])
                                if "image" in message:
                                    st.image(message["image"])

                        # Chat input
                        if prompt := st.chat_input("Share your feelings..."):
                            # Add user message
                            st.session_state.chat_history[category].append({
                                "role": "user",
                                "content": prompt,
                                "timestamp": datetime.now().strftime("%I:%M %p")
                            })
                            
                            # Get AI response
                            response = get_ai_response(prompt, category)
                            st.session_state.chat_history[category].append({
                                "role": "assistant",
                                "content": response,
                                "timestamp": datetime.now().strftime("%I:%M %p")
                            })
                            st.rerun()

                    with tab2:
                        st.write("Express yourself through art 🎨")
                        st.write("Share your artwork and get supportive analysis ✨")
                        uploaded_file = st.file_uploader(
                            "Upload your drawing",
                            type=['png', 'jpg', 'jpeg']
                        )
                        
                        if uploaded_file:
                            image = Image.open(uploaded_file)
                            st.image(image, caption="Your artwork 🎨")
                            
                            share_option = st.radio(
                                "Would you like to:",
                                ["Get private analysis ✨", "Share with community 💕"],
                                key="art_share_option"
                            )
                            

                            if st.button("✨ Analyze My Art"):
                                with st.spinner("Analyzing your artwork with care and empathy... 💫"):
                                    # Get AI analysis
                                    analysis = get_ai_response(None, category, image)
                                    
                                    if share_option == "Get private analysis ✨":
                                        # Display analysis directly
                                        st.markdown("### 🎨 Art Analysis")
                                        st.markdown(analysis)
                                        
                                        # Add to chat history
                                        st.session_state.chat_history[category].append({
                                            "role": "user",
                                            "content": "I created this artwork to express my feelings...",
                                            "image": image,
                                            "timestamp": datetime.now().strftime("%I:%M %p")
                                        })
                                        
                                        st.session_state.chat_history[category].append({
                                            "role": "assistant",
                                            "content": analysis,
                                            "timestamp": datetime.now().strftime("%I:%M %p")
                                        })
                                        
                                        # Simple follow-up option
                                        if st.button("Share more about your art? 💫"):
                                            st.markdown("I'd love to hear more about what inspired this piece! What were you feeling while creating it? 💕")
                                    
                                    else:  # Share with community
                                        # Add to community posts
                                        st.session_state.community_posts.insert(0, {
                                            "category": category,
                                            "content": "Expressing my feelings through art...",
                                            "image": image,
                                            "support_message": analysis,
                                            "timestamp": datetime.now().strftime("%I:%M %p"),
                                            "hugs": 0,
                                            "support": 0,
                                            "comments": []
                                        })
                                        st.success("Thank you for sharing your art! The community is here for you 💕")
                                        
                                        # Follow-up options
                                        st.markdown("### Would you like to... 💭")
                                        col1, col2 = st.columns(2)
                                        with col1:
                                            if st.button("Share more about this 💫"):
                                                followup_msg = "I'm here to listen and understand. Would you like to tell me more about what inspired this artwork? 💕"
                                                st.session_state.chat_history[category].append({
                                                    "role": "assistant",
                                                    "content": followup_msg,
                                                    "timestamp": datetime.now().strftime("%I:%M %p")
                                                })
                                                st.markdown(followup_msg)
                                        
                                        with col2:
                                            if st.button("Get support tips 🌟"):
                                                support_msg = get_ai_response(
                                                    "Based on this artwork, what helpful coping strategies would you suggest?",
                                                    category
                                                )
                                                st.session_state.chat_history[category].append({
                                                    "role": "assistant",
                                                    "content": support_msg,
                                                    "timestamp": datetime.now().strftime("%I:%M %p")
                                                })
                                                st.markdown(support_msg)
                                    
                        

                else:
                    # Regular chat interface for other categories
                    for message in st.session_state.chat_history[category]:
                        with st.chat_message(message["role"]):
                            st.write(message["content"])

                    if prompt := st.chat_input("Tell me what's on your mind..."):
                        # Add user message
                        st.session_state.chat_history[category].append({
                            "role": "user",
                            "content": prompt,
                            "timestamp": datetime.now().strftime("%I:%M %p")
                        })
                        
                        # Get AI response
                        response = get_ai_response(prompt, category)
                        st.session_state.chat_history[category].append({
                            "role": "assistant",
                            "content": response,
                            "timestamp": datetime.now().strftime("%I:%M %p")
                        })
                        st.rerun()

            else:  # Public Share mode
                with st.form(key=f"public_share_{category}"):
                    st.write("Share with the community 💕")
                    share_text = st.text_area("Your story matters!")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        anonymous = st.checkbox("Stay anonymous", value=True)
                    with col2:
                        allow_comments = st.checkbox("Allow comments", value=True)
                    
                    if st.form_submit_button("Share 💝"):
                        if share_text:
                            # Get AI support message
                            support_msg = get_ai_response(share_text, category)
                            
                            # Add to community posts
                            st.session_state.community_posts.insert(0, {
                                "category": category,
                                "content": share_text,
                                "support_message": support_msg,
                                "timestamp": datetime.now().strftime("%I:%M %p"),
                                "anonymous": anonymous,
                                "allow_comments": allow_comments,
                                "hugs": 0,
                                "support": 0,
                                "comments": []
                            })
                            st.success("Thanks for sharing, bestie! 💕")
                            st.rerun()

        elif st.session_state.view == 'community':
            st.markdown("### 💕 Community Board")
            
            # Filter options
            col1, col2 = st.columns([2, 1])
            with col1:
                filter_cat = st.selectbox(
                    "Filter by category",
                    ["All"] + list(CATEGORIES.keys())
                )
            with col2:
                sort_by = st.selectbox(
                    "Sort by",
                    ["Latest", "Most Support", "Most Hugs"]
                )

            # Sort posts
            posts = st.session_state.community_posts.copy()
            if sort_by == "Most Support":
                posts.sort(key=lambda x: x.get('support', 0), reverse=True)
            elif sort_by == "Most Hugs":
                posts.sort(key=lambda x: x.get('hugs', 0), reverse=True)

            # Display posts
            for idx, post in enumerate(posts):
                if filter_cat == "All" or filter_cat == post["category"]:
                    with st.container():
                        # Post content
                        st.markdown(f"""
                            <div style='background-color: {CATEGORIES[post["category"]]["color"]}40; 
                                     padding: 15px; border-radius: 10px; margin: 10px 0;'>
                                <p style='color: #666; font-size: 0.9em;'>
                                    {post["category"]} • {"Anonymous" if post.get("anonymous", True) else "Someone"} • {post["timestamp"]}
                                </p>
                                <p>{post["content"]}</p>
                            </div>
                        """, unsafe_allow_html=True)

                        # Display image if present
                        if "image" in post:
                            st.image(post["image"])

                        # Support message if present
                        if "support_message" in post:
                            st.info(post["support_message"])

                        # Interaction buttons
                        col1, col2, col3 = st.columns([1,1,2])
                        with col1:
                            if st.button(f"🫂 Hug ({post.get('hugs', 0)})", key=f"hug_{idx}"):
                                post['hugs'] = post.get('hugs', 0) + 1
                                st.rerun()
                        with col2:
                            if st.button(f"💝 Support ({post.get('support', 0)})", key=f"support_{idx}"):
                                post['support'] = post.get('support', 0) + 1
                                st.rerun()
                        with col3:
                            if post.get('allow_comments', True):
                                with st.expander("💭 Comments"):
                                    # Display existing comments
                                    for comment in post.get('comments', []):
                                        st.write(f"Anonymous: {comment}")
                                    
                                    # Add new comment
                                    new_comment = st.text_input("Add a supportive comment", key=f"comment_{idx}")
                                    if st.button("Send 💕", key=f"send_{idx}"):
                                        if new_comment:
                                            if 'comments' not in post:
                                                post['comments'] = []
                                            post['comments'].append(new_comment)
                                            st.rerun()

        else:
            st.markdown("""
                ### Welcome to Your Safe Space! 💕
                Choose a category on the left to:
                - Chat privately with AI support
                - Share with the community
                - Give and receive support
                
                Remember: You're never alone here! 🫂
            """)
