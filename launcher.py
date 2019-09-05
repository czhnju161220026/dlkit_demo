# encoding=utf-8

from pytorch_demos.demo1.main import main as pt_m1
from datetime import datetime

tasks = {
    'Pytorch Minist': pt_m1
}



def launch(func_name):
    func = tasks[func_name]
    start = datetime.now()
    print('{:-^60s}'.format(func_name))
    print('%s starts executing at %s' % (func_name.ljust(20), start.strftime('%Y/%m/%d, %H:%M:%S')))
    func()
    elapsed = datetime.now() - start
    print('%s finished, Elapsed time:%.4f ms' % (func_name.ljust(20), elapsed.microseconds))


if __name__ == '__main__':
    for task in tasks:
        launch(task)
