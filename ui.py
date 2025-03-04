import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLineEdit, QTextEdit, QStatusBar
from email_sender import send_bulk_emails

class EmailSenderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Email Sender")
        self.setGeometry(100, 100, 400, 300)

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

    def send_emails(self):
        csv_file = self.csv_path_label.text()
        subject = self.subject_input.text()
        body = self.body_input.toPlainText()
        if csv_file and subject and body:
            recipients = send_bulk_emails(csv_file, subject, body)
            self.statusBar.showMessage(f"Emails Sent Successfully")
        else:
            self.statusBar.showMessage("Please fill in all fields.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmailSenderApp()
    window.show()
    sys.exit(app.exec_())
