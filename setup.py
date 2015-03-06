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
Pythonpy can't create a file in:
    /etc/bash_completion.d
The error was:
    %s
It looks like you either didn't run this command using sudo, or don't have
bash completions set up.
1) If this is intentional (e.g., because you're in a virtualenv), you can
   configure tab completion without root using:
   source /path/to/virtualenv/bash_completion.d/pycompletion.sh
2) Otherwise, remember that pip requires sudo by default
   on most systems. py is a simple python script that does not require any
   root access or special privileges. If you don't like using root,
   learn virtualenv and refer to 1).
Installation proceeding without root access...
******************************************************************************''') % e
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
    version='0.3.8',
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
