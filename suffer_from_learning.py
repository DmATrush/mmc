from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,
                              QSpinBox, QGroupBox, QHBoxLayout, QRadioButton, QButtonGroup, QMessageBox, QListWidget)
from data import questiones
layout_learn = QVBoxLayout()
btn_home = QPushButton()
btn_home.setText('Додому')
btn_showanswer = QPushButton('Show Answer')
answers = QListWidget()
layout_learn.addWidget(btn_home, alignment=Qt.AlignLeft)
layout_learn.addWidget(answers)
layout_learn.addWidget(btn_showanswer)
for question in questiones:
    answers.addItem(question.text)



