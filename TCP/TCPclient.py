'''
Name: Ante Lucev
Date: 3-26-2020
Desc: client.py for client/server chat room
'''
import socket
import threading
import pickle
import random
from tkinter import *

master = Tk()
master.minsize(width=500, height=150)
color = random.choice(["firebrick","darksalmon","green","coral","yellowgreen","aquamarine","cyan","lightpink","royalblue"])
master.configure(background=color)
count = 0
limit = 0

def listen_worker(s):
    print("Waiting for message")
    global count, color, limit
    while True:
        rcv = s.recv(1024)
        (name, text) = pickle.loads(rcv)

        def entry_destroy():
            if count != 0:
                label_on.destroy()

        if name == "On are:":
            entry_destroy()
            label = Label(master, text=name, font=('Calibri', 15), background=color)
            label.grid(column=0, row=4)
            label_on = Label(master, text=text, font=('Calibri', 15), background=color)
            label_on.grid(column=1, row=4, columnspan=10, pady=20)
        else:
            label = Label(master, text=name, font=('Calibri', 15), background=color)
            label.grid(column=0, row=5 + count)
            if name == "You":
                limit += 1
                label = Label(master, text=text, font=('Calibri', 15), background=color)
                label.grid(column=1, row=5 + count, columnspan=10, sticky=W)
            else:
                limit = 0
                label = Label(master, text=text, font=('Calibri', 15), background=color)
                label.grid(column=1, row=5 + count, columnspan=10, sticky=E, padx=10)
        count += 1


port = 5556  # Send to port above 1024

host = socket.gethostname()
host = '127.0.0.1'

def clear_widgets():
    list = master.grid_slaves()
    for l in list:
        l.destroy()

def connect():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = ip_box.get()
        s.connect((host, port))
        name = name_box.get()
        s.sendall(name.encode('ascii'))
        thread = threading.Thread(target=listen_worker, args=[s])
        thread.start()

        clear_widgets()
        global limit
        def send():
            if limit < 5:
                message = pickle.dumps((text_box.get()))
                s.sendall(message)

        def send_emoji():
            if limit < 5:
                message = pickle.dumps((emoji.cget('text')))
                s.sendall(message)
        def send_emoji1():
            if limit < 5:
                message = pickle.dumps((emoji1.cget('text')))
                s.sendall(message)
        def send_emoji2():
            if limit < 5:
                message = pickle.dumps((emoji2.cget('text')))
                s.sendall(message)
        def send_emoji3():
            if limit < 5:
                message = pickle.dumps((emoji3.cget('text')))
                s.sendall(message)
        def send_emoji4():
            if limit < 5:
                message = pickle.dumps((emoji4.cget('text')))
                s.sendall(message)
        def send_emoji5():
            if limit < 5:
                message = pickle.dumps((emoji5.cget('text')))
                s.sendall(message)
        def send_emoji6():
            if limit < 5:
                message = pickle.dumps((emoji6.cget('text')))
                s.sendall(message)
        def send_emoji7():
            if limit < 5:
                message = pickle.dumps((emoji7.cget('text')))
                s.sendall(message)
        def send_emoji8():
            if limit < 5:
                message = pickle.dumps((emoji8.cget('text')))
                s.sendall(message)
        def send_emoji9():
            if limit < 5:
                message = pickle.dumps((emoji9.cget('text')))
                s.sendall(message)
        def send_emoji10():
            if limit < 5:
                message = pickle.dumps((emoji10.cget('text')))
                s.sendall(message)
        def send_emoji11():
            if limit < 5:
                message = pickle.dumps((emoji11.cget('text')))
                s.sendall(message)
        def send_emoji12():
            if limit < 5:
                message = pickle.dumps((emoji12.cget('text')))
                s.sendall(message)
        def send_emoji13():
            if limit < 5:
                message = pickle.dumps((emoji13.cget('text')))
                s.sendall(message)
        def send_emoji14():
            if limit < 5:
                message = pickle.dumps((emoji14.cget('text')))
                s.sendall(message)
        def send_emoji15():
            if limit < 5:
                message = pickle.dumps((emoji15.cget('text')))
                s.sendall(message)
        def send_emoji16():
            if limit < 5:
                message = pickle.dumps((emoji16.cget('text')))
                s.sendall(message)
        def send_emoji17():
            if limit < 5:
                message = pickle.dumps((emoji17.cget('text')))
                s.sendall(message)

        while True:
            label = Label(master, text="Your Message:", font=('Calibri', 15), background=color)
            label.grid(column=0, row=0, padx=10, pady=20)
            text_box = Entry(master, font=('Calibri', 15), width=50)
            text_box.grid(column=1, row=0, columnspan=10)
            send_button = Button(master, text="Send", command=send, font=('Courier New', 10), width=12)
            send_button.grid(column=11, row=0, padx=15)

            label = Label(master, text="Send emojis:", font=('Calibri', 15), background=color)
            label.grid(column=0, row=1, padx=10, pady=20)
            emoji = Button(master, text="\ud83d\ude02", command=send_emoji,font=('', 20))
            emoji.grid(column=1, row=1)
            emoji1 = Button(master, text="\ud83d\ude04", command=send_emoji1, font=('', 20))
            emoji1.grid(column=2, row=1)
            emoji2 = Button(master, text="\ud83d\ude09", command=send_emoji2, font=('', 20))
            emoji2.grid(column=3, row=1)
            emoji3 = Button(master, text="\ud83d\ude0a", command=send_emoji3, font=('', 20))
            emoji3.grid(column=4, row=1)
            emoji4 = Button(master, text="\ud83d\ude0d", command=send_emoji4, font=('', 20))
            emoji4.grid(column=5, row=1)
            emoji5 = Button(master, text="\ud83d\ude14", command=send_emoji5, font=('', 20))
            emoji5.grid(column=6, row=1)
            emoji6 = Button(master, text="\ud83d\ude22", command=send_emoji6, font=('', 20))
            emoji6.grid(column=7, row=1)
            emoji7 = Button(master, text="\ud83d\ude31", command=send_emoji7, font=('', 20))
            emoji7.grid(column=8, row=1)
            emoji8 = Button(master, text="\ud83d\ude37", command=send_emoji8, font=('', 20))
            emoji8.grid(column=9, row=1)

            emoji9 = Button(master, text="\ud83d\ude4f", command=send_emoji9,font=('', 20))
            emoji9.grid(column=1, row=2)
            emoji10 = Button(master, text="\ud83c\udfca", command=send_emoji10, font=('', 20))
            emoji10.grid(column=2, row=2)
            emoji11 = Button(master, text="\ud83d\udc4d", command=send_emoji11, font=('', 20))
            emoji11.grid(column=3, row=2)
            emoji12 = Button(master, text="\ud83d\udc4e", command=send_emoji12, font=('', 20))
            emoji12.grid(column=4, row=2)
            emoji13 = Button(master, text="\ud83d\udc93", command=send_emoji13, font=('', 20))
            emoji13.grid(column=5, row=2)
            emoji14 = Button(master, text="\ud83d\udc94", command=send_emoji14, font=('', 20))
            emoji14.grid(column=6, row=2)
            emoji15 = Button(master, text="\ud83d\udca9", command=send_emoji15, font=('', 20))
            emoji15.grid(column=7, row=2)
            emoji16 = Button(master, text="\ud83d\udcaf", command=send_emoji16, font=('', 20))
            emoji16.grid(column=8, row=2)
            emoji17 = Button(master, text="\ud83c\udf0d", command=send_emoji17, font=('', 20))
            emoji17.grid(column=9, row=2)

            mainloop()

        s.close()

label = Label(master, text="IP Address:", font=('Calibri', 15), background=color)
label.grid(column=0, row=0, padx=10, pady=20)
ip_box = Entry(master, font=('Calibri', 15))
ip_box.grid(column=1, row=0, columnspan=10)
label = Label(master, text="Your Name:", font=('Calibri', 15), background=color)
label.grid(column=0, row=1, padx=10, pady=20)
name_box = Entry(master, font=('Calibri', 15))
name_box.grid(column=1, row=1, columnspan=10)
connect_button = Button(master, text="Connect", command=connect, font=('Courier New', 10), width=12)
connect_button.grid(column=11, row=1, padx=30)

mainloop()