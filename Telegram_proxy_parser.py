import re, os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit,\
                            QLabel, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QClipboard, QFont, QFontDatabase
from PyQt5 import uic
import webbrowser


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # set default values
        self.__path = os.path.dirname(os.path.abspath(__file__))
        self.__proxy = {
            "server": None,
            "port": None,
            "secret": None
        }
        # regex pattern for validate proxy link
        self.__pattern = r"https:\/\/t\.me\/proxy\?server=((2[01234]\d|25[0-5]|1\d{2}|\d{2}|\d)\.(2[01234]\d|25[0-5]|1\d{2}|\d{1,2})\.(2[01234]\d|25[0-5]|1\d{2}|\d{2}|\d)\.(2[01234]\d|25[0-5]|1\d{2}|\d{2}|\d)|((\w|\.|\-|\_)+))&port=(\d{1,4}|[1-5]\d{4}|6[0-5][0-5][0-3][0-5])&secret=(.+)"

        uic.loadUi(self.__path + "\\app.ui", self)
        self.setMinimumSize(600, 500)
        self.setWindowIcon(QIcon(self.__path + "\\image\\Telegram_logo.png"))

        self.__find_all_components()
        self.__load_styles()
        self.__set_functions()

        # self.show()

    def __find_all_components(self):
        self.header: QLabel = self.findChild(QLabel, "header")

        self.text_0: QLabel = self.findChild(QLabel, "text")

        self.text_sr: QLabel = self.findChild(QLabel, "text_sr")
        self.text_sc: QLabel = self.findChild(QLabel, "text_sc")
        self.text_p: QLabel = self.findChild(QLabel, "text_p")

        self.link_input: QLineEdit = self.findChild(QLineEdit, "link_input")

        self.confrim_btn: QPushButton = self.findChild(QPushButton, "confrim_btn")
        self.clear_btn: QPushButton = self.findChild(QPushButton, "clear_btn")
        
        self.port_btn: QPushButton = self.findChild(QPushButton, "port_btn")
        self.server_btn: QPushButton = self.findChild(QPushButton, "server_btn")
        self.secret_btn: QPushButton = self.findChild(QPushButton, "secret_btn")


    def __get_link_and_verify(self):
        # get link and validate it
        link = self.link_input.text().strip()
        if re.match(self.__pattern, link) is None: # doesn't match
            # create a message box and show the error
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowIcon(QIcon(self.__path + "\\image\\error.png"))
            msg_box.setWindowTitle("Invalied Link")
            msg_box.setText("Your link is not valied !\nPlease review the link.\nIf you sure that link is coorect,\
                            \nplease click on \"open\" button to creating an issue in Github to fix the bug.\
                            \nGithub ID: galaxy248")
            msg_box.setStyleSheet("QMessageBox { font: 14pt \"Open Sans Medium\" rgb(0, 0, 127);\
                                   background-color: rgb(221, 239, 255) }")
            msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Open | QMessageBox.Help)
            btn = msg_box.exec_()
            if btn == QMessageBox.Ok:
                pass
            elif btn == QMessageBox.Open:
                webbrowser.open_new_tab("https://github.com/galaxy248/telegram_proxy_parser/issues")
            elif btn == QMessageBox.Help:
                # create a message box and show the help page
                help_msg_box = QMessageBox()
                help_msg_box.setIcon(QMessageBox.Information)
                help_msg_box.setWindowIcon(QIcon(self.__path + "\\image\\info.png"))
                help_msg_box.setWindowTitle("Valied Format Link")
                help_msg_box.setText("Valied Format Link:\n(https|http)://(telegram|t).me/proxy?server=(SERVER IP|LINK)&port=(NUMBER LESS THAN 65,535)&secret=(KEY EXPRESSION)")
                help_msg_box.setStyleSheet("QMessageBox { font: 14pt \"Open Sans Medium\" rgb(0, 0, 127); background-color: rgb(221, 239, 255)}")
                help_msg_box.setStandardButtons(QMessageBox.Ok)
                help_msg_box.exec_()
            else:
                pass
        else:
            sections = re.findall(self.__pattern, link)
            self.__proxy["server"] = sections[0][0]
            self.__proxy["port"] = sections[0][7]
            self.__proxy["secret"] = sections[0][8]

    def __clear_link_input(self):
        self.link_input.clear()
        self.__proxy["server"] = None
        self.__proxy["secret"] = None
        self.__proxy["port"] = None

    def __server_copy_button_clicked(self):
        clipboard: QClipboard = QApplication.clipboard()
        clipboard.clear()
        clipboard.setText(self.__proxy["server"])

    def __secret_copy_button_clicked(self):
        clipboard: QClipboard = QApplication.clipboard()
        clipboard.clear()
        clipboard.setText(self.__proxy["secret"])

    def __port_copy_button_clicked(self):
        clipboard: QClipboard = QApplication.clipboard()
        clipboard.clear()
        clipboard.setText(self.__proxy["port"])

    def __set_functions(self):
        self.confrim_btn.clicked.connect(self.__get_link_and_verify)
        self.clear_btn.clicked.connect(self.__clear_link_input)
        
        self.server_btn.clicked.connect(self.__server_copy_button_clicked)
        self.secret_btn.clicked.connect(self.__secret_copy_button_clicked)
        self.port_btn.clicked.connect(self.__port_copy_button_clicked)

    def __load_styles(self):
        # load fonts
        QFontDatabase.addApplicationFont(self.__path + "\\font\\Colakind.ttf")
        QFontDatabase.addApplicationFont(self.__path + "\\font\\PartyConfetti.ttf")
        QFontDatabase.addApplicationFont(self.__path + "\\font\\Roboto.ttf")
        QFontDatabase.addApplicationFont(self.__path + "\\font\\OpenSans-Medium.ttf")
        QFontDatabase.addApplicationFont(self.__path + "\\font\\Vazirmatn.ttf")
        # set styles
        header_font: QFont = QFont("ColaKind", 30)
        self.header.setFont(header_font)

        style = "QLabel { font: 18pt Roboto; color: rgb(0, 0, 127); }"
        self.text_0.setStyleSheet(style)
        
        style = "QLabel { font: 28pt \"Party Confetti\"; color: rgb(0, 0, 127); }"
        self.text_p.setStyleSheet(style)
        self.text_sc.setStyleSheet(style)
        self.text_sr.setStyleSheet(style)

        style = "QPushButton { border-radius: 15px; background-color: rgb(0, 68, 255); \
                 color: rgb(255, 255, 127); font: 22pt \"Party Confetti\" } \
                 QPushButton:pressed { background-color: rgb(0, 132, 255); border: 3px solid #55aaff }"
        self.confrim_btn.setStyleSheet(style)
        self.clear_btn.setStyleSheet(style)
        
        style = "QPushButton { border-radius: 15px; background-color: rgb(0, 68, 255); \
                color: rgb(255, 255, 127); font: 22pt \"Party Confetti\"; \
                width: 208px; height: 56px; } \
                QPushButton:pressed { background-color: rgb(0, 132, 255); border: 3px solid #55aaff }"
        self.port_btn.setStyleSheet(style)
        self.secret_btn.setStyleSheet(style)
        self.server_btn.setStyleSheet(style)


app = QApplication(sys.argv)

win = MainWindow()
win.show()

sys.exit(app.exec_())
