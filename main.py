import functools
import sys
import PyQt5.Qt
import socket



class MainWindow(PyQt5.Qt.QWidget):
    def __init__(self):
        PyQt5.Qt.QWidget.__init__(self)
        self.chatbox = PyQt5.Qt.QTextEdit(self)
        self.chatbox.setReadOnly(True)
        self.chatbox.installEventFilter(self)
        self.messagebar = PyQt5.Qt.QLineEdit(self)
        self.messagebar.installEventFilter(self)
        layout = PyQt5.Qt.QVBoxLayout(self)
        layout.addWidget(self.chatbox)
        layout.addWidget(self.messagebar)


class UserForm(PyQt5.Qt.QWidget):
    def __init__(self):
        PyQt5.Qt.QWidget.__init__(self)
        parentLayout = PyQt5.Qt.QVBoxLayout()

        ## QT5 Widgets
        self.line = PyQt5.Qt.QLineEdit(self)
        self.line.installEventFilter(self)
        self.server = PyQt5.Qt.QLineEdit(self)
        self.server.installEventFilter(self)
        self.port = PyQt5.Qt.QLineEdit(self)
        self.port.installEventFilter(self)

        ## Forum Rows & Layout
        forumlayout = PyQt5.Qt.QFormLayout()
        forumlayout.addRow("Name:", self.line)
        forumlayout.addRow("Server:", self.server)
        forumlayout.addRow("Port:", self.port)


        ## Button Actions and Connectors
        button = PyQt5.Qt.QDialogButtonBox()
        button.setStandardButtons(
            PyQt5.Qt.QDialogButtonBox.Ok | PyQt5.Qt.QDialogButtonBox.Cancel
        )
        button.accepted.connect(self.close)
        button.accepted.connect(self.show_Chat_Window)
        button.rejected.connect(sys.exit)

        ## Add Layout
        parentLayout.addLayout(forumlayout)
        parentLayout.addWidget(button)
        self.setLayout(parentLayout)




        ## Show Chat Window
    def show_Chat_Window(self):
        ## Network Connection

        ### Try to Connect
        try:
            self.networkconnect = ServerConnection()
            self.networkconnect.ip = self.server.displayText()
            self.networkconnect.port = self.port.displayText()
            self.networkconnect.connect(host=self.networkconnect.ip, port=self.networkconnect.port)

            ## Currently print to console and exit app
        except:
            print("Could not connect to host")
            sys.exit()



        ChatWindow.chatbox.wordWrapMode()
        ChatWindow.messagebar.returnPressed.connect(self.show_text)
        ChatWindow.show()
        ChatWindow.activateWindow()

    def show_text(self):
        HostMessage = ChatWindow.messagebar.displayText()
        self.networkconnect.send_message(HostMessage)
        ChatWindow.chatbox.append(f"{self.line.displayText()}: {HostMessage}")

        ChatWindow.messagebar.clear()

class ServerConnection:


    def __init__(self):
        self.clientInfo = UserForm()
        self.socket = socket.socket()


    def connect(self,host,port):
        self.host = host
        self.port = int(port)
        self.server = (self.host, self.port)
        self.socket.connect(self.server)

    def send_message(self, Message):
        self.message = Message
        self.socket.send(self.message.encode())


### Global Variables
app = PyQt5.Qt.QApplication(sys.argv)

ChatWindow = MainWindow()
ChatWindow.setGeometry(800, 500, 500, 500)
messages = []
message_history = []



## Functions
def main():
    thisUser = UserForm()
    thisUser.show()
    sys.exit(app.exec())
   ### Show

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
