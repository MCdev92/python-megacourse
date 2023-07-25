import sys        
from PyQt6.QtGui import QAction                                                       
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        
        add_student_action = QAction("Add Student", self)
        file_menu_item.addAction(add_student_action)
        
        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)
        

        
app = QApplication(sys.argv)
calculator = MainWindow()
calculator.show()
sys.exit(app.exec())