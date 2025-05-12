# Gui Goes here
import sys
import os
import sqlite3
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
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QLabel {
                font-size: 14px;
                color: #333;
            }
            QTextEdit {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
                font-size: 12px;
            }
            QPushButton {
                background-color: #0078d7;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 15px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
            QPushButton:pressed {
                background-color: #003f73;
            }
        """)
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a vertical layout
        layout = QVBoxLayout()

        header_label = QLabel("831 Show Scraper")
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #0078d7;")
        layout.addWidget(header_label)
        
        # Add a label
        label = QLabel("Enter Instagram profile names (comma-separated):", self)
        label.setStyleSheet("font-size: 14px; color: #333;")
        layout.addWidget(label)

        # Add a large text area for input
        self.text_area = QTextEdit(self)
        self.text_area.setPlaceholderText("e.g., teamsbpromotions, sk831.promotions")
        self.text_area.setStyleSheet("border: 1px solid #ccc; border-radius: 5px; padding: 5px; font-size: 12px;")
        layout.addWidget(self.text_area)

        # Add a button to trigger scraping
        scrape_button = QPushButton("Scrape Profiles", self)
        scrape_button.setStyleSheet("""
            background-color: #0078d7;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 8px 15px;
            font-size: 12px;
        """)
        scrape_button.clicked.connect(self.scrape_profiles)  # Connect button to scrape function
        scrape_button_layout = QHBoxLayout()
        scrape_button_layout.addStretch()
        scrape_button_layout.addWidget(scrape_button)
        scrape_button_layout.addStretch()
        layout.addLayout(scrape_button_layout)
        
        # Add a text area to display results
        self.results_display = QTextEdit(self)
        self.results_display.setReadOnly(True)
        self.results_display.setPlaceholderText("Results will appear here...")
        self.results_display.setStyleSheet("border: 1px solid #ccc; border-radius: 5px; padding: 5px; font-size: 12px;")
        layout.addWidget(self.results_display)

        # Add a button to print database contents
        print_db_button = QPushButton("Print Database Contents", self)
        print_db_button.setStyleSheet("""
            background-color: #0078d7;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 8px 15px;
            font-size: 12px;
        """)
        print_db_button.clicked.connect(self.print_database_contents)  # Connect button to print database function
        print_db_button_layout = QHBoxLayout()
        print_db_button_layout.addStretch()
        print_db_button_layout.addWidget(print_db_button)
        print_db_button_layout.addStretch()
        layout.addLayout(print_db_button_layout)
        
        # Set the layout for the central widget
        central_widget.setLayout(layout)

    def print_database_contents(self):
        # Connect to the SQLite database
        conn = sqlite3.connect("instagram_posts.db")
        cursor = conn.cursor()

        # Query all rows from the posts table
        cursor.execute("SELECT * FROM posts")
        rows = cursor.fetchall()
        print(rows)

        # Display the results in the results_display text area
        self.results_display.clear()
        if rows:
            for row in rows:
                self.results_display.append(f"ID: {row[0]}")
                self.results_display.append(f"Username: {row[1]}")
                self.results_display.append(f"Post URL: {row[2]}")
                self.results_display.append(f"Caption: {row[3]}")
                self.results_display.append(f"Image URL: {row[4]}")
                self.results_display.append(f"Alt Image: {row[5]}")
                self.results_display.append(f"Tagged Users: {row[6] if row[6] else 'No tagged users'}")
                self.results_display.append("-" * 50)
        else:
            self.results_display.append("No data found in the database.")

        # Close the database connection
        conn.close()
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