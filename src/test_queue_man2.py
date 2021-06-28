import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
        QMenu, QPushButton, QRadioButton, QHBoxLayout, QWidget, QLabel)
import paho.mqtt.client as mqtt
import threading
import time
import logging

class QueueManagerWindow(QWidget):
    checkout_queue = [0, 0, 0, 0, 0]
    platform_queue = [0, 0, 0]
    customer_service_queue = [0]
    buttons = []
    
    def __init__(self, mqtt_client):
        super().__init__()
        
        self.client = mqtt_client
        
        grid = QGridLayout()
        grid.addWidget(self.checkout_group(), 0, 0)
        grid.addWidget(self.platform_group(), 1, 0)
        grid.addWidget(self.customer_service_group(), 2, 0)
        self.setLayout(grid)
        
        self.update_in_queue_text()
    
    @Slot()
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
        
        self.buttons.append(self.button_counter1)
        self.buttons.append(self.button_counter2)
        self.buttons.append(self.button_counter3)
        self.buttons.append(self.button_counter4)
        self.buttons.append(self.button_counter5)
        
        self.button_counter1.setStyleSheet(f"background-color: #1ced2e")
        self.button_counter2.setStyleSheet(f"background-color: #1ced2e")
        self.button_counter3.setStyleSheet(f"background-color: #1ced2e")
        self.button_counter4.setStyleSheet(f"background-color: #1ced2e")
        self.button_counter5.setStyleSheet(f"background-color: #1ced2e")

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
    
    @Slot()    
    def platform_group(self):
        groupBox = QGroupBox("Platform counters")

        self.label_counter6 = QLabel()
        self.label_counter7 = QLabel()
        self.label_counter8 = QLabel()
        self.button_counter6 = QPushButton("Counter 6")
        self.button_counter7 = QPushButton("Counter 7")
        self.button_counter8 = QPushButton("Counter 8")
        
        self.buttons.append(self.button_counter6)
        self.buttons.append(self.button_counter7)
        self.buttons.append(self.button_counter8)
        
        self.button_counter6.setMaximumWidth(75)
        self.button_counter7.setMaximumWidth(75)
        self.button_counter8.setMaximumWidth(75)
        
        self.button_counter6.setStyleSheet(f"background-color: #1ced2e")
        self.button_counter7.setStyleSheet(f"background-color: #1ced2e")
        self.button_counter8.setStyleSheet(f"background-color: #1ced2e")
        
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
    
    @Slot()
    def customer_service_group(self):
        groupBox = QGroupBox("Customer Service counters")

        self.label_counter9 = QLabel()
        self.button_counter9 = QPushButton("Counter 9")
        
        self.buttons.append(self.button_counter9)
        
        self.button_counter9.setMaximumWidth(75)
        
        self.button_counter9.setStyleSheet(f"background-color: #1ced2e")
        
        self.button_counter9.clicked.connect(lambda: self.decrease_queue('S', 0))
        
        grid = QGridLayout()
        grid.addWidget(self.button_counter9, 0, 0)
        grid.addWidget(self.label_counter9, 1, 0)

        groupBox.setLayout(grid)

        return groupBox
    
    @Slot()
    def assign_button_color(self, tickets_in_queue):
        green = '#1ced2e'
        red = '#fc3d3d'
        
        print("tickets in queue {}".format(tickets_in_queue))
        if (tickets_in_queue == 0):
            print("green")
            return green
        else:
            print("red")
            return red
    

    @Slot()
    def decrease_queue(self, type, index):
        if (type == 'C' and self.checkout_queue[index] != 0):
            self.checkout_queue[index] -= 1
            # Send msg of ticket attended: type,index
            self.client.publish("BQMS/ticket_attended", f"C,{index + 1}")
        elif (type == 'P' and self.platform_queue[index] != 0):
            self.platform_queue[index] -= 1
            # Send msg of ticket attended: type,index
            self.client.publish("BQMS/ticket_attended", f"P,{index + 1}")
        elif (type == 'S' and self.customer_service_queue[index] != 0):
            self.customer_service_queue[index] -= 1
            # Send msg of ticket attended: type,index
            self.client.publish("BQMS/ticket_attended", f"S,{index + 1}")

        self.update_button_color(type, index)
        self.update_in_queue_text()
    
    @Slot()
    def increase_queue(self, msg):
        print(msg)
        ss = msg.split(',')
        print(ss)
        id = ss[0]
        index = int(ss[1]) - 1
        print(id)
        print(index)
        type = ''
        
        if (id[0] == 'C'):
            type = 'C'
            print(self.checkout_queue)
            self.checkout_queue[index] += 1
            print(self.checkout_queue)
        elif (id[0] == 'P'):
            type = 'P'
            print(self.platform_queue)
            self.platform_queue[index] += 1
            print(self.platform_queue)
        elif (id[0] == 'S'):
            type = 'S'
            print(self.customer_service_queue)
            self.customer_service_queue[index] += 1
            print(self.customer_service_queue)
            
        self.update_button_color(type, index)
        self.update_in_queue_text()
            
        
    @Slot()
    def update_in_queue_text(self):
        #print("update in queue text")
        self.label_counter1.setText(f'In queue: {self.checkout_queue[0]}')
        print(f'In queue: {self.checkout_queue[0]}')
        self.label_counter2.setText(f'In queue: {self.checkout_queue[1]}')
        print(f'In queue: {self.checkout_queue[1]}')
        self.label_counter3.setText(f'In queue: {self.checkout_queue[2]}')
        print(f'In queue: {self.checkout_queue[2]}')
        self.label_counter4.setText(f'In queue: {self.checkout_queue[3]}')
        print(f'In queue: {self.checkout_queue[3]}')
        self.label_counter5.setText(f'In queue: {self.checkout_queue[4]}')
        print(f'In queue: {self.checkout_queue[4]}')
        self.label_counter6.setText(f'In queue: {self.platform_queue[0]}')
        print(f'In queue: {self.platform_queue[0]}')
        self.label_counter7.setText(f'In queue: {self.platform_queue[1]}')
        print(f'In queue: {self.platform_queue[1]}')
        self.label_counter8.setText(f'In queue: {self.platform_queue[2]}')
        print(f'In queue: {self.platform_queue[2]}')
        self.label_counter9.setText(f'In queue: {self.customer_service_queue[0]}')
        print(f'In queue: {self.customer_service_queue[0]}')
    
    @Slot()
    def update_button_color(self, type, index):
        print('entre a update buton color')
        print(type)
        print(index)
        if type == 'C':
            print("entr a tipo C")
            self.buttons[index].setStyleSheet(f"background-color: {self.assign_button_color(self.checkout_queue[index])}")
        elif type == 'P':
            self.buttons[index + 5].setStyleSheet(f"background-color: {self.assign_button_color(self.platform_queue[index])}")
        elif type == 'S':
            self.buttons[8].setStyleSheet(f"background-color: {self.assign_button_color(self.customer_service_queue[0])}")

def on_connect(client, userdata, flags, rc):
    logging.info("Connected with result code " + str(rc))
    client.subscribe("BQMS/#")
    
def on_message(client, userdata, msg):
    global checkout_queue
    if msg.topic == "BQMS/new_ticket":
        print(f"New ticket ID,counter: {str(msg.payload)}")
        userdata[0].increase_queue(str(msg.payload, "utf-8"))
        
    print(msg.topic+" "+str(msg.payload))

def thread_function(client):
    logging.info("Thread mqtt_sub: starting")
    client.loop_start()

def close_mqtt(client):
    logging.info("Main thread (GUI): finishing")
    logging.info("Thread mqtt_sub: finishing")
    client.loop_stop()

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    # mqtt client
    client_userdata = []
    client = mqtt.Client(userdata=client_userdata)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("test.mosquitto.org", 1883, 60)
    
    # Start mqtt subscribe thread
    mqtt_sub_thread = threading.Thread(target=thread_function, args=(client,))
    mqtt_sub_thread.start()
    
    # GUI
    app = QApplication(sys.argv)
    app.lastWindowClosed.connect(lambda: close_mqtt(client))
    
    widget = QueueManagerWindow(client)
    widget.setWindowTitle("Queue Manager")
    widget.show()
    
    client_userdata.append(widget)
    print(client_userdata)
    
    # Run the main Qt loop
    logging.info("Main thread (GUI): starting")
    sys.exit(app.exec())
    #t2 = threading.Thread(target=thread_2, args=(app,))
    #t2.start()