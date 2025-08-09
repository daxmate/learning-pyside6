from dax import DWidget

from forms.guess_number import Ui_guess
from random import randrange


class GuessNumber(DWidget, Ui_guess):
    def __init__(self, mainwindow=None):
        super().__init__(mainwindow)
        self.setupUi(self)
        self.target = None
        self.restart()
        self.confirm_btn.clicked.connect(self.confirm)
        self.restart_btn.clicked.connect(self.restart)

    def confirm(self):
        guess = self.input_sb.value()
        if guess == self.target:
            self.result_label.setText("你猜对了")
        elif guess > self.target:
            self.result_label.setText("大")
        else:
            self.result_label.setText("小")

    def restart(self):
        self.result_label.setText("开始吧")
        self.target = randrange(1, 101)
        self.input_sb.setValue(50)
