"""
Tic Tac Toe Game with Tkinter
Features:
- Single player (vs Computer) and Two player modes
- Win/draw detection and score tracking
- Reset board and reset all
- Menu with help and cheat options
"""


import tkinter as tk
from tkinter import simpledialog, messagebox


# ----------------- Main Window -----------------
window = tk.Tk()
window.geometry("800x800+550+40")
window.title("Tic Tac Toe")
window.resizable(height= False, width= False)


# ------------- Global Variables -------------
player1 = ""
player2 = ""

player1_symbol= ""
player2_symbol= ""

score_o = 0
score_x = 0

turn = "X"

row_line = None
column_line = None

game_over = False


# ----------------- Start Frame -----------------
start_frame= tk.Frame(window)
start_frame.pack()


mode_label= tk.Label(start_frame, text="Choose the Mode:", font=22)
mode_label.grid(column=0, row=0, columnspan=2)


mode_var = tk.StringVar(value= "two player")

def update_mode():
    if mode_var.get() == "one player":
        p2_entry.delete(0, tk.END)
        p2_entry.insert(0, "Computer")
        p2_entry.config(state="disabled")
    else:
        p2_entry.config(state="normal")
        p2_entry.delete(0, tk.END)



single_player= tk.Radiobutton(start_frame, text="single Player", variable=mode_var, value="one player", command=update_mode, font=10)
single_player.grid(row=1, column=0, pady=5)

double_player= tk.Radiobutton(start_frame, text="double Player", variable=mode_var, value="two player", command=update_mode, font=10)
double_player.grid(row=1, column=1, pady=5)


p1_label = tk.Label(start_frame, text="Player 1 Name:", font=10)
p1_label.grid(row=2, column=0,pady=5)

p1_entry = tk.Entry(start_frame, width=25, justify="center")
p1_entry.grid(row=2, column=1, pady=5)


p2_label = tk.Label(start_frame, text="Player 2 Name:", font=10)
p2_label.grid(row=3, column=0, pady=5)

p2_entry= tk.Entry(start_frame, width=25, justify="center")
p2_entry.grid(row=3, column=1, pady=5)



choose_label = tk.Label(start_frame, text= "What Player-1 wants to be, Choose X or O :   ", font= 8)
choose_label.grid(row= 8, column=0, columnspan=2, pady= 50)

symbol_var = tk.StringVar(value="X")

choose_X = tk.Radiobutton(start_frame, text= "X     or", variable= symbol_var, value="X", font= 9)
choose_X.grid(row= 8, column=2)

choose_O = tk.Radiobutton(start_frame, text= "O", variable= symbol_var, value="O", font= 9)
choose_O.grid(row= 8, column=3)


choose_label_2 = tk.Label(start_frame, text= "What Player-2 would be, X or O   ", font= 8)
choose_label_2.grid(row= 9, column=0, columnspan=2)
choose_entry_2 = tk.Entry(start_frame, width= 15, justify="center", state="disabled")
choose_entry_2.grid(row= 9, column=2, columnspan=2)



def start_game():
    global turn,   player1,player2,   player1_symbol, player2_symbol

    player1 = p1_entry.get()
    player2 = p2_entry.get()

    if not player1:
        player1 = "Player-1"
        p1_entry.insert(0, "Player-1")
        
    p1_entry.config(state="disabled")
    print(f"\n\n{player1} is Player-1 ...")

    if not player2:
        player2="Player-2"
        p2_entry.insert(0, "Player-2")
        
    p2_entry.config(state="disabled")
    print(f"{player2} is Player-2...\n")
    
    window.after(500, lambda: print(f"Ready, {player1} vs {player2}"))

    symbol = symbol_var.get()

    player1_symbol = symbol
    player2_symbol = "O" if player1_symbol == "X" else "X"

    
    if player1_symbol == "X":
        choose_entry_2.config(state="normal")
        choose_entry_2.delete(0, tk.END)
        choose_entry_2.insert(0, "O")
    else:
        choose_entry_2.config(state="normal")
        choose_entry_2.insert(0, "X")
        
    turn = player1_symbol

    # Disabled all
    choose_entry_2.config(state="disabled")
    choose_X.config(state= "disabled")
    choose_O.config(state= "disabled")
    single_player.config(state= "disabled")
    double_player.config(state= "disabled")

    
    window.update_idletasks()      #This forces Tkinter to update the screen right now
    window.after(1500, lambda:(
                 start_frame.pack_forget(),
                 game_frame.pack()))

start_button= tk.Button(start_frame, text="Start Game", font=5, command=start_game)
start_button.grid(row=15, column=0, columnspan=2, pady= 20)



# ----------------- Game Frame -----------------
game_frame= tk.Frame(window)
game_frame.pack_forget()


label = tk.Label(game_frame, text= "Who will rule the board?", font= ("Times 20 bold",20,"bold"))
label.pack(pady= (20,0))


score_label = tk.Label(game_frame, text= f"Score  |   {player1_symbol} (P1):   {score_x}     |   {player2_symbol} (P2):   {score_o}     ", font=("Arial", 14, "bold"), bg="#222222", fg="#FFD700")
score_label.pack(side="top", anchor="ne", pady=7)


frame= tk.Frame(game_frame,)
frame.pack(pady= 10)
frame.pack_propagate(False)

reset_button= tk.Button(game_frame, text="Reset", width=15, height=1
                        ,command= lambda: [reset_game(), reset_button.pack_forget()])



# ----------------- Functions -----------------
def check_result(text_result, symbol_result):
    label.config(text= (f"'{text_result}' is the WINNER({symbol_result})"))


# Updating the score
def update_score_label():
    global score_x, score_o
    score_label.config(text=f"Score  |   {player1_symbol} (P1):   {score_x}     |   {player2_symbol} (P2):   {score_o}     ")
    reset_button.pack()


# Check who wins
def check_win():
    global game_over, row_line, column_line, score_x, score_o
    
    for i in range(3):
        # Check Rows
        if(button[i][0]["text"]==button[i][1]["text"]==button[i][2]["text"] !=""):
            
           if (winner := button[i][0]["text"]) == player1_symbol:
               print(f"'{player1}' is the WINNER({player1_symbol})")
               check_result(player1, winner)
               score_x +=1
           else:
               print(f"'{player2}' is the WINNER({player2_symbol})")
               check_result(player2, winner)
               score_o +=1

           update_score_label()
           
           row = 84 + (i * 187)
           row_line= tk.Canvas(frame, bg="darkred" if winner == "X" else "darkblue",
                              width=630, height= 3,highlightthickness=0,)
           row_line.place(x=14, y=row)
           row_line.create_line(30, 2, 640, 2, width=40,fill="",tags="line")
           
           play_sound()
                        
           game_over = True
           return


        
        #Check Columns
        if(button[0][i]["text"]==button[1][i]["text"]==button[2][i]["text"] !=""):

            if (winner := button[0][i]["text"]) == player1_symbol:
                print(f"'{player1}' is the WINNER({player1_symbol})")
                check_result(player1, winner)
                score_x +=1
            else:
                 print(f"'{player2}' is the WINNER({player2_symbol})")
                 check_result(player2, winner)
                 score_o +=1

            update_score_label()
            
            column = 111 + (i * 226)
            column_line= tk.Canvas(frame, bg="darkred" if winner == "X" else "darkblue",
                                   width=3, height= 500,highlightthickness=0,)
            column_line.place(x=column, y=20)
            column_line.create_line(2, 30, 2, 370, width=40,fill="",tags="line")
            
            play_sound()
            
            game_over = True
            return



    # Check Diagonals
    if(button[0][0]["text"]==button[1][1]["text"]==button[2][2]["text"] !=""):
        
        if button[0][0]["text"] == player1_symbol:
            print(f"'{player1}' is the WINNER({player1_symbol})")
            check_result(player1 ,button[0][0]["text"])
            score_x +=1
        else:
            print(f"'{player2}' is the WINNER({player2_symbol})")
            check_result(player2 ,button[0][0]["text"])
            score_o +=1
            
        update_score_label()
        play_sound()

        game_over = True
        return



    if(button[0][2]["text"]==button[1][1]["text"]==button[2][0]["text"] !=""):
        
        if button[0][2]["text"] == player1_symbol:
            print(f"'{player1}' is the WINNER({player1_symbol})")
            check_result(player1 ,button[0][2]["text"])
            score_x +=1
        else:
            print(f"'{player2}' is the WINNER({player2_symbol})")
            check_result(player2 ,button[0][2]["text"])
            score_o +=1

        update_score_label()
        play_sound()
        
        game_over = True
        return

    # Check Draw(tie)
    draw = True
    for row in button:
        for b in row:
            if b["text"] == "":
                draw = False               
    if draw:
        label.config(text = "It's a DRAW")
        print("It's a DRAW")
                
        global turn

        disable()
        play_sound()
        update_score_label()
        
        game_over = True
        turn = None


# This play sound after win
def play_sound():
    try:
        import winsound
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
    except ImportError:
        # If not Windows, just skip the sound
        pass

# This disable all the buttons
def disable():
    for row in button:
        for b in row:
            b.config(state= "disable")


def get_player_name(symbol):
    return player1 if symbol == player1_symbol else player2



def on_click(b):
    global turn,game_over

    # Stop the game if already over, or if the button is already clicked
    if b["text"] !="":
      return

    if game_over:
       return

    # Mark the clicked button with X or O
    b.config(text= turn, font= ("Times 20 bold", 11, "bold"))

    # Check all win conditions (8 ways)
    check_win()

    if game_over:
       return
            
    # Switch turns
    if turn == "X":
       b.config(fg= "Red")
       label.config(text= f"O's Turn('{get_player_name('O')}')")
       turn = "O"

    else:
        b.config(fg= "Blue")
        label.config(text= f"X's Turn('{get_player_name('X')}')")
        turn = "X"



# ----------------- Buttons -----------------
button = []
for rows in range(3):
  row_button = []     #Starts a new row list to store 3 buttons.
  for columns in range(3):

      btn= tk.Button(frame, text= "", bg= "darkgrey", height= 9, width= 24)
      btn.grid(row= rows, column= columns, sticky="nswe", pady=1,padx=1)

      btn.config(command= lambda b=btn: on_click(b))

      row_button.append(btn)
      
  button.append(row_button)



def reset_game():
    global game_over, turn
    game_over = False
    turn = player1_symbol
    
    label.config(text= "Who will rule the board?")
    
    for i in range(3):
        for j in range(3):
            button[i][j].config(text= "", state= "normal")

    # Destory the line
    global row_line, column_line

    if row_line is not None:
       row_line.destroy()
       row_line = None
    if column_line is not None:
       column_line.destroy()
       column_line = None



def reset_all():
    # reseting the start_frame
    single_player.config(state= "normal")
    double_player.config(state= "normal")
    
    p1_entry.config(state="normal")
    p2_entry.config(state="normal")

    p1_entry.delete(0, tk.END)
    p2_entry.delete(0, tk.END)
 
    choose_X.config(state= "normal")
    choose_O.config(state= "normal")
    
    choose_entry_2.config(state="normal")
    choose_entry_2.delete(0, tk.END)
    choose_entry_2.config(state="disable")

    score_o = 0
    score_x = 0
    score_label.config(text=f"Score  |   {player1_symbol} (P1):   {score_x}     |   {player2_symbol} (P2):   {score_o}     ")
       
    # Resetting the mode selection to default
    mode_var.set("two player")
    symbol_var.set("X")

    # reseting the game_frame
    reset_game()

    # Show start frame and hide game frame
    game_frame.pack_forget()
    start_frame.pack()


reset_all_button = tk.Button(start_frame, text="Reset All", width=15, height=1
                        ,command= lambda: [reset_all(), reset_all_button.grid_forget()])


# Go back and look
def just_view():
    game_frame.pack_forget()
    start_frame.pack()
    reset_all_button.grid(column=0, columnspan=2)



def show_info():
    help_window = tk.Toplevel(game_frame)
    help_window.title("How to play!")
    help_window.geometry("300x200")
    help_window.resizable(False, False)


    tk.Label(help_window, text="How to Play Tic Tac Toe", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(help_window, text=
        "1. X starts the game.\n"
        "2. Click any empty box to mark X or O.\n"
        "3. First to get 3 in a row wins.\n"
        "4. Use Reset to start again.",
        justify="left", font=("Arial", 11)
    ).pack(padx=10)

    tk.Button(help_window, text="Close", command=help_window.destroy).pack(pady=10)


# Change Symbol   
def choose_symbol():
    global turn
    
    symbol = simpledialog.askstring("Cheat","Do you want to be X or O? (Cheating)")
    if symbol and symbol.upper() in ["X" , "O"]:
        turn = symbol.upper()
        label.config(text=f"{turn}'s Turn")
    elif symbol:
        print("You can only choose X or O")
        messagebox.showerror("Invalid Choice", "You can only choose X or O")
        


# ----------------- Menu -----------------
menu = tk.Menu(game_frame, tearoff=0)

reset_menu = tk.Menu(menu, tearoff=0)

reset_menu.add_command(label= "Reset Game/Board", command= reset_game)
reset_menu.add_command(label= "Reset ALL", command= reset_all)
reset_menu.add_command(label= "Just view", command= just_view)

menu.add_cascade(label="Reset", menu= reset_menu)


menu.add_command(label="Exit", command=window.destroy)
menu.add_command(label="Show_Info/Help", command=show_info)
menu.add_command(label="Choose/change Symbol", command=choose_symbol)



window.config(menu=menu)

window.mainloop()
