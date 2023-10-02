import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, 
                             QMenuBar, QMenu, QLabel, QAction)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Basic Window Properties
        self.setWindowTitle("Intrusion Detection System")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('icon_path.png'))  # Set a window icon (Replace 'icon_path.png' with your icon's path)

        # Main Layout
        layout = QVBoxLayout()

        # Status Indicator
        self.status_label = QLabel("Status: Stopped")
        layout.addWidget(self.status_label)

        # Start/Stop IDS Button
        self.start_button = QPushButton("Start IDS")
        self.start_button.clicked.connect(self.toggle_ids)
        layout.addWidget(self.start_button)

        # Alerts Log
        self.log_window = QTextEdit()
        self.log_window.setReadOnly(True)
        layout.addWidget(self.log_window)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Menu Bar
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        
        self.file_menu = QMenu("File", self)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        self.file_menu.addAction(exit_action)

        self.menu_bar.addMenu(self.file_menu)

    def toggle_ids(self):
        # Toggle IDS state and update the interface accordingly
        if self.start_button.text() == "Start IDS":
            self.log_window.append("IDS Started!")
            self.start_button.setText("Stop IDS")
            self.status_label.setText("Status: Running")
        else:
            self.log_window.append("IDS Stopped!")
            self.start_button.setText("Start IDS")
            self.status_label.setText("Status: Stopped")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())