from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from random import shuffle

app = QApplication([])

from layout import *
from data import *
from suffer_from_learning import *

i = 0

winda = QWidget()
menu_wind = QWidget()
learn_wind = QWidget()
winda.resize(500,600)
menu_wind.resize(500,600)
learn_wind.resize(500, 600)
winda.setWindowTitle('Memory Card')
menu_wind.setWindowTitle('Menu MMC')
learn_wind.setWindowTitle('Learn')
winda.setLayout(main_line_quizzi)
menu_wind.setLayout(main_menu)
learn_wind.setLayout(layout_learn)
menu_wind.show()
shuffle(questiones)
questiones[i].show_questione(quest_lb, rbtns)
    

a = 0
def is_clicked():
    global i
    global a
    print(bool(korobka.checkedButton()))
    if vidpovid.text() == 'Відповісти':
        if korobka.checkedButton():
            groupa.hide()
            groupa2.show()
            vidpovid.setText('Наступне питання')
            if rbtns[1].isChecked():
                answer.setText('Correct')
                a += 1
            else:
                answer.setText('Incorrect')
        else:
            rrr = QMessageBox()
            rrr.setText('Unable to continue! Check your answer or restart code!!')
            rrr.exec_()
    else:
        if i < 19 and vidpovid.text():
            korobka.setExclusive(False)
            for b in rbtns:
                b.setChecked(False)
            korobka.setExclusive(True)
            groupa.show()
            groupa2.hide()
            vidpovid.setText('Відповісти')
            i += 1
            shuffle(rbtns)
            questiones[i].show_questione(quest_lb, rbtns)
        else:
            msg = QMessageBox()
            msg.setText(str(a))
            msg.exec_()
            menu_is_clicked()

vidpovid.clicked.connect(is_clicked)

def unable():
    #you can`t continue ;)
    pass

def is_clicked_menu1():
    menu_wind.hide()
    winda.show()

def menu_is_clicked():
    global i
    i = 0
    shuffle(questiones)
    questiones[i].show_questione(quest_lb, rbtns)
    winda.hide()
    menu_wind.show()


def is_clicked_learning():
    menu_wind.hide()
    learn_wind.show()

def learn_click():
    learn_wind.hide()
    menu_wind.show()

def imprinting():
    print(bool())

btn_home.clicked.connect(learn_click)
buh_menu2.clicked.connect(is_clicked_learning)
buh_menu1.clicked.connect(is_clicked_menu1)
menu.clicked.connect(menu_is_clicked)
buh_menu3.clicked.connect(lambda : app.exit())
rest.clicked.connect(lambda: app.exit())

app.exec_()