d = {}
execfile("execfile_test.py", d, d)
del d['__builtins__']['copyright']
print "====start\n", d, "\nend======"