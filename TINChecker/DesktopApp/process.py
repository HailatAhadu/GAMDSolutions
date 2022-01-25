import tkinter as tk
import xml.etree.ElementTree
import xml.etree.ElementTree as ET
import requests
from tkinter import messagebox
from bs4 import BeautifulSoup


def clickMe():
    tin = name.get()

    if not tin:
        messagebox.showerror("Input Error", "Please input the Tin Number and try again")
    elif not tin.isdigit():
        messagebox.showerror("Input Error", "Please input number not other character")
    else:
        try:
            # request = requests.get(url + tin, timeout=timeout)
            req = requests.get(url + tin).text
            data1 = BeautifulSoup(req, 'lxml')
            body = data1.body.text
            body = body.strip()

            try:
                myroot = ET.fromstring(body)
                mytree = list(myroot)
                z = 0

                for y in mytree:
                    print(y.tag, y.text)
                    label1 = tk.Label(window, text=y.tag, font=("", 14))
                    label2 = tk.Label(window, text=y.text, padx=10)
                    label1.grid(row=2 + z, column=0)
                    label2.grid(row=2 + z, column=1)

                    z = z + 1

            except xml.etree.ElementTree.ParseError as err:
                print(body)
                messagebox.showerror("Input Error", "The TIN Number you input is not find")

        except (requests.ConnectionError, requests.Timeout):
            messagebox.showerror("Input Error", "Please check the Internet Connection")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Think Checker Box")
    window.minsize(600, 400)
    scroll = tk.Scrollbar(window)

    url = "http://www.erca.gov.et:8008/wserca/index.jsf?tin="
    timeout = 5

    label = tk.Label(window, text="Please Enter the TIN Number: ", font=("", 14))
    label.grid(column=0, row=1, )

    name = tk.StringVar()
    nameEntered = tk.Entry(window, width=25, textvariable=name, font=("", 14))
    nameEntered.grid(column=1, row=1)

    button = tk.Button(window, text="Search", command=clickMe)
    button.grid(column=2, row=1, padx=10)

    window.mainloop()
    clickMe()
