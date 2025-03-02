import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk

def validation(score):
    return 0 <= score <= 100

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def GPA_calc(letter):
    return {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}.get(letter, 0.0)

def calculate_gpa():
    try:
        scores = [int(entry.get()) for entry in score_entries]
        if not all(validation(s) for s in scores):
            messagebox.showerror("Error", "Please enter values between 0 and 100.")
            return
        avg = sum(scores) / len(scores)
        letter = grade(avg)
        gpa = GPA_calc(letter)
        result_label.config(text=f"\n🔥 Average: {avg:.2f}\n🎓 Grade: {letter}\n🏆 GPA: {gpa} 🔥", foreground='#00ff00')
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def add_subject():
    entry = ttk.Entry(frame, font=("Segoe UI", 14))
    entry.pack(pady=5, padx=10, fill=tk.X, expand=True)
    score_entries.append(entry)

# GUI Setup
root = ThemedTk(theme="equilux")  # ثيم داكن احترافي
root.title("🔥 GPA Calculator 🔥")
root.geometry("520x700")
root.minsize(520, 700)
root.configure(bg="#121212")

style = ttk.Style()
style.configure("TFrame", background="#121212")
style.configure("TLabel", background="#121212", font=("Segoe UI", 14), foreground="#ffffff")
style.configure("TButton", font=("Segoe UI", 14, "bold"), padding=10, background="#03DAC6", foreground="#000000", borderwidth=2, relief="flat")
style.map("TButton", background=[("active", "#018786")])

frame = ttk.Frame(root, padding=20)
frame.pack(fill=tk.BOTH, expand=True)

title_label = ttk.Label(frame, text="🔥 GPA Calculator 🔥", font=("Segoe UI", 22, "bold"), foreground="#BB86FC")
title_label.pack(pady=10)

ttk.Label(frame, text="Enter Scores:", font=("Segoe UI", 14, "bold"), foreground="#ffffff").pack()

score_entries = []
for _ in range(3):  # Default 3 subjects
    add_subject()

ttk.Button(frame, text="➕ Add Subject", command=add_subject, style="TButton").pack(pady=10, fill=tk.X)
ttk.Button(frame, text="🔥 Calculate GPA 🔥", command=calculate_gpa, style="TButton").pack(pady=10, fill=tk.X)

result_label = ttk.Label(frame, text="", font=("Segoe UI", 16, "bold"), foreground="#00ff00")
result_label.pack(pady=10)

root.mainloop()
