# Pythonpy 0.4
Removed documentation for flags --ji, --jo, --so, --si, --i, and -fx. 
These flags are not deprecated. Users should feel comfortable continuing to use them,
but from some simple polling I have found that they are infrequently used due to
their complexity and unorthodox double-dash form.

# 0.4.9
Pythonpy no longer automatically tries to install pycompletion.sh into /etc/bash_completion.d
The .sh script is provided in the completion directory and users that want this feature may add

    source `find_pycompletion.sh`

to their .bashrc.
