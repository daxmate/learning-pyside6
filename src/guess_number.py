from dax import DWidget

from forms.guess_number import Ui_guess
from random import randrange


class GuessNumber(DWidget, Ui_guess):
    def __init__(self, mainwindow=None):
        super().__init__(mainwindow)
        self.setFixedSize(615, 410)
        self.setupUi(self)
        self.target = None
        self.restart()
        self.confirm_btn.clicked.connect(self.confirm)
        self.restart_btn.clicked.connect(self.restart)
        self.delete_btn.clicked.connect(self.delete)
        for num in range(10):
            button = eval(f'self.num{num}_btn')
            button.clicked.connect(lambda checked, n=num: self.num_input(n))

    def delete(self):
        text = self.guess_le.text()
        if text:
            self.guess_le.setText(text[:-1])

    def confirm(self):
        guess = int(self.guess_le.text())
        if guess == self.target:
            self.result_label.setText("你猜对了")
        elif guess > self.target:
            self.result_label.setText("大")
        else:
            self.result_label.setText("小")

    def restart(self):
        self.result_label.setText("开始吧")
        self.target = randrange(1, 101)
        self.guess_le.setText(str(50))

    def num_input(self, num):
        text = self.guess_le.text() + str(num)
        self.guess_le.setText(text)
