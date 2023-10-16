# Chatbot AI Application 🤖

The Chatbot Application is a graphical user interface (GUI) program built using PyQt6 and Python. It allows users to interact with a chatbot powered by the Chatbot class from the backend module.

## Installation 🏗️

### Prerequisites
* Python 3.7+
* PyQt6 library
* openai library
* OpenAI account with an API key

### Setup
1. Sign up for an OpenAI account and obtain your API key.
2. Set the API key as an environment variable named `OPENAIKEY` on your system.
3. Install the required Python libraries:
   - Install the `openai` library:
     ```bash
     pip install openai
     ```
   - Install the PyQt6 library:
     ```bash
     pip install PyQt6
     ```

#### Running the Chatbot Application
* Execute the following Python script to run the chatbot application:

```python
import sys
import threading
from backend import Chatbot
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton

class ChatbotWindow(QMainWindow):
    # ... (your ChatbotWindow class code)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ChatbotWindow()
    sys.exit(app.exec())

#### Using the Chatbot 
* Once the chatbot application is launched, you can start interacting with the chatbot using the following steps:

1. User Input: In the application window, type your messages in the input field.

2. Sending Messages: Press Enter or click the "Send" button to send your message to the chatbot.

3. Receiving Responses: The chatbot, powered by the OpenAI GPT-3 model, will respond to your messages. The conversation will be displayed in the chat area within the application window.

