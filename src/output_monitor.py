import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
        QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget, QLabel)

class OutputMonitorWindow(QWidget):
    ticket_queue = ['C055', 1, 'P502', 2, 'S101', 5, 'C003', 4, '', '']
    add_counter = 0
    adds = ['cocacola.jpg', 'uber.jpg', 'mac.jpg', 'uber2.jpg', 'walmart.jpg']
    
    def __init__(self, parent=None):
        super().__init__()

        self.grid = QGridLayout()
        self.grid.addWidget(self.current_ticket_group(), 0, 0, 4, 1)
        self.grid.addWidget(self.up_next_group1(self.ticket_queue[2], self.ticket_queue[3]), 0, 1)
        self.grid.addWidget(self.up_next_group2(self.ticket_queue[4], self.ticket_queue[5]), 1, 1)
        self.grid.addWidget(self.up_next_group3(self.ticket_queue[6], self.ticket_queue[7]), 2, 1)
        self.grid.addWidget(self.up_next_group4(self.ticket_queue[8], self.ticket_queue[9]), 3, 1)
        self.grid.addWidget(self.banner_group(), 4, 0, 1, 2)

        self.setLayout(self.grid)

        #self.resize(1080, 300)
    def current_ticket_group(self):
        groupBox = QGroupBox("Now Serving")
        self.my_font24 = QFont("Times New Roman", 24)
        self.my_font75b = QFont("Times New Roman", 75, QFont.Bold)
        self.my_font22 = QFont("Times New Roman", 22)
        self.my_font24b = QFont("Times New Roman", 28, QFont.Bold)
        self.my_font35 = QFont("Times New Roman", 35)
        self.my_font35b = QFont("Times New Roman", 35, QFont.Bold)
        
        self.label_1 = QLabel("Token Number")
        self.label_1.setFont(self.my_font35)
        self.label_1.setAlignment(Qt.AlignCenter)
        
        self.label_2 = QLabel(self.ticket_queue[0])
        self.label_2.setFont(self.my_font75b)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setStyleSheet("color: red")
        
        
        self.label_3 = QLabel("Please Proceed To")
        self.label_3.setFont(self.my_font24)
        self.label_3.setAlignment(Qt.AlignCenter)
        
        self.label_4 = QLabel(f"Counter {self.ticket_queue[1]}")
        self.label_4.setFont(self.my_font35b)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setStyleSheet("color: blue")
        
        # TEST TO DEBUG UPDATE FUNCTION
        button = QPushButton('holi')
        button.clicked.connect(lambda: self.update_queue_and_add(['A055', 3, 'A502', 6, 'A101', 9, 'A003', 6, 'A152', 3]))
        vbox = QVBoxLayout()
        vbox.addWidget(button)
        vbox.addWidget(self.label_1)
        vbox.addWidget(self.label_2)
        vbox.addWidget(self.label_3)
        vbox.addWidget(self.label_4)
        #vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox
        
    def up_next_group1(self, id, counter):
        groupBox = QGroupBox("Up Next")
        
        counter_text = ''
        if bool(counter):
            counter_text = f"Counter {counter}"
        
        self.label_5 = QLabel(id)
        self.label_5.setFont(self.my_font24b)
        self.label_5.setAlignment(Qt.AlignCenter)
        #self.label_5.setStyleSheet("color: blue")
        
        
        self.label_6 = QLabel(counter_text)
        self.label_6.setFont(self.my_font22)
        self.label_6.setAlignment(Qt.AlignCenter)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.label_5)
        
        vbox.addWidget(self.label_6)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox
        
    def up_next_group2(self, id, counter):
        groupBox = QGroupBox("Up Next")
        
        counter_text = ''
        if bool(counter):
            counter_text = f"Counter {counter}"
        
        self.label_7 = QLabel(id)
        self.label_7.setFont(self.my_font24b)
        self.label_7.setAlignment(Qt.AlignCenter)
        #self.label_5.setStyleSheet("color: blue")
        
        
        self.label_8 = QLabel(counter_text)
        self.label_8.setFont(self.my_font22)
        self.label_8.setAlignment(Qt.AlignCenter)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.label_7)
        
        vbox.addWidget(self.label_8)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

    def up_next_group3(self, id, counter):
        groupBox = QGroupBox("Up Next")
        
        counter_text = ''
        if bool(counter):
            counter_text = f"Counter {counter}"
        
        self.label_9 = QLabel(id)
        self.label_9.setFont(self.my_font24b)
        self.label_9.setAlignment(Qt.AlignCenter)
        #self.label_5.setStyleSheet("color: blue")
        
        
        self.label_10 = QLabel(counter_text)
        self.label_10.setFont(self.my_font22)
        self.label_10.setAlignment(Qt.AlignCenter)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.label_9)
        
        vbox.addWidget(self.label_10)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox    

    def up_next_group4(self, id, counter):
        groupBox = QGroupBox("Up Next")
        
        counter_text = ''
        if bool(counter):
            counter_text = f"Counter {counter}"
        
        self.label_11 = QLabel(id)
        self.label_11.setFont(self.my_font24b)
        self.label_11.setAlignment(Qt.AlignCenter)
        #self.label_5.setStyleSheet("color: blue")
        12
        
        self.label_12 = QLabel(counter_text)
        self.label_12.setFont(self.my_font22)
        self.label_12.setAlignment(Qt.AlignCenter)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.label_11)
        
        vbox.addWidget(self.label_12)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

    def banner_group(self):
        groupBox = QGroupBox("Advertisements")
        
        self.label_add = QLabel(self)
        self.pixmap = QPixmap('images/walmart.jpg')
        self.label_add.setPixmap(self.pixmap)
        self.label_add.setScaledContents(True)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.label_add)
        
        groupBox.setLayout(vbox)
        
        return groupBox
    
    Slot()
    def update_queue_and_add(self, queue):
        # Update text from now serving ticket
        self.label_2.setText(queue[0])
        self.label_4.setText(f"Counter {queue[1]}")
        
        # Update text from the next tickets in queue
        self.label_5.setText(queue[2])
        self.label_6.setText(f"Counter {queue[3]}" if bool(queue[3]) else '')
        self.label_7.setText(queue[4])
        self.label_8.setText(f"Counter {queue[5]}" if bool(queue[5]) else '')
        self.label_9.setText(queue[6])
        self.label_10.setText(f"Counter {queue[7]}" if bool(queue[7]) else '')
        self.label_11.setText(queue[8])
        self.label_12.setText(f"Counter {queue[9]}" if bool(queue[9]) else '')
        
        self.update_add()
    
    Slot()
    def update_add(self):
        image = ''
        if (self.add_counter == len(self.adds)):
            self.add_counter = 0
        
        image = self.adds[self.add_counter]
        self.add_counter += 1
        
        self.pixmap = QPixmap(f'images/{image}')
        self.label_add.setPixmap(self.pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    widget = OutputMonitorWindow()
    widget.setWindowTitle("Output Monitor")
    widget.show()
    
    # Run the main Qt loop
    sys.exit(app.exec())