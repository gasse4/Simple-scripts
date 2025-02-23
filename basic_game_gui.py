from random import randint
import customtkinter as ctk


def name(s):
    if s == 1:
        return "Rock 🪨"
    elif s == 2:
        return "Scissors ✂️"
    else:
        return "Paper 📜"


def input_rounds(ss=0):
    return 3


def check_game(choice, cpu_choice):
    if (
        (choice == 1 and cpu_choice == 2)
        or (choice == 2 and cpu_choice == 3)
        or (choice == 3 and cpu_choice == 1)):
        return 1, 0, f"🎉 You win!\nCPU chose {name(cpu_choice)}"
    elif choice == cpu_choice:
        return 0, 0, f"🤝 Tie!\nCPU chose {name(cpu_choice)}"
    else:
        return 0, 1, f"😿 CPU wins!\nCPU chose {name(cpu_choice)}"


def end_game(user_points, cpu_points):
    result_str = "🏆 Final Score:\n"
    result_str += f"User: {user_points} 🌟\n"
    result_str += f"CPU: {cpu_points} 🤖\n"
    if user_points > cpu_points:
        result_str += "🎊 You win the game! 🎊"
    elif cpu_points > user_points:
        result_str += "🤖 CPU wins the game! 😿"
    else:
        result_str += "🤝 It's a tie! 🤝"
    return result_str


class RockPaperScissorsGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors")
        self.geometry("650x700")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.user_score = 0
        self.cpu_score = 0
        self.rounds = 3
        self.current_round = 0
        self.user_choice = 0

        self.configure(fg_color="#F5F7FA")

        self.title_label = ctk.CTkLabel(
            self,
            text="🪨✂️📜 Rock Paper Scissors",
            font=("Arial", 40, "bold"),
            text_color="#1A3C34",
        )
        self.title_label.pack(pady=30)

        self.rounds_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.rounds_frame.pack(pady=20)
        self.rounds_label = ctk.CTkLabel(
            self.rounds_frame, text="Rounds:", font=("Arial", 16), text_color="#1A3C34"
        )
        self.rounds_label.pack(side=ctk.LEFT, padx=10)
        self.rounds_entry = ctk.CTkEntry(
            self.rounds_frame,
            width=70,
            height=40,
            corner_radius=15,
            border_color="#8A817C",
        )
        self.rounds_entry.pack(side=ctk.LEFT, padx=10)
        self.rounds_entry.insert(0, "3")
        self.rounds_button = ctk.CTkButton(
            self.rounds_frame,
            text="Set 🎲",
            width=100,
            height=40,
            corner_radius=20,
            command=self.set_rounds,
            fg_color="#E07A5F",
            hover_color="#D6684A",
        )
        self.rounds_button.pack(side=ctk.LEFT, padx=10)

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=30)
        self.rock_button = ctk.CTkButton(
            self.button_frame,
            text="Rock 🪨",
            width=160,
            height=60,
            corner_radius=25,
            font=("Arial", 18),
            command=lambda: self.play_round(1),
            fg_color="#3D405B",
            hover_color="#2E3147",
        )
        self.rock_button.pack(side=ctk.LEFT, padx=15)
        self.scissors_button = ctk.CTkButton(
            self.button_frame,
            text="Scissors ✂️",
            width=160,
            height=60,
            corner_radius=25,
            font=("Arial", 18),
            command=lambda: self.play_round(2),
            fg_color="#81B29A",
            hover_color="#6A957F",
        )
        self.scissors_button.pack(side=ctk.LEFT, padx=15)
        self.paper_button = ctk.CTkButton(
            self.button_frame,
            text="Paper 📜",
            width=160,
            height=60,
            corner_radius=25,
            font=("Arial", 18),
            command=lambda: self.play_round(3),
            fg_color="#F2CC8F",
            hover_color="#E0B876",
        )
        self.paper_button.pack(side=ctk.LEFT, padx=15)

        self.status_label = ctk.CTkLabel(
            self,
            text=f"Round 1 of {self.rounds} 🎮",
            font=("Arial", 22, "bold"),
            text_color="#1A3C34",
        )
        self.status_label.pack(pady=20)

        self.result_frame = ctk.CTkFrame(self, fg_color="#EDEDED", corner_radius=15)
        self.result_frame.pack(pady=20, padx=20, fill="x")
        self.result_label = ctk.CTkLabel(
            self.result_frame,
            text="",
            font=("Arial", 18),
            wraplength=580,
            justify="center",
            text_color="#1A3C34",
        )
        self.result_label.pack(pady=15)

        self.score_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.score_frame.pack(pady=25)
        self.user_score_label = ctk.CTkLabel(
            self.score_frame,
            text=f"User: {self.user_score} 🌟",
            font=("Arial", 20, "bold"),
            text_color="#E07A5F",
        )
        self.user_score_label.pack(side=ctk.LEFT, padx=30)
        self.cpu_score_label = ctk.CTkLabel(
            self.score_frame,
            text=f"CPU: {self.cpu_score} 🤖",
            font=("Arial", 20, "bold"),
            text_color="#3D405B",
        )
        self.cpu_score_label.pack(side=ctk.RIGHT, padx=30)

        self.restart_button = ctk.CTkButton(
            self,
            text="Restart 🔄",
            width=160,
            height=60,
            corner_radius=25,
            font=("Arial", 18),
            command=self.restart_game,
            fg_color="#619B8A",
            hover_color="#4F826F",
        )
        self.restart_button.pack(pady=30)
        self.restart_button.configure(state="disabled")

    def set_rounds(self):
        try:
            new_rounds = int(self.rounds_entry.get())
            if new_rounds % 2 == 0:
                new_rounds += 1
            if new_rounds <= 0:
                raise ValueError
            self.rounds = new_rounds
            self.current_round = 0
            self.restart_game()
            self.status_label.configure(text=f"Round 1 of {self.rounds} 🎮")
        except ValueError:
            self.result_label.configure(text="⚠️ Enter a positive number!")

    def play_round(self, user_choice):
        if self.current_round < self.rounds:
            self.current_round += 1
            cpu_choice = randint(1, 3)
            user_result, cpu_result, message = check_game(user_choice, cpu_choice)
            self.user_score += user_result
            self.cpu_score += cpu_result
            self.result_label.configure(text=message)
            self.user_score_label.configure(text=f"User: {self.user_score} 🌟")
            self.cpu_score_label.configure(text=f"CPU: {self.cpu_score} 🤖")
            self.status_label.configure(
                text=f"Round {self.current_round + (0 if self.current_round < self.rounds else -1)} of {self.rounds} 🎮"
            )
            if self.current_round >= self.rounds:
                self.end_round()
        else:
            self.end_round()

    def end_round(self):
        self.result_label.configure(text=end_game(self.user_score, self.cpu_score))
        self.rock_button.configure(state="disabled")
        self.scissors_button.configure(state="disabled")
        self.paper_button.configure(state="disabled")
        self.restart_button.configure(state="normal")
        self.rounds_button.configure(state="disabled")

    def restart_game(self):
        self.user_score = 0
        self.cpu_score = 0
        self.current_round = 0
        self.user_score_label.configure(text=f"User: {self.user_score} 🌟")
        self.cpu_score_label.configure(text=f"CPU: {self.cpu_score} 🤖")
        self.result_label.configure(text="")
        self.status_label.configure(
            text=f"Round {self.current_round + 1} of {self.rounds} 🎮"
        )
        self.rock_button.configure(state="normal")
        self.scissors_button.configure(state="normal")
        self.paper_button.configure(state="normal")
        self.restart_button.configure(state="disabled")
        self.rounds_button.configure(state="normal")


if __name__ == "__main__":
    app = RockPaperScissorsGUI()
    app.mainloop()
