
from PyQt5.QtWidgets import QApplication
from time import sleep
from random import choice, shuffle 

app = QApplication([])
#створюємо вікно

from main_window import *
from menu_window import *

class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1       
    def got_wrong(self):
        self.count_ask += 1


q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
questions = [q1, q2, q3, q4]

def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_Question.setText(cur_q.question)
    lb_Correct.setText(cur_q.answer)
    shuffle(radio_buttons)

    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)

new_question()

def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_Correct.text():
                cur_q.got_right()
                lb_Result.setText('Вірно!')
                answer.setChecked(False)
                break
    else:                
        lb_Result.setText('Не вірно!')
        cur_q.got_wrong()

    RadioGroup.setExclusive(True)

def switch_screen():
    if btn_OK.text() == 'Відповісти':
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Наступне питання')
    else:
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_OK.setText('Відповісти')
        RadioGroup.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroup.setExclusive(True)

btn_OK.clicked.connect(switch_screen)

def rest():
    win_card.hide()
    n = sp_rest.value()*60
    sleep(n)
    win_card.show()

btn_Sleep.clicked.connect(rest)

def menu_generation():
    if cur_q.count_ask == 0:
        c = 0
    else:
        c = (cur_q.count_right/cur_q.count_ask)*100

    text = f'разів відповіли: {cur_q.count_ask}\n' \
        f'Вірних відповідей: {cur_q.count_right}\n' \
        f'Успішність: {c}%' \

    lb_statistic.setText(text)
    menu_win.show()
    win_card.hide()

btn_Menu.clicked.connect(menu_generation)

def back_menu():
    menu_win.hide()
    win_card.show()

btn_back.clicked.connect(back_menu)

def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()

btn_clear.clicked.connect(clear)

def add_questions():
    new_q = Questions(le_question.text(), le_right_ans.text(),
        le_wrong_ans1, le_wrong_ans2, le_wrong_ans3             )
    quwstions.append(new_q)
    clear()

btn_add_question.clicked.connect(add_questions)

win_card.show()
app.exed_()