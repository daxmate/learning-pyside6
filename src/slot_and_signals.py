import sys
import random
import time
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QProgressBar, QLabel, QTextEdit, QHBoxLayout
)
from PySide6.QtCore import (
    QThread, Signal, Slot, QObject, Qt, QTimer
)


class Worker(QObject):
    """
    工作线程的任务类，执行实际工作并通过信号与主线程通信
    """
    # 定义信号
    progress_updated = Signal(int, int)  # 线程ID, 进度百分比
    task_completed = Signal(int, str)    # 线程ID, 结果
    error_occurred = Signal(int, str)    # 线程ID, 错误信息

    def __init__(self, worker_id):
        super().__init__()
        self.worker_id = worker_id
        self._is_running = True

    def do_work(self):
        """模拟长时间任务"""
        try:
            for i in range(1, 101):
                if not self._is_running:
                    self.task_completed.emit(self.worker_id, "Canceled")
                    return

                # 模拟工作
                time.sleep(0.05 * random.random())

                # 随机模拟错误
                if random.random() < 0.01:  # 1%概率出错
                    raise ValueError(f"Random error in worker {self.worker_id}")

                # 更新进度
                self.progress_updated.emit(self.worker_id, i)

            # 任务完成
            result = f"Result from worker {self.worker_id}"
            self.task_completed.emit(self.worker_id, result)

        except Exception as e:
            self.error_occurred.emit(self.worker_id, str(e))

    def cancel(self):
        """取消任务"""
        self._is_running = False


class MainWindow(QMainWindow):
    """
    主窗口，管理多个工作线程并显示进度
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("复杂信号与槽示例 - 多线程任务监控")
        self.setGeometry(100, 100, 600, 400)

        # 工作线程和worker列表
        self.threads = []
        self.workers = []
        self.completed_count = 0

        # UI初始化
        self.init_ui()

        # 状态跟踪
        self.task_count = 5  # 5个工作线程
        self.running_tasks = 0

    def init_ui(self):
        """初始化用户界面"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # 控制按钮区域
        control_layout = QHBoxLayout()
        self.start_btn = QPushButton("开始任务")
        self.start_btn.clicked.connect(self.start_tasks)
        self.cancel_btn = QPushButton("取消所有任务")
        self.cancel_btn.clicked.connect(self.cancel_all_tasks)
        self.cancel_btn.setEnabled(False)
        control_layout.addWidget(self.start_btn)
        control_layout.addWidget(self.cancel_btn)
        layout.addLayout(control_layout)

        # 总进度条
        self.total_progress = QProgressBar()
        self.total_progress.setRange(0, 100)
        layout.addWidget(QLabel("总进度:"))
        layout.addWidget(self.total_progress)

        # 单个任务进度区域
        self.task_progress_layout = QVBoxLayout()
        layout.addLayout(self.task_progress_layout)

        # 日志区域
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        layout.addWidget(QLabel("日志:"))
        layout.addWidget(self.log_area)

        # 状态标签
        self.status_label = QLabel("准备就绪")
        layout.addWidget(self.status_label)

    def start_tasks(self):
        """启动多个工作线程"""
        self.log("开始执行任务...")
        self.start_btn.setEnabled(False)
        self.cancel_btn.setEnabled(True)
        self.completed_count = 0
        self.running_tasks = self.task_count

        # 清除旧的进度条
        for i in reversed(range(self.task_progress_layout.count())):
            self.task_progress_layout.itemAt(i).widget().setParent(None)

        # 创建新的进度条
        self.progress_bars = []
        for i in range(self.task_count):
            label = QLabel(f"任务 {i+1}:")
            progress = QProgressBar()
            progress.setRange(0, 100)

            self.task_progress_layout.addWidget(label)
            self.task_progress_layout.addWidget(progress)
            self.progress_bars.append(progress)

        # 重置总进度
        self.total_progress.setValue(0)

        # 创建并启动工作线程
        for i in range(self.task_count):
            self.create_worker_thread(i)

    def create_worker_thread(self, worker_id):
        """创建并启动一个工作线程"""
        # 创建线程和worker
        thread = QThread()
        worker = Worker(worker_id + 1)  # ID从1开始

        # 将worker移动到线程
        worker.moveToThread(thread)

        # 连接信号与槽
        worker.progress_updated.connect(self.update_task_progress)
        worker.task_completed.connect(self.task_finished)
        worker.error_occurred.connect(self.task_error)

        # 线程开始时执行工作
        thread.started.connect(worker.do_work)

        # 线程结束时自动删除
        thread.finished.connect(thread.deleteLater)

        # 存储引用
        self.threads.append(thread)
        self.workers.append(worker)

        # 启动线程
        thread.start()

    @Slot(int, int)
    def update_task_progress(self, worker_id, progress):
        """更新单个任务的进度"""
        # 更新对应的进度条
        self.progress_bars[worker_id - 1].setValue(progress)

        # 计算并更新总进度
        total = sum(bar.value() for bar in self.progress_bars)
        avg_progress = total // len(self.progress_bars)
        self.total_progress.setValue(avg_progress)

        self.status_label.setText(f"运行中... 平均进度: {avg_progress}%")

    @Slot(int, str)
    def task_finished(self, worker_id, result):
        """任务完成处理"""
        self.log(f"任务 {worker_id} 完成: {result}")
        self.completed_count += 1
        self.check_all_tasks_completed()

    @Slot(int, str)
    def task_error(self, worker_id, error_msg):
        """任务出错处理"""
        self.log(f"任务 {worker_id} 出错: {error_msg}", is_error=True)
        self.completed_count += 1
        self.check_all_tasks_completed()

    def check_all_tasks_completed(self):
        """检查是否所有任务都已完成"""
        if self.completed_count >= self.task_count:
            self.log("所有任务已完成!")
            self.cleanup_threads()
            self.start_btn.setEnabled(True)
            self.cancel_btn.setEnabled(False)
            self.status_label.setText("所有任务已完成")

    def cancel_all_tasks(self):
        """取消所有任务"""
        self.log("正在取消所有任务...")
        for worker in self.workers:
            worker.cancel()

        QTimer.singleShot(1000, self.force_cleanup)

    def force_cleanup(self):
        """强制清理线程"""
        self.log("强制终止所有线程")
        for thread in self.threads:
            if thread.isRunning():
                thread.quit()
                thread.wait()

        self.cleanup_threads()
        self.start_btn.setEnabled(True)
        self.cancel_btn.setEnabled(False)
        self.status_label.setText("任务已取消")

    def cleanup_threads(self):
        """清理线程资源"""
        for thread in self.threads:
            if thread.isRunning():
                thread.quit()
                thread.wait()

        self.threads.clear()
        self.workers.clear()

    def log(self, message, is_error=False):
        """记录日志"""
        timestamp = time.strftime("%H:%M:%S")
        if is_error:
            self.log_area.append(f'<font color="red">[{timestamp}] {message}</font>')
        else:
            self.log_area.append(f"[{timestamp}] {message}")

    def closeEvent(self, event):
        """窗口关闭时确保所有线程停止"""
        if any(thread.isRunning() for thread in self.threads):
            self.cancel_all_tasks()
            event.ignore()
        else:
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())