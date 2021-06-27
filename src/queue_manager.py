import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
        QMenu, QPushButton, QRadioButton, QHBoxLayout, QWidget, QLabel)

class QueueManagerWindow(QWidget):
    checkout_queue = [1, 0, 2, 0, 4]
    platform_queue = [0, 0, 2]
    customer_service_queue = [3]
    
    def __init__(self, parent=None):
        super().__init__()

        grid = QGridLayout()
        grid.addWidget(self.checkout_group(), 0, 0)
        grid.addWidget(self.platform_group(), 1, 0)
        grid.addWidget(self.customer_service_group(), 2, 0)
        self.setLayout(grid)
        
        self.update_button_color()
        self.update_in_queue_text()

    def checkout_group(self):
        groupBox = QGroupBox("Checkout counters")
        self.label_counter1 = QLabel()
        self.label_counter2 = QLabel()
        self.label_counter3 = QLabel()
        self.label_counter4 = QLabel()
        self.label_counter5 = QLabel()
        self.button_counter1 = QPushButton("Counter 1")
        self.button_counter2 = QPushButton("Counter 2")
        self.button_counter3 = QPushButton("Counter 3")
        self.button_counter4 = QPushButton("Counter 4")
        self.button_counter5 = QPushButton("Counter 5")

        self.button_counter1.clicked.connect(lambda: self.decrease_queue('C', 0))
        self.button_counter2.clicked.connect(lambda: self.decrease_queue('C', 1))
        self.button_counter3.clicked.connect(lambda: self.decrease_queue('C', 2))
        self.button_counter4.clicked.connect(lambda: self.decrease_queue('C', 3))
        self.button_counter5.clicked.connect(lambda: self.decrease_queue('C', 4))
        
        grid = QGridLayout()
        grid.addWidget(self.button_counter1, 0, 0)
        grid.addWidget(self.button_counter2, 0, 1)
        grid.addWidget(self.button_counter3, 0, 2)
        grid.addWidget(self.button_counter4, 0, 3)
        grid.addWidget(self.button_counter5, 0, 4)
        grid.addWidget(self.label_counter1, 1, 0)
        grid.addWidget(self.label_counter2, 1, 1)
        grid.addWidget(self.label_counter3, 1, 2)
        grid.addWidget(self.label_counter4, 1, 3)
        grid.addWidget(self.label_counter5, 1, 4)
        groupBox.setLayout(grid)

        return groupBox
    
    Slot()    
    def platform_group(self):
        groupBox = QGroupBox("Platform counters")

        self.label_counter6 = QLabel()
        self.label_counter7 = QLabel()
        self.label_counter8 = QLabel()
        self.button_counter6 = QPushButton("Counter 6")
        self.button_counter7 = QPushButton("Counter 7")
        self.button_counter8 = QPushButton("Counter 8")
        self.button_counter6.setMaximumWidth(75)
        self.button_counter7.setMaximumWidth(75)
        self.button_counter8.setMaximumWidth(75)
        
        self.button_counter6.clicked.connect(lambda: self.decrease_queue('P', 0))
        self.button_counter7.clicked.connect(lambda: self.decrease_queue('P', 1))
        self.button_counter8.clicked.connect(lambda: self.decrease_queue('P', 2))
        
        grid = QGridLayout()
        grid.addWidget(self.button_counter6, 0, 0)
        grid.addWidget(self.button_counter7, 0, 1)
        grid.addWidget(self.button_counter8, 0, 2)
        grid.addWidget(self.label_counter6, 1, 0)
        grid.addWidget(self.label_counter7, 1, 1)
        grid.addWidget(self.label_counter8, 1, 2)

        groupBox.setLayout(grid)

        return groupBox
        
    def customer_service_group(self):
        groupBox = QGroupBox("Customer Service counters")

        self.label_counter9 = QLabel()
        self.button_counter9 = QPushButton("Counter 9")
        self.button_counter9.setMaximumWidth(75)
        
        self.button_counter9.clicked.connect(lambda: self.decrease_queue('S', 0))
        
        grid = QGridLayout()
        grid.addWidget(self.button_counter9, 0, 0)
        grid.addWidget(self.label_counter9, 1, 0)

        groupBox.setLayout(grid)

        return groupBox
    
    Slot()
    def assign_button_color(self, tickets_in_queue):
        green = '#1ced2e'
        red = '#fc3d3d'
        
        if (tickets_in_queue == 0):
            return green
        else:
            return red
    

    Slot()
    def decrease_queue(self, type, index):
        if (type == 'C' and self.checkout_queue[index] != 0):
            self.checkout_queue[index] -= 1
        elif (type == 'P' and self.platform_queue[index] != 0):
            self.platform_queue[index] -= 1
        elif (type == 'S' and self.customer_service_queue[index] != 0):
            self.customer_service_queue[index] -= 1

        self.update_button_color()
        self.update_in_queue_text()
    
    Slot()
    def update_in_queue_text(self):
        self.label_counter1.setText(f'In queue: {self.checkout_queue[0]}')
        self.label_counter2.setText(f'In queue: {self.checkout_queue[1]}')
        self.label_counter3.setText(f'In queue: {self.checkout_queue[2]}')
        self.label_counter4.setText(f'In queue: {self.checkout_queue[3]}')
        self.label_counter5.setText(f'In queue: {self.checkout_queue[4]}')
        self.label_counter6.setText(f'In queue: {self.platform_queue[0]}')
        self.label_counter7.setText(f'In queue: {self.platform_queue[1]}')
        self.label_counter8.setText(f'In queue: {self.platform_queue[2]}')
        self.label_counter9.setText(f'In queue: {self.customer_service_queue[0]}')
    
    Slot()
    def update_button_color(self):
        self.button_counter1.setStyleSheet(f"background-color: {self.assign_button_color(self.checkout_queue[0])}")
        self.button_counter2.setStyleSheet(f"background-color: {self.assign_button_color(self.checkout_queue[1])}")
        self.button_counter3.setStyleSheet(f"background-color: {self.assign_button_color(self.checkout_queue[2])}")
        self.button_counter4.setStyleSheet(f"background-color: {self.assign_button_color(self.checkout_queue[3])}")
        self.button_counter5.setStyleSheet(f"background-color: {self.assign_button_color(self.checkout_queue[4])}")
        self.button_counter6.setStyleSheet(f"background-color: {self.assign_button_color(self.platform_queue[0])}")
        self.button_counter7.setStyleSheet(f"background-color: {self.assign_button_color(self.platform_queue[1])}")
        self.button_counter8.setStyleSheet(f"background-color: {self.assign_button_color(self.platform_queue[2])}")
        self.button_counter9.setStyleSheet(f"background-color: {self.assign_button_color(self.customer_service_queue[0])}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    widget = QueueManagerWindow()
    widget.setWindowTitle("Queue Manager")
    widget.show()
    
    # Run the main Qt loop
    sys.exit(app.exec())