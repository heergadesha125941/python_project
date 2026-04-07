import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
import random

accounts = []

# ---------------- FUNCTIONS ---------------- #

def validate_aadhar(P):
    return P.isdigit() and len(P) <= 12


def add_account():
    name = entry_name.get()
    acc_no = entry_acc.get()
    acc_type = combo_type.get()
    aadhar = entry_aadhar.get()
    balance = entry_balance.get()

    if not name or not acc_no or not balance or not acc_type or not aadhar:
        messagebox.showerror("Error", "Fill all fields")
        return

    try:
        balance = float(balance)
    except:
        messagebox.showerror("Error", "Invalid balance")
        return

    accounts.append({
        "name": name,
        "acc_no": acc_no,
        "type": acc_type,
        "aadhar": aadhar,
        "balance": balance
    })
    display_accounts()


def deposit():
    index = listbox.curselection()
    if not index:
        messagebox.showerror("Error", "Select account first")
        return

    try:
        amt = float(entry_amount.get())
    except:
        messagebox.showerror("Error", "Invalid amount")
        return

    accounts[index[0]]["balance"] += amt
    display_accounts()


def withdraw():
    index = listbox.curselection()
    if not index:
        messagebox.showerror("Error", "Select account first")
        return

    try:
        amt = float(entry_amount.get())
    except:
        messagebox.showerror("Error", "Invalid amount")
        return

    if accounts[index[0]]["balance"] < amt:
        messagebox.showerror("Error", "Low Balance")
        return

    accounts[index[0]]["balance"] -= amt
    display_accounts()


def delete_account():
    index = listbox.curselection()
    if not index:
        messagebox.showerror("Error", "Select account first")
        return

    accounts.pop(index[0])
    display_accounts()


def update_account():
    index = listbox.curselection()
    if not index:
        messagebox.showerror("Error", "Select account first")
        return

    try:
        balance = float(entry_balance.get())
    except:
        messagebox.showerror("Error", "Invalid balance")
        return

    accounts[index[0]] = {
        "name": entry_name.get(),
        "acc_no": entry_acc.get(),
        "type": combo_type.get(),
        "aadhar": entry_aadhar.get(),
        "balance": balance
    }

    display_accounts()


def display_accounts():
    listbox.delete(0, tk.END)
    for acc in accounts:
        listbox.insert(
            tk.END,
            f"{acc['name']} | {acc['acc_no']} | {acc['type']} | {acc['aadhar']} | {acc['balance']}"
        )


def select_account(event):
    try:
        i = listbox.curselection()[0]
        acc = accounts[i]

        entry_name.delete(0, tk.END)
        entry_name.insert(0, acc["name"])

        entry_acc.delete(0, tk.END)
        entry_acc.insert(0, acc["acc_no"])

        combo_type.set(acc["type"])

        entry_aadhar.delete(0, tk.END)
        entry_aadhar.insert(0, acc["aadhar"])

        entry_balance.delete(0, tk.END)
        entry_balance.insert(0, acc["balance"])
    except:
        pass


# ---------------- GRAPHS ---------------- #

def balance_graph():
    names = [a["name"] for a in accounts]
    bal = [a["balance"] for a in accounts]

    plt.figure()
    plt.bar(names, bal)
    plt.title("Balances")
    plt.show()


def accounts_graph():
    types = [a["type"] for a in accounts]
    unique = list(set(types))
    counts = [types.count(t) for t in unique]

    plt.figure()
    plt.bar(unique, counts)
    plt.title("Account Type Distribution")
    plt.show()


# ---------------- UI ---------------- #

root = tk.Tk()
root.title("Premium Banking System")
root.state("zoomed")

canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Gradient Background
for i in range(height):
    color = "#%02x%02x%02x" % (30, 30 + i//5, 60 + i//6)
    canvas.create_line(0, i, width, i, fill=color)

# Floating ₹ symbols
coins = []
for _ in range(40):
    x = random.randint(0, width - 50)
    y = random.randint(0, height - 50)
    img = canvas.create_text(x, y, text="₹", font=("Arial", 16), fill="white")
    coins.append([img, random.randint(1, 3)])

def animate():
    for coin in coins:
        canvas.move(coin[0], 0, coin[1])
        pos = canvas.coords(coin[0])
        if pos[1] > height:
            canvas.coords(coin[0], random.randint(0, width - 50), 0)
    root.after(50, animate)

animate()

main_frame = tk.Frame(root, bg="#000000")
canvas.create_window(width//2, height//2, window=main_frame)

# Title
tk.Label(main_frame, text="💳 Banking Dashboard",
         font=("Arial", 18, "bold"),
         bg="black", fg="white").pack(pady=10)

frame = tk.Frame(main_frame, bg="black")
frame.pack(pady=10)

# Fields

tk.Label(frame, text="Name", bg="black", fg="white").grid(row=0, column=0)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Account No", bg="black", fg="white").grid(row=1, column=0)
entry_acc = tk.Entry(frame)
entry_acc.grid(row=1, column=1)

tk.Label(frame, text="Account Type", bg="black", fg="white").grid(row=2, column=0)
combo_type = ttk.Combobox(frame, values=["Saving", "Current", "Fixed"])
combo_type.grid(row=2, column=1)

tk.Label(frame, text="Aadhar No", bg="black", fg="white").grid(row=3, column=0)
vcmd = (root.register(validate_aadhar), "%P")
entry_aadhar = tk.Entry(frame, validate="key", validatecommand=vcmd)
entry_aadhar.grid(row=3, column=1)

tk.Label(frame, text="Balance", bg="black", fg="white").grid(row=4, column=0)
entry_balance = tk.Entry(frame)
entry_balance.grid(row=4, column=1)

tk.Label(frame, text="Amount", bg="black", fg="white").grid(row=5, column=0)
entry_amount = tk.Entry(frame)
entry_amount.grid(row=5, column=1)

# Buttons
btn_frame = tk.Frame(main_frame, bg="black")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=12, command=add_account).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", width=12, command=update_account).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Deposit", width=12, command=deposit).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Withdraw", width=12, command=withdraw).grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="Delete", width=12, command=delete_account).grid(row=0, column=4, padx=5)

tk.Button(btn_frame, text="Balance Graph", command=balance_graph).grid(row=1, column=1, pady=5)
tk.Button(btn_frame, text="Type Graph", command=accounts_graph).grid(row=1, column=2, pady=5)

listbox = tk.Listbox(main_frame, width=90)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", select_account)

root.bind("<Escape>", lambda e: root.state("normal"))

root.mainloop()
