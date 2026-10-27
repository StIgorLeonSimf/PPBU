from tkinter import *
import math
from datetime import datetime


def validator():
    data = entry.get()
    valid_data = ''.join((b for b in data if b in '0123456789'))
    if data != valid_data:
        entry.delete(0, END)
        entry.insert(0, valid_data)


root = Tk()
X = root.winfo_screenwidth()
Y = root.winfo_screenheight()
WIDTH = 600
HEIGHT = 400
root.geometry(f"{WIDTH}x{HEIGHT}+{X // 2 - WIDTH // 2}+"
              f"{Y // 2 - HEIGHT // 2}")

cx, cy, r = 250, 200, 130

canvas = Canvas(root, width=WIDTH - 20, height=HEIGHT - 20, bg="lightgray")
canvas.pack()

# --- Циферблат ---
canvas.create_oval(100, 50, 400, 350, fill="light blue")
canvas.create_text(250, 70, text='12', font=('Arial', 20, 'bold'))

for h in range(1, 12):                       # 1..11, 12 уже нарисована
    angle = math.radians(h * 30 - 90)
    x = cx + r * math.cos(angle)
    y = cy + r * math.sin(angle)
    canvas.create_text(x, y, text=str(h), font=('Arial', 20, 'bold'))

# --- Стрелки: создаём один раз, потом только меняем координаты ---
hour_hand   = canvas.create_line(cx, cy, cx, cy, fill="black", width=6)
minute_hand = canvas.create_line(cx, cy, cx, cy, fill="black", width=3)
second_hand = canvas.create_line(cx, cy, cx, cy, fill="red",   width=2)

# Центральная точка поверх стрелок
canvas.create_oval(cx - 5, cy - 5, cx + 5, cy + 5, fill="black")

# Длины стрелок
R_HOUR = r - 70
R_MIN  = r - 45
R_SEC  = r - 20


def update_clock():
    now = datetime.now()
    h = now.hour % 12
    m = now.minute
    s = now.second

    # Углы: 12 часов -> -90°, дальше по часовой стрелке
    a_h = math.radians(h * 30 + m * 0.5 - 90)
    a_m = math.radians(m * 6 + s * 0.1 - 90)
    a_s = math.radians(s * 6 - 90)

    canvas.coords(hour_hand,
                  cx, cy,
                  cx + R_HOUR * math.cos(a_h),
                  cy + R_HOUR * math.sin(a_h))

    canvas.coords(minute_hand,
                  cx, cy,
                  cx + R_MIN * math.cos(a_m),
                  cy + R_MIN * math.sin(a_m))

    canvas.coords(second_hand,
                  cx, cy,
                  cx + R_SEC * math.cos(a_s),
                  cy + R_SEC * math.sin(a_s))

    # Перерисовываем 5 раз в секунду — секундная двигается плавнее
    root.after(200, update_clock)


update_clock()
root.mainloop()