"""
Implement a mock of cd (change directory) command on Unix. The code doesn't have to change actual directories, just return the new path after cd was executed.

The function takes two arguments (current working directory and directory to change to), and returns the output directory as if cd command was executed. There's no filesystem underneath; all paths are valid.


| cwd      | cd (arg)       | output
| -------- | -------------- | ------
| /        | foo            | /foo
| /baz     | /bar           | /bar
| /baz     | bar            | /baz/bar
| /foo/bar | ../../../../.. | /
| /x/y     | ../p/../q      | /x/q
| /x/y     | /p/./q         | /p/q
| /x/y     | /p/../q        | /q
"""

'''
'string
'valid input
'bazbar'\
' ./../

'''

'''
break string (/)
run
1. Chack arg for special chars
if / forget cwd and append it to cd. return
if . append cd to cwd with / in btw. retun
if .. get parent and append to cd. retun

get parent(arr.[tok], ind). 0.., 1.., ../../..
    retunr ind-1
get
'''

'/p/../q
def mock_cd(cwd, cd):

    dir_name = ''

    new_cd = cd.split('/') p,.., q
    
    for token in new_cd:
        if token == '.':
            dir_name = process_dot()
        elif token == '..':
            dir_name = process_ddot()
        else:
             dir_name = cd + cwd
    return dir_name


