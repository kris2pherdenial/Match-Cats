import tkinter as tk
import random

from util import resource_path

#CONSTANTS
btn_size = 100

def start(window, menu_frame):
    
    game_frame = tk.Frame(window)
    game_frame.pack()

    def reset_game():
        game_frame.destroy()
        start(window,menu_frame)


    win_count = 0

    attempts = 6

    images = {
        1: tk.PhotoImage(file=resource_path("assets/img1.png")),
        2: tk.PhotoImage(file=resource_path("assets/img2.png")),
        3: tk.PhotoImage(file=resource_path("assets/img3.png")),
        4: tk.PhotoImage(file=resource_path("assets/img4.png")),
        5: tk.PhotoImage(file=resource_path("assets/img5.png")),
        6: tk.PhotoImage(file=resource_path("assets/img6.png")),
    } 

    blank = tk.PhotoImage()

    matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    random.shuffle(matches)

    # Frame for buttons
    button_frame = tk.Frame(game_frame)
    button_frame.pack(pady=10)

    # Tracking variables
    ctr = 0
    answer_list = [] # Tracks while tiles were clicked
    answer_dict = {} # Answer key

    label = tk.Label(game_frame, text="", font=("Helvetica", 14))
    label.pack(pady=20)

    attempts_left = tk.Label(game_frame, text=f"Attempts Left: {attempts}", font=("Helvetica", 14))
    attempts_left.pack(pady=10)

    reset_btn = tk.Button(game_frame, text="Reset", font=("Helvetica", 12), command=reset_game)
    reset_btn.pack(pady=10)

    def win_game():
        label.config(text="You win!")

    def lose_game():
        label.config(text="You lose!")

    # Click function
    def click(btn, num):
        nonlocal ctr, answer_list, answer_dict, win_count, attempts

        if btn["image"] == str(blank) and ctr < 2 and attempts > 0:
            btn["image"] = images[matches[num]]
            answer_list.append(num)
            answer_dict[btn] = matches[num]
            ctr += 1

        # Check if correct
        if len(answer_list) == 2:
            if matches[answer_list[0]] == matches[answer_list[1]]:
                label.config(text="Match!")
                for key in answer_dict:
                    key["state"] = "disabled"
                
                # Reset tracking for the next turn
                ctr = 0
                answer_list = []
                answer_dict = {}
                
                # Add win count
                win_count += 1   
                if win_count == 6:
                    win_game()  

            else:
                label.config(text="Wrong!")
                
                attempts -= 1
                attempts_left.config(text=f"Attempts Left: {attempts}")

                def flip_tile():
                    nonlocal ctr, answer_list, answer_dict
                    
                    # Flip the tiles back
                    for b in answer_dict:
                        b["image"] = blank

                    # Reset tracking ONLY after the delay
                    ctr = 0
                    answer_list = []
                    answer_dict = {}
                    
                    label.config(text="") 
                
                    if attempts == 0:
                        lose_game()

                game_frame.after(200, flip_tile)

    # Buttons
    btn1 = tk.Button(button_frame, image=blank, height=btn_size, width=btn_size, command=lambda: click(btn1, 0))
    btn2 = tk.Button(button_frame, image=blank, height=btn_size, width=btn_size, command=lambda: click(btn2, 1))
    btn3 = tk.Button(button_frame, image=blank, height=btn_size, width=btn_size, command=lambda: click(btn3, 2))
    btn4 = tk.Button(button_frame, image=blank, height=btn_size, width=btn_size, command=lambda: click(btn4, 3))
    btn5 = tk.Button(button_frame, image=blank, height=btn_size, width=btn_size, command=lambda: click(btn5, 4))
    btn6 = tk.Button(button_frame, image=blank, height=btn_size, width=btn_size, command=lambda: click(btn6, 5))
    btn7 = tk.Button(button_frame, image=blank, height=btn_size, width=btn_size, command=lambda: click(btn7, 6))
    btn8 = tk.Button(button_frame, image=blank, height=btn_size, width=btn_size, command=lambda: click(btn8, 7))
    btn9 = tk.Button(button_frame, image=blank, height=btn_size, width=btn_size, command=lambda: click(btn9, 8))
    btn10 = tk.Button(button_frame, image=blank, height=btn_size, width=btn_size, command=lambda: click(btn10, 9))
    btn11 = tk.Button(button_frame, image=blank, height=btn_size, width=btn_size, command=lambda: click(btn11, 10))
    btn12 = tk.Button(button_frame, image=blank, height=btn_size, width=btn_size, command=lambda: click(btn12, 11))

    # Button grid
    btn1.grid(row=0, column=0)
    btn2.grid(row=0, column=1)
    btn3.grid(row=0, column=2)
    btn4.grid(row=0, column=3)

    btn5.grid(row=1, column=0)
    btn6.grid(row=1, column=1)
    btn7.grid(row=1, column=2)
    btn8.grid(row=1, column=3)

    btn9.grid(row=2, column=0)
    btn10.grid(row=2, column=1)
    btn11.grid(row=2, column=2)
    btn12.grid(row=2, column=3)

    