
from PyQt5.QtWidgets import *

import databaze


def menu_window():
    window = QDialog()
    quest_lbl = QLabel("Введіь запитання")
    right_ans_lbl = QLabel("Введіть правильну відповідь")
    lie1_ans_lbl = QLabel("Ведіть першу неправильну відповідь")
    lie2_ans_lbl = QLabel("Ведіть другу неправильну відповідь")
    lie3_ans_lbl = QLabel("Ведіть третю неправильну відповідь")
    quest_edit = QLineEdit()
    right_ans_edit = QLineEdit()
    lie1_ans_edit = QLineEdit()
    lie2_ans_edit = QLineEdit()
    lie3_ans_edit = QLineEdit()
    add_question_btn = QPushButton("Додати запитання")

    main_line = QVBoxLayout()
    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_edit)
    h1.addWidget(right_ans_lbl)
    h1.addWidget(right_ans_edit)
    h1.addWidget(lie1_ans_lbl)
    h1.addWidget(lie1_ans_edit)
    h1.addWidget(lie2_ans_lbl)
    h1.addWidget(lie2_ans_edit)
    h1.addWidget(lie3_ans_lbl)
    h1.addWidget(lie3_ans_edit)
    h1.addWidget(add_question_btn)

    main_line.addLayout(h1)
    def add_quest_func():
        a = {
            "Запитання": quest_edit.text(),
            "Правильна відповідь": right_ans_edit.text(),
            "Неправильна 1": lie1_ans_edit.text(),
            "Неправильна 2": lie2_ans_edit.text(),
            "Неправильна 3": lie3_ans_edit.text()
        }
        databaze.questions.append(a)
    window.setLayout(main_line)
    add_question_btn.clicked.connect(add_quest_func)
    window.exec()
