from PyQt6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout
)
from PyQt6.QtCore import Qt
import sys

from src import Audio, Video

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 250)
        self.setWindowTitle("Downloader Youtube")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input = QLineEdit()
        self.input.setFixedWidth(150)
        layout.addWidget(self.input, alignment= Qt.AlignmentFlag.AlignCenter)
        
        self.input2 = QLineEdit()
        self.input2.setFixedWidth(150)
        layout.addWidget(self.input2, alignment= Qt.AlignmentFlag.AlignCenter)

        button = QPushButton("Download Audio")
        button.clicked.connect(self.download_audio)
        layout.addWidget(button)
        
        button = QPushButton("Download Video")
        button.clicked.connect(self.download_video)
        layout.addWidget(button)

    def download_audio(self):
        audio=Audio(url=self.input.text(),path=self.input2.text())
        audio.download_audio()
        
    def download_video(self):
        video=Video(url=self.input.text(),path=self.input2.text())
        video.download_video()

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())