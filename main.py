
from implementation import TetrisStack
t = TetrisStack(width=10)
# example sequence
seq = [3,4,10,7,10,2]
for val in seq:
    cleared = t.push_line(val)
    print(f'Pushed {val}, cleared {cleared}, height now {t.height()}')
