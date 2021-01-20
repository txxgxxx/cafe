import tkinter as tk


window = tk.Tk()
# 창 설정
window.title("Cafe")
window.geometry("640x400+100+100")
window.resizable(False, False)


welcome_frame = tk.Frame(window)
order_frame = tk.Frame(window)
total_frame = tk.Frame(window)


def switch_frame(open_frame, close_frame):
    close_frame.destroy()
    open_frame.pack()


welcome_frame.pack()

tk.Label(welcome_frame, text='Welcome', font=('Helvetica', 18, 'bold')).pack()
tk.Button(welcome_frame, text='Go to order', font=('Helvetica', 18, 'bold'), command=lambda: switch_frame(order_frame, welcome_frame)).pack()


tk.Label(order_frame, text='Order', font=('Helvetica', 18, 'bold')).pack(side='top')

total = {'price': 0}
americano = {'name': 'americano', 'price': 3000, 'kind': 'coffee', 'num': 0}
latte = {'name': 'latte', 'price': 3500, 'kind': 'coffee', 'num': 0}


def total_button():
    total_price = total['price']
    tk.Label(total_frame, text=("총 %d원" % total_price), font=('Helvetica', 18, 'bold')).pack()
    tk.Button(total_frame, text="주문해주셔서 감사합니다.", font=('Helvetica', 18, 'bold'), command=lambda: window.quit()).pack()


def order(menu):
    global total_order
    global menu_1
    global menu_2
    if menu == americano:
        if total['price'] < 0:
            total['price'] = 0
            total_order.config(text="총 %d원" % total['price'])
        total['price'] += americano['price']
        americano['num'] += 1
        menu_1.config(text=americano['name'] + " " + str(americano['num']))
        total_order.config(text="총 %d원" % total['price'])

    elif menu == latte:
        if total['price'] < 0:
            total['price'] = 0
            total_order.config(text="총 %d원" % total['price'])
        total['price'] += latte['price']
        latte['num'] += 1
        menu_2.config(text=latte['name'] + " " + str(latte['num']))
        total_order.config(text="총 %d원" % total['price'])
        print("메뉴가 라떼일때 성공했습니다.")

def order_cancel(cancel):
    if cancel == americano:
        if total['price'] < americano['price']:
            total_order.config(text="총 %d원" % total['price'])
        elif americano['num'] >= 1:
            total['price'] -= 3000
            americano['num'] -= 1
            menu_1.config(text=americano['name'] + " " + str(americano['num']))
            total_order.config(text="총 %d원" % total['price'])
    elif cancel == latte:
        if total['price'] < latte['price']:
            total_order.config(text="총 %d원" % total['price'])
        elif latte['num'] >= 1:
            total['price'] -= 3500
            latte['num'] -= 1
            menu_2.config(text=latte['name'] + " " + str(latte['num']))
            total_order.config(text="총 %d원" % total['price'])
        else:
            return


class Menu_Americano:
    def __init__(self, order_frame):
        self.americano_frame = tk.Frame(order_frame)
        self.americano_frame.pack(fill='x', anchor ='n')
        self.menu_button_1 = tk.Button(self.americano_frame, text=americano['name'], font=('Helvetica', 18, 'bold'),
                                       command=lambda: order(americano))
        self.menu_button_1.pack(side='left', padx=10, pady=10)
        self.cancel_button_1 = tk.Button(self.americano_frame, text='americano 취소', font=('Helvetica', 18, 'bold'),
                                         command=lambda: order_cancel(americano))
        self.cancel_button_1.pack(side='left', pady= 10)


class Menu_Latte:

    def __init__(self, order_frame):
        self.latte_frame = tk.Frame(order_frame)
        self.latte_frame.pack(fill='x', anchor ='n')
        self.menu_button_2 = tk.Button(self.latte_frame, text=latte['name'], font=('Helvetica', 18, 'bold'), command=lambda: order(latte))
        self.menu_button_2.pack(side='left', padx=10, pady=10)
        self.cancel_button_2 = tk.Button(self.latte_frame, text='latte 취소', font=('Helvetica', 18, 'bold'), command=lambda: order_cancel(latte))
        self.cancel_button_2.pack(side='left', padx=10, pady=10)


class User_order:
    def __init__(self, order_frame):
        self.user_frame = tk.Frame(order_frame)
        self.user_frame.pack(fill='x', anchor ='n')
        self.menu_1 = tk.Label(self.user_frame, text=americano['name'] + " " + str(americano['num']), font=('Helvetica', 18, 'bold'))
        self.menu_1.pack(side='left', padx=10, pady=10)
        self.menu_2 = tk.Label(self.user_frame, text=latte['name'] + " " + str(latte['num']), font=('Helvetica', 18, 'bold'))
        self.menu_2.pack(side='left', padx=10, pady=10)
        self.total_order = tk.Label(self.user_frame, text="총 %d원" % total['price'], font=('Helvetica', 18, 'bold'))
        self.total_order.pack(side='left', padx=10, pady=10)
        self.total_total = tk.Button(self.user_frame, text='결제', font=('Helvetica', 18, 'bold'),
                                     command=lambda: (total_button(), switch_frame(total_frame, order_frame))).pack(side='bottom')


container1 = Menu_Americano(order_frame)
container2 = Menu_Latte(order_frame)
container3 = User_order(order_frame)
window.mainloop()
