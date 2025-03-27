import tkinter as tk
import random
from tkinter import messagebox

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        
        # Word list and game setup
        self.words = ["PYTHON", "JAVA", "HANGMAN", "PROGRAMMING", "DEVELOPER"]
        self.secret_word = random.choice(self.words)
        self.guessed_letters = []
        self.lives = 6
        
# Hangman visual stages (ASCII art in labels)
        self.hangman_stages = [
            """
            -----
            |   |
                |
                |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
                |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
            |   |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
           /|   |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
           /|\\  |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
           /|\\  |
           /    |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
           /|\\  |
           / \\  |
                |
            --------
            """
        ]
        
        # GUI Elements
        self.word_display = tk.Label(root, text="_ " * len(self.secret_word), font=("Arial", 24))
        self.word_display.pack(pady=20)
        
        self.hangman_label = tk.Label(root, text=self.hangman_stages[0], font=("Courier", 12), justify="left")
        self.hangman_label.pack()
        
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=10)
        
        # Create letter buttons (A-Z)
        self.letter_buttons = {}  # Stores buttons for later reference
        self.create_letter_buttons()
        
        # Restart button
        self.restart_button = tk.Button(root, text="Restart Game", command=self.restart_game)
        self.restart_button.pack(pady=10)
    
    def create_letter_buttons(self):
        for i in range(26):
            letter = chr(65 + i)  # A-Z
            button = tk.Button(
                self.buttons_frame, 
                text=letter, 
                width=4, 
                height=2,
                font=("Arial", 10),
                bg="#f0f0f0",  # Default light gray
                activebackground="#d0d0d0",  # Slightly darker when clicked
                relief=tk.RAISED,
                command=lambda l=letter: self.guess_letter(l)
            )
            button.grid(row=i // 7, column=i % 7, padx=2, pady=2)
            self.letter_buttons[letter] = button  # Store button reference
    
    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            return
        
        self.guessed_letters.append(letter)
        
        # Update button style (bolder appearance)
        self.letter_buttons[letter].config(
            state=tk.DISABLED,
            bg="#a0a0a0",  # Darker gray for pressed buttons
            relief=tk.SUNKEN  # Makes it look "pressed"
        )
        
        if letter in self.secret_word:
            # Update word display
            display_word = ""
            for char in self.secret_word:
                if char in self.guessed_letters:
                    display_word += char + " "
                else:
                    display_word += "_ "
            self.word_display.config(text=display_word)
            
            # Check if player won
            if "_" not in display_word:
                messagebox.showinfo("Congratulations!", "You won! The word was: " + self.secret_word)
                self.restart_game()
        else:
            self.lives -= 1
            self.hangman_label.config(text=self.hangman_stages[6 - self.lives])
            
            # Check if player lost
            if self.lives == 0:
                messagebox.showinfo("Game Over", "You lost! The word was: " + self.secret_word)
                self.restart_game()
    
    def restart_game(self):
        self.secret_word = random.choice(self.words)
        self.guessed_letters = []
        self.lives = 6
        self.word_display.config(text="_ " * len(self.secret_word))
        self.hangman_label.config(text=self.hangman_stages[0])
        
        # Reset all buttons (enable and revert style)
        for letter, button in self.letter_buttons.items():
            button.config(
                state=tk.NORMAL,
                bg="#f0f0f0",  # Light gray (default)
                relief=tk.RAISED  # Raised appearance
            )

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()