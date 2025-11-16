
from implementation import TetrisStack
if __name__ == '__main__':
    t = TetrisStack(width=5)
    print('Clear count:', t.push_line(5))  # clears immediately
    print('Height after clear:', t.height())
    t.push_line(3); t.push_line(5); print('Height:', t.height())
