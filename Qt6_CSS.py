import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QMainWindow, QMessageBox,
                             QVBoxLayout, QHBoxLayout)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sajan Display")
        self.setMinimumSize(200, 200)
        self.setContentsMargins(20, 20, 20, 20)  # Gives space between contents and Main window

        # Step 1: Create and set the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Step 2: Create the main layout and sub-layouts
        main_layout = QVBoxLayout()
        horizontal_layout = QHBoxLayout()
        vertical_layout = QVBoxLayout()

        # Adding sub-layouts to main layout
        main_layout.addLayout(horizontal_layout)
        main_layout.addLayout(vertical_layout)

        # Step 3: Create the child widgets (buttons)
        self.button = QPushButton("Display")
        self.button_2 = QPushButton('Color')
        self.button_3 = QPushButton('Close')
        self.button_4 = QPushButton("Disp 4")
        self.button_5 = QPushButton('Colo 5')
        self.button_6 = QPushButton('Clos 6')

        # Set fixed sizes for buttons
        self.button.setFixedSize(70, 25)
        self.button_2.setFixedSize(70, 25)
        self.button_3.setFixedSize(70, 25)
        self.button_4.setFixedSize(70, 25)
        self.button_5.setFixedSize(70, 25)
        self.button_6.setFixedSize(70, 25)

        # Step 4: Add the child widgets to the layout manager
        horizontal_layout.addWidget(self.button)
        horizontal_layout.addWidget(self.button_2)
        horizontal_layout.addWidget(self.button_3)

        vertical_layout.addWidget(self.button_4, alignment=Qt.AlignmentFlag.AlignCenter)
        vertical_layout.addWidget(self.button_5, alignment=Qt.AlignmentFlag.AlignCenter)
        vertical_layout.addWidget(self.button_6, alignment=Qt.AlignmentFlag.AlignCenter)

        # Applying stylesheets to buttons
        self.button_2.setStyleSheet("""
            QPushButton {
                background-color: lightgray;
                color: red;
            }
        """)

        self.button_4.setStyleSheet("""
            QPushButton {
                background-color: white;
            }
        """)

        self.button_5.setStyleSheet("""
            QPushButton {
                border: 1px solid black;
                padding: 3px;
            }
            QPushButton:hover {
                color: blue;
            }
        """)

        # Step 5: Set the layout for the central widget
        central_widget.setLayout(main_layout)

        # Connecting the buttons to their respective functions
        self.button.clicked.connect(self.clicking)
        self.button_3.clicked.connect(self.close)
        self.button_2.clicked.connect(self.dialog_box)
        self.button_4.clicked.connect(self.button_4_link)
        self.button_5.clicked.connect(self.button_5_link)
        self.button_6.pressed.connect(self.button_6_link)

    def button_4_link(self):
        """Change the main window background color to light yellow."""
        self.setStyleSheet("""
            QMainWindow {
                background-color: lightyellow;
            }
        """)

    def button_5_link(self):
        """Placeholder for button 5 action."""
        pass

    def button_6_link(self):
        """Print a message when button 6 is pressed."""
        print('Only prints when pressed')

    def dialog_box(self):
        """Display a dialog box with a message."""
        dialog = QMessageBox()
        dialog.setText('Created A dialog box')
        dialog.exec()

    def clicking(self):
        """Print a message when the 'Display' button is clicked."""
        print('Hi Sajan')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
