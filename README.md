# AI-mail-automation-using-ML

# AI Mail Automation using NLP & LLM

This project automates bulk email sending using AI-generated content powered by NLP and LLM. It integrates OpenAI's GPT API to create dynamic email content and sends emails securely using Python.

## Features

- **Bulk Email Sending**: Reads recipient emails from CSV files.
- **AI-Powered Email Generation**: Uses GPT API to generate professional email content.
- **GUI for User Interaction**: Provides an interface to customize and send emails.
- **Secure Email Handling**: Uses environment variables for credentials.
- **WhatsApp Messaging (Optional)**: Includes WhatsApp automation.

## Project Structure

```
📂 AI Mail Automation
 ├── badri/
 │   ├── main.py               # Main script for bulk email automation
 │   ├── email_sender.py       # Handles email sending via SMTP
 │   ├── Email Gen.py          # AI-generated email content
 │   ├── Email_GUI.py          # GUI interface for email automation
 │   ├── Fast GUI.py           # Alternate GUI version
 │   ├── Normal_Email_GUI.py   # Basic GUI version
 │   ├── try.py, tryGUI.py     # Test scripts
 │   ├── whts.py               # WhatsApp automation script
 │   ├── contacts.csv          # Sample recipient email list
 │   ├── email.csv             # Email storage file
 │   ├── try.html, try2.html   # Email template files
 │   ├── PyWhatKit_DB.txt      # WhatsApp-related database
 ├── __pycache__/              # Compiled Python files
```

## Installation

### Prerequisites

- Python 3.x
- OpenAI API Key
- SMTP Email Account (Gmail recommended)

### Setup

1. Install dependencies:
   ```bash
   pip install openai smtplib python-dotenv csv
   ```
2. Set up environment variables:
   - Create a `.env` file in the project root with:
   ```
   OPENAI_API_KEY=your_openai_api_key
   SENDER_EMAIL=your_email@gmail.com
   SENDER_PASSWORD=your_email_password
   ```

## Usage

### Running the Main Script

```bash
python main.py
```

- This reads email addresses from `contacts.csv` and sends AI-generated emails.

### Running the GUI

```bash
python Email_GUI.py
```

- Opens a user-friendly interface to send custom emails.

## Future Improvements

- Implement OAuth for secure email authentication.
- Improve AI-generated responses with fine-tuned prompts.
- Add email scheduling functionality.

## Contributing

Feel free to fork this project and submit pull requests!
