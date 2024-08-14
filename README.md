# NL2CodeExecutor

NL2CodeExecutor is a Python-based project that translates natural language prompts into executable Python code. This project leverages OpenAI's GPT-3.5 Turbo model to generate Python code from user input and then runs the code in a sandboxed environment.

## Features

- Convert natural language instructions into Python code.
- Automatically extract and execute the generated Python code.
- Run the code in a background process.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed on your machine.
- An OpenAI API key. You can get one by signing up at [OpenAI](https://platform.openai.com/signup).
- The following Python packages:
  - `requests`
  - `subprocess`
  - `re`

## Installation

1. Clone the repository:

   ```bash
    git clone https://github.com/thejsondev/NL2CodeExecutor.git
    cd NL2CodeExecutor
    pip install requests
    python assist.py```

By default, the script is set to request a Python function for calculating the factorial of a number. You can modify the prompt variable in the main() function to use different prompts.

## Example
When prompted with "Write a Python function to calculate the factorial of a number," the script will:

- Send the request to the OpenAI API.
- Extract the generated Python code from the response.
- Save the code to response.py.
- Execute the code in the background.
- The generated Python code and execution results will be displayed in the terminal.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any feature suggestions, bug reports, or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
OpenAI for providing the GPT-3.5 Turbo model.
The Python community for the development of essential packages.