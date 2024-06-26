![llamashell](https://github.com/xHand-Eye/ShellLLama/assets/99139432/c9c32eeb-db0e-4251-9193-3e6acc959400)

# 🐑 ShellLLama: Minimalist Ollama CLI

```
   _____ _          _ _ _     _                         
  / ____| |        | | | |   | |                        
 | (___ | |__   ___| | | |   | |     __ _ _ __ ___   __ 
  \___ \| '_ \ / _ \ | | |   | |    / _` | '_ ` _ \ / _ \
  ____) | | | |  __/ | | |___| |___| (_| | | | | | | (_) |
 |_____/|_| |_|\___|_|_|_____|______\__,_|_| |_| |_|\__,_|
                                                         
 Minimalist Ollama CLI - Efficiency in Every Shell
```

## About
ShellLLama is a minimalist command-line interface for interacting with Ollama models. It provides a simple way to generate and execute Python code using Ollama's capabilities.

## Features
- Seamless integration with Ollama models
- Interactive Python code generation and execution
- Basic safety checks for code execution
- Minimal dependencies (only requires Python standard library)

## Quick Start
1. Ensure Ollama is installed and running on your system.
2. Save the `ShellLLama.py` script to your desired location.
3. Make the script executable:
   ```
   chmod +x ShellLLama.py
   ```
4. Run with your preferred Ollama model:
   ```
   ./ShellLLama.py MODEL_NAME
   ```
   Replace `MODEL_NAME` with your chosen Ollama model.

## Usage
After starting ShellLLama:
- Enter prompts to generate Python code
- Confirm execution of generated code
- Type 'quit' to exit

Example:
```
> Write a function to calculate factorial
AI: Here's a Python function to calculate factorial:
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
result = factorial(5)
```
AI suggested code. Execute? (y/n): y
Code output:
120
```

## Requirements
- Python 3.6+
- Ollama

## Contributing
Contributions are welcome. Please feel free to submit a Pull Request.

## License
This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements
- Ollama team for their AI models
