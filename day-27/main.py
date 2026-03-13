import tkinter

def button_clicked():
    #  my_label.config(text="You clicked me")
    my_label.config(text=input.get())
    print("Clicked")

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 25, "bold"))
my_label.config(text="New text")
my_label.grid(row=0, column=0)

# Button
button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(row=0, column=2)

#Entry
input = tkinter.Entry(width=10)
print(input.get())
input.grid(row=2, column=3)

window.mainloop()