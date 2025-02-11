import google.generativeai as genai
import regex as re

def process_code_review(api_key, input_code):
    try:
        genai.configure(api_key=api_key)

        system_prompt = """You are a Python Code Reviewer and you are provided with a Python code. 
        You must Write a bug report of the code in 2-3 lines and fix the code. 
        Keep it simple and professional. Don't respond if u don't know the answer, 
        Just review the syntax; if wrong, report it."""

        model = genai.GenerativeModel(
            model_name="models/gemini-2.0-pro-exp",
            generation_config=genai.types.GenerationConfig(temperature=0.1, top_k=1, top_p=0.1),
            system_instruction=system_prompt
        ) 

        response = model.generate_content(input_code)

        match = re.search(r"Bug Report:\s*(.*?)\s*Fixed Code:\s*(.*)", response.text, re.DOTALL)

        if match:
            bug_report = match.group(1).strip()
            fixed_code = match.group(2).strip()
            return bug_report, fixed_code
        else:
            return "Error: Could not extract bug report and fixed code.", None

    except Exception as e:
        return f"An error occurred: {str(e)}", None
