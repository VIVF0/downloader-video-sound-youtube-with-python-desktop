import tkinter as tk
from tkinter import filedialog, ttk
from src import Audio, Video
import threading
import pathlib
from PIL import Image, ImageTk 

directory = pathlib.Path('img')

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Downloader Youtube")
        self.geometry("300x250")

        self.path = None

        self.input = tk.Entry(self, width=30)
        self.input.pack(pady=10, padx=10)

        select_folder_button = tk.Button(self, text="Selecionar pasta", command=self.select_directory)
        select_folder_button.pack(pady=5)

        audio_button = tk.Button(self, text="Download Audio", command=self.download_audio)
        audio_button.pack(pady=5)

        video_button = tk.Button(self, text="Download Video", command=self.download_video)
        video_button.pack(pady=5)

        self.label = tk.Label(self, text=f'Path: {self.path}')
        self.label.pack(pady=10)

        self.progress_bar = None 

    def select_directory(self):
        folder_path = filedialog.askdirectory(title="Selecione uma pasta")

        if folder_path:
            self.path = folder_path
            self.label.config(text=f'Path: {self.path}')

    def download_audio(self):
        if self.path is not None:
            self.show_progress_bar()
            thread = threading.Thread(target=self._download_audio)
            thread.start()

    def _download_audio(self):
        audio = Audio(url=self.input.get(), path=self.path)
        success, text = audio.download_audio()
        self.hide_progress_bar()
        if success:
            print(text)
            success_page = SuccessPage(self)
        else:
            print(text)
            faliure_page = FailurePage(self)
        self.withdraw()

    def download_video(self):
        if self.path is not None:
            self.show_progress_bar()
            thread = threading.Thread(target=self._download_video)
            thread.start()

    def _download_video(self):
        video = Video(url=self.input.get(), path=self.path)
        success, text = video.download_video()
        self.hide_progress_bar()
        if success:
            print(text)
            success_page = SuccessPage(self)
        else:
            print(text)
            faliure_page = FailurePage(self)
        self.withdraw()

    def show_progress_bar(self):
        # Cria a barra de progresso se ainda não foi criada
        if not self.progress_bar:
            self.progress_bar = ttk.Progressbar(self, length=200, mode='indeterminate')
            self.progress_bar.pack(pady=5)
            self.progress_bar.start()

    def hide_progress_bar(self):
        # Para e esconde a barra de progresso
        if self.progress_bar:
            self.progress_bar.stop()
            self.progress_bar.destroy()
            self.progress_bar = None

class SuccessPage(tk.Toplevel):
    def __init__(self, window):
        super().__init__(window)
        self.title("Sucesso no Download")
        self.geometry("250x250")
        self.iconbitmap(f'{directory}/youtube-logo.ico')
        
        image = Image.open(f'{directory}/true.png').resize(size=(150, 150))
        photo = ImageTk.PhotoImage(image)

        image_label = tk.Label(self, image=photo)
        image_label.image = photo
        image_label.pack(pady=10)

        button1 = tk.Button(self, text="Novo Download", command=self.show_main_window, fg='green')
        button1.pack(pady=10)

    def show_main_window(self):
        self.destroy()
        self.master.deiconify()  # Exibe a janela principal
        
class FailurePage(tk.Toplevel):
    def __init__(self, window):
        super().__init__(window)
        self.title("Falha no Download")
        self.geometry("250x250")
        self.iconbitmap(f'{directory}/youtube-logo.ico')
        
        image = Image.open(f'{directory}/false.webp').resize(size=(150, 150))
        photo = ImageTk.PhotoImage(image)

        image_label = tk.Label(self, image=photo)
        image_label.image = photo
        image_label.pack(pady=10)

        button1 = tk.Button(self, text="Novo Download", command=self.show_main_window, fg='red')
        button1.pack(pady=10)

    def show_main_window(self):
        self.destroy()
        self.master.deiconify()  # Exibe a janela principal

if __name__ == "__main__":
    app = Window()
    app.iconbitmap(f'{directory}/youtube-logo.ico')
    app.mainloop()