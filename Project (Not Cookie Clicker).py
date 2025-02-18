import tkinter as tk

window = tk.Tk()
window.title('Not Cookie Clicker')
window.geometry("300x200+10+10")

label = tk.Label(window, text="Enter Your Username", fg='red', font=("Helvetica", 16))
label.place(x=60, y=50)

txtfld = tk.Entry(window, text="", bd=5)
txtfld.place(x=80, y=150)

def button_clicked():
    print("Button clicked!")

button = tk.Button(window, 
                   text="Click Me", 
                   command = button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button.pack(padx=20, pady=20)

window.mainloop()