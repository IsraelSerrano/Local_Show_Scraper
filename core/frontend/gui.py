# Gui Goes here
import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


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
        
        grid_layout = QGridLayout()
        for row in range(4):
            text_edit = QLineEdit(self)  # Create a text edit
            button = QPushButton(f"Button {row + 1}", self)  # Create a button with a label
            grid_layout.addWidget(text_edit, row, 0)  # Add text edit to column 0
            grid_layout.addWidget(button, row, 1)  # Add button to column 1

        # Set the layout for the central widget
        central_widget.setLayout(grid_layout)
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()