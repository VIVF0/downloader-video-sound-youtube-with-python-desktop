from PyQt6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QFileDialog
)
from PyQt6.QtCore import Qt, QDir
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
        self.input.setMaximumWidth(300)
        layout.addWidget(self.input, alignment=Qt.AlignmentFlag.AlignCenter)

        button = QPushButton("Selecionar pasta")
        button.clicked.connect(self.select_directory)
        layout.addWidget(button)

        button = QPushButton("Download Audio")
        button.clicked.connect(self.download_audio)
        layout.addWidget(button)

        button = QPushButton("Download Video")
        button.clicked.connect(self.download_video)
        layout.addWidget(button)

        self.path = None

    def select_directory(self):
        folder_path = QFileDialog.getExistingDirectory(
            None, "Selecione uma pasta", "", QFileDialog.Option.ShowDirsOnly
        )

        if folder_path:
            self.path = folder_path

    def download_audio(self):
        if self.path is not None:
            audio = Audio(url=self.input.text(), path=self.path)
            audio.download_audio()

    def download_video(self):
        if self.path is not None:
            video = Video(url=self.input.text(), path=self.path)
            video.download_video()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
