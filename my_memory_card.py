#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QRadioButton,
    QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup, QMessageBox
)
import random
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions = list()
questions.append(Question('Кто немного озабочен обвалом на фондовом рынке?', 'Уильям', 'Томас', 'Генри', 'Майкл'))
questions.append(Question('Как звали гг в уцц?', 'Помни', 'Забудь', 'XDDCC', 'Remember'))
questions.append(Question('Какой сегодня год?', '2024', '1987', '2077', '2007'))
questions.append(Question('Какой пол у Мангл?', 'Да', 'Жен', 'Нет', 'Муж'))
questions.append(Question('У меня кончаются идеи вопросов', 'Правильно', 'Не правильно', 'Не правильно', 'Не правильно'))
questions.append(Question('Кто открыл окно в Европу?', 'Пётр 1', 'Путин', 'Князь Владимир', 'я'))
questions.append(Question('Какой сегодня праздник?', 'никакой', 'восьм марты', 'нова года', 'мой др'))
questions.append(Question('H2O девиз не наш. Наш:', 'C2H5OH', '(Fe(OH))2CO3', 'HClO4', 'C17H21NO4'))
questions.append(Question('Какого цвета был серый конь Александра Македонского?', 'Серый', 'Лавандовый', 'Красный', 'Кактус'))
questions.append(Question('Сумма углов?', '180', '360', '90', '240'))

def next_question():
    if win.q_index == len(questions):
        win.q_index = 0
        show_score()
        win.score = 0

    if win.q_index == 0:
        random.shuffle(questions)

    ask(questions[win.q_index])
    win.q_index += 1

def show_score():
    percent = win.score / win.total * 100
    percent = round(percent, 1)

    text = 'Здарова отец!\n'
    text += 'Вы на ' + str(percent) +' процентов правильны\n'
    text += 'Вы правильно ответили на ' + str(win.score) + ' из ' + str(win.total) + ' вопросиков\n'
    text += 'После закрытия результата - контрольная начнётся заново. Молодец'

    msg_box = QMessageBox()
    msg_box.setWindowTitle('Результат')
    msg_box.setText(text)
    msg_box.exec()
        
def ask(q):
    question_text.setText(q.question)
    random.shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

def check_answer():
    for rbtn in answers:
        if rbtn.isChecked():
            if rbtn.text() == answers[0].text():
                right_text.setText('Правильно')
                right_answer.setText('Поздравляем!')
                win.score += 1
            else:
                right_text.setText('Неправильно')
                right_answer.setText('Не поздравляем! Правильный ответ:' + answers[0].text())

#никто не увидит этот текст хахахахахззпзахпзхазпзхпзахпзхапз ёмаё(

def show_result():
    grp_box.hide()
    grp_box_result.show()
    btn.setText('Следующий вопрос')
    check_answer()

def show_question():
    next_question()
    grp_box.show()
    grp_box_result.hide()
    btn.setText('ответить')
    radio_group.setExclusive(False)
    radio1.setChecked(False)
    radio2.setChecked(False)
    radio3.setChecked(False)
    radio4.setChecked(False)
    radio_group.setExclusive(True)

def start_test():
    if btn.text() == 'ответить':
        show_result()
    else:
        show_question()



app = QApplication([])
win = QWidget()
win.setWindowTitle('MemoryCard')
win.resize(400, 300)
win.q_index = 0
win.score = 0
win.total = len(questions)

question_text = QLabel('Вопросик')
grp_box = QGroupBox('Варики ответиков')
radio1=QRadioButton('Варик 1')
radio2=QRadioButton('Варик 2')
radio3=QRadioButton('Варик 3')
radio4=QRadioButton('Варик 4')
btn = QPushButton('Ответить')
grp_box_result = QGroupBox('Результат')
right_text = QLabel('Правильно/Неправильно')
right_answer = QLabel('Правильный ответ')

radio_group = QButtonGroup()
radio_group.addButton(radio1)
radio_group.addButton(radio2)
radio_group.addButton(radio3)
radio_group.addButton(radio4)
answers = [radio1, radio2, radio3, radio4]

main_layout= QVBoxLayout()
h_main1 = QHBoxLayout()
h_main2 = QHBoxLayout()
h_main3 = QHBoxLayout()
grp_box_layout = QHBoxLayout()
grp_box_v1 = QVBoxLayout()
grp_box_v2 = QVBoxLayout()
grp_box_result_layout = QVBoxLayout()

grp_box_result_layout.addWidget(right_text)
grp_box_result_layout.addWidget(right_answer, alignment=Qt.AlignCenter)
grp_box_result.setLayout(grp_box_result_layout)

grp_box_v1.addWidget(radio1)
grp_box_v1.addWidget(radio2)
grp_box_v2.addWidget(radio3)
grp_box_v2.addWidget(radio4)
grp_box_layout.addLayout(grp_box_v1)
grp_box_layout.addLayout(grp_box_v2)
grp_box.setLayout(grp_box_layout)

h_main1.addWidget(question_text, alignment=Qt.AlignCenter)
h_main2.addWidget(grp_box)
h_main2.addWidget(grp_box_result)
h_main3.addStretch()
h_main3.addWidget(btn, stretch=2)
h_main3.addStretch(1)

main_layout.addLayout(h_main1)
main_layout.addLayout(h_main2)
main_layout.addLayout(h_main3)

win.setLayout(main_layout)
btn.clicked.connect(start_test)

next_question()
grp_box_result.hide() 
win.show()
app.exec()