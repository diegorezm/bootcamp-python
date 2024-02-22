import tkinter as tk

root = tk.Tk()

def on_submit():
    miles = float(miles_var.get())  # Convert miles_var value to float
    km = miles * 1.609  # Convert miles to kilometers
    km_var.set(str(km))

root.wm_geometry("500x400")
root.wm_title("conversion")

miles_var = tk.StringVar()
km_var = tk.StringVar()

miles_label = tk.Label(root, text="miles:").place(x=100,y=60)
miles_input = tk.Entry(root, width=30, textvariable=miles_var).place(x=140, y=60)

km_label = tk.Label(root, text="km:").place(x=100,y=90)
km_input = tk.Entry(root, width=30,textvariable=km_var, state="readonly", bg="#000" ,fg="#fff").place(x=140, y=90)

km_input = tk.Entry(root, width=30, textvariable=km_var, state='readonly', bg="#000", fg="#fff")

submit_btn = tk.Button(root, text="submit", width=20, command=on_submit).place(x=140,y=120)

root.mainloop()
