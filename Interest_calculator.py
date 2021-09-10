from tkinter import *


def clear_all():
    principle_field.delete(0, END)
    rate_field.delete(0, END)
    time_field.delete(0, END)
    simple_field.delete(0, END)   # result

    principle_field.focus_set()


def calculate_si():
    principle = int(principle_field.get())

    rate = float(rate_field.get())

    time = int(time_field.get())

    # Calculates compound interest
    SI = (principle * rate * time) / 100

    # insert method inserting the
    # value in the text entry box.
    simple_field.delete(0, END)
    simple_field.insert(10, SI)


if __name__ == "__main__":
    # Create a GUI window
    root = Tk()

    # Set the background colour of GUI window
    root.configure(background='grey')

    # Set the configuration of GUI window
    root.geometry("400x250")

    # set the name of tkinter GUI window
    root.title("Simple Interest Calculator")

    # Create a Principle Amount : label
    label1 = Label(root, text="Principle Amount(Rs) : ", fg='black', bg='white')

    # Create a Rate : label
    label2 = Label(root, text="Rate(%) : ",fg='black', bg='white')

    # Create a Time : label
    label3 = Label(root, text="Time(years) : ",fg='black', bg='white')

    # Create a Compound Interest : label
    label4 = Label(root, text="Simple Interest : ",fg='black', bg='white')

    label1.grid(row=1, column=0, padx=10, pady=10)
    label2.grid(row=2, column=0, padx=10, pady=10)
    label3.grid(row=3, column=0, padx=10, pady=10)
    label4.grid(row=5, column=0, padx=10, pady=10)

    principle_field = Entry(root)
    rate_field = Entry(root)
    time_field = Entry(root)
    simple_field = Entry(root)

    principle_field.grid(row=1, column=1, padx=10, pady=10)
    rate_field.grid(row=2, column=1, padx=10, pady=10)
    time_field.grid(row=3, column=1, padx=10, pady=10)
    simple_field.grid(row=5, column=1, padx=10, pady=10)

    button1 = Button(root, text="Submit", bg="white", fg="black", activebackground="grey", command=calculate_si)

    button2 = Button(root, text="Clear", bg="white", fg="black",activebackground="grey", command=clear_all)

    button1.grid(row=4, column=1, pady=10)
    button2.grid(row=6, column=1, pady=10)

    root.mainloop()