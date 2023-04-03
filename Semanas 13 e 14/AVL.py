# definição da classe Node que representa um nó da árvore AVL
class Node:
    def __init__(self, val):
        self.val = val # valor do nó
        self.left = None  # referência ao nó filho esquerdo
        self.right = None # referência ao nó filho direito
        self.height = 1 # altura do nó - inicializado em 1 - 

# função que calculará a altura de um nó da árvore AVL
def height(node):
    return node.height if node else 0 # retorna a altura do nó ou 0 caso não exista

# função que calculará o fator de balanceamento de um nó da árvore AVL
def balance_factor(node):
    return height(node.left) - height(node.right) if node else 0 # calcula o fator de balanceamento do nó

# função que rotacionará a árvore à esquerda a partir de um determinado nó
def rotate_left(node):
    r = node.right # define o nó à direita como 'r'
    s = r.left # define o filho esquerdo de 'r' como 's'
    r.left = node # faz a rotação à esquerda
    node.right = s # atualiza a referência do filho direito do nó
    node.height = max(height(node.left), height(node.right)) + 1 # atualiza a altura do nó
    r.height = max(height(r.left), height(r.right)) + 1 # atualiza a altura do nó 'r'
    return r # retorna o nó 'r'

# função que rotacionará a árvore à direita a partir de um determinado nó
def rotate_right(node):
    l = node.left # define o nó à esquerda como 'l'
    s = l.right # define o filho direito de 'l' como 's'
    l.right = node  # faz a rotação à direita
    node.left = s # atualiza a referência do filho esquerdo do nó
    node.height = max(height(node.left), height(node.right)) + 1 # atualiza a altura do nó
    l.height = max(height(l.left), height(l.right)) + 1  # atualiza a altura do nó 'l'
    return l # retorna o nó 'l'

# função para inserir um novo nó na árvore AVL
def insert(node, val):
    # se o nó for nulo, cria um novo nó com o valor passado como argumento
    if not node:
        return Node(val) # cria um novo nó caso não exista
     # se o valor passado for menor que o valor do nó atual, insere na subárvore esquerda
    elif val < node.val:
        node.left = insert(node.left, val)  # insere o valor no nó filho esquerdo
    # caso contrário, insere na subárvore direita
    else:
        node.right = insert(node.right, val)  # insere o valor no nó filho direito
    node.height = max(height(node.left), height(node.right)) + 1 # atualiza a altura do nó
    bf = balance_factor(node)   # calcula o fator de balanceamento do nó
    # verifica se é necessário realizar alguma rotação para balancear a árvore
    if bf > 1 and val < node.left.val:
        return rotate_right(node)  # faz a rotação à direita
    elif bf > 1 and val > node.left.val:
        node.left = rotate_left(node.left) # faz a rotação à esquerda no filho esquerdo
        return rotate_right(node) # faz a rotação à direita no nó
    elif bf < -1 and val > node.right.val:
        return rotate_left(node) # faz a rotação à esquerda
    elif bf < -1 and val < node.right.val:
        node.right = rotate_right(node.right)
        return rotate_left(node)
    # se não for necessário realizar rotação, retorna o nó atual
    return node

# função que executará a travessia preOrdem na árvore
def preOrder(node, res):
    if node:
        # adiciona o valor do nó atual na lista de resultados
        res.append(str(node.val))
         # faz a travessia na subárvore esquerda
        preOrder(node.left, res)
         # faz a travessia na subárvore direita
        preOrder(node.right, res)

# função que executará a travessia inOrdem na árvore
def inOrder(node, res):
    if node:
        # faz a travessia na subárvore esquerda
        inOrder(node.left, res)
        # adiciona o valor do nó atual na lista de resultados
        res.append(str(node.val))
        # faz a travessia na subárvore direita
        inOrder(node.right, res)

# função que executará a travessia posOrdem na árvore
def postOrder(node, res):
    if node:
        # faz a travessia na subárvore esquerda
        postOrder(node.left, res)
        # faz a travessia na subárvore direita
        postOrder(node.right, res)
        # adiciona o valor do nó atual na lista de resultados
        res.append(str(node.val))

# função principal que cria a árvore AVL e executa as travessias
def buildAVL(input_file, output_file):
    # lê os dados do arquivo de entrada
    with open(input_file, 'r') as f:
        # lê o número de valores a serem inseridos na árvore
        n = int(f.readline().strip())
        # lê os valores a serem inseridos na árvore
        values = list(map(int, f.readline().split()))

    # cria a árvore AVL a partir dos valores lidos do arquivo
    root = None
    for val in values:
        root = insert(root, val)

    # executa as travessias e grava no arquivo de saída
    with open(output_file, 'w') as f:
         # executa a travessia preOrdem na árvore e armazena o resultado na lista res
        res = []
        preOrder(root, res)
        # escreve a lista res no arquivo de saída com o resultado da travessia preOrdem
        f.write(f"preOrdem: {' '.join(res)}\n")
        # executa a travessia inOrdem na árvore e armazena o resultado na lista res
        res = []
        inOrder(root, res)
        # escreve a lista res no arquivo de saída com o resultado da travessia inOrdem
        f.write(f"inOrdem: {' '.join(res)}\n")
        # executa a travessia posOrdem na árvore e armazena o resultado na lista res
        res = []
        postOrder(root, res)
         # escreve a lista res no arquivo de saída com o resultado da travessia posOrdem
        f.write(f"posOrdem: {' '.join(res)}\n")

# exemplo de uso - basta escolher o input que irá ser usado e alterar o nome do output. 
buildAVL('input2.txt', 'output2.txt')
