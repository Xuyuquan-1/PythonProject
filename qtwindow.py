import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit
)
from PyQt6.QtCore import Qt

# 导入计算模块（示例）
from calculator import calculate


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建主布局
        main_layout = QVBoxLayout()

        # 输入区域
        input_layout = QHBoxLayout()
        self.input_label = QLabel("输入数值:")
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("请输入数字")
        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_field)
        main_layout.addLayout(input_layout)

        # 按钮区域
        button_layout = QHBoxLayout()
        self.calculate_button = QPushButton("计算")
        self.clear_button = QPushButton("清空")
        button_layout.addWidget(self.calculate_button)
        button_layout.addWidget(self.clear_button)
        main_layout.addLayout(button_layout)

        # 结果显示区域
        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setPlaceholderText("计算结果将显示在这里...")
        main_layout.addWidget(self.result_display)

        # 设置布局
        self.setLayout(main_layout)

        # 连接信号和槽
        self.calculate_button.clicked.connect(self.on_calculate)
        self.clear_button.clicked.connect(self.on_clear)

        # 设置窗口属性
        self.setWindowTitle('PyQt6计算器应用')
        self.setGeometry(300, 300, 500, 400)
        self.show()

    def on_calculate(self):
        """处理计算按钮点击事件"""
        input_text = self.input_field.text().strip()

        if not input_text:
            self.result_display.append("错误: 输入不能为空")
            return

        try:
            # 将输入转换为浮点数
            value = float(input_text)

            # 调用计算模块进行计算
            result = calculate(value)

            # 显示计算结果
            self.result_display.append(f"输入值: {value}")
            self.result_display.append(f"计算结果: {result}")
            self.result_display.append("-" * 50)

        except ValueError:
            self.result_display.append("错误: 请输入有效的数字")

    def on_clear(self):
        """处理清空按钮点击事件"""
        self.input_field.clear()
        self.result_display.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorApp()
    sys.exit(app.exec())