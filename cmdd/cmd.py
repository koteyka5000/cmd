import tkinter as tk
isImportedCommands = True
try:  import commands
except:
    print('===FATAL===\nНету файла с командами.\n \
Его нужно скачать и поместить в одну папку \
с этим файлом!')
    isImportedCommands = False

root = tk.Tk()
root.geometry('400x300')
root['bg'] = 'cyan'
root.title('Cmd')
root.resizable(False, False)

inputTextVar = tk.StringVar(root)

outputText = tk.Text(root, height=11, width=45, state=tk.DISABLED)
outputText.place(x=20, y=100)

inputText = tk.Entry(root, textvariable=inputTextVar, width=50)
inputText.place(x=20, y=30)


def run(command):  # Подготовка к обработке
    command = command.split()
    command, *args = command
    if not isImportedCommands:
        return '===FATAL===\nНету файла с командами.\n\
Его нужно скачать и поместить в одну папку \
с этим файлом!\nэх'
    return connect(command, *args)

def connect(command, *args):  # Обработка команд
    if command == 'cls':  cls()
    elif command == 'kill':  kill()
    else:
        try:  return eval(f'commands.{command}(*args)', )
        except:  return 'IncorrectCommandError'
    
def kill(event):  # Выход
    exit()

def beautifulPrint(text):  #  Красивый вывод
    try:
        for letter in text:
            root.after(50)
            write(letter)
            root.update() 
        write('\n')
    except Exception:
        print('Flush now')
 
def write(text):  # Запись в текстовое поле
    outputText.configure(state=tk.NORMAL)
    outputText.insert(tk.END, text)
    outputText.configure(state=tk.DISABLED)
    

def start(event=None):  # Запуск комманды
    command = inputTextVar.get()
    if len(command) == 0: output = 'EmptyStringError'
    else: output = run(command)
    beautifulPrint(output)

def cls():
    outputText.configure(state='normal')
    outputText.delete(1.0, tk.END) 
    outputText.configure(state='disabled')
    inputText.delete(0, tk.END)

tk.Label(text='>', bg='cyan').place(x=6, y=28)
tk.Button(root, bg='cyan', text='Enter', command=start, activebackground='blue').place(x=345, y=25)
tk.Button(root, bg='cyan', text='Cls', command=cls, activebackground='blue').place(x=20, y=280)
root.bind('<Alt_L>', start)
root.bind('<Escape>', kill)

root.mainloop()
