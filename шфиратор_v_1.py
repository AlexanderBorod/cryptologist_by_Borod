import tkinter as tk 
from tkinter import END, Button, Label, messagebox
from tkinter.font import NORMAL         
import tkinter.filedialog as fd
from tkinter.tix import Y_REGION
from turtle import st
from idlelib.tooltip import Hovertip        


def create_chipher():
    # check that our cipher consists of numbers only
    try:                
        int(Key_shifr.get()) 
    except:
        messagebox.showinfo("Внимание", 'Шифр должен состоять только из цифр')
    # stop the code if the cipher is less than 2 characters. (because then the encryption is insecure)
    if len(Key_shifr.get()) < 4:
        messagebox.showinfo("Внимание", 'Шифр должен состоять не менее, чеми из 4 знаков')   
    else:
        code_cipher = Key_shifr.get()
        password_word = text.get("1.0", "end")
    
        if list(password_word)[-1] == '\n': # and all because with the list() function, if the length of the encrypted part == the length of the cipher_key, then / n is added at the end
            password_word = list(password_word)
            password_word = password_word[:-1]
    
        print('Начинается шифровка')
        
        code_cipher = list(code_cipher)
        for i in range(len(code_cipher)):
        # 0 does not change the original text and creates errors if it is the first in the cipher, so we will replace it simply so as not to disturb the user
            if code_cipher[i] == '0': 
                code_cipher[i] = '2'
        code_cipher = ''.join(code_cipher)
        #the cipher must consist of even numbers (1 number indicates a change in the original number, and 2 number indicates what action we are performing. \
        # Because, if necessary, we remove the last number if the code is odd
        if len(code_cipher) % 2 != 0:
            code_cipher = code_cipher[:len(code_cipher)-1]
            code_cipher = list(code_cipher)
        else:
            code_cipher = list(code_cipher)
        
        password_word_cipher = list(password_word)
        
        for i in range(len(password_word_cipher)):
            password_word_cipher[i] = ord(password_word_cipher[i])
        
        code_cipher_step = 0
        
        our_chipher = []
        #the source code is divided into a list.\
        # Each element is converted to Decimal from ASCII. \
        # Then add or multiply. If the total is greater or less than ASCII allows us, then we subtract 50 until we get into the ASCII diapochon. \
        # After we put "Jer" if it was taken away and the sign how many times was taken away, and "All" if it was added
        for i in range(len(password_word_cipher)):
            step_it = 0
            if code_cipher_step == len(code_cipher):
                code_cipher_step = 0
            
            if int(code_cipher[code_cipher_step]) % 2 == 0:
                time_num = int(password_word_cipher[i]) + int(code_cipher[code_cipher_step+1])   
                if time_num > 126:
                    while time_num > 126:
                        time_num -= 50
                        step_it += 1
                    our_chipher.append('Jer')
                    our_chipher.append(str(step_it))
                elif time_num <33:
                    step_it = 0
                    while time_num < 33:
                        time_num += 50
                        step_it -= 1
                    our_chipher.append('All')
                    our_chipher.append(str(step_it))
        
                our_chipher.append(chr(int(password_word_cipher[i]) + int(code_cipher[code_cipher_step+1]) - step_it * 50))
                code_cipher_step += 2
        
            elif int(code_cipher[code_cipher_step]) % 2 == 1:
                time_num = int(password_word_cipher[i]) * int(code_cipher[code_cipher_step+1])
                if time_num > 126:
                    while time_num > 126:
                        time_num -= 50
                        step_it += 1
                    our_chipher.append('Jer')
                    our_chipher.append(str(step_it))
                elif time_num < 33:
                    while time_num < 33:
                        time_num += 50
                        step_it -= 1
                    our_chipher.append('All')
                    our_chipher.append(str(step_it))
                 # we translating the text from decimal to Char
                our_chipher.append(chr(int(password_word_cipher[i]) * int(code_cipher[code_cipher_step+1]) - step_it * 50))
                code_cipher_step += 2
    
        print('Шифровка окончена')  
        
        text2.insert(0.1, ' '.join(our_chipher))


def de_cipher():
    #all actions are similar to create_chipher(), only + becomes -, and * - /
    print('Начинается дешифровка')
    code_cipher = str(Key_shifr.get())
    our_chipher = (text.get("1.0", "end")).split()

    print(our_chipher)
    
    if len(code_cipher) % 2 != 0:
        code_cipher = code_cipher[:len(code_cipher)-1]
        code_cipher = list(code_cipher)
    else:
        code_cipher = list(code_cipher)
    
    code_cipher = list(code_cipher)
    for i in range(len(code_cipher)):
        if code_cipher[i] == '0':
            code_cipher[i] = '2'
    code_cipher = ''.join(code_cipher)
    
    our_chipher_translate_step_1st = []
    
    step = 0
    while step < len(our_chipher):
        if our_chipher[step] == 'Jer':
            num = int(ord(our_chipher[step+2])) + 50 * int(our_chipher[step+1])
            step += 3
        elif our_chipher[step] == 'All':
            num = int(ord(our_chipher[step+2])) - 50 * int(our_chipher[step+1])
            step += 3
        else:
            num = ord(our_chipher[step])
            step += 1
        our_chipher_translate_step_1st.append(num)
    
    code_cipher_step = 0
    for i in range(len(our_chipher_translate_step_1st)):
        if code_cipher_step == len(code_cipher):
            code_cipher_step = 0
    
        if int(code_cipher[code_cipher_step]) % 2 == 0:
            our_chipher_translate_step_1st[i] = chr(int(our_chipher_translate_step_1st[i] - int(code_cipher[code_cipher_step+1])))
            code_cipher_step += 2
        elif int(code_cipher[code_cipher_step]) % 2 == 1:
            our_chipher_translate_step_1st[i] = chr(int(our_chipher_translate_step_1st[i] / int(code_cipher[code_cipher_step+1])))
            code_cipher_step += 2

    print('Дешифровка окончена')
    text2.insert(0.1, ''.join(our_chipher_translate_step_1st))





#=============================================================

def copy_to_text():
    win.clipboard_clear()  # Очистить буфер обмена
    win.clipboard_append(text.get('1.0', tk.END).rstrip())

def clear_text():                          
    text.delete("1.0","end")
    print( 'Очищаем поле' )

def paste():
   win.clipboard_clear()
   win.clipboard_append(text)
   text.text = win.selection_get(selection='CLIPBOARD')


def copy_to_text2():
    win.clipboard_clear()  # Очистить буфер обмена
    win.clipboard_append(text2.get('1.0', tk.END).rstrip())

def clear_text2():                          
    text2.delete("1.0","end")
    print( 'Очищаем поле' )   




win = tk.Tk()
win.geometry( f'710x450+150+200' )
#photo = tk.PhotoImage(file='Icon.png')
#win.iconphoto(False, photo)
win['bg'] = '#9ba29b'
win.title('What is this')
win.resizable(True, True)


text = tk.Text(win, width=1, height=1, wrap='word')
text.grid(row=1, column=0,  columnspan=3, padx=1, pady=1, stick='nwes', rowspan=4)

scroll = tk.Scrollbar(win, command=text.yview)
scroll.grid(row = 1, column=3, stick='snw', padx = 0, pady = 0, columnspan=1, rowspan=4) 
text.config(yscrollcommand=scroll.set)


#btn_past_text = Button(win, text = 'Past', font=('PFDINDISPLAYPRO', 13), bd = 4, command=paste, bg = '#ffffff', 
#                       activebackground ='#d7db00').grid(row = 6, column=0, stick='we', padx = 25, pady = 5, columnspan=1) 
btn_del_text = Button(win, text = 'Clear', font=('PFDINDISPLAYPRO', 13), bd = 4, command=clear_text, bg = '#ffffff', 
                       activebackground ='#d7db00').grid(row = 5, column=0, stick='we', padx = 25, pady = 5, columnspan=1) 
btn_save_text = Button(win, text = 'Copy', font=('PFDINDISPLAYPRO', 13), bd = 4, command=copy_to_text, bg = '#ffffff',
                       activebackground ='#d7db00').grid(row = 5, column=1, stick='w', padx = 1, pady = 5, columnspan=1) 

info_key = tk.Label(win, font='PFDINDISPLAYPRO 10', text='Укажите шифр. \nВнимание. Шифр должен состоять из цифр и быть более двух знаков', 
                    bg='#9ba29b', wraplength=200).grid( row=1, column=4, stick='we', padx = 2, pady = 5, columnspan=2)

Key_shifr = tk.Entry(win, font = 'PFDINDISPLAYPRO 10', width=(2), justify=tk.CENTER, bd = 4)
Key_shifr.grid( row=2, column=4, stick='we', padx = 2, pady = 5, columnspan=2)
Key_shifr.insert(0, '12345678')


Button_shifr = tk.Button(win, text = 'Зашифровать', font=('PFDINDISPLAYPRO', 13), bd = 4, bg = '#ffffff', command=create_chipher, 
                       activebackground ='#d7db00').grid(row = 3, column=4, stick='ew', padx = 1, pady = 5, columnspan=2)


Button_shifr = tk.Button(win, text = 'Расшифровать', font=('PFDINDISPLAYPRO', 13), bd = 4, bg = '#ffffff', command=de_cipher,
                       activebackground ='#d7db00').grid(row = 4, column=4, stick='ew', padx = 1, pady = 5, columnspan=2)


text2 = tk.Text(win, width=20, height=1, wrap='word')
text2.grid(row=1, column=7,  columnspan=3, padx=1, pady=1, stick='nwes', rowspan=4)

scroll2 = tk.Scrollbar(win, command=text2.yview)
scroll2.grid(row = 1, column=10, stick='snw', padx = 0, pady = 0, columnspan=1, rowspan=4) 
text2.config(yscrollcommand=scroll2.set)

btn_del_text2 = Button(win, text = 'Clear', font=('PFDINDISPLAYPRO', 13), bd = 4, command=clear_text2, bg = '#ffffff', 
                       activebackground ='#d7db00').grid(row = 5, column=7, stick='we', padx = 25, pady = 5, columnspan=1) 
btn_save_text2 = Button(win, text = 'Copy', font=('PFDINDISPLAYPRO', 13), bd = 4, command=copy_to_text2, bg = '#ffffff',
                       activebackground ='#d7db00').grid(row = 5, column=8, stick='w', padx = 1, pady = 5, columnspan=1) 







win.grid_rowconfigure(0, minsize='40')
win.grid_rowconfigure(1, minsize='40')
win.grid_rowconfigure(2, minsize='40')
win.grid_rowconfigure(3, minsize='40')
win.grid_rowconfigure(4, minsize='40')
win.grid_rowconfigure(5, minsize='40')



win.grid_columnconfigure(0, minsize='40')
win.grid_columnconfigure(1, minsize='40')
win.grid_columnconfigure(2, minsize='40')
win.grid_columnconfigure(3, minsize='40')
win.grid_columnconfigure(4, minsize='40')
win.grid_columnconfigure(5, minsize='40')
win.grid_columnconfigure(6, minsize='40')
win.grid_columnconfigure(7, minsize='40')
win.grid_columnconfigure(8, minsize='40')
win.grid_columnconfigure(9, minsize='40')
win.grid_columnconfigure(10, minsize='40')





win.mainloop()
