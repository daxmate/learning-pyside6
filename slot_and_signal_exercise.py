from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QProgressBar,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtCore import (
    Signal,
    Slot,
    QObject,
    QThread,
)
import sys
import time
import random


class Worker(QObject):
    progress_updated = Signal(int, int)  # ID, 百分比
    task_completed = Signal(int, str)  # ID, 完成信息
    error_occurred = Signal(int, str)  # ID, 错误信息

    def __init__(self, worker_id):
        super().__init__()
        self.worker_id = worker_id
        self._is_running = True

    def do_work(self):
        try:
            for i in range(1, 101):
                if not self._is_running:
                    self.task_completed.emit(self.worker_id, "Canceled")
                    return

                time.sleep(0.05 * random.random())  # 模拟工作

                # 模拟随机出错
                if random.random() < 0.01:  # 1%的出错率
                    raise ValueError(f'Random error in worker {self.worker_id}')

                # 更新进度
                self.progress_updated.emit(self.worker_id, i)

            # 任务完成
            self.task_completed.emit(f'Worker {self.worker_id} completed')


        except Exception as e:
            self.error_occurred.emit(self.worker_id, str(e))


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # widgets
        self.start_btn = None
        self.cancel_btn = None
        self.log_area = None
        self.status_bar = None
        self.task_layout = None
        self.log = None

        self.threads = []
        self.workers = []

        self.init_ui()

        self.task_count = 5

    def init_ui(self):
        """"初始化界面"""

        # 设置尺寸与位置
        self.resize(800, 600)
        center = self.screen().availableGeometry().center()
        self.geometry().moveCenter(center)

        # 主布局
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 控制按钮区
        control_layout = QHBoxLayout()
        if self.start_btn is None:
            self.start_btn = QPushButton("开始任务")
            control_layout.addWidget(self.start_btn)

            self.start_btn.clicked.connect(self.start_tasks)

        if self.cancel_btn is None:
            self.cancel_btn = QPushButton("取消任务")
            control_layout.addWidget(self.cancel_btn)
        layout.addLayout(control_layout)

        # 总进度区
        total_progress_layout = QHBoxLayout()
        total_progress_label = QLabel("总进度：")
        total_progress_bar = QProgressBar()
        total_progress_bar.setRange(0, 100)
        total_progress_layout.addWidget(total_progress_label)
        total_progress_layout.addWidget(total_progress_bar)
        layout.addLayout(total_progress_layout)

        # 任务进度条区
        if self.task_layout is None:
            self.task_layout = QVBoxLayout()
        layout.addLayout(self.task_layout)

        # 日志区
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        layout.addWidget(self.log_area)

        # 状态栏区
        self.status_bar = QLabel()
        layout.addWidget(self.status_bar)

    def start_tasks(self):
        for i in range(0, self.task_count):
            worker = Worker(i)
            thread = QThread()

            worker.moveToThread(thread)

            # 创建进度条
            progress_bar_layout = QHBoxLayout()
            progress = QProgressBar()
            progress.setRange(0, 100)
            progress_label = QLabel(f'Worker {i+1}')
            progress.setValue(0)

            progress_bar_layout.addWidget(progress_label)
            progress_bar_layout.addWidget(progress)
            self.task_layout.addLayout(progress_bar_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
