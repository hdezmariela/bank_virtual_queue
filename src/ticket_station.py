#!/usr/bin/python

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QFont
from datetime import datetime

class TicketStationWidget(QWidget):
    checkout_ticket_counter = 0
    platform_ticket_counter = 0
    customer_service_ticket_counter = 0
    checkout_queue = [0, 0, 0, 0, 0]
    platform_queue = [0, 0, 0]
    customer_service_queue = [0]
        
    def __init__(self):
        super().__init__()
        
        my_font20 = QFont("Times New Roman", 20, QFont.Bold)
        my_font16 = QFont("Times New Roman", 16, QFont.Bold)
        my_font12 = QFont("Times New Roman", 12)
        
        
        #Create a Qt Vertical Layout
        self.layout = QVBoxLayout(self)
        
        self.label_welcome = QLabel("WELCOME!")
        self.label_welcome.setAlignment(Qt.AlignCenter)
        self.label_welcome.setFont(my_font20)
        self.label_welcome.setStyleSheet("color: blue")
        
        self.label_instructions = QLabel("Please select an option")
        self.label_instructions.setAlignment(Qt.AlignCenter)
        self.label_instructions.setFont(my_font16)
        
        self.button_checkout = QPushButton('Checkout')
        self.button_checkout.setFont(my_font12)
        
        self.button_platform = QPushButton('Platform')
        self.button_platform.setFont(my_font12)
        
        self.button_customer_service = QPushButton('Customer Service')
        self.button_customer_service.setFont(my_font12)
        
        self.layout.addWidget(self.label_welcome)
        self.layout.addWidget(self.label_instructions)
        self.layout.addStretch(1)
        self.layout.addWidget(self.button_checkout)
        self.layout.addWidget(self.button_platform)
        self.layout.addWidget(self.button_customer_service)
        
        self.button_checkout.clicked.connect(self.new_checkout_ticket)
        self.button_platform.clicked.connect(self.new_platform_ticket)
        self.button_customer_service.clicked.connect(self.new_customer_service_ticket)
    
    @Slot()
    def new_checkout_ticket(self):
        self.datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Calculate new checkout ID ticket
        id = 'C' + str(self.checkout_ticket_counter).zfill(3)
        
        # Assign the counter
        min_value = min(self.checkout_queue)
        min_index = self.checkout_queue.index(min_value)
        
        # Print log
        print(f"{self.datetime}   New checkout ticket! ID: {id}, Counter: {min_index + 1}")
        
        # Increase internal counts
        self.checkout_ticket_counter += 1 
        self.checkout_queue[min_index] += 1
        
        # For debug
        print(f'checkout: {self.checkout_queue}')
        print(f'platform: {self.platform_queue}')
        print(f'customer service: {self.customer_service_queue}')

    @Slot()
    def new_platform_ticket(self):
        self.datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Calculate new checkout ID ticket
        id = 'P' + str(self.platform_ticket_counter).zfill(3)
        
        # Assign the counter
        min_value = min(self.platform_queue)
        min_index = self.platform_queue.index(min_value)
        
        # Print log
        print(f"{self.datetime}   New platform ticket! ID: {id}, Counter: {min_index +1 }")
        
        # Increase internal counts
        self.platform_ticket_counter += 1 
        self.platform_queue[min_index] += 1

        # For debug
        print(f'checkout: {self.checkout_queue}')
        print(f'platform: {self.platform_queue}')
        print(f'customer service: {self.customer_service_queue}')
        
    @Slot()
    def new_customer_service_ticket(self):
        self.datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Calculate new checkout ID ticket
        id = 'P' + str(self.customer_service_ticket_counter).zfill(3)
        
        # Assign the counter
        min_value = min(self.customer_service_queue)
        min_index = self.customer_service_queue.index(min_value)
        
        # Print log
        print(f"{self.datetime}   New customer service ticket! ID: {id}, Counter: {min_index +1 }")
        
        # Increase internal counts
        self.customer_service_ticket_counter += 1 
        self.customer_service_queue[min_index] += 1
        
        # For debug
        print(f'checkout: {self.checkout_queue}')
        print(f'platform: {self.platform_queue}')
        print(f'customer service: {self.customer_service_queue}')

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = TicketStationWidget()
    widget.setWindowTitle('Ticket Station')
    widget.resize(200, 200)
    widget.show()
    
    # Run the main Qt loop
    sys.exit(app.exec())