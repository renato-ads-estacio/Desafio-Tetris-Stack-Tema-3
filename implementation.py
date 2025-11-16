
from typing import List

class TetrisStack:
    """
    Modelo simples de empilhamento de Tetris usando lista como pilha.
    Cada linha é representada como lista de 0/1 com largura `width`.
    - push_line(filled) adiciona uma linha com 'filled' blocos (preenchidos da esquerda para direita)
    - clear full lines automatically and return number of cleared lines
    - height() returns current height of stack
    """
    def __init__(self, width: int = 10):
        self.width = width
        self.stack: List[List[int]] = []

    def push_line(self, filled: int) -> int:
        if filled < 0 or filled > self.width:
            raise ValueError('filled must be between 0 and width')
        line = [1]*filled + [0]*(self.width - filled)
        self.stack.append(line)
        cleared = 0
        # clear any full lines (could be more than 1 if multiple pushes make them full)
        # in this simplified model, only check and remove full lines anywhere
        new_stack = []
        for ln in self.stack:
            if sum(ln) == self.width:
                cleared += 1
            else:
                new_stack.append(ln)
        self.stack = new_stack
        return cleared

    def height(self) -> int:
        return len(self.stack)

    def __repr__(self):
        return f'<TetrisStack width={self.width} height={self.height()}>'

if __name__ == '__main__':
    t = TetrisStack(width=10)
    print('Push 10 -> clear:', t.push_line(10))
    print('Push 6 -> clear:', t.push_line(6))
    print('Height:', t.height())
