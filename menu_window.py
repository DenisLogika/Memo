from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout

menu = QWidget()

lb_quesion = QLabel('Введіть запитання на яке неможливо відповісти:')
lb_right_ans = QLabel('Введіть вірну відповідь:')
lb_wrong_ans1 = QLabel('Введіть першу не вірну відповідь:')
lb_wrong_ans2 = QLabel('Введіть другу не вірну відповідь:')
lb_wrong_ans3 = QLabel('Введіть третю не вірну відповідь:')

le_quesion = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

btn_add_quesion = QPushButton('Додати запитання')
btn_clear = QPushButton('Очистити')
btn_back = QPushButton('Назад')

lb_stat = QLabel('Статистика')
lb_stat.setStyleSheet('font-size: 20px; font-weight: bold')

lb_statistic = QLabel('АЛО, АЛО, АЛО, АЛО, АЛО! 10 НА 10 БУДЕ 20')

line_h1 = QHBoxLayout()
line_h2 = QHBoxLayout()
line_h3 = QHBoxLayout()
line_h4 = QHBoxLayout()
line_h5 = QHBoxLayout()
line_h6 = QHBoxLayout()
line_h7 = QHBoxLayout()
line_h8 = QHBoxLayout()
line_h9 = QHBoxLayout()

line_h1.addWidget(lb_quesion)
line_h1.addWidget(le_quesion)

line_h2.addWidget(lb_right_ans)
line_h2.addWidget(le_right_ans)

line_h3.addWidget(lb_wrong_ans1)
line_h3.addWidget(le_wrong_ans1)

line_h4.addWidget(lb_wrong_ans2)
line_h4.addWidget(le_wrong_ans2)

line_h5.addWidget(lb_wrong_ans3)
line_h5.addWidget(le_wrong_ans3)

line_h6.addWidget(btn_add_quesion)
line_h6.addWidget(btn_clear)

line_h7.addWidget(lb_stat)

line_h8.addWidget(lb_statistic)

line_h9.addWidget(btn_back)

line = QVBoxLayout()

line.addLayout(line_h1)
line.addLayout(line_h2)
line.addLayout(line_h3)
line.addLayout(line_h4)
line.addLayout(line_h5)
line.addLayout(line_h6)
line.addLayout(line_h7)
line.addLayout(line_h8)
line.addLayout(line_h9)

menu.setLayout(line)
menu.resize(400, 300)