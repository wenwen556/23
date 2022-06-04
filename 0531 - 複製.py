import tkinter as tk

import tkinter.ttk as ttk

def end():
    window_3 = tk.Tk()
    window_3.title('付款')
    window_3.geometry('600x600')

    label_9 = tk.Label(window_3, text='請線上支付保費或至超商繳費。付款成功後保單即成立。')
    label_9.place(x=100,y=100)
        

def start():
    global entry_1
    global entry_2
    global entry_3
    global entry_4
    window = tk.Tk()
    window.title('加保')
    window.geometry('600x600')

    label_1 = tk.Label(window, text='請提供您的姓名:')
    label_1.grid(row=0, column=0)
        
    entry_1 = tk.Entry(window)
       
    entry_1.grid(row=0, column=1)
    label_2 = tk.Label(window, text='請提供您伴侶的姓名:')
    label_2.grid(row=2, column=0)
    entry_2 = tk.Entry(window)

    entry_2.grid(row=2, column=1)
        
    label_3 = tk.Label(window, text='請提供您的電話號碼:')
    label_3.grid(row=3, column=0)
    entry_3 = tk.Entry(window)

    entry_3.grid(row=3, column=1)
    label_4 = tk.Label(window, text='請提供您伴侶的電話號碼:')
    label_4.grid(row=4, column=0)
    entry_4 = tk.Entry(window)
     
    entry_4.grid(row=4, column=1)
    La_3 = tk.Label(window, text='戀愛險總保費為新台幣2,400元，每個月須繳納新台幣200元，連續繳納一年。若您於投保後第三~五年內結婚，即可申請新台幣20,000元的理賠。')
    La_3.place(x=100, y=150)
    button_3 = tk.Button(window,text = '確定加保', command = get_data)  
    button_3.place(x=100,y=200)
    window.mainloop()


def insurance():
    window = tk.Tk()
    window.title('戀愛險')
    window.geometry('600x600')
    La_2 = tk.Label(window, text='請問過去一年內您是否投保過本公司的「戀愛險」？')
    La_2.place(x=100, y=100)
        
    button_3 = tk.Button(window,         
                       text = '是',  
                       command = command_1) 
    button_3.place(x=150,y=150)
    button_2 = tk.Button(window,text = '否',command = start)
    button_2.place(x=200,y=150)

    window.mainloop()
def command_1():
    window_1 = tk.Tk()
    window_1.title('加保')
    window_1.geometry('600x600')
    labelText=tk.Label(window_1, text='您已投保過，謝謝!')
    labelText.place(x=150,y=100)



def get_data():

    
    window = tk.Tk()
    window.title('確認加保')
    window.geometry('600x600')
    label_11 = tk.Label(window, text='<戀愛險保單申請>')
    label_11.grid(row=0, column=0)
    label_12 = tk.Label(window, text='保戶姓名:')
    label_12.grid(row=1, column=0)
    label_13 = tk.Label(window, text=entry_1.get())
    label_13.grid(row=1, column=3)
    label_14 = tk.Label(window, text='保戶手機號碼:')
    label_14.grid(row=2, column=0)
    label_15 = tk.Label(window, text=entry_3.get())
    label_15.grid(row=2, column=3)
    label_16 = tk.Label(window, text='伴侶姓名:')
    label_16.grid(row=3, column=0)
    label_17 = tk.Label(window, text=entry_2.get())
    label_17.grid(row=3, column=3)
    label_18 = tk.Label(window, text='伴侶手機號碼:')
    label_18.grid(row=4, column=0)
    label_19 = tk.Label(window, text=entry_4.get())
    label_19.grid(row=4, column=3)
        
        
        
    button_4 = tk.Button(window,
                       text = '確認資料正確',  
                       command = end)
    button_4.place(x=100, y=200)
    window.mainloop()


        

window_2 = tk.Tk()
window_2.title('戀愛險')
window_2.geometry("300x100+250+150")
La_1 = tk.Label(window_2, text='為您們的愛情買一個保障。只需每個月投入一點點，讓我們為您們的感情保駕護航。「戀愛險」現特別擴大了保險範圍，即使您和您的伴侶是網戀關係，也可以申請投保，為您的愛情保一個心安。若選擇投保，請按下「投保」，並回答我們幾題問題，就可以輕鬆投保！')
La_1.place(x=100, y=230)
button = tk.Button(window_2, text = '投保',  
                       command = insurance)


button.pack()
window_2.mainloop()








