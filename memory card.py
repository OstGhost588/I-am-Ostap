import random

from PyQt5.QtWidgets import *

import databaze
app = QApplication([])

window = QWidget()
window.resize(700, 500)
menu_btn = QPushButton("Меню")
group = QGroupBox("Варіанти Відповідей")
queston_lbl = QLabel("Яблуко")
ans1 = QRadioButton("Bulding")
ans2 = QRadioButton("home")
ans3 = QRadioButton("apllication")
ans4 = QRadioButton("apple")
result_lbl = QLabel("Результат")
result_lbl.hide()
answers = [ans1, ans2, ans3, ans4]
random.shuffle(answers)
vidpovistu_btn = QPushButton("Відповісти")
main_lain = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
h1.addWidget(menu_btn)
h1.addStretch(1)
main_lain.addLayout(h1)
main_lain.addLayout(h2)
main_lain.addLayout(h3)
main_lain.addWidget(queston_lbl)

group_line = QVBoxLayout()
group_line.addWidget(answers[0])
group_line.addWidget(answers[1])
group_line.addWidget(answers[2])
group_line.addWidget(answers[3])
group_line.addWidget(result_lbl)
group.setLayout(group_line)
main_lain.addWidget(group)
main_lain.addWidget(vidpovistu_btn)

window.setLayout(main_lain)
def set_question():
    num = databaze.question_number
    queston_lbl.setText(databaze.questions[num]["Запитання"])
    answers[0].setText(databaze.questions[num]["Правильна відповідь"])
    answers[1].setText(databaze.questions[num]["Неправильна відповідь1"])
    answers[2].setText(databaze.questions[num]["Неправильна відповідь2"])
    answers[3].setText(databaze.questions[num]["Неправильна відповідь3"])

set_question()
def answer_click():
    if answers[0].isChecked():
        result_lbl.setText("Правильно!")
    else:
        result_lbl.setText("Неправильно")
    result_lbl.show()
    answers[0].hide()
    answers[1].hide()
    answers[2].hide()
    answers[3].hide()
vidpovistu_btn.clicked.connect(answer_click)
window.show()
app.exec()
