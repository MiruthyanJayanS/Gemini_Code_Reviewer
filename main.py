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
Code_review_gif = load_lottiefile("E:\\Project\\Gemini_Code_Reviewer\\assets\\code_review.json")
# Use Streamlit columns to place title and animation side by side
col1, col2 = st.columns([0.8, 0.2]) 

with col1:
    st.title("AI Code Review Tool") 

with col2:
    st_lottie(Code_review_gif, height=100, width=100, speed=1, loop=True, quality='high', key='CodeReview')

with st.sidebar:
    api_key = st.radio(""":blue[Select the method for API Key]""", ["Demo_API_Key", "API_Key Input", "Env_API_Key"], captions=["Demo purpose API key", "Input the API key", "API key stored in .env file "])

    API_Key = None  # Initialize to None

    if api_key == "Env_API_Key":
        from dotenv import load_dotenv
        import os
        load_dotenv()
        API_Key = os.getenv('API_KEY')
    elif api_key == "API_Key Input":
        API_Key = st.text_input("Enter your API Key", type="password")
    else:
        API_Key = "AIzaSyBAmdMvFun4OydB4S945fbEcRJZOBSc-QU"

    if not API_Key:
        st.error('API key not found')
        st.stop()

input_code = st.text_area(""":green[Enter your code down here ... 👇]""", height=200)

left,middle,right = st.columns(3)

if middle.button("Submit", use_container_width=True):

    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(3)
    my_bar.empty()

    bug_report, fixed_code = process_code_review(API_Key, input_code)
    st.header("Code Review Results")
    if bug_report and fixed_code:
        st.markdown(""":red["Bug Report"]""")
        st.write(bug_report)
        st.markdown(""":rainbow["Fixed Code"]""")
        st.code(fixed_code)
    else:
        st.error(bug_report)  # Display error message
        st.stop()
    st.button("Close")  # Close the app