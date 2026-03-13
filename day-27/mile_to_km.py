from tkinter import *

def Calculate():
    miles = float(miles_input.get())
    km = miles * 1.60934
    result.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(500, 300)
window.config(padx=20, pady=20)

miles_input = Entry()

# Label
equal = Label(text="is equal to", font=("Arial", 25, "bold"))
equal.grid(row=1, column=0)

miles = Label(text="Miles", font=("Arial", 25, "bold"))
miles.grid(row=0, column=2)

km = Label(text="Km", font=("Arial", 25, "bold"))
km.grid(row=1, column=2)

result = Label(text="0", font=("Arial", 25, "bold"))
result.grid(row=1, column=1)

# Button
calculate = Button(text="Calculate", command=Calculate)
calculate.grid(row=2, column=1)

#Entry Miles
miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

window.mainloop()