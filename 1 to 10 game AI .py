from tkinter import *
from tkinter import ttk, messagebox
import time
import random
import threading
from tkinter import PhotoImage

def center_window(window, width, height):
    root.update_idletasks()
    x = root.winfo_x() + (root.winfo_width() // 2) - (width // 2)
    y = root.winfo_y() + (root.winfo_height() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

#check numbers
def check_guess():
    try:
        user_number= int(entry.get())
        #only user number less than 100
        if user_number<=100:
            random_number = random.randint(1,100)
            print(random_number)
            def process():
                steps = [
                    "Analyzing Brainwaves...",
                    "Scanning Memories...",
                    "Calculating Probabilities...",
                    "Decoding Thoughts...",
                ]

                progress_win =Toplevel(root)
                progress_win.title("Finding Guess Number")
                center_window(progress_win, 350, 120)
                progress_win.transient(root)
                progress_win.grab_set()

                progress_label =Label(progress_win, text="Starting mind reading...", font=("Arial", 11))
                progress_label.pack(pady=10)

                progress =ttk.Progressbar(progress_win, orient=HORIZONTAL, length=300, mode='determinate')
                progress.pack(pady=10)
                for i in range(100):
                    time.sleep(0.05)
                    progress["value"] = i + 1
                    if i % 25 == 0 and i // 25 < len(steps):
                        progress_label.config(text=steps[i // 25])
                    progress_win.update()

                progress_win.destroy()
                if user_number == random_number:
                    if not messagebox.askretrycancel("Result", "You win!"):
                        root.destroy()
                    else:
                        entry.delete(0,END)
                        entry.focus()
                else:
                    # my code
                    messagebox.showinfo("Result",f"Try again!\n*************************\nYour guess : {user_number}\nRandom number : {random_number}" )
                    entry.delete(0,END)
                    entry.focus()

            threading.Thread(target=process).start()
        else:
            messagebox.showwarning("Invalid Input", "Please enter a number less than 100 !!")
            entry.delete(0,END)
            entry.focus()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number !!")
        entry.delete(0,END)
        entry.focus()
        
 
# Window 
root = Tk()
root.title("Guessing Game")
root.geometry("500x600")
#img=Image.open("IMG_3233.png")
#tk_img=ImageTK.photoImage(img)
#img=PhotoImage(file="IMG_3233.png")
#root.configure(bg="orange")
root.iconbitmap(r"C:\Users\saji\Desktop\123_number_icon.ico")
#root.resizable(width=False,height=False)

#background image
Image_path=PhotoImage(file=r"C:\Users\saji\Desktop\IMG_3233.png")
bg_image=Label(root,image=Image_path)
bg_image.place(relheight=1,relwidth=1)


# Label
label = Label(root, text="Guess any Random number 0 to 100", font=("Georgia",14))
label.pack(padx=100,pady=90)


# Entry
entry = Entry(root, width=10, justify='center', font=("Arial", 20))
entry.pack(pady=0.1)

# Button
button = Button(root, text="Goooo!", command=check_guess, bg="orange", font=("Arial", 12, "bold"))
button.pack(pady=50)

root.mainloop()