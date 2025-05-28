import tkinter as tk

'''
pack() packs items out in order based on side... one at a time.
place() allows for precise positioning based on x and y value.

'''

window = tk.Tk()
window.title("my first gui")
window.minsize(width=600, height=500)

#label
label = tk.Label(text="this is a label", font=("Arial",24))
label.grid(row=0, column=0, columnspan=3)
label.config(foreground="#ccc", background="#333", padx=10, pady= 5, width=30)

#button
def click_button():
    input_text = input.get()
    label["text"]=input_text

button_1 = tk.Button(text="1", font=("Arial",18), command=click_button)
button_1.grid(row=1, column=0, sticky="WE")
button_2 = tk.Button(text="2", font=("Arial",18), command=click_button)
button_2.grid(row=1, column=1, sticky="WE")
button_3 = tk.Button(text="3", font=("Arial",18), command=click_button)
button_3.grid(row=1, column=2, sticky="WE")
button_4 = tk.Button(text="4", font=("Arial",18), command=click_button)
button_4.grid(row=2, column=0, columnspan=3, sticky="WE")
button_5 = tk.Button(text="5", font=("Arial",18), command=click_button)
button_5.grid(row=3, column=0, sticky="WE")
button_6 = tk.Button(text="6", font=("Arial",18), command=click_button)
button_6.grid(row=3, column=2, sticky="WE")
button_7 = tk.Button(text="7", font=("Arial",18), command=click_button)
button_7.grid(row=4, column=0)

#entry
input = tk.Entry()
input.grid(row=5, column= 2, sticky="W") # place = precise positioning.


window.mainloop()