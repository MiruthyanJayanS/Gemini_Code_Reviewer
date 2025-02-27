import json  
import time
import streamlit as st 
from streamlit_lottie import st_lottie 
from ai_code_review import process_code_review

# Fetch Lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)    

# Load Lottie animation
Code_review_gif = load_lottiefile(r"assets\code_review.json")

# Use Streamlit columns to place title and animation side by side
col1, col2 = st.columns([0.8, 0.2]) 

with col1:
    st.title("AI Code Review Tool") 

with col2:
    st_lottie(Code_review_gif, height=100, width=100, speed=1, loop=True, quality='high', key='CodeReview')

def handle_api_key():
    with st.sidebar:
        st.subheader("🔑 API Key Settings")

        google_api_key = st.radio(
            ":blue[Select API Key Method]", 
            ["API_Key Input", "Env_API_Key"], 
            captions=["Manually enter API key", "Use stored API key"]
        )

        api_key = None  # Initialize API key variable

        if google_api_key == "Env_API_Key":
            from dotenv import load_dotenv
            import os
            load_dotenv()
            api_key = os.getenv('API_KEY') or st.secrets.get("GOOGLE_API_KEY")

        elif google_api_key == "API_Key Input":
            user_input_key = st.text_input("Enter your API Key", type="password")

        # Submit API key button
        if st.button("Submit API Key", key="api_submit_button", use_container_width=True):
            if google_api_key == "API_Key Input" and user_input_key:
                st.session_state["API_Key"] = user_input_key
                st.success("✅ API Key attached successfully!")
            elif google_api_key == "Env_API_Key" and api_key:
                st.session_state["API_Key"] = api_key
                st.success("✅ API Key loaded from environment!")
            else:
                st.error("❌ API key not found. Please provide a valid key.")

# API Key Handling
handle_api_key()

# Code input section
st.subheader("📝 Enter Your Code")
input_code = st.text_area("Paste your code here:", height=200)

# Separate button for code submission
if st.button("Submit Code", use_container_width=True):
    if "API_Key" not in st.session_state or not st.session_state["API_Key"]:
        st.error("⚠ Please submit your API Key before proceeding.")
        st.stop()

    if not input_code.strip():
        st.error("⚠ Please enter your code before submitting.")
        st.stop()

    progress_text = "🔄 Reviewing your code, please wait..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(1, 101):
        time.sleep(0.05)
        my_bar.progress(percent_complete, text=progress_text)
    
    time.sleep(1)
    my_bar.empty()

    # Process code review
    api_key = st.session_state["API_Key"]
    result = process_code_review(api_key, input_code)

    if isinstance(result, tuple) and len(result) == 3:
        bug_report, fixed_code, explanation = result
        st.header("📌 Code Review Results")
        st.markdown(":red[**Bug Report:**]")
        st.write(bug_report)
        st.markdown(":rainbow[**Fixed Code:**]")
        st.code(fixed_code, language='python')
        st.markdown(":violet[**Explanation:**]")
        st.write(explanation)
    else:
        st.error(result)  # Display error message
        st.stop()

    st.button("Close")  # Close the app
