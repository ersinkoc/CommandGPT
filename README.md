# CommandGPT

CommandGPT is a simple command line tool that leverages GPT-3.5 to convert between natural language and command line scripts. Supported conversions are:

- Natural Language to PowerShell command
- Natural Language to Bash command
- Bash to PowerShell command
- PowerShell to Natural Language
- Bash to Natural Language

## Requirements

- Python 3.x
- An OpenAI API key (you can get one from https://beta.openai.com/signup)

## Installation

1. Clone this repository:

```git clone https://github.com/ersinkoc/CommandGPT.git```


2. Change to the cloned directory:

```cd CommandGPT```

3. Install the required dependencies:

```pip install openai```

## API KEY

For Unix-like systems (Linux, macOS):
```
export OPENAI_API_KEY=your_api_key
```

For Windows (Command Prompt):
```
set OPENAI_API_KEY=your_api_key
```

For Windows (PowerShell):
```
$env:OPENAI_API_KEY="your_api_key"
```

## Usage

Run the `commandgpt.py` script with the desired conversion type, input text, and your OpenAI API key:

python commandgpt.py -t NL2PS -k your_api_key "create a new folder named 'example'"


Replace `your_api_key` with your actual OpenAI API key.

## Conversion Types

- `-t NL2PS`: Natural Language to PowerShell command
- `-t NL2Bash`: Natural Language to Bash command
- `-t Bash2PS`: Bash to PowerShell command
- `-t PS2NL`: PowerShell to Natural Language
- `-t Bash2NL`: Bash to Natural Language
