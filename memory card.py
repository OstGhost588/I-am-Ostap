import random

from PyQt5.QtWidgets import *

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
answers = [ans1, ans2, ans3, ans4]
random.shuffle(answers)
vidpovistu_btn = QPushButton("Відповісти")
main_lain = QVBoxLayout()
h1 = QHBoxLayout()
h1.addWidget(menu_btn)
h1.addStretch(1)
main_lain.addLayout(h1)
main_lain.addWidget(queston_lbl)

group_line = QVBoxLayout()
group_line.addWidget(answers[0])
group_line.addWidget(answers[1])
group_line.addWidget(answers[2])
group_line.addWidget(answers[3])

group.setLayout(group_line)
main_lain.addWidget(group)
main_lain.addWidget(vidpovistu_btn)

window.setLayout(main_lain)
window.show()
app.exec()
