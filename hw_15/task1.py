import pathlib
from collections import namedtuple
from logger import log_dec
import argparse

DIRSUBJECT = namedtuple('DIRSUBJECT',['file_name', 'ext', 'flag', 'parent'])

#@log_dec
def dir_info(path):
    path = pathlib.Path(path)
    new_list = []
    for file in path.iterdir():
        new_list.append(DIRSUBJECT(file.name, file.suffix, file.is_dir(), file.parent))

    return new_list

def pars():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', default=1)
    args = parser.parse_args

    return print(f'В скрипт передано: {args}')

print(pars())

print(dir_info('D:\GB\Python Auto HW\Home_work_15\python'))