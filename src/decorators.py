import os.path


def log(func, filename: str = ''):
    def wrapper(*args, **kwargs):
        log = []
        try:
            result = func(*args, **kwargs)
            log.append(f'result is {result}')
        except Exception:
            log.append('Function call failed.')
            log.append(f'Function arguments are: {Exception.args}')

        # time_2 = time()
        # print(f'Time for work: {time_2 - time_1}')
        if filename and os.path.exists(filename):
            with open(filename, 'a', encoding='utf-8') as f:
                f.writelines(log)
        else:
            print(log, sep='\n')
        return result

    return wrapper
