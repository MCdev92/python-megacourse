import sys        
import sqlite3
from PyQt6.QtGui import QAction                                                       
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        
        add_student_action = QAction("Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)
        
        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)
        
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)
        
        
    def load_data(self):
        connection = sqlite3.connect("OOP/student-management-system/database.db")
        result = connection.execute("SELECT * FROM students")
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close() 
    
    def insert(self):
        dialog = InsertDialog()
        dialog.exec()
 
class InsertDialog(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Insert Student Data")         
            self.setFixedWidth(300)
            self.setFixedHeight(300)
            
            layout = QVBoxLayout()
            
            # Add student name widget
            self.student_name = QLineEdit()
            self.student_name.setPlaceholderText("Name")
            layout.addWidget(self.student_name)
            
            # Add combo box of courses
            self.course_name = QComboBox()
            courses = ["Biology", "Math", "Astronomy", "Physics"]
            self.course_name.addItems(courses)
            layout.addWidget(self.course_name)
            
            # Add mobile widget
            self.cell_phone = QLineEdit()
            self.cell_phone.setPlaceholderText("Phone Number")
            layout.addWidget(self.cell_phone)
            
            # Add a submit button
            button = QPushButton("Register")
            button.clicked.connect(self.add_student)
            layout.addWidget(button)
            
            self.setLayout(layout)
        def add_student(self):
            name = self.student_name.text()
            course =  self.course_name.itemText(self.course_name.currentIndex())
            mobile = self.cell_phone.text()
            connection = sqlite3.connect("OOP/student-management-system/database.db")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO students (name, course, mobile) Values (?, ?, ?)",
                           (name, course, mobile))
            connection.commit()
            cursor.close()
            connection.close()
            main_window.load_data()
  
                 
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())