import sys        
import sqlite3
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon                                                       
from PyQt6.QtWidgets import QApplication, QToolBar, QStatusBar, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(800, 600)
        
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")
        
        add_student_action = QAction(QIcon("OOP/student-management-system/icons/add.png"),"Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)
        
        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)
        
        search_action = QAction(QIcon("OOP/student-management-system/icons/search.png"),"Search", self)
        edit_menu_item.addAction(search_action)
        search_action.triggered.connect(self.search)
        
        
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)
        
        # Create toolbar and add toolbar elements
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)
        
        # Create status bar and add status bar elements
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        
        # Detect a cell click
        self.table.cellClicked.connect(self.cell_clicked)
        
    def cell_clicked(self):
        edit_button = QPushButton("Edit Record")    
        edit_button.clicked.connect(self.edit)
        
        delete_button = QPushButton("Delete Record")    
        delete_button.clicked.connect(self.delete)
        
        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)
        
        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)
        
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
    
    def search(self):
        dialog = SearchDialog()
        dialog.exec()
    
    def edit(self):
        dialog = EditDialog()
        dialog.exec()
    
    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()   
         
class EditDialog(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Update Student Data")         
            self.setFixedWidth(300)
            self.setFixedHeight(300)
            
            layout = QVBoxLayout()
            # Get student name from selected row
            index = main_window.table.currentRow()
            student_name = main_window.table.item(index, 1).text()
            
            # Get ID form selected row
            self.student_id = main_window.table.item(index, 0).text()
            
            # Edit student name widget
            self.student_name = QLineEdit(student_name)
            self.student_name.setPlaceholderText("Name")
            layout.addWidget(self.student_name)
            
            # Add combo box of courses
            course_name = main_window.table.item(index, 2).text()
            self.course_name = QComboBox()
            courses = ["Biology", "Math", "Astronomy", "Physics"]
            self.course_name.addItems(courses)
            self.course_name.setCurrentText(course_name)
            layout.addWidget(self.course_name)
            
            # Add mobile widget
            monile = main_window.table.item(index, 3).text()
            self.mobile = QLineEdit()
            self.mobile.setPlaceholderText("Phone Number")
            layout.addWidget(self.mobile)
            
            # Add a submit button
            button = QPushButton("Update")
            button.clicked.connect(self.update_student)
            layout.addWidget(button)
            
            self.setLayout(layout)
        
        def update_student(self):
            connection = sqlite3.connect("OOP/student-management-system/database.db")
            cursor = connection.cursor()
            cursor.execute("UPDATE students SET name = ?, course = ?, mobile = ? WHERE id = ?",
                           (self.student_name.text(), 
                            self.course_name.itemText(self.course_name.currentIndex()), 
                            self.mobile.text(), 
                            self.student_id))
            connection.commit()
            cursor.close()
            connection.close()
            
            # Refresh the table
            main_window.load_data()

    
    
class DeleteDialog(QDialog):
        pass
    
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
            self.mobile = QLineEdit()
            self.mobile.setPlaceholderText("Phone Number")
            layout.addWidget(self.cell_phone)
            
            # Add a submit button
            button = QPushButton("Register")
            button.clicked.connect(self.add_student)
            layout.addWidget(button)
            
            self.setLayout(layout)
        def add_student(self):
            name = self.student_name.text()
            course =  self.course_name.itemText(self.course_name.currentIndex())
            mobile = self.mobile.text()
            connection = sqlite3.connect("OOP/student-management-system/database.db")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO students (name, course, mobile) Values (?, ?, ?)",
                           (name, course, mobile))
            connection.commit()
            cursor.close()
            connection.close()
            main_window.load_data()
            
class SearchDialog(QDialog): 
    def __init__(self):
        super().__init__()
        # Set window title and size
        self.setWindowTitle("Search Student") 
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        
        # Create layout and input widget
        layout = QVBoxLayout()
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)
        
        # Create button
        button = QPushButton("Search")
        button.clicked.connect(self.search)
        layout.addWidget(button)
        
        self.setLayout(layout)
    
    def search(self):
        name = self.student_name.text()
        connection = sqlite3.connect("OOP/student-management-system/database.db")
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        rows = list(result)
        print(rows)
        items = main_window.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            print(item)
            main_window.table.item(item.row(), 1).setSelected(True)
            
        cursor.close()
        connection.close()
                 
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())