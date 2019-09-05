# encoding=utf-8

import argparse
from pytorch_demos.demo1.main import main as pt_m1
from pytorch_demos.demo2.entry import main as pt_m2
from pytorch_demos.demo3.entry import main as pt_m3
from datetime import datetime

tasks = {
    'Pytorch Minist': pt_m1,
    'Dcgan': pt_m2,
    'Vae' : pt_m3
}


def launch(func_name, dataset, epoch):
    func = tasks[func_name]
    start = datetime.now()
    print('{:-^60s}'.format(func_name))
    print('%s starts executing at %s' % (func_name.ljust(20), start.strftime('%Y/%m/%d, %H:%M:%S')))
    func(dataset, epoch)
    elapsed = datetime.now() - start
    print('%s finished, Elapsed time:%.4f ms' % (func_name.ljust(20), elapsed.microseconds))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--all', help='run all demos', action='store_true')
    parser.add_argument('-n', '--name', help='the name of the task you want to run', type=str, default='Pytorch Minist')
    parser.add_argument('-e', '--epoch', help='set num of epochs', type=int, default=10)
    parser.add_argument('data', type=str, help='path to data set')
    options = parser.parse_args()
    print(options)
    if options.all:
        print('Run all demos')
        for task in tasks:
            launch(task, options.data, options.epoch)
    else:
        print('Run %s' % options.name)
        launch(options.name, options.data, options.epoch)
