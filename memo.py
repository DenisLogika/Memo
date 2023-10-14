from PyQt5.QtWidgets import QApplication
from random import choice, shuffle

app = QApplication([])

from main_window import *
from menu_window import *

class Question():
    def __inif__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0    # Кількість відповідей
        self.count_right = 0  # Кількість правильних відповідей
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_ask += 1

q1 = Question('Яблуко', 'apple', 'appleid', 'apply', 'apole')
q2 = Question('Дім', 'house', 'houses', 'hause', 'home')
q3 = Question('Миша', 'mouse', 'mause', 'mousa', 'mouse.')
q4 = Question('Число', 'number', 'namber', 'numbur', 'apole')

radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] #Список радіо кнопок
questions = [q1, q2, q3, q4] #Список

def ne_question():
    global curent_question
    curent_question = choice(Question)

    lb_quesion.setText(curent_question.question)

    shuffle(radio_buttons)
    radio_buttons[0].setText(curent_question.answer)
    radio_buttons[1].setText(curent_question.wrong_asnwer1)
    radio_buttons[2].setText(curent_question.wrong_asnwer2)
    radio_buttons[3].setText(curent_question.wrong_asnwer3)

ne_question()

def check():
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_correct.text():
                curent_question.got_right()
                lb_result.setText('Вірно!')
                break
    else:
        lb_result.setText('Не вірно!')
        curent_question.got_wrong()

def click_ok():
    if btn_ok.text() == 'Відповісти':
        check()
        rbtn_1.hide()
        rbtn_2.hide()
        rbtn_3.hide()
        rbtn_4.hide()

        btn_ok.setText('Наступне запитання')
    else:
        rbtn_1.show()
        rbtn_2.show()
        rbtn_3.show()
        rbtn_4.show()

        btn_ok.setText('Відповісти')

btn_ok.clicked.connect(click_ok)

def clear():
    le_quesion.clear()
    le_right_ans.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()

btn_clear.clicked.connect(clear)

def menu_generation():
    menu.show()
    window.hide()

def back_menu():
    menu.hide()
    window.show()

btn_menu.clicked.connect(menu_generation)
btn_back.clicked.connect(menu_generation)

window.show()
app.exec_()