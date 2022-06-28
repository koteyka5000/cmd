def shampoo(*args):
    try:
        via = args[0]
        mark = args[1]
        ml = args[2]
        flush = args[3]
    except Exception:
        return 'SyntaxError'
    if not checkCommand('shampoo', *args):  # 
        return 'SyntaxError'

    if flush == 'true':
        return f'FLUSHED SHAMPOO via {mark}, {ml} Ml'
    else:
        return f'RUN SHAMPOO -> {mark}, {ml} Ml'

def crush(*args):
    try:
        flag = args[0]
        flag2 = args[1]
    except Exception:
        return 'to crush enter "crush -f 739"\nThis will crush Python!'
    if flag == '-f' and flag2 == '739':
        q = 999999999999**9999999999999999
    else:
        return 'to crush enter "crush -f 739"'

def connect(*args):
    try:
        ip = args[0]
        user = args[1]
    except Exception:
        return 'SyntaxError'
    if not checkCommand('connect', *args):
        return 'connection refused! Incorrect IPv4 Adress'
    return f'connecting to {user} via IPv4: {ip}'

def exec(*args):
    exec(*args)
    return 'Done'

def help(*args):
    if len(args) == 0:
        txt = """============HELP MENU=============
        commands: shampoo, connect, cls, crush, exec
        Чтобы получить помощь по команде введи help и название команды, например:
        help crush"""
        return txt
    else:
        arg = args[0]
        if arg == 'shampoo':
            return 'Просто команда для теста. \nСинтаксис: shampoo via <марка> <миллилитры> <true/false>'
        elif arg == 'connect':
            return 'Типо подключение на ip. \nСинтаксис: connect <ip> <user>'
        elif arg == 'cls':
            return 'Очистка поля вывода.'
        elif arg == 'crush':
            return 'Крашит программу путём вычисления большого числа. \nСинтаксис: crush -f 739'
        elif arg == 'exec':
            return 'Выполнение команды как в python, например 1+1'
        else:
            return 'Команды не существует. Введи help для получения списка программ'

def checkCommand(cmd, *args):  # Проверка правильности введёной команды
    if cmd == 'shampoo':
        via = args[0]
        mark = args[1]
        ml = args[2]
        flush = args[3]
        return True if via == 'via' and flush == 'true' or flush == 'false' else False

    elif cmd == 'connect':
        try:
            ip = args[0]
            user = args[1]
            q = ip.split('.')
            for w in q:
                w = int(w)
                if not w <= 255 and w >= 0:
                    return False
        except Exception:
            return False
        return True

    else:
        return 'Access Denied:\nSystem func!'
