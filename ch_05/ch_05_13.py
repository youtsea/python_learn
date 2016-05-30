import os

names = os.listdir('.')

print names

import os.path

names = [name for name in os.listdir('.') if os.path.isfile(os.path.join('.', name))]

print names

dirnames = [name for name in os.listdir('.') if os.path.isdir(os.path.join('somedir', name))]

print dirnames

pyfiles = [name for name in os.listdir('.') if name.endswith('.py')]

print pyfiles

import glob

pyfiles = glob.glob('*py')

print pyfiles

from fnmatch import fnmatch

pyfiles = [name for name in os.listdir('.') if fnmatch(name, '*py')]

print pyfiles

pyfiles = glob.glob('*.py')
name_sz_data = [(name, os.path.getsize(name), os.path.getmtime(name)) for name in pyfiles]

print name_sz_data

for name, size , mtime in name_sz_data:
    print (name, size, mtime)

file_metadata = [(name, os.stat(name)) for name in pyfiles]

for name, meta in file_metadata:
    print (name, meta.st_size, meta.st_mtime)