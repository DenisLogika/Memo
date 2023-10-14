''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)

window = QWidget()

# віджети, які треба буде розмістити:
# кнопка повернення в основне вікно 
btn_menu = QPushButton("Меню з відповідями")
# кнопка прибирає вікно і повертає його після закінчення таймера
btn_sleep = QPushButton("Відпочити")
# введення кількості хвилин
box_time = QSpinBox()
box_time.setValue(30)
lb_time = QLabel('століття')
# кнопка відповіді "Ок" / "Наступний"
btn_ok = QPushButton('Ну все, давай вже відповідь')
# текст питання
lb_question = QLabel('Soo...')
# Опиши групу перемикачів
radio_group_box = QGroupBox('Варіанти відповідей для A0')
radio_group = QButtonGroup()

rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('You are good')
rbtn_3 = QRadioButton('Jamal')
rbtn_4 = QRadioButton('Ярик')

radio_group.addButton(rbtn_1)
radio_group.addButton(rbtn_2)
radio_group.addButton(rbtn_3)
radio_group.addButton(rbtn_4)
# Опиши панень з результатами
answer_group_box = QGroupBox('Результат теста')
lb_result = QLabel('') # Правильно / неправильно
lb_correct = QLabel('') # Правильна відповідь
# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card
layout_h1 = QHBoxLayout()
layout_h2 = QHBoxLayout()
layout_h3 = QHBoxLayout()
layout_v1 = QVBoxLayout()
layout_v2 = QVBoxLayout()
layout_h4 = QHBoxLayout()

layout_h1.addWidget(btn_menu)
layout_h1.addStretch(1)
layout_h1.addWidget(btn_sleep)
layout_h1.addWidget(box_time)
layout_h1.addWidget(lb_time)

layout_h2.addWidget(lb_question)

layout_v1.addWidget(rbtn_1)
layout_v1.addWidget(rbtn_2)
layout_v2.addWidget(rbtn_3)
layout_v2.addWidget(rbtn_4)
layout_h3.addLayout(layout_v1)
layout_h3.addLayout(layout_v2)

layout_h4.addWidget(btn_ok)

line = QVBoxLayout()
line.addLayout(layout_h1, stretch=1)
line.addLayout(layout_h2, stretch=2)
line.addLayout(layout_h3, stretch=8)
line.addStretch(1)
line.addLayout(layout_h4)
line.addStretch(1)
line.addSpacing(5)

window.setLayout(line)
window.resize(550, 450)