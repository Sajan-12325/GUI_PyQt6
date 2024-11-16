import sys
from PyQt6.QtWidgets import QApplication,QWidget, QPushButton, QMainWindow, QTextEdit, QMenuBar, QMenu,  QToolBar, QStatusBar, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sajan Display")
        self.setMinimumSize(300, 200)

        # Step 1: Create and set the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Step 2: Create the child widget
        self.button = QPushButton("Press Here")

        # Step 3: Create a layout manager
        layout = QHBoxLayout()

        # Step 4: Add the child widget to the layout manager
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignLeft)

        # Step 5: Set the layout for the central widget
        central_widget.setLayout(layout)

        # Connect the button click signal to the slot
        self.button.clicked.connect(self.clicking)

    

    def clicking(self):
        print('You pushed the button')




        # Central widget
        """ self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

        # Menu bar
        self.menu_bar = self.menuBar()

        # File menu
        file_menu = self.menu_bar.addMenu("File")
        new_action = QAction("New", self)
        open_action = QAction("Open...", self)
        save_action = QAction("Save", self)
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

       

        # Tools menu
        tools_menu = self.menu_bar.addMenu("Tools")
        settings_action = QAction("Settings", self)
        tools_menu.addAction(settings_action)  """

        

        


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
