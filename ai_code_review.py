import google.generativeai as genai
import regex as re

def process_code_review(api_key, input_code):
    try:
        genai.configure(api_key=api_key)

        system_prompt = """You are a Python Code Reviewer. Analyze the provided Python code for syntax and logical errors. If any issues are found, structure your response into two sections:
        Bug Report: Briefly describe the issue in 2-3 lines, including both syntax and logical errors.
        Fixed Code: Provide the corrected version of the code with necessary explanations if needed.
        Explanation: Brief Explanation about how the code is fixed.
        Keep the feedback professional and to the point."""

        model = genai.GenerativeModel(
            model_name="models/gemini-2.0-pro-exp",
            generation_config=genai.types.GenerationConfig(temperature=0.1, top_k=10, top_p=0.3),
            system_instruction=system_prompt
        ) 

        response = model.generate_content(input_code)

        match = re.search(r"Bug Report:\s*(.*?)\s*Fixed Code:\s*(.*?)\s*Explanation:\s*(.*)", response.text, re.DOTALL)

        if match:
            bug_report = match.group(1).strip()
            bug_report = re.sub(r"^\*\*\s*", "", bug_report)
            bug_report = re.sub(r"\*\*\s*$", "", bug_report)
            fixed_code = match.group(2).strip()
            fixed_code = re.sub(r"^\*\*\s*", "", fixed_code)
            fixed_code = re.sub(r"\*\*\s*$", "", fixed_code)    
            explanation = match.group(3).strip()
            explanation = re.sub(r"^\*\*\s*", "", explanation)
            return bug_report, fixed_code, explanation
        else:
            return "Error: Could not extract bug report and fixed code.", None

    except Exception as e:
        return f"An error occurred: {str(e)}", None
