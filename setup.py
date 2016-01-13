#!/usr/bin/env python
from setuptools import setup
import os
import sys
import tempfile

for path in os.environ['PATH'].split(':'):
    target = os.path.join(os.path.dirname(path), 'etc', 'bash_completion.d')
    if os.path.isdir(target):
        break
else:
    # Fall back to the default used by many Linux distros
    target = '/etc/bash_completion.d'

try:
    with tempfile.TemporaryFile(dir=target) as t:
        pass
except OSError as e:
    print(
'''******************************************************************************
Pythonpy was not able to install bash completion because it does not have write
access to /etc/bash_completion.d.
If you would still like to install bash completion, either:
1) Reinstall with `sudo pip install pythonpy`
2) Configure tab completion manually:
   source /path/to/virtualenv/bash_completion.d/pycompletion.sh

Installation proceeding without root access...
******************************************************************************''')
    target='bash_completion.d'

data_files = [(target, ['pythonpy/pycompletion.sh']),]

py_entry = 'py%s = pythonpy.__main__:main'
pycompleter_entry = 'pycompleter%s = pythonpy.pycompleter:main'
endings = ('', sys.version[:1], sys.version[:3])
entry_points_scripts = []
for e in endings:
    entry_points_scripts.append(py_entry % e)
    entry_points_scripts.append(pycompleter_entry % e)

setup(
    name='pythonpy',
    version='0.4.4',
    description='python -c, with tab completion and shorthand',
    data_files=data_files,
    license='MIT',
    url='https://github.com/Russell91/pythonpy',
    long_description='https://github.com/Russell91/pythonpy',
    packages = ['pythonpy'],
    entry_points = {
        'console_scripts': entry_points_scripts
    },
)
