import tkinter as tk
from tkinter import scrolledtext, messagebox

class Player:
    def __init__(self, jersey_number):
        self.jersey_number = jersey_number
        self.next_player = None

class FootballTeam:
    def __init__(self):
        self.captain = None

    def sign_player_front(self, jersey_number):
        new_player = Player(jersey_number)
        new_player.next_player = self.captain
        self.captain = new_player

    def sign_player_end(self, jersey_number):
        new_player = Player(jersey_number)

        if self.captain is None:
            self.captain = new_player
            return

        current_player = self.captain

        while current_player.next_player:
            current_player = current_player.next_player

        current_player.next_player = new_player

    def sign_player_position(self, jersey_number, squad_position):
        new_player = Player(jersey_number)

        if squad_position == 0:
            new_player.next_player = self.captain
            self.captain = new_player
            return

        current_player = self.captain

        for _ in range(squad_position - 1):
            if current_player is None:
                raise IndexError("Position out of bounds.")
            current_player = current_player.next_player

        new_player.next_player = current_player.next_player
        current_player.next_player = new_player

    def release_player_number(self, jersey_number):
        current_player = self.captain

        if current_player is not None:
            if current_player.jersey_number == jersey_number:
                self.captain = current_player.next_player
                return

        while current_player is not None:
            if current_player.jersey_number == jersey_number:
                break

            previous_player = current_player
            current_player = current_player.next_player

        if current_player is None:
            return

        previous_player.next_player = current_player.next_player

    def release_player_position(self, squad_position):
        if self.captain is None:
            return

        current_player = self.captain

        if squad_position == 0:
            self.captain = current_player.next_player
            return

        for _ in range(squad_position - 1):
            current_player = current_player.next_player

            if current_player is None or current_player.next_player is None:
                raise IndexError("Position out of bounds.")

        next_member = current_player.next_player.next_player
        current_player.next_player = next_member

    def get_team(self):
        players = []
        current_player = self.captain

        while current_player:
            players.append(str(current_player.jersey_number))
            current_player = current_player.next_player

        return players

team = FootballTeam()

def display_team():
    output.delete(1.0, tk.END)
    output.insert(tk.END, "Om Wala S119\n")
    output.insert(tk.END, "=" * 50 + "\n\n")

    players = team.get_team()

    if not players:
        output.insert(tk.END, "No players are currently in the football team.")
    else:
        output.insert(tk.END, "Football Team Lineup:\n\n")
        output.insert(tk.END, " -> ".join(players))

def add_front():
    try:
        jersey = int(entry_jersey.get())
        team.sign_player_front(jersey)
        display_team()
    except:
        messagebox.showerror("Error", "Enter a valid jersey number.")

def add_end():
    try:
        jersey = int(entry_jersey.get())
        team.sign_player_end(jersey)
        display_team()
    except:
        messagebox.showerror("Error", "Enter a valid jersey number.")

def add_position():
    try:
        jersey = int(entry_jersey.get())
        pos = int(entry_position.get())
        team.sign_player_position(jersey, pos)
        display_team()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def remove_number():
    try:
        jersey = int(entry_jersey.get())
        team.release_player_number(jersey)
        display_team()
    except:
        messagebox.showerror("Error", "Enter a valid jersey number.")

def remove_position():
    try:
        pos = int(entry_position.get())
        team.release_player_position(pos)
        display_team()
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Football Team Manager - Om Wala S119")
root.geometry("850x650")
root.configure(bg="#DCEEFF")

title = tk.Label(
    root,
    text="Football Team Manager",
    font=("Arial",20,"bold"),
    bg="#1565C0",
    fg="white",
    pady=10
)
title.pack(fill="x")

frame = tk.Frame(root,bg="#DCEEFF")
frame.pack(pady=10)

tk.Label(frame,text="Jersey Number",font=("Arial",11,"bold"),bg="#DCEEFF").grid(row=0,column=0,padx=10,pady=5)
entry_jersey = tk.Entry(frame,font=("Arial",11),width=15)
entry_jersey.grid(row=0,column=1,padx=10)

tk.Label(frame,text="Position",font=("Arial",11,"bold"),bg="#DCEEFF").grid(row=0,column=2,padx=10)
entry_position = tk.Entry(frame,font=("Arial",11),width=15)
entry_position.grid(row=0,column=3,padx=10)

button_frame = tk.Frame(root,bg="#DCEEFF")
button_frame.pack(pady=10)

tk.Button(button_frame,text="Add Front",bg="#1976D2",fg="white",font=("Arial",10,"bold"),width=18,command=add_front).grid(row=0,column=0,padx=5,pady=5)

tk.Button(button_frame,text="Add End",bg="#1976D2",fg="white",font=("Arial",10,"bold"),width=18,command=add_end).grid(row=0,column=1,padx=5,pady=5)

tk.Button(button_frame,text="Add at Position",bg="#1976D2",fg="white",font=("Arial",10,"bold"),width=18,command=add_position).grid(row=0,column=2,padx=5,pady=5)

tk.Button(button_frame,text="Remove by Jersey",bg="#1976D2",fg="white",font=("Arial",10,"bold"),width=18,command=remove_number).grid(row=1,column=0,padx=5,pady=5)

tk.Button(button_frame,text="Remove by Position",bg="#1976D2",fg="white",font=("Arial",10,"bold"),width=18,command=remove_position).grid(row=1,column=1,padx=5,pady=5)

tk.Button(button_frame,text="Display Team",bg="#1976D2",fg="white",font=("Arial",10,"bold"),width=18,command=display_team).grid(row=1,column=2,padx=5,pady=5)

output = scrolledtext.ScrolledText(root,width=95,height=22,font=("Consolas",11))
output.pack(padx=10,pady=15)

display_team()

root.mainloop()
