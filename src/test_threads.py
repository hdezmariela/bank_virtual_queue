# import logging
# import threading
# import time

# def thread_function(name):
    # logging.info("Thread %s: starting", name)
    # time.sleep(2)
    # logging.info("Thread %s: finishing", name)

# if __name__ == "__main__":
    # format = "%(asctime)s: %(message)s"
    # logging.basicConfig(format=format, level=logging.INFO,
                        # datefmt="%H:%M:%S")

    # logging.info("Main    : before creating thread")
    # x = threading.Thread(target=thread_function, args=(1,))
    # logging.info("Main    : before running thread")
    # x.start()
    # logging.info("Main    : wait for the thread to finish")
    # x.join()
    # logging.info("Main    : all done")
    
from PySide6 import QtGui
import sys


def keep_alive():
    print("ah..ah..ah..ah...staying alive...staying alive")
    #window.setVisibility(QtGui.QWindow.Minimized)


if __name__ == '__main__':
    app = QtGui.QGuiApplication()
    #app.setQuitOnLastWindowClosed(False)
    app.lastWindowClosed.connect(keep_alive)

    window = QtGui.QWindow()
    window.show()

    sys.exit(app.exec())