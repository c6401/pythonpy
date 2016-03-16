_py()
{
    COMPREPLY=($(pycompleter "${COMP_WORDS[@]:1}" ))
}

complete -F _py -o nospace py
