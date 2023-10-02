from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QSpinBox, QVBoxLayout, QPushButton, QFormLayout, 
                             QDialogButtonBox, QMessageBox, QGroupBox, QCheckBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
import re  # For regex validation

class SettingsWindow(QWidget):
    def __init__(self, config=None):
        super().__init__()

        self.config = config if config else {}

        # Window basics
        self.setWindowTitle("IDS Settings")
        self.setGeometry(300, 300, 500, 400)

        # Database settings
        self.db_line_edit = QLineEdit(self.config.get("database", ""))
        self.db_label = QLabel("Database Connection:")

        # Email settings
        self.email_line_edit = QLineEdit(self.config.get("email", ""))
        self.email_label = QLabel("Alert Email Address:")

        # Password for SMTP
        self.email_password_line_edit = QLineEdit(self)
        self.email_password_line_edit.setEchoMode(QLineEdit.Password)
        self.email_password_label = QLabel("Email Password:")

        # Scan frequency
        self.scan_spinbox = QSpinBox()
        self.scan_spinbox.setRange(1, 3600)
        self.scan_spinbox.setValue(self.config.get("scan_frequency", 10))
        self.scan_label = QLabel("Scan Frequency (seconds):")

        # Advanced settings
        self.advanced_groupbox = QGroupBox("Advanced Settings")
        self.advanced_groupbox.setCheckable(True)
        self.advanced_groupbox.setChecked(False)

        self.smtp_server_line_edit = QLineEdit(self.config.get("smtp_server", ""))
        self.smtp_server_label = QLabel("SMTP Server:")

        advanced_layout = QFormLayout()
        advanced_layout.addRow(self.smtp_server_label, self.smtp_server_line_edit)
        self.advanced_groupbox.setLayout(advanced_layout)

        # Save & Cancel
        self.button_box = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.save_settings)
        self.button_box.rejected.connect(self.close)

        layout = QFormLayout()
        layout.addRow(self.db_label, self.db_line_edit)
        layout.addRow(self.email_label, self.email_line_edit)
        layout.addRow(self.email_password_label, self.email_password_line_edit)
        layout.addRow(self.scan_label, self.scan_spinbox)
        layout.addRow(self.advanced_groupbox)
        layout.addWidget(self.button_box)

        self.setLayout(layout)

        # Styling
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(palette)

    def save_settings(self):
        # Validations
        if not self.db_line_edit.text() or not self.email_line_edit.text():
            QMessageBox.warning(self, "Validation Error", "Database and Email fields cannot be empty!")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email_line_edit.text()):
            QMessageBox.warning(self, "Validation Error", "Please enter a valid email address!")
            return

        # Save logic (just updating the internal config for now)
        self.config["database"] = self.db_line_edit.text()
        self.config["email"] = self.email_line_edit.text()
        self.config["scan_frequency"] = self.scan_spinbox.value()
        self.config["smtp_server"] = self.smtp_server_line_edit.text() if self.advanced_groupbox.isChecked() else ""

        QMessageBox.information(self, "Success", "Settings saved successfully!")
        self.close()

# Testing and development
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = SettingsWindow()
    window.show()
    sys.exit(app.exec_())