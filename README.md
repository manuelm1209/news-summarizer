# News Summarizer AI

News Summarizer AI is a Python-based application designed to fetch and summarize news articles on a specific topic using the OpenAI GPT model and the NewsAPI. The application leverages Streamlit for its user interface, making it easy to interact with.

## Features

- **Fetch News Articles**: Retrieve news articles from [NewsAPI](https://newsapi.org/) based on a topic.
- **Summarize News**: Use OpenAI's GPT model to create concise summaries of the retrieved news articles.
- **Streamlit Integration**: An interactive user interface for input and displaying results.

## Prerequisites

Before you can run the project, ensure you have the following installed:

- Python 3.8+
- [pipenv](https://pipenv.pypa.io/en/latest/) or `pip`
- API key for [NewsAPI](https://newsapi.org/)
- API key for [OpenAI](https://platform.openai.com/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/news-summarizer-AI.git
   cd news-summarizer-AI
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your API keys:
     ```plaintext
     NEWS_API_KEY=your_newsapi_key
     OPENAI_API_KEY=your_openai_api_key
     ```

## Usage

1. Run the application:
   ```bash
   streamlit run main.py
   ```

2. Open the application in your browser at `http://localhost:8501`.

3. Enter a topic in the input field and click **Run Assistant** to generate summaries for the latest news on that topic.

## Project Structure

```plaintext
.
├── main.py               # Main application file
├── requirements.txt      # Project dependencies
├── .env                  # Environment variables (not included in the repo)
├── README.md             # Project documentation
```

## How It Works

1. **Fetching News**:
   - The `get_news` function queries the NewsAPI for articles based on the user's topic.
   - Retrieves up to 5 articles and their metadata.

2. **Summarizing News**:
   - The `AssistantManager` class interacts with OpenAI's GPT API.
   - A personal assistant is created to process and summarize the news articles.

3. **Interactive Interface**:
   - Users can interact with the app via a Streamlit-powered UI.

## Dependencies

- `openai`
- `streamlit`
- `python-dotenv`
- `requests`

Install all dependencies using:
```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any feature requests or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [OpenAI](https://openai.com/) for their powerful GPT model.
- [NewsAPI](https://newsapi.org/) for providing a robust news aggregation service.
- [Streamlit](https://streamlit.io/) for making web app development simple and intuitive.
