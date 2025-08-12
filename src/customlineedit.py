from PySide6.QtCore import Qt, QEvent, QObject
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from pprint import pprint

from PySide6.scripts.qtpy2cpp_lib import qt


class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._event_filter_object = _LineEditEventFilter(self)
        self.installEventFilter(self._event_filter_object)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        # 定义配对符号映射（左边符号: 右边符号）
        pairs: dict[str, str] = {
            '"': '"',
            "'": "'",
            '(': ')',
            '[': ']',
            '{': '}',
            '<': '>'
        }

        # 获取当前光标位置
        pos = self.cursorPosition()
        text = self.text()
        if event.key() in (Qt.Key.Key_QuoteDbl, Qt.Key.Key_Apostrophe,
                           Qt.Key.Key_ParenLeft, Qt.Key.Key_BracketLeft,
                           Qt.Key.Key_BraceLeft, Qt.Key.Key_Less):

            # 获取按下的字符
            char = event.text()

            # 检查是否有选中文本
            selected_text = self.selectedText()

            if selected_text:
                # 如果有选中文本，则在选中文本两侧添加配对符号
                new_text = (text[:self.selectionStart()] +
                            char + selected_text + pairs[char] +
                            text[self.selectionEnd():])
                self.setText(new_text)
                # 将光标放在选中文本末尾的配对符号前
                self.setCursorPosition(self.selectionStart() + len(selected_text) + 1)
            else:
                # 没有选中文本时，直接插入配对符号
                new_text = text[:pos] + char + pairs[char] + text[pos:]
                self.setText(new_text)
                # 将光标移动到两个符号中间
                self.setCursorPosition(pos + 1)

                return  # 阻止默认输入行为
        if event.key() in (Qt.Key.Key_QuoteDbl, Qt.Key.Key_Apostrophe, Qt.Key.Key_ParenRight, Qt.Key.Key_BracketRight,
                           Qt.Key.Key_BraceRight, Qt.Key.Key_Greater):
            pos = self.cursorPosition()
            if pos < len(text) and event.text() == text[pos]:
                self.setText(text)
                self.setCursorPosition(pos + 1)
                return

        super().keyPressEvent(event)  # 其他按键正常处理


class _LineEditEventFilter(QObject):
    def __init__(self, line_edit):
        super().__init__()
        self._line_edit = line_edit
        self.history = []
        self.current_index = -1
        self._line_edit.setPlaceholderText("请输入命令")

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if (event.type() == QEvent.Type.KeyPress and
                isinstance(event, QKeyEvent)):

            if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
                # 安全示例 - 仅打印不执行
                text = self._line_edit.text()
                self.history.append(text)
                # 只保留10条记录
                if len(self.history) > 10:
                    self.history = self.history[-10:]
                self.current_index = -1
                try:
                    eval(text)
                except Exception as e:
                    print(e)
                self._line_edit.clear()
                # pprint(f'Enter pressed with text: {text}')
                # 如果需要处理回车，建议发出信号而不是直接执行代码
                return True  # 表示已处理该事件
            if event.key() == Qt.Key.Key_Up:
                self.current_index -= 1
                if self.current_index < 0:
                    self.current_index = 0
                current_text = self.history[self.current_index]
                self._line_edit.setText(current_text)
            elif event.key() == Qt.Key.Key_Down:
                self.current_index += 1
                if self.current_index >= len(self.history):
                    self.current_index = -1
                current_text = self.history[self.current_index]
                self._line_edit.setText(current_text)

        return super().eventFilter(watched, event)
