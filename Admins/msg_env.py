from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import Qt
import sys
import Resources_rc
class message_ui:
    def __init__(self,msg_text,etat):
        if etat == 1:
            self.text = ":/Icons/Icons/277-2778613_success-icon-png-transparent-png-removebg-preview.png"

        else :
            self.text = ":/Icons/Icons/refuse-removebg-preview.png"
        icon = QIcon(self.text)
        msg = QMessageBox()
        msg.setIconPixmap(icon.pixmap(60, 60))
        msg.setText(msg_text)
        msg.exec_()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ui = message_ui('hh',2)
    sys.exit(app.exec_())



    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    
    sys.exit(app.exec_())