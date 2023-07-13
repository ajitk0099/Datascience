import tkinter as tk

# Define initial variables
num_wickets = 10
num_reviews = 2

# Define function to handle review requests
def handle_review():
    global num_reviews, num_wickets
    if num_reviews > 0:
        result_label.config(text="Review successful.")
        num_reviews -= 1
    else:
        result_label.config(text="No reviews remaining.")
    num_wickets -= 1
    wickets_label.config(text="Remaining wickets: {}".format(num_wickets))
    reviews_label.config(text="Remaining reviews: {}".format(num_reviews))

# Define GUI
root = tk.Tk()
root.title("Cricket DRS")

wickets_label = tk.Label(root, text="Remaining wickets: {}".format(num_wickets))
wickets_label.pack()

reviews_label = tk.Label(root, text="Remaining reviews: {}".format(num_reviews))
reviews_label.pack()

button = tk.Button(root, text="Take wicket and request review", command=handle_review)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
