import tkinter as tk

def calc_kilos ():
    miles = miles_input.get()
    if miles.isdigit():
        response_label["text"] = f"is equal to {round(int(miles) * 1.609,1)} Km."
    else:
        response_label["text"] = ""

window = tk.Tk()
window.title("Mile to Kilometer Converter")
window.geometry("300x100")


miles_input = tk.Entry()
miles_label = tk.Label(text="miles")
response_label = tk.Label(text="")
button = tk.Button(text="calculate", command=calc_kilos)

miles_input.grid(row=0, column=0, sticky="WE", padx=5)
miles_label.grid(row=0, column=1, sticky="W")
response_label.grid(row=1, column=0, columnspan=2, sticky="W", padx=5)
button.grid(row=2,column=1)

window.mainloop()