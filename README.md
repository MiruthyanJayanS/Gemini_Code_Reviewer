# Gemini_Code_Reviewer 

A Streamlit-based AI-powered Python code review tool using Google's Gemini AI. This tool analyzes code, identifies potential issues, and suggests fixes to improve code quality.  

## Demo


https://github.com/user-attachments/assets/6b809cb9-4749-471d-9c93-313373d3f5fc


## Features  
- AI-driven bug detection and code improvement  
- Secure API key handling via environment variables or manual input  
- Intuitive Streamlit UI with Lottie animations  
- Simple and efficient bug reporting  

## Tech Stack  
- Python  
- Streamlit  
- Google Generative AI (Gemini)  
- Regex  
- Lottie Animations  

## Installation  

### 1. Clone the Repository  
```
git clone https://github.com/your-username/ai-code-review-tool.git
cd ai-code-review-tool
```
### 2. Create a Virtual Environment (Optional)
```
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate      # For Windows
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Set Up API Key
This tool requires an API key from Google Gemini AI.
- Option 1: Add an API key to a .env file:
```
API_KEY=your_google_gemini_api_key
```
- Option 2: Enter the API key manually in the Streamlit UI when prompted.
### 5. Run the Application
```
streamlit run main.py
```
### Project Structure
```
📂 ai-code-review-tool
├── main.py                # Streamlit UI
├── ai_code_review.py      # AI code review logic
├── requirements.txt       # Dependencies
├── .env.example          # Example environment file
├── README.md              # Documentation
```
### Contributing
- Fork the repository
- Create a feature branch (git checkout -b feature-name)
- Commit your changes (git commit -m "Added a new feature")
- Push to your branch (git push origin feature-name)
- Open a Pull Request

### Credits
[LottieFiles_Animation](https://lottiefiles.com/eauuxvb8nq) Creator Faizan Jiya 
### Author
Developed by [Miruthyan Jayan S]
