from tkinter import *
import random

attempts = 10

answer = random.randint(1, 99)

def check_answer():
    global attempts
    global text

    attempts -= 1

    guess = int(entry_window.get())

    if answer == guess:
        text.set("Angka yang kamu tebak benar! Selamat!!")
        btn_check.pack_forget()

    elif attempts == 0:
        text.set("Wahh.. kamu sudah menghabiskan kesempatanmu!")
        btn_check.pack_forget()
    elif guess < answer:
        text.set(f"Salah! Kamu mempunyai {str(attempts)} kesempatan lagi - Tebak angkanya lebih tinggi lagi!")
    elif guess > answer:
        text.set(f"Salah! Kamu mempunyai {str(attempts)} kesempatan lagi - Tebak angkanya lebih rendah lagi!")


root = Tk()

root.title("Tebak Angka (GUI)")

root.geometry("500x150")

label = Label(root, text="Tebak angka antara 1-99")
label.pack()

entry_window = Entry(root, width=40, borderwidth=4)
entry_window.pack()

btn_check = Button(root, text="Check", command=check_answer)
btn_check.pack()

btn_quit = Button(root, text="Keluar", command=root.destroy)
btn_quit.pack()

text = StringVar()
text.set("Kamu mempunyai 10 kesempatan untuk menebak angka! Semoga berhasil!")

guess_attempts = Label(root, textvariable=text)
guess_attempts.pack()


root.mainloop()