from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit
)
from qtwindow import CalculatorApp
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorApp()
    sys.exit(app.exec())
