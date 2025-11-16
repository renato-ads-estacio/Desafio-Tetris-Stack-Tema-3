
# Desafio Tetris Stack

## Descrição da solução
Modelo simplificado de Tetris que usa uma lista como pilha para linhas. Cada linha é uma lista de inteiros 0/1.
Ao empilhar uma linha completa (todos 1s), a linha é removida (clear) — comportamento semelhante ao Tetris.

### Estruturas usadas
- `list` (pilha) para representar o empilhamento de linhas.

### Complexidade
- push_line: O(h) para verificar e filtrar linhas (h = altura atual). Pode ser otimizado com contadores, mas suficiente para o propósito didático.
- Espaço: O(h * width).

### Execução
```bash
python3 main.py
```
