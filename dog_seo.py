from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO
import requests
import os


def get_dog_image(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()

        return data['message']
    except Exception as err:
        print(f'Ошибка чтения API: {err}')
        return None

def show_image():
    global image_s
    image_url = get_dog_image('https://dog.ceo/api/breeds/image/random')
    try:
        resp = requests.get(image_url)
        resp.raise_for_status()
        image_data = BytesIO(resp.content)
        image_s = Image.open(image_data)
        image = image_s
        image.thumbnail((600, 480))
        image = ImageTk.PhotoImage(image)
        label.config(image=image)
        label.image=image
    except Exception as err:
        print(f'Ошибка загрузки: {err}')
        return None


def save_image():
    global image_s
    if image_s is None:
        messagebox.showinfo('картинка',
                            'Отсутствие загруженного изображения')
        return

    def_name = os.path.basename(name_file)
    fp = filedialog.asksaveasfilename(
        defaultextension='.png',
        filetypes=[('PNG', '*.png'),
                   ('JPEG', '*.jpg'),
                   ('All Files', '*.*')],
        initialfile=def_name
    )

    if fp:
        image_s.save(fp)
        messagebox.showinfo('Save',
                            f'Saved: {fp}')


image_s = ''
name_file = 'image_'
root = Tk()
root.title('Dogs')
root.geometry('620x550')
label = Label(root)
label.pack()

btn = Button(root, text='Загрузить', command=show_image)
btn.pack(pady=5)

save_btn = Button(root, text='Сохранить', command=save_image)
save_btn.pack()


show_image()
root.mainloop()