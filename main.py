from tkinter import *

# Creating window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=100, width=200)
window.config(padx=20, pady=20)



#Creating entry box
entry = Entry()
entry.insert(END, string="0")
entry.grid(column=1, row=0)
entry.config(width=10)


#Creating label
calculate_label = Label(text="0")
calculate_label.grid(column=1, row=1)


# miles to km conversion
def miles_to_km():
    user_input = entry.get()
    miles_km_formula = float(user_input)*1.6
    calculate_label.config(text=f"{miles_km_formula}")


# creating Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# All the extra labels
equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

miles_label = Label(text= "Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


window.mainloop()
