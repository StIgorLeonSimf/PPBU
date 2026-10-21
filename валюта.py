from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import json
import pprint

from bottle import response


def update_currency_label(event):
    code = combobox.get()
    name = currencies[code]
    currency_label.config(text=name)

def exchange():
    # code = entry.get().upper().strip()
    code = combobox.get()
    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                currency_name = currencies[code]
                mb.showinfo('Курс обмена',
                            f'Курс к USD: {exchange_rate:.1f} {code} за 1 USD')
            else:
                mb.showerror('Ошибка',
                            f'Валюта не найдена')
        except Exception as er:
            mb.showerror('Ошибка', er)

    else:
        mb.showwarning('Внимание', 'Введите код валюты')


currencies = {
    'EUR': 'Евро',
    'JPY': '',
    'GBP': '',
    'AUD': '',
    'RUB': 'Российский рубль'

}

root = Tk()
root.title('Курс обмена валют USD')
root.geometry('360x180')

Label(root, text='Введите код валюты' ).pack(pady=10, padx=10)
popular_currencies = ['EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF',
                      'CNY', 'RUB', 'KZT', 'UZS']
combobox = ttk.Combobox(root, values=popular_currencies, state='readonly')
combobox.pack(pady=10, padx=10)
combobox.bind('<<ComboboxSelected>>', update_currency_label)

currency_label = ttk.Label()
currency_label.pack()
# entry = Entry(root)
# entry.pack()

Button(text='Получить курс обмена к доллару',
       command=exchange).pack(pady=10, padx=10)


root.mainloop()
# p = pprint.PrettyPrinter(indent=4)
# result = requests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)
# p.pprint(data)