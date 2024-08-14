import requests
import re
import subprocess

# Set your OpenAI API key here
api_key = 'OPENAI-API-KEY'  # Replace with your actual API key

def send_request_to_chatgpt(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

def extract_python_code(text):
    code_blocks = re.findall(r"```python(.*?)```", text, re.DOTALL)
    if code_blocks:
        return code_blocks[0].strip()
    return None

def save_and_run_code(python_code):
    with open("response.py", "w") as f:
        f.write(python_code)
    
    # Run the file in the background
    subprocess.Popen(["python3", "response.py"])

def main():
    
    request = input("Enter your order to execute\n")
    prompt = "create a python code to do this order : \n" + request
    try:
        response = send_request_to_chatgpt(prompt)
        print(response)
        python_code = extract_python_code(response)
        if python_code:
            save_and_run_code(python_code)
            print("executed")
        else:
            print("No Python code found in the response.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
