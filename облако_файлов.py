from tkinter import *
from tkinter import ttk, filedialog as fd, messagebox as mb
import requests
import pyperclip
import json
import os


def show_history():
    if not os.path.exists(history_file):
        mb.showinfo('История', 'История загрузок пуста')
        return
    history_window = Toplevel(root)
    history_window.title('История загрузок')
    files_listbox = Listbox(history_window, width=50, height=20)
    files_listbox.grid(row=0, column=0, padx=(10, 0), pady=10)
    links_listbox = Listbox(history_window, width=50, height=20)
    links_listbox.grid(row=0, column=1, padx=(0, 10), pady=10)
    with open(history_file, 'r') as f:
        history = json.load(f)
        for item in history:
            files_listbox.insert(END, item['file_path'])
            links_listbox.insert(END, item['download_link'])


def save_history(file_path, download_link):
    history = []
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history = json.load(f)
    history.append({'file_path': os.path.basename(file_path),
                    'download_link': download_link})
    with open(history_file, 'w') as f:
        json.dump(history, f, indent=4)


def upload():
    try:
        filepath = fd.askopenfilename()
        if filepath:
            with open(filepath, 'rb') as f:
                files = {'file': f}
                response = requests.post('https://store1.gofile.io/uploadFile',
                                         files=files)
                response.raise_for_status()
                if response.status_code == 200:
                    data = response.json()
                    download_link = data['data']['downloadPage']
                    entry.insert(0, download_link)
                    pyperclip.copy(download_link)
                    save_history(filepath, download_link)
                    mb.showinfo('Ссылка скопирована',
                                f'Ссылка {download_link} в буфере обмена')
                else:
                    raise ValueError('Не удалось получить ссылку для скачивания')
    except ValueError as err:
        mb.showerror('Ошибка', f'Произошла ошибка {err}')
    except Exception as err:
        mb.showerror('Ошибка', f'Произошла ошибка {err}')


history_file = 'upload_history.json'
root = Tk()
root.title('Облачное хранилище файлов')
root.geometry('400x120')

upload_button = ttk.Button(text='загрузить файл', command=upload)
upload_button.pack()
entry = ttk.Entry(width=40)
entry.pack(pady=5)
history_btn = ttk.Button(root, text='Показать историю', command=show_history)
history_btn.pack()
root.mainloop()
