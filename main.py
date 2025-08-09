import tkinter as tk
from tkinter import messagebox
import random

# Word bank
word_bank = {
    "Animal": ["tiger", "zebra", "koala", "eagle", "shark", "panda", "otter", "horse", "camel", "rhino"],
    "Place": ["paris", "delhi", "tokyo", "london", "sydney", "cairo", "osaka", "berlin", "miami"],
    "Object": ["chair", "table", "piano", "brush", "clock", "phone", "torch", "glass", "spoon", "plant"]
}

# Colors
COLOR_CORRECT = "#6aaa64"   # Green
COLOR_PRESENT = "#c9b458"   # Yellow
COLOR_ABSENT = "#787c7e"    # Gray

# Game state
TARGET_WORD = ""
MAX_TRIES = 5
WORD_LENGTH = 5
tries = 0

# Start game with selected category
def start_game():
    global TARGET_WORD, tries
    tries = 0
    selected_category = category_var.get()
    TARGET_WORD = random.choice(word_bank[selected_category])
    entry.config(state="normal")
    submit_btn.config(state="normal")
    entry.delete(0, tk.END)
    for widget in frame.winfo_children():
        widget.destroy()
    print("Target word:", TARGET_WORD)

# Check guess and give feedback
def check_guess():
    global tries
    guess = entry.get().lower()
    if len(guess) != WORD_LENGTH:
        messagebox.showwarning("Oops!", f"Enter a {WORD_LENGTH}-letter word.")
        return

    for i in range(WORD_LENGTH):
        letter = guess[i]
        lbl = tk.Label(frame, text=letter.upper(), width=4, height=2, font=("Arial", 16, "bold"))
        if letter == TARGET_WORD[i]:
            lbl.config(bg=COLOR_CORRECT, fg="white")
        elif letter in TARGET_WORD:
            lbl.config(bg=COLOR_PRESENT, fg="white")
        else:
            lbl.config(bg=COLOR_ABSENT, fg="white")
        lbl.grid(row=tries, column=i, padx=2, pady=2)

    tries += 1
    entry.delete(0, tk.END)

    if guess == TARGET_WORD:
        messagebox.showinfo(" You Win!", f"You guessed it in {tries} tries!")
        entry.config(state="disabled")
        submit_btn.config(state="disabled")
    elif tries == MAX_TRIES:
        messagebox.showinfo(" Game Over", f"The word was: {TARGET_WORD.upper()}")
        entry.config(state="disabled")
        submit_btn.config(state="disabled")

# GUI setup
window = tk.Tk()
window.title("Guess the Word Game ")
window.geometry("500x600")
window.iconbitmap("Main_icon.ico")
window.config(bg="lightgray")

tk.Label(window, text="Choose a category:", font=("Arial", 12)).pack(pady=5)
category_var = tk.StringVar(value="Animal")
tk.OptionMenu(window, category_var, *word_bank.keys()).pack()

tk.Button(window, text="Start Game", font=("Arial", 12), command=start_game).pack(pady=10)

tk.Label(window, text="Enter a 5-letter word:", font=("Arial", 14)).pack()
entry = tk.Entry(window, font=("Arial", 14), justify="center", state="disabled")
entry.pack(pady=5)

submit_btn = tk.Button(window, text="Submit", font=("Arial", 12), command=check_guess, state="disabled")
submit_btn.pack(pady=5)

frame = tk.Frame(window)
frame.pack(pady=10)

window.mainloop()