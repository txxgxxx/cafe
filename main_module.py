
def switch_frame(open_frame, close_frame):
    close_frame.destroy()
    Frame2 = open_frame()
    Frame2.order_frame.pack()

def cafe():
    import tkinter as tk
    total = {'price': 0}
    americano = {'name': 'americano', 'price': 3000, 'kind': 'coffee', 'num': 0}
    latte = {'name': 'latte', 'price': 3500, 'kind': 'coffee', 'num': 0}

    # def total_button():
    #     total_price = total['price']
    #     tk.Label(total_frame, text=("총 %d원" % total_price), font=('Helvetica', 18, 'bold')).pack()
    #     tk.Button(total_frame, text="주문해주셔서 감사합니다.", font=('Helvetica', 18, 'bold'),
    #               command=lambda: window.quit()).pack()

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
