# Gui Goes here
import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QTextEdit)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from core.backend.api_scraper import api_scrape_profiles

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("831 Show Scraper")
        self.setGeometry(700, 300, 800, 500)
        icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/guitar.png"))
        self.setWindowIcon(QIcon(icon_path))
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a vertical layout
        layout = QVBoxLayout()

        # Add a label
        label = QLabel("Enter Instagram profile names (comma-separated):", self)
        layout.addWidget(label)

        # Add a large text area for input
        self.text_area = QTextEdit(self)
        self.text_area.setPlaceholderText("e.g., teamsbpromotions, sk831.promotions")
        layout.addWidget(self.text_area)

        # Add a button to trigger scraping
        scrape_button = QPushButton("Scrape Profiles", self)
        scrape_button.clicked.connect(self.scrape_profiles)  # Connect button to scrape function
        layout.addWidget(scrape_button)

        # Set the layout for the central widget
        central_widget.setLayout(layout)
        
    def scrape_profiles(self):
        # Get the input from the text area
        input_text = self.text_area.toPlainText()
        if not input_text.strip():
            self.results_display.append("No profiles entered.")
            return

        # Split the input into a list of profiles
        profiles = [profile.strip() for profile in input_text.split(",") if profile.strip()]
        api_scrape_profiles(profiles)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()