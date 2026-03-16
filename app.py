import streamlit as st
from google import genai
from google.genai import types
from google.oauth2 import service_account
from PIL import Image
import io

# --- 1. THE SAFETY SWITCH - this is set to avoid billing during my multiple runs for testing---
# This was Set to True only for the final Run and Demo video!
HACKATHON_MODE = False

# --- 2. To Set PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Gemini 3 Master Agent",
    page_icon="🤖",
    layout="wide"
)

# --- 3. I used CSS FOR ANIMATED PULSING LOGO ---
st.markdown("""
<style>
@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(0, 210, 255, 0.7); transform: scale(1); }
  70% { box-shadow: 0 0 0 20px rgba(0, 210, 255, 0); transform: scale(1.05); }
  100% { box-shadow: 0 0 0 0 rgba(0, 210, 255, 0); transform: scale(1); }
}
.master-logo {
    background: linear-gradient(135deg, #00d2ff 0%, #3a7bd5 100%);
    border-radius: 50%;
    width: 80px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: bold;
    font-size: 28px;
    animation: pulse 2s infinite;
    margin: 10px auto;
    border: 3px solid #ffffff;
}
</style>
""", unsafe_allow_html=True)

# --- 4. API INITIALIZATION (THE "SWITCH" PATH) 
# this dual mode was set to minimize the billing cost---
def get_client():
    if HACKATHON_MODE:
        # when its set to true it uses Vertex AI and Google Cloud 
        # Vertex AI Path: Uses .streamlit/secrets.toml
        sa_info = dict(st.secrets["gcp_service_account"])
        
        # Defined the scope required for Vertex AI
        scopes = ['https://www.googleapis.com/auth/cloud-platform']
        
        # Passing the scopes into the credentials object
        credentials = service_account.Credentials.from_service_account_info(
            sa_info, 
            scopes=scopes
        )
        
        return genai.Client(
            vertexai=True, 
            project=st.secrets["GCP_PROJECT_ID"], 
            location="us-central1",
            credentials=credentials
        )
    else:
        # Local Path: Used the Gemini API Key
        # I used this while building so that the billing is minimum.
        # this works when the Hackthon mode is set to False.
        return genai.Client(api_key=st.secrets["FREE_GEMINI_API_KEY"])

# Here I Initialize the model and client
MODEL_ID = "gemini-3-flash-preview" 
client = get_client()

# --- SESSION STATE ---
if "story_result" not in st.session_state: st.session_state.story_result = None
if "nav_result" not in st.session_state: st.session_state.nav_result = None
if "code_result" not in st.session_state: st.session_state.code_result = None
if "reset_trigger" not in st.session_state: st.session_state.reset_trigger = 0

# --- 5. SIDEBAR NAVIGATION - for clean and good User exprience---
with st.sidebar:
    st.markdown('<div class="master-logo">G3</div>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Master Agent</h2>", unsafe_allow_html=True)
    st.divider()
    mode = st.radio("Select Module:", ["Home", "Creative Storyteller ✍️", "UI Navigator ☸️", "Code Architect 💻"])
    st.divider()
    st.info(f"Mode: {'Local (Free)' if HACKATHON_MODE else 'Vertex AI (GCP)'}")

# --- 6. HOME MODULE - I thought to implement all 3 topics rather than just one, a multi-agent---
if mode == "Home":
    st.title("🚀 Gemini 3 Master Agent")
    st.subheader("Triple-Threat Multimodal Intelligence")
    st.write("""
    1. **Storyteller:** Process Audio & Text into narratives.
    2. **Navigator:** Pixel-perfect UI analysis from screenshots.
    3. **Code Architect:** Expert logic and optimization.
    """)
    st.warning("Ensure HACKATHON_MODE is TRUE before final deployment.")

# --- 7. STORYTELLER MODULE ---
elif mode == "Creative Storyteller ✍️":
    st.header("✍️ Creative Storyteller")
    col1, col2 = st.columns(2)
    with col1:
        audio_key = f"audio_{st.session_state.reset_trigger}"
        audio_data = st.audio_input("Record voice brief", key=audio_key)
    with col2:
        text_key = f"text_{st.session_state.reset_trigger}"
        text_data = st.text_area("Or type idea:", key=text_key, height=100)

    if st.button("🚀 Generate Masterpiece"):
        prompt_parts = []
        if audio_data:
            prompt_parts.append(types.Part.from_bytes(data=audio_data.read(), mime_type="audio/wav"))
        if text_data:
            prompt_parts.append(text_data)
        
        if prompt_parts:
            with st.spinner("Crafting..."):
                response = client.models.generate_content(model=MODEL_ID, contents=prompt_parts)
                st.session_state.story_result = response.text
                st.session_state.reset_trigger += 1
                st.rerun()

    if st.session_state.story_result:
        st.divider()
        st.markdown(st.session_state.story_result)

# --- 8. UI NAVIGATOR ---
elif mode == "UI Navigator ☸️":
    st.header("☸️ UI Navigator")
    uploaded_file = st.file_uploader("Upload UI Screenshot", type=["png", "jpg", "jpeg"])
    task = st.text_input("What is your goal?", placeholder="e.g., 'Find the checkout button'")

    if uploaded_file and st.button("🔍 Analyze Interface"):
        img = Image.open(uploaded_file)
        with st.spinner("Scanning pixels..."):
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=[f"Act as a UI Navigator. Task: {task}. Tell me the exact location or steps.", img]
            )
            st.session_state.nav_result = response.text
    
    if st.session_state.nav_result:
        st.divider()
        st.markdown(st.session_state.nav_result)

# --- 9. CODE ARCHITECT ---
elif mode == "Code Architect 💻":
    st.header("💻 Code Architect")
    st.write("Expert optimization and logic analysis.")
    code_input = st.text_area("Paste code or logic requirement:", height=200)
    
    if st.button("⚡ Optimize Logic"):
        if code_input:
            with st.spinner("Analyzing architecture..."):
                response = client.models.generate_content(
                    model=MODEL_ID,
                    contents=[f"Act as a Senior Software Engineer. Review and optimize this: {code_input}"]
                )
                st.session_state.code_result = response.text
        else:
            st.warning("Provide code to analyze.")

    if st.session_state.code_result:
        st.divider()
        st.code(st.session_state.code_result, language='python')