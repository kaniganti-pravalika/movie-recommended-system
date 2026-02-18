import tkinter as tk
from tkinter import ttk
import pickle

movie = pickle.load(open("movie_list.pkl", "rb"))
movie_list = movie['title'].astype(str).tolist()

similarity = pickle.load(open("movie_similarity.pkl", "rb"))

def recommendation(movie_name):
    index = movie[movie.title == movie_name].index[0]
    distance = list(enumerate(similarity[index]))
    distance = sorted(distance, key=lambda x:x[1], reverse=True)
    recommended_movie = []
    for i in distance[:10]:
        recommended_movie.append(movie.iloc[i[0]].title)
    return recommended_movie

def show_recommend():
    result_list.delete(0, tk.END)   
    recommended = recommendation(combo.get())
    for idx, movie in enumerate(recommended, start=1):
        result_list.insert(tk.END, f"{idx}. {movie}")

root = tk.Tk()
root.geometry("500x450")

tk.Label(root, text="Movie Recommendatin System",
         font=('Arial', 18, 'bold')).pack(pady=15)

tk.Label(root, text="Select Movie:",
         font=('Arial', 12)).pack(pady=5)

combo = ttk.Combobox(root, values=movie_list, width=50)
combo.pack()

btn = tk.Button(root, text="Show Recommend",
                command=show_recommend,
                font=('Arial', 12, 'bold'),
                bg='green', fg='white')
btn.pack(pady=10)

tk.Label(root, text='Top 10 Recommended Movie',
         font=('Arial', 14, "bold")).pack(pady=15)

result_list = tk.Listbox(root, width=60)
result_list.pack()
root.mainloop()