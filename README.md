# Simple Topic Classification System on Python

A command-line tool that uses a language model (LLM) to classify text by a predefined set of **topics**. Built with `langchain-together`, `langchain-core` and `pydantic`, this tool allows for quick and easy topic classification from the command line. 

For a detailed explanation of the approach, algorithms, potential improvements, and evaluation strategies, please see the [Project Write-Up](writeup.md).


## Features

- **Text Classification**: Categorizes text into predefined topics: `sports`, `politics`, `entertainment`, and `technology`.

## Installation

### Prerequisites

- **Python 3.8** or higher
- **API Key** for the LLM model from `together-ai`

### Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/imuki2004/Topic-Classification-using-LLM.git
    cd topic-classification-using-llm
    ```
    

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:

    - Create a `.env` file in the project root directory.
    - You can refer to `.envexample` file to see how to setup your API key.
    - Add your API key:

    ```plaintext
    API_KEY=your_api_key_here
    ```
    
## Usage

After installation, use the following command to classify any text directly from the terminal:

    python main.py "Your text here"

### Example

1. Classify a sports-related statement:

```bash
python main.py "Magnus Carlsen is the greatest chess player in the history."
```

- `Expected Output`:
```bash
{"topic":"sports"}
```

2. If the statement is not the part of any of the `predefined topics`:

```bash
python main.py "My name is Imash."
```

- `Expected Output`:

```bash
{"topic":"other"}
```

## Project Structure

- `classifier.py`: Contains the core classification logic and LLM setup.
- `main.py`: Handles the command-line interface (CLI) setup and arguments.
- `.envexample.txt`: Shows an example of how to store the API key.
- `requirements.txt`: Contains a list of packages needed to work on a project.
- `README.md`: Provides setup and usage instructions.
- `writeup.md`: Provides detailed information on the project (approach, algorithms, model explanation etc.).

## License

This project is licensed under the MIT License.