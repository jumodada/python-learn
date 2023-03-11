# coding:utf-8

import os

from shutil import copy, copyfile, move, make_archive, unpack_archive

path = os.path.join(os.getcwd(), 'test1.txt')
target = os.path.join(os.getcwd(), 'test1')

copy(path, target)

copyfile(path, 'abc.txt')

#move('abc.txt', 'test1/efg.txt')
move('abc.txt', 'efg.txt')

make_archive('test1', 'zip', os.path.join(os.getcwd(), 'test1'))
target = os.path.join(os.getcwd(), 'test2')
unpack_archive('test1.zip', target)

# os.remove('efg.txt')

