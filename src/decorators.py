from time import time, ctime
from functools import wraps


def log(filename: str = ''):        # декоратор для журналирования работы функций
    def wrapper(func):
        @wraps(func)                # сохраняем справочную информацию по декорируемой функции и ее имя
        def inner(*args, **kwargs):
            log = []
            result = None
            try:
                time_start = time()
                log.append(f'{func.__name__}() call start at {ctime(time_start)}')
                result = func(*args, **kwargs)
                time_end = time()
                log.append(f'{func.__name__}() ok')
                log.append(f'{func.__name__}() finished at {ctime(time_end)}')
                log.append(f'Run time: {time_end - time_start}')
                log.append(f'Result is {result}')
            except Exception as e:          # фиксируем информацию по исключению
                args_line = ''
                if args:                    # фиксируем список значений аргументов
                    for arg in args:
                        args_line = args_line + ',' + str(arg)
                if kwargs:
                    for arg in kwargs:
                        args_line = args_line + ',' + str(arg)
                while args_line and args_line[0] == ',':
                    args_line = args_line[1:].strip()

                log.append(f'{func.__name__}() error: {e}. Inputs: {args_line}')

            if filename:                                            # выводим лог в файл
                with open(filename, 'a', encoding='utf-8') as f:
                    for line in log:
                        f.write(line+'\n')
            else:                                                   # выводим лог в консоль
                for line in log:
                    print(line)
            return result
        return inner
    return wrapper
