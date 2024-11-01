# Simple Topic Classification System built on Python

A command-line tool that uses a language model (LLM) to classify text by a predefined set of **topics**. Built with `langchain-together`, `langchain-core` and `pydantic`, this tool allows for quick and easy topic classification from the command line.

## Features

- **Text Classification**: Categorizes text into predefined topics: `sports`, `politics`, `entertainment`, and `technology`.

## Installation

### Prerequisites

- **Python 3.8** or higher
- **API Key** for the LLM model from `together-ai`

### Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/imuki2004/DocPro-Demo.git
    cd docpro-demo
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
    - Add your API key:

    ```plaintext
    API_KEY=your_api_key_here
    ```

5. **Install the package**:

    ```bash
    pip install .
    ```
    
## Usage

After installation, use the classifier command to classify any text directly from the terminal:

    classifier "Your text here"

### Example

Classify a sports-related statement:

    classifier "Magnus Carlsen is the greatest chess player in the history."


Expected Output:

    { "topic": "sports" }

## Project Structure

- `classifier.py`: Contains the core classification logic and LLM setup.
- `main.py`: Handles the command-line interface (CLI) setup and arguments.
- `setup.py`: Configuration for package installation and CLI entry point.
- `.env`: Stores environment variables like the API key.
- `README.md`: Provides setup and usage instructions.

## License

This project is licensed under the MIT License.