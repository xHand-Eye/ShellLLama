#!/usr/bin/env python3
import argparse
import subprocess
import re

def query_ollama(model: str, prompt: str) -> str:
    """Query Ollama model and return the response."""
    try:
        result = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"

def extract_python_code(text: str) -> str | None:
    """Extract Python code from text enclosed in triple backticks."""
    pattern = r'```python\n(.*?)\n```'
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1) if match else None

def execute_python_code(code: str) -> str:
    """Execute Python code and return the output."""
    try:
        output = {}
        exec(code, {}, output)
        return str(output.get('result', ''))
    except Exception as e:
        return f"Error executing code: {str(e)}"

def get_system_prompt():
    return """
You are an AI assistant integrated into a minimalistic command-line interface. Your primary function is to assist users by generating and executing Python code based on their requests. Here are your key characteristics and capabilities:

1. Code Generation: You can write Python scripts to accomplish various tasks. Always enclose your Python code in triple backticks with 'python' after the opening backticks.

2. Code Execution: You have the ability to run Python code. The last line of any code you generate should assign the result to a variable named 'result'.

3. Safety First: You are cautious about executing potentially dangerous operations. Always ask for user confirmation before suggesting any code that could modify the system or access sensitive information.

4. Clarity: You provide clear, concise explanations along with your code. Explain what the code does and why you've chosen that approach.

5. Efficiency: You strive to write efficient, minimal code that adheres to the principles of minimalism.

6. Adaptability: You can handle a wide range of requests, from simple calculations to more complex data processing tasks, as long as they can be accomplished with Python.

7. Limitations: You cannot access the internet, external databases, or any information beyond your training data. You also cannot persist information between user queries.

Remember, your responses should be direct and to the point. Avoid unnecessary pleasantries or verbose explanations unless specifically asked. Your goal is to provide useful, executable Python code along with brief, clear explanations.

When responding to user queries, follow this structure:
1. A brief explanation of what you're going to do.
2. The Python code to accomplish the task, enclosed in triple backticks.
3. A very brief explanation of how to interpret the result, if necessary.

Are you ready to assist with Python code generation and execution?
"""

def get_ascii_banner():
    return r"""
   _____ _          _ _ _     _                         
  / ____| |        | | | |   | |                        
 | (___ | |__   ___| | | |   | |     __ _ _ __ ___   __ 
  \___ \| '_ \ / _ \ | | |   | |    / _` | '_ ` _ \ / _ \
  ____) | | | |  __/ | | |___| |___| (_| | | | | | | (_) |
 |_____/|_| |_|\___|_|_|_____|______\__,_|_| |_| |_|\__,_|
                                                         

    """

def main(model: str):
    print(get_ascii_banner())
    print(f"Model: {model}")
    print("Enter your prompts. The AI can generate and execute Python code.")
    print("Type 'quit' to exit.")
    print("=" * 50)  # Add a separator line for clarity
    
    system_prompt = get_system_prompt()
    
    while True:
        try:
            user_input = input("\n> ")
            if user_input.lower() == 'quit':
                break
            
            full_prompt = f"{system_prompt}\n\nUser: {user_input}\nAI:"
            ai_response = query_ollama(model, full_prompt)
            print(f"\nAI: {ai_response}")
            
            python_code = extract_python_code(ai_response)
            if python_code:
                confirm = input("AI suggested code. Execute? (y/n): ")
                if confirm.lower() == 'y':
                    code_output = execute_python_code(python_code)
                    print("\nCode output:")
                    print(code_output)
                else:
                    print("Code execution cancelled.")
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ShellLlama: Minimalist ollama cli for python script generattion and execution ")
    parser.add_argument("model", help="Ollama model to use")
    args = parser.parse_args()
    
    main(args.model)
