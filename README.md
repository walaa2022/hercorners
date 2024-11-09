# HerCorners - Your Digital Safe Space to Slay! ✨

A multi-modal AI platform empowering Gen Z girls through mentor chats, emotional support, and skill development.

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- Active internet connection

### 🌟 Installation Steps

1. **Download the Project**
   ```bash
   # Clone the repository
   git clone https://github.com/[username]/hercorners.git
   cd hercorners
   ```

2. **Install Dependencies**
   ```bash
   # Install required packages
   pip install -r requirements-final.txt
   ```

   Required packages:
   - streamlit==1.24.0
   - google-generativeai==0.3.1
   - elevenlabs==0.2.24
   - python-dotenv==1.0.0
   - Pillow==9.5.0
   - requests==2.31.0
   - python-dateutil==2.8.2

3. **API Keys Setup**
   - Get Gemini API Key from: https://makersuite.google.com/app/apikey
   - Get ElevenLabs API Key from: https://elevenlabs.io/speech-synthesis
   
   Create `.env` file in project root:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key
   ELEVEN_LABS_API_KEY=your_elevenlabs_key
   ```

4. **Run the App**
   ```bash
   streamlit run main.py
   ```

5. **Access the App**
   - Open browser: http://localhost:8501/
   - Or use link from terminal

## 📁 Project Structure
```
hercorners/
├── main.py                 # Main application file
├── .env                    # Environment variables
├── requirements-final.txt  # Dependencies
├── config.py              # Configuration settings
├── pages/
│   ├── she_legends.py     # AI Mentor chats
│   ├── she_melted_mascara.py  # Emotional support
│   ├── she_glows.py       # Learning paths
│   └── she_fuels.py       # Achievement sharing
└── images/                # Mentor images
```

## ✨ Features

### 👑 She Legends
- Voice-enabled AI mentor chats
- Inspiring role model personas
- Personalized advice

### 💧 She Melted Mascara
- Emotional support chat
- AI art therapy analysis
- Safe sharing space

### 🌟 She Glows
- Interactive learning paths
- Skill development
- Achievement tracking

### 🔥 She Fuels
- Achievement sharing
- Community support
- Success celebration

## 🛠️ Technologies Used
- Gemini AI for conversations and art analysis
- ElevenLabs for voice synthesis
- Streamlit for web interface
- Python for backend logic

## ⚠️ Troubleshooting

### Common Issues:
1. **API Keys**
   - Verify keys in `.env`
   - Check quota limits
   - Ensure proper formatting

2. **Image Upload**
   - Use PNG/JPEG formats
   - Keep files under 5MB
   - Check permissions

3. **Voice Synthesis**
   - Verify ElevenLabs key
   - Check internet connection
   - Try page refresh

## 📫 Support
- Create an issue
- Contact walaa.nasr@lablab.club

## 👩‍💻 Contributing
We welcome contributions! 

## 📄 License

MIT License

Copyright (c) 2024 HerCorners

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---
Created with 💕 for Gen Z girls to slay!
