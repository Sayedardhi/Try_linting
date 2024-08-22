from .base_linter import BaseLinter
import ollama
import re

class LLAMA3_linter(BaseLinter):
    def __init__(self):
        super().__init__('llama3')

    def fix_linting(self, code, linter_report):
        prompt = (
            f"""
            You are a post pylint fixer. I will give you the original code, and pylint report, and you have to fix the problems. 
            Here is the code:
            {code}

            Here is the pylint report:
            {linter_report}

            **STRICTLY FOLLOW THE RULES BELOW:**
            - Do not introduce unrelated code, or unrelated fixes.
            - Every function should have a docstring. If missing, add a docstring to the function.
            - Don't uncomment code that is commented out.
            - Don't just say "insert original code here", actually provide the corrected code.
            - Don't change the functionality of the code. As in, for example, don't just make a recursive function iterative because you want to when that was not prompted by the linter. 
            - Return only the corrected code within the specific markers, and provide a rationale for each change.
            - Add a module docstring at the beginning of the code if missing, and is suggested by the linter. You can use the name of the file as the module name.
            - If a linting rule requires you to break up a line of code or add a line, please do so.
            - Do not put random imports that were not part of the original code.
            - Do not just leave sections of the code to be filled in by the user; fully complete the code.
            - It is imperative that you do not change the functionality of the code unless directly needed by the linter. So keep most of the code from the original file and fix what's needed. This is imperative, as the code is being linted for a specific purpose, and changing the functionality could have unintended consequences.
            Return the response in the following format:
            ```python
            <corrected code>
            ```
            """
        )
        
        print(f"Sending request to {self.model_name} model with prompt:\n{prompt}")
        try:
            response = ollama.chat(model=self.model_name, messages=[
                {
                    'role': 'user',
                    'content': prompt,
                },
            ])
            print(f"Response received from {self.model_name} model:\n{response}")
            content = response['message']['content']
            corrected_code = self.extract_corrected_code(content)
            return corrected_code
        except Exception as e:
            print(f"Error with {self.model_name} model: {e}")
            return ""

    @staticmethod
    def extract_corrected_code(content):
        code_block_match = re.search(r'```python\n(.*?)\n```', content, re.DOTALL)
        if code_block_match:
            return code_block_match.group(1).strip()
        return content