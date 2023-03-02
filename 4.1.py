# 1. Вычислить число c заданной точностью d

n = 3
pi = 3.1415926
tmpl = '{:.' + str(n) + 'f}'
print(tmpl.format(pi))