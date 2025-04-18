import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QLineEdit, QTextEdit, QStatusBar, QGraphicsOpacityEffect
from PyQt5.QtCore import QPropertyAnimation, QRect
from email_sender import send_bulk_emails
import ollama




class EmailSenderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Email Sender")
        self.setGeometry(100, 100, 500, 500)

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

        self.send_button = QPushButton("Send Emails")
        self.send_button.clicked.connect(self.send_emails)
        self.layout.addWidget(self.send_button)

        self.central_widget.setLayout(self.layout)

        # Status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # Apply styles
        self.apply_styles()
        
        # Animations
        self.animate_widgets()

    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        csv_file, _ = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv)", options=options)
        if csv_file:
            self.csv_path_label.setText(csv_file)

    def send_emails(self):
        csv_file = self.csv_path_label.text()
        subject = self.subject_input.text()
        body = self.body_input.toPlainText()
        if csv_file and subject and body:
            recipients = send_bulk_emails(csv_file, subject, body)
            self.statusBar.showMessage(f"Emails Sent Successfully to: {', '.join(recipients)}")
        else:
            self.statusBar.showMessage("Please fill in all fields.")

    def generate_prompt(self):
        prompt = self.prompt_input.text()
        if prompt:
            self.statusBar.showMessage("Generating Please Wait...")
            # Here you can define the logic to generate the desired content based on the prompt
            # For now, let's just append the prompt to the email body
            
            stream = ollama.chat(
            model='llama3',
            # messages=[{'role': 'user', 'content': text+' Give answer in 20 words but dont mention 20 words dont use symbols'}],
            messages=[{'role': 'user', 'content': prompt+' Give short answer in max 50 words if necessary and your name is Meta Sapien and you are created by Pranay Mahendrakar'}],
            stream=True,
            )

            x = ""
            # print("\n\nEmail : ",end='')
            current_body = self.body_input.toPlainText()
            self.body_input.setPlainText(current_body + x)
            for chunk in stream:
                print(chunk['message']['content'], end='', flush=True)
                x = x+str(chunk['message']['content'])
                self.body_input.setPlainText(current_body + x)

            
            current_body = self.body_input.toPlainText()
            
            # self.body_input.setPlainText(current_body + "\n" + prompt)
            self.statusBar.showMessage("Email Generated.")
            
            
        else:
            self.statusBar.showMessage("Please enter a prompt.")

    def apply_styles(self):
        self.setStyleSheet("""
            QLabel {
                font-size: 14px;
            }
            QLineEdit, QTextEdit {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton {
                background-color: red;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QStatusBar {
                font-size: 12px;
                color: #007bff;
            }
        """)

    def animate_widgets(self):
        self.animate_widget(self.csv_button)
        self.animate_widget(self.prompt_button)
        self.animate_widget(self.send_button)

    def animate_widget(self, widget):
        effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(effect)
        self.animation = QPropertyAnimation(effect, b"opacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmailSenderApp()
    window.show()
    sys.exit(app.exec_())
