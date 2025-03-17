from tkinter import *

# Create the GUI
root = Tk()
root.title("Cat Descriptions")

# Define the lists of verbs and adjectives
verbs = ["trip over", "pick up", "sneeze at", "feed", "pat", "put out"]
adjectives = ["cute", "wailing", "annoying", "furry", "purring", "hungry"]

# Function to update the label
def update_label():
    verb = verb_var.get()
    adjective = adjective_var.get()
    sentence = f"I am going to {verb} the {adjective} cat."
    label.config(text=sentence)

# Create the verb and adjective sections using grid
root.grid_columnconfigure(0, weight=1)  # To make sure the columns stretch equally

# Create the frame for the verbs
verb_frame = Frame(root)
verb_frame.grid(row=0, column=0, padx=10, pady=10)

# Create the Radiobuttons for the verbs
verb_var = StringVar()
verb_var.set(verbs[0])
for verb in verbs:
    verb_button = Radiobutton(verb_frame, text=verb, variable=verb_var, value=verb, width=12, bg="white", anchor=W, command=update_label)
    verb_button.pack(anchor=W)

# Create the frame for the adjectives
adjective_frame = Frame(root)
adjective_frame.grid(row=0, column=1, padx=10, pady=10)

# Create the Radiobuttons for the adjectives
adjective_var = StringVar()
adjective_var.set(adjectives[0])
for adjective in adjectives:
    adjective_button = Radiobutton(adjective_frame, text=adjective, variable=adjective_var, value=adjective, width=12, bg="grey", anchor=E, command=update_label)
    adjective_button.pack(anchor=W)

# Create the label under the verb and adjective sections and center it
label = Label(root, text="")
label.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
