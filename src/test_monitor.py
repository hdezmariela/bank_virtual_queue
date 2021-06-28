import sys
from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
        QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget, QLabel)
import paho.mqtt.client as mqtt
import threading
import logging

class OutputMonitorWindow(QWidget):
    # ticket_queue = ['', '', '', '', '', '', '', '', '', '']
    # #ticket_queue = list = ['', '', '', '', '', '', '', '', '', '', 'P003', 1, 'P004', 2, 'C001', 2, 'S001', 1, 'S002', 1]
    # add_counter = 0
    # adds = ['cocacola.jpg', 'uber.jpg', 'mac.jpg', 'uber2.jpg', 'walmart.jpg']
    # first_time = True
    valueUpdated = Signal(list)
    def __init__(self):
        super().__init__()
        self.ticket_queue = ['', '', '', '', '', '', '', '', '', '']
        #ticket_queue = list = ['', '', '', '', '', '', '', '', '', '', 'P003', 1, 'P004', 2, 'C001', 2, 'S001', 1, 'S002', 1]
        self.add_counter = 0
        self.adds = ['cocacola.jpg', 'uber.jpg', 'mac.jpg', 'uber2.jpg', 'walmart.jpg']
        self.first_time = True
        
        
        self.grid = QGridLayout()
        self.grid.addWidget(self.current_ticket_group(), 0, 0, 4, 1)
        self.grid.addWidget(self.up_next_group1(self.ticket_queue[2], self.ticket_queue[3]), 0, 1)
        self.grid.addWidget(self.up_next_group2(self.ticket_queue[4], self.ticket_queue[5]), 1, 1)
        self.grid.addWidget(self.up_next_group3(self.ticket_queue[6], self.ticket_queue[7]), 2, 1)
        self.grid.addWidget(self.up_next_group4(self.ticket_queue[8], self.ticket_queue[9]), 3, 1)
        self.grid.addWidget(self.banner_group(), 4, 0, 1, 2)
        
        self.setLayout(self.grid)
        
        self.valueUpdated.connect(self.add_ticket_to_queue)

        #self.resize(1080, 300)
    @Slot()
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
        
        self.label_2 = QLabel(self.ticket_queue[0] if len(self.ticket_queue) > 0 else '')
        self.label_2.setFont(self.my_font75b)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setStyleSheet("color: red")
        
        
        self.label_3 = QLabel("Please Proceed To")
        self.label_3.setFont(self.my_font24)
        self.label_3.setAlignment(Qt.AlignCenter)
        
        self.label_4 = QLabel(f"Counter {self.ticket_queue[1]}" if len(self.ticket_queue) > 1 else '')
        self.label_4.setFont(self.my_font35b)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setStyleSheet("color: blue")
        
        # TEST TO DEBUG UPDATE FUNCTION
        button = QPushButton('magia')
        #button.clicked.connect(lambda: self.update_queue_and_add(['A055', 3, 'A502', 6, 'A101', 9, 'A003', 6, 'A152', 3]))
        button.clicked.connect(self.magia)
        vbox = QVBoxLayout()
        vbox.addWidget(button)
        vbox.addWidget(self.label_1)
        vbox.addWidget(self.label_2)
        vbox.addWidget(self.label_3)
        vbox.addWidget(self.label_4)
        #vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

    def magia(self):
        print("magia")


    @Slot()    
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
    
    @Slot()
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

    @Slot()
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

    @Slot()
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

    @Slot()
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
    
    
    @Slot()
    def update_add(self):
        print("llegue aqui")
        image = ''
        if (self.add_counter == len(self.adds)):
            self.add_counter = 0
        
        image = self.adds[self.add_counter]
        self.add_counter += 1
        
        self.pixmap = QPixmap(f'images/{image}')
        self.label_add.setPixmap(self.pixmap)
        print("llegue aqui anuncio")
        widget.show()
    
    @Slot()
    def add_ticket_to_queue(self, msg):
        print("printing msg: {}".format(msg))
        #print(msg)
        ss = msg[0].split(',')
        print(ss)
        id = ss[0]
        print('ss1')
        print(ss[1])
        counter = int(ss[1])
        print(id)
        print(counter)
        flag = False
        #replace = False
        
        for i in range(len(self.ticket_queue)):
            if self.ticket_queue[i] == '' and self.ticket_queue[i+1] == '':
                self.ticket_queue[i] = id
                self.ticket_queue[i+1] = counter
                flag = True
                break
            else:
                flag = False
        
        if not flag:
            self.ticket_queue.append(id)
            self.ticket_queue.append(counter)
        
        print("####### TICKET QUEUE ######")
        print(self.ticket_queue)
        
        # Update labels
        print('llegue auqi')
        self.label_5.setText(self.ticket_queue[0])
        print('llegue auqi22')
        self.label_6.setText(f"Counter {self.ticket_queue[1]}")
        self.label_7.setText(self.ticket_queue[4])
        self.label_8.setText(f"Counter {self.ticket_queue[5]}")
        self.label_9.setText(self.ticket_queue[6])
        self.label_10.setText(f"Counter {self.ticket_queue[7]}")
        self.label_11.setText(self.ticket_queue[8])
        self.label_12.setText(f"Counter {self.ticket_queue[9]}")
        print('llegue auqi')
        widget.show()
        self.update_add()
        print('llegue auqi')
        
        #widget.main()
        
    
    @Slot()
    def update_serving_now(self, msg):
        print(msg)
        ss = msg.split(',')
        print(ss)
        #type = ss[0]
        type = 'C'
        #counter = int(ss[1])
        counter = 3
        print(type)
        print(counter)
        
        found_it = False
        index = ''
        
        for i in range(len(self.ticket_queue)):
            res = isinstance(self.ticket_queue[i], str)
            if res and len(self.ticket_queue[i]) > 0:
                id = self.ticket_queue[i]
                if id[0] == type:
                    if self.ticket_queue[i+1] == counter:
                        print(self.ticket_queue[i])
                        found_it = True
                        index = i
        
        del self.ticket_queue[index]
        del self.ticket_queue[index]
        
        # Update text from now serving ticket
        self.label_2.setText(self.ticket_queue[index])
        self.label_4.setText(f"Counter {self.ticket_queue[index + 1]}")
        self.update_add()
    
def on_connect(client, userdata, flags, rc):
    print("Se conecto con mqtt " + str(rc))
    client.subscribe("BQMS/#")
    
def on_message(client, userdata, msg):
    if msg.topic == "BQMS/new_ticket":
        print(f"New ticket ID,counter: {str(msg.payload)}")
        #userdata[0].update_queue_and_add(str(msg.payload, "utf-8"))
        #userdata[0].add_ticket_to_queue(str(msg.payload, "utf-8"))
        userdata[0].valueUpdated.emit([str(msg.payload, "utf-8")])
        print("estoy en on msg")
    elif msg.topic == "BQMS/ticket_attended":
        print(f"Tickect attended: {str(msg.payload)}")
        userdata[0].update_serving_now(str(msg.payload, "utf-8"))
    print(msg.topic+" "+str(msg.payload))

def thread_function(client):
    logging.info("Thread mqtt_sub: starting")
    client.loop_start()

def close_mqtt(client):
    logging.info("Main thread (GUI): finishing")
    logging.info("Thread mqtt_sub: finishing")
    client.loop_stop()

def destroy():
    print("about to be destroyed")

def Start():
    global widget
    widget = OutputMonitorWindow()
    widget.setWindowTitle("Output Monitor")
    widget.show()
    return widget

if __name__ == '__main__':
    # mqtt client
    client_userdata = []
    client = mqtt.Client(userdata=client_userdata)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("test.mosquitto.org", 1883, 60)
    
    # Start mqtt subscribe thread
    mqtt_sub_thread = threading.Thread(target=thread_function, args=(client,))
    mqtt_sub_thread.start()

    app = QApplication(sys.argv)
    #app.setQuitOnLastWindowClosed(False)
    app.lastWindowClosed.connect(lambda: close_mqtt(client))
    #app.destroyed.connect(destroy)
    
    #global widget
    #widget = OutputMonitorWindow()
    #widget.setWindowTitle("Output Monitor")
    #widget.show()
    window = Start()
    client_userdata.append(widget)
    
    
    app.exec()
    # Run the main Qt loop
    logging.info("Main thread (GUI): starting")
    #print(app.exec())
    #sys.exit(app.exec())