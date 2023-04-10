import os
import argparse
import openai

def init_openai(api_key):
    openai.api_key = api_key

def convert_text(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5
        )

        return response.choices[0].text.strip()

    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='CommandGPT: Convert between natural language and command line scripts')
    parser.add_argument('text', type=str, help='The text to convert')
    parser.add_argument('-t', '--type', type=str, choices=['NL2PS', 'NL2Bash', 'Bash2PS', 'PS2NL', 'Bash2NL'], required=True, help='The type of conversion')
    parser.add_argument('-k', '--key', type=str, required=True, help='Your OpenAI API key')
    
    args = parser.parse_args()
    
    prompt_map = {
        'NL2PS': 'Translate the following natural language text to a PowerShell command: {}',
        'NL2Bash': 'Translate the following natural language text to a Bash command: {}',
        'Bash2PS': 'Convert the following Bash command to PowerShell: {}',
        'PS2NL': 'Explain the following PowerShell command in natural language: {}',
        'Bash2NL': 'Explain the following Bash command in natural language: {}'
    }

    init_openai(args.key)
    prompt = prompt_map[args.type].format(args.text)
    result = convert_text(prompt)

    if result:
        print(result)

if __name__ == "__main__":
    main()
