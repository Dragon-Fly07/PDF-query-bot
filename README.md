# PDF-query-bot

## Introduction
A bot where you can specify the path to your PDF file, and query it based on the PDF file as a reference

## Set up instructions
**Linux**<br>
Start by setting up a virtual environment 
```bash
python -m venv .virt && source ./bin/activate
```
Clone the repository to the same directory as the virtual environment
```bash
git clone https://github.com/Dragon-Fly07/PDF-query-bot
```
Installed the required dependencies with the command 
```bash
pip install -r requirements.txt
```
Create a `.env` file and declare the variable `GOOGLE_API_KEY` to be your gemini api key. To create the gemini API key, you can use the <a href="https://ai.google.dev/gemini-api/docs/api-key">official documentation</a>.<br><br>
Finally, run the application using 
```bash
streamlit run streamlit.py
```