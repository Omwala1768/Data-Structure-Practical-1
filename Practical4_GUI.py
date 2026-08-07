import tkinter as tk
from tkinter import scrolledtext, messagebox

class Movie:
    def __init__(self, movie_id):
        self.movie_id = movie_id
        self.next_movie = None
        self.previous_movie = None

class MovieCollection:
    def __init__(self):
        self.first_movie = None

    def add_movie_front(self, movie_id):
        new_movie = Movie(movie_id)

        if self.first_movie is None:
            self.first_movie = new_movie
        else:
            new_movie.next_movie = self.first_movie
            self.first_movie.previous_movie = new_movie
            self.first_movie = new_movie

    def add_movie_end(self, movie_id):
        new_movie = Movie(movie_id)

        if self.first_movie is None:
            self.first_movie = new_movie
        else:
            current_movie = self.first_movie

            while current_movie.next_movie:
                current_movie = current_movie.next_movie

            current_movie.next_movie = new_movie
            new_movie.previous_movie = current_movie

    def add_movie_position(self, movie_id, position):
        if position == 0:
            self.add_movie_front(movie_id)
            return

        new_movie = Movie(movie_id)
        current_movie = self.first_movie

        for _ in range(position):
            if current_movie is None:
                raise IndexError("Position out of bounds.")
            current_movie = current_movie.next_movie

        if current_movie is None:
            raise IndexError("Position out of bounds.")

        new_movie.next_movie = current_movie
        new_movie.previous_movie = current_movie.previous_movie

        if current_movie.previous_movie:
            current_movie.previous_movie.next_movie = new_movie

        current_movie.previous_movie = new_movie

    def remove_first_movie(self):
        if self.first_movie is None:
            return

        if self.first_movie.next_movie is None:
            self.first_movie = None
        else:
            self.first_movie = self.first_movie.next_movie
            self.first_movie.previous_movie = None

    def remove_last_movie(self):
        if self.first_movie is None:
            return

        if self.first_movie.next_movie is None:
            self.first_movie = None
        else:
            current_movie = self.first_movie

            while current_movie.next_movie:
                current_movie = current_movie.next_movie

            current_movie.previous_movie.next_movie = None

    def remove_movie_position(self, position):
        if self.first_movie is None:
            return

        if position == 0:
            self.remove_first_movie()
            return

        current_movie = self.first_movie

        for _ in range(position):
            if current_movie is None:
                raise IndexError("Position out of bounds.")
            current_movie = current_movie.next_movie

        if current_movie is None:
            raise IndexError("Position out of bounds.")

        if current_movie.previous_movie:
            current_movie.previous_movie.next_movie = current_movie.next_movie

        if current_movie.next_movie:
            current_movie.next_movie.previous_movie = current_movie.previous_movie

    def search_movie(self, movie_id):
        current_movie = self.first_movie

        while current_movie:
            if current_movie.movie_id == movie_id:
                return True
            current_movie = current_movie.next_movie

        return False

    def total_movies(self):
        count = 0
        current_movie = self.first_movie

        while current_movie:
            count += 1
            current_movie = current_movie.next_movie

        return count

    def get_movies(self):
        movies = []
        current_movie = self.first_movie

        while current_movie:
            movies.append(str(current_movie.movie_id))
            current_movie = current_movie.next_movie

        return movies

collection = MovieCollection()

def show_output(message=""):
    output.delete(1.0, tk.END)
    output.insert(tk.END, "Om Wala S119\n")
    output.insert(tk.END, "=" * 55 + "\n\n")

    movies = collection.get_movies()

    if movies:
        output.insert(tk.END, "Movie Collection:\n")
        output.insert(tk.END, " <-> ".join(movies) + "\n\n")
    else:
        output.insert(tk.END, "Movie Collection is empty.\n\n")

    if message:
        output.insert(tk.END, message)

def add_front():
    try:
        movie = int(entry_movie.get())
        collection.add_movie_front(movie)
        show_output("Movie added at the beginning.")
    except:
        messagebox.showerror("Error", "Enter a valid Movie ID.")

def add_end():
    try:
        movie = int(entry_movie.get())
        collection.add_movie_end(movie)
        show_output("Movie added at the end.")
    except:
        messagebox.showerror("Error", "Enter a valid Movie ID.")

def add_position():
    try:
        movie = int(entry_movie.get())
        pos = int(entry_position.get())
        collection.add_movie_position(movie, pos)
        show_output(f"Movie inserted at position {pos}.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def remove_first():
    collection.remove_first_movie()
    show_output("First movie removed.")

def remove_last():
    collection.remove_last_movie()
    show_output("Last movie removed.")

def remove_position():
    try:
        pos = int(entry_position.get())
        collection.remove_movie_position(pos)
        show_output(f"Movie at position {pos} removed.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_movie():
    try:
        movie = int(entry_movie.get())

        if collection.search_movie(movie):
            show_output("Movie found in collection.")
        else:
            show_output("Movie not found.")
    except:
        messagebox.showerror("Error", "Enter a valid Movie ID.")

def total_movies():
    show_output(f"Total Movies: {collection.total_movies()}")

root = tk.Tk()
root.title("Movie Collection Manager - Om Wala S119")
root.geometry("900x700")
root.configure(bg="#DCEEFF")

title = tk.Label(
    root,
    text="Movie Collection Manager",
    bg="#1565C0",
    fg="white",
    font=("Arial",20,"bold"),
    pady=10
)
title.pack(fill="x")

frame = tk.Frame(root,bg="#DCEEFF")
frame.pack(pady=10)

tk.Label(frame,text="Movie ID",bg="#DCEEFF",font=("Arial",11,"bold")).grid(row=0,column=0,padx=10,pady=5)
entry_movie = tk.Entry(frame,font=("Arial",11),width=15)
entry_movie.grid(row=0,column=1)

tk.Label(frame,text="Position",bg="#DCEEFF",font=("Arial",11,"bold")).grid(row=0,column=2,padx=10)
entry_position = tk.Entry(frame,font=("Arial",11),width=15)
entry_position.grid(row=0,column=3)

button_frame = tk.Frame(root,bg="#DCEEFF")
button_frame.pack(pady=10)

tk.Button(button_frame,text="Add Front",width=18,bg="#1976D2",fg="white",font=("Arial",10,"bold"),command=add_front).grid(row=0,column=0,padx=5,pady=5)

tk.Button(button_frame,text="Add End",width=18,bg="#1976D2",fg="white",font=("Arial",10,"bold"),command=add_end).grid(row=0,column=1,padx=5,pady=5)

tk.Button(button_frame,text="Add Position",width=18,bg="#1976D2",fg="white",font=("Arial",10,"bold"),command=add_position).grid(row=0,column=2,padx=5,pady=5)

tk.Button(button_frame,text="Remove First",width=18,bg="#1976D2",fg="white",font=("Arial",10,"bold"),command=remove_first).grid(row=1,column=0,padx=5,pady=5)

tk.Button(button_frame,text="Remove Last",width=18,bg="#1976D2",fg="white",font=("Arial",10,"bold"),command=remove_last).grid(row=1,column=1,padx=5,pady=5)

tk.Button(button_frame,text="Remove Position",width=18,bg="#1976D2",fg="white",font=("Arial",10,"bold"),command=remove_position).grid(row=1,column=2,padx=5,pady=5)

tk.Button(button_frame,text="Search Movie",width=18,bg="#1976D2",fg="white",font=("Arial",10,"bold"),command=search_movie).grid(row=2,column=0,padx=5,pady=5)

tk.Button(button_frame,text="Total Movies",width=18,bg="#1976D2",fg="white",font=("Arial",10,"bold"),command=total_movies).grid(row=2,column=1,padx=5,pady=5)

tk.Button(button_frame,text="Display Collection",width=18,bg="#1976D2",fg="white",font=("Arial",10,"bold"),command=show_output).grid(row=2,column=2,padx=5,pady=5)

output = scrolledtext.ScrolledText(root,width=100,height=22,font=("Consolas",11))
output.pack(padx=10,pady=10)

show_output()

root.mainloop()
