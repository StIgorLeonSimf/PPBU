from tkinter import *
from tkinter import ttk
from io import BytesIO


from PIL import Image, ImageTk
import requests


def load_image(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        image_data = BytesIO(resp.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as er:
        print('Ошибка', er)
        return None


def set_image():
    img = load_image(url)
    if img:
        label.configure(image=img)
        label.image = img


def open_new_window():
    # tag = tag_entry.get()
    tag = tag_combobox.get()
    url_with_tag = (f'https://cataas.com/cat/{tag}' if tag
                    else 'https://cataas.com/cat')
    img = load_image(url_with_tag)
    if img:
        new_window = Toplevel(root)
        new_window.title('Картинка с котиком')
        new_window.geometry('620x520')
        label = Label(new_window, image=img)
        label.image = img
        label.pack()


def exit():
    root.destroy()


ALLOWED_TAGS = ['sleep', 'jump', 'smile', 'fight', 'black', 'white',
                'red', 'siamese', 'bengal']


root = Tk()
root.title('Cats')
root.geometry('620x550')
label = Label(root)
label.pack()

menu_bar = Menu(root)
root.config(menu=menu_bar)
file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit)
# tag_entry = Entry(root)
# tag_entry.pack()

tag_label = Label(text='Выбери тег')
tag_label.pack()
tag_combobox = ttk.Combobox(values=ALLOWED_TAGS)
tag_combobox.pack()

load_button = Button(text='Загрузка по тегу', command=open_new_window)
load_button.pack(pady=5)


# update_btn = Button(text=' Следующая ', command=set_image)
# update_btn.pack(pady=5)

url = 'https://cataas.com/cat'


set_image()

root.mainloop()