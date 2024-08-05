import os

cur_dir = os.path.abspath(os.path.curdir)
# print(cur_dir)
# os.system("pause")

home = os.path.expanduser('~')
home = home.replace("\\", "\\\\")

run_reg = os.path.join(cur_dir, 'run.reg')

with open(run_reg, 'wb') as f:
    reg_content = rf'''
Windows Registry Editor Version 5.00
[HKEY_LOCAL_MACHINE\SOFTWARE\GNU]
[HKEY_LOCAL_MACHINE\SOFTWARE\GNU\Emacs]
"HOME"="{home}"
"SPACEMACSDIR"="{home}\\.spacemacs.d"
    '''.encode("utf-8")
    reg_content = reg_content.strip()
    f.write(reg_content)

os.system(run_reg)
