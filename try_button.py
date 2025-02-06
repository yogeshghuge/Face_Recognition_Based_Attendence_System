import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
root.tk_setPalette("black")

btn_frame = tk.Frame(root)

canvas = tk.Canvas(btn_frame, height=100, width=100)
canvas.pack()

btn_frame.pack(side=tk.LEFT)


btn_frame1 = tk.Frame(root)

canvas1 = tk.Canvas(btn_frame1, height=100, width=100)
canvas1.pack()

btn_frame1.pack(side=tk.LEFT, padx=10)



def round_rectangle(obj, x1, y1, x2, y2, r=25, **kwargs):    
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    return obj.create_polygon(points, **kwargs, smooth=True)

round_rectangle(canvas, 5, 50, 100, 100, 25, fill="white")

round_rectangle(canvas1, 5, 50, 100, 100, 25, fill="white")

btn_1 = tk.Button(btn_frame, text="Start", font=("Bold", 15),
bg="white", fg="black", bd=0)

btn_1.place(x=10, y=57, width=80)



btn_2 = tk.Button(btn_frame1, text="Exit", font=("Bold", 15),
bg="white", fg="black", bd=0)

btn_2.place(x=10, y=57, width=80)


root.mainloop()