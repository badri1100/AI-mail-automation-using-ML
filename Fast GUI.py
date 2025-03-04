import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QLineEdit, QTextEdit, QStatusBar
from email_sender import send_bulk_emails
import pyttsx3 as p
import speech_recognition as sr
import ollama
from google.generativeai import GenerativeModel, configure

configure(api_key="")

model = GenerativeModel('gemini-1.5-pro')


engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


class EmailSenderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Email Sender")
        self.setGeometry(100, 100, 400+400, 400+300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.csv_label = QLabel("Select CSV File:")
        self.layout.addWidget(self.csv_label)

        self.csv_path_label = QLabel("")
        self.layout.addWidget(self.csv_path_label)

        self.csv_button = QPushButton("Browse")
        self.csv_button.clicked.connect(self.open_file_dialog)
        self.layout.addWidget(self.csv_button)

        self.subject_label = QLabel("Email Subject:")
        self.layout.addWidget(self.subject_label)

        self.subject_input = QLineEdit()
        self.layout.addWidget(self.subject_input)

        self.body_label = QLabel("Email Body:")
        self.layout.addWidget(self.body_label)

        self.body_input = QTextEdit()
        self.layout.addWidget(self.body_input)

        self.prompt_label = QLabel("Prompt:")
        self.layout.addWidget(self.prompt_label)

        self.prompt_layout = QHBoxLayout()
        self.prompt_input = QLineEdit()
        self.prompt_layout.addWidget(self.prompt_input)
        self.prompt_button = QPushButton("Generate")
        self.prompt_button.clicked.connect(self.generate_prompt)
        self.prompt_layout.addWidget(self.prompt_button)
        self.layout.addLayout(self.prompt_layout)

        self.attachment_label = QLabel("Attachment:")
        self.layout.addWidget(self.attachment_label)

        self.attachment_path_label = QLabel("")
        self.layout.addWidget(self.attachment_path_label)

        self.attachment_button = QPushButton("Browse")
        self.attachment_button.clicked.connect(self.open_attachment_dialog)
        self.layout.addWidget(self.attachment_button)

        self.send_button = QPushButton("Send Emails")
        self.send_button.clicked.connect(self.send_emails)
        self.layout.addWidget(self.send_button)

        self.central_widget.setLayout(self.layout)

        # Status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        csv_file, _ = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv)", options=options)
        if csv_file:
            self.csv_path_label.setText(csv_file)

    def open_attachment_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        attachment_file, _ = QFileDialog.getOpenFileName(self, "Select Attachment", "", "All Files (*)", options=options)
        if attachment_file:
            self.attachment_path_label.setText(attachment_file)

    def send_emails(self):
        csv_file = self.csv_path_label.text()
        subject = self.subject_input.text()
        body = self.body_input.toPlainText()
        attachment_path = self.attachment_path_label.text()
        if csv_file and subject and body:
            recipients = send_bulk_emails(csv_file, subject, body, attachment_path)
            self.statusBar.showMessage(f"Emails Sent Successfully")
        else:
            self.statusBar.showMessage("Please fill in all fields.")

    def generate_prompt(self):
        prompt = self.prompt_input.text()
        if prompt:
            self.statusBar.showMessage("Generating Please Wait...")
            # Here you can define the logic to generate the desired content based on the prompt
            # For now, let's just append the prompt to the email body
            
            # stream = ollama.chat(
            # model='llama3',
            # # messages=[{'role': 'user', 'content': text+' Give answer in 20 words but dont mention 20 words dont use symbols'}],
            # messages=[{'role': 'user', 'content': prompt+' \n\n write a email for this topic be specific with statements and dont give any suggestion just directly start writing mail'}],
            # stream=True,
            # )
            response = model.generate_content(prompt+' \n\n write a email for this topic be specific with statements and dont give any suggestion just directly start writing mail')

            print(response.text)

            x = ""
            # print("\n\nEmail : ",end='')
            current_body = self.body_input.toPlainText()
            self.body_input.setPlainText(current_body + x)
            
            self.body_input.setPlainText(current_body + str(response.text))

            
            current_body = self.body_input.toPlainText()
            
            # self.body_input.setPlainText(current_body + "\n" + prompt)
            self.statusBar.showMessage("Email Generated.")
            
            
        else:
            self.statusBar.showMessage("Please enter a prompt.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmailSenderApp()
    window.show()
    sys.exit(app.exec_())
