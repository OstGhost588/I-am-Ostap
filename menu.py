from PyQt5.QtWidgets import *

import databaze


def menu_window():
    window = QDialog()
    quest_lbl = QLabel("Введіь запитання")
    right_ans_lbl = QLabel("Введіть правильну відповідь")
    quest_edit = QLineEdit()
    right_ans_edit = QLineEdit()
    add_question_btn = QPushButton("Додати запитання")

    main_line = QVBoxLayout()
    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_edit)
    h1.addWidget(add_question_btn)
    main_line.addLayout(h1)
    def add_quest_func():
        a = {
            "Запитання": quest_edit.text(),
            "Правильна відповідь": "",
            "Неправильна 1": "",
            "Неправильна 2": "",
            "Неправильна 3": ""
        }
        databaze.questions.append(a)
    window.setLayout(main_line)
    add_question_btn.clicked.connect(add_quest_func)
    window.exec()
