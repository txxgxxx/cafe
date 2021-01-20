import tkinter as tk
window = tk.Tk()
class First_Frame:
    import tkinter as tk
    def __init__ (self):
        window.title("First_Frame")
        from main_module import switch_frame
        self.original_frame = tk.Frame(window)
        self.original_frame.pack()

        self.tk.Label(self.original_frame, text='Welcome', font=('Helvetica', 18, 'bold')).pack()
        self.tk.Button(self.original_frame, text='Go to order', font=('Helvetica', 18, 'bold'),
                       command=lambda: switch_frame(Second_Frame, self.original_frame)).pack()


class Second_Frame:
    import tkinter as tk
    def __init__(self):
        window.title("Second_Frame")
        from main import Menu_Americano
        from main import Menu_Latte
        from main import User_order
        self.order_frame = tk.Frame(window)
        self.order_frame.pack()
        from main_module import switch_frame
        self.tk.Label(self.order_frame, text='Order', font=('Helvetica', 18, 'bold')).pack(side='top')
        container1 = self.Menu_Americano(self.order_frame)
        container2 = self.Menu_Latte(self.order_frame)
        container3 = self.User_order(self.order_frame)





Frame1 = First_Frame()



























window.geometry("640x400+100+100")
window.resizable(False, False)
window.mainloop()
