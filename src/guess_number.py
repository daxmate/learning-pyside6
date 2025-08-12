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
            self.result_label.setText(f"🎯 完美命中！答案就是 {self.target}")
            self.result_label.setStyleSheet("color: #4CAF50; font-size: 16px;")
            self.confirm_btn.setEnabled(False)  # 猜对后禁用确认按钮
        elif guess > self.target:
            diff = guess - self.target
            if diff > 30:
                msg = "太大了"
            elif diff > 15:
                msg = "还是大了"
            else:
                msg = "接近了，但还大一点点"
            self.result_label.setText(msg)
            self.result_label.setStyleSheet("color: #2196F3;")
        else:
            diff = self.target - guess
            if diff > 30:
                msg = "太小了"
            elif diff > 15:
                msg = "还是小了"
            else:
                msg = "接近了，但还小一点点"
            self.result_label.setText(msg)
            self.result_label.setStyleSheet("color: #F44336;")

        # 清空输入框，准备下一次猜测
        self.guess_le.clear()

    def restart(self):
        self.result_label.setText("开始吧")
        self.target = randrange(1, 101)
        self.guess_le.clear()

    def num_input(self, num):
        text = self.guess_le.text() + str(num)
        self.guess_le.setText(text)
