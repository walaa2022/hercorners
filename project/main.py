import streamlit as st

def switch_page(page_name):
    st.session_state.current_page = page_name
    st.rerun()

def show_main():
    # Page config
    st.set_page_config(
        page_title="HerCorners",
        page_icon="✨",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Hide streamlit default menu and footer
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .stDeployButton {display:none;}
            
            /* Style for sidebar buttons */
            div.stButton > button {
                width: 100%;
                padding: 10px 10px;
                border: none;
                background-color: #FFE4E1;
                color: black;
                border-radius: 10px;
                text-align: left;
                margin: 5px 0;
            }
            
            div.stButton > button:hover {
                background-color: #FFB6C1;
                color: white;
            }
            
            /* Style for title box */
            .title-box {
                background: linear-gradient(45deg, #FF69B4, #FFB6C1);
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
                text-align: center;
                color: white;
                cursor: pointer;
            }

            /* Style for home button */
            .home-button {
                background-color: #FFB6C1;
                color: white;
                padding: 10px;
                border-radius: 10px;
                text-align: center;
                margin: 10px 0;
                cursor: pointer;
            }
        </style>
    """, unsafe_allow_html=True)

    # Initialize session state
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'

    # Sidebar navigation
    with st.sidebar:
        # Title box that works as home button
        st.markdown("""
            <div class="title-box" onclick="window.location.href='#'">
                <h1>✨ HerCorners ✨</h1>
                <p>Your safe space to slay! 💅</p>
            </div>
        """, unsafe_allow_html=True)

        # Home button at the top of navigation
        if st.button("🏠 Home", use_container_width=True):
            switch_page('home')

        st.markdown("<hr>", unsafe_allow_html=True)  # Divider

        # Navigation buttons
        if st.button("👑 She Legends", use_container_width=True):
            switch_page('legends')
            
        if st.button("💧 She Melted Mascara", use_container_width=True):
            switch_page('mascara')
            
        if st.button("✨ She Glows", use_container_width=True):
            switch_page('glows')
            
        if st.button("🔥 She Fuels", use_container_width=True):
            switch_page('fuels')

    # Main content area
    if st.session_state.current_page == 'home':
        st.markdown("""
            <div style='text-align: center; padding: 50px;'>
                <h1>Welcome to HerCorners! ✨</h1>
                <p style='font-size: 20px; margin: 20px 0;'>Choose from our spaces:</p>
            </div>
        """, unsafe_allow_html=True)

        # Feature cards
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
                <div style='background-color: #FFE4E1; padding: 20px; border-radius: 10px; margin: 10px 0;'>
                    <h3>👑 She Legends</h3>
                    <p>Chat with inspiring mentors for guidance and support!</p>
                </div>
                
                <div style='background-color: #E6E6FA; padding: 20px; border-radius: 10px; margin: 10px 0;'>
                    <h3>💧 She Melted Mascara</h3>
                    <p>Share your feelings in a safe, supportive space!</p>
                </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
                <div style='background-color: #98FB98; padding: 20px; border-radius: 10px; margin: 10px 0;'>
                    <h3>✨ She Glows</h3>
                    <p>Learn new skills and level up your life!</p>
                </div>
                
                <div style='background-color: #FFB6C1; padding: 20px; border-radius: 10px; margin: 10px 0;'>
                    <h3>🔥 She Fuels</h3>
                    <p>Share your wins and inspire others!</p>
                </div>
            """, unsafe_allow_html=True)

    else:
        # Add home button in main content area when not on home page
        if st.button("🏠 Back to Home", type="secondary"):
            switch_page('home')
            
        # Import and show the appropriate page
        if st.session_state.current_page == 'legends':
            from pages.she_legends import show_page
            show_page()
        elif st.session_state.current_page == 'mascara':
            from pages.she_melted_mascara import show_page
            show_page()
        elif st.session_state.current_page == 'glows':
            from pages.she_glows import show_page
            show_page()
        elif st.session_state.current_page == 'fuels':
            from pages.she_fuels import show_page
            show_page()

if __name__ == "__main__":
    show_main()