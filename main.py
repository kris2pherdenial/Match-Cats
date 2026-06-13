import tkinter as tk
from game import start
from util import resource_path

window = tk.Tk()
window.geometry("500x550")
window.title("Match Cats")

# Menu Screen
menu_frame = tk.Frame(window)
menu_frame.pack(fill="both", expand=True) 

def start_game():
    menu_frame.pack_forget() 
    start(window, menu_frame)


bg = tk.PhotoImage(file=resource_path("assets/background.png"))
background = tk.Label(menu_frame, image=bg)
background.place(x=0,y=0,relwidth=1,relheight=1)
background.lower()

menu = tk.Label(
    background, 
    text="Match Cats",
    font=("Roboto", 24),
    fg="Black",
)
menu.pack(pady=50)

play = tk.Button(background, text="Play", command=start_game)
play.pack(pady=40)

exit_btn = tk.Button(background, text="Exit Game", command=window.quit)
exit_btn.pack()

window.mainloop()