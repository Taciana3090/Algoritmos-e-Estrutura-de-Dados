# criação da classe para definir cada nó da lista ligada
class Node:
    def __init__(self, key, value):
        # cada nó armazena uma chave (key) e um valor (value)
        self.key = key
        self.value = value
        # o próximo nó da lista ligada
        self.next = None

# criação da classe da tabela hash com encadeamento externo
class HashTable:
    def __init__(self, size=1000):
        # inicialização da tabela hash com um tamanho específico (padrão: 1000)
        self.size = size
        self.table = [None] * self.size
        
    # criação da função de espalhamento
    def hash_function(self, key):
        # calculará o valor hash da chave usando uma função simples (soma do valor ASCII de cada caractere)
        # e divide por 6 (número escolhido para tentar minimizar colisões)
        # em seguida, usará o operador de módulo para garantir que o resultado esteja dentro do tamanho da tabela
        hash_value = sum(ord(char) for char in key) // 6 % self.size
        return hash_value
        
    # função para inserir um novo elemento na tabela hash
    def insert(self, key, value=1):
        # calculará o valor hash da chave
        hash_value = self.hash_function(key)
        # se a posição na tabela hash estiver vazia, insere o novo nó nessa posição
        if self.table[hash_value] is None:
            self.table[hash_value] = Node(key, value)
        # se a posição já estiver ocupada, percorrerá a lista ligada até encontrar o nó com a chave ou chegar ao final da lista
        else:
            current_node = self.table[hash_value]
            while True:
                # se encontrar o nó com a chave, incrementa o valor
                if current_node.key == key:
                    current_node.value += value
                    break
                # se chegar ao final da lista, insere o novo nó
                elif current_node.next is None:
                    current_node.next = Node(key, value)
                    break
                # senão, continua percorrendo a lista
                else:
                    current_node = current_node.next
    
    # função que busca a contagem de um elemento na tabela hash
    def search(self, key):
        # calcula o valor hash da chave
        hash_value = self.hash_function(key)
        # se a posição na tabela hash estiver vazia, retorna 0
        if self.table[hash_value] is None:
            return 0
        # se a posição estiver ocupada, percorre a lista ligada até encontrar o nó com a chave ou chegar ao final da lista
        else:
            current_node = self.table[hash_value]
            while current_node is not None:
                # se encontrar o nó com a chave, retorna o valor
                if current_node.key == key:
                    return current_node.value
                # senão, continua percorrendo a lista
                else:
                    current_node = current_node.next
            # se chegar ao final da lista sem encontrar o nó, retorna 0
            return 0
        
        
    def items(self):
        items_list = []
        # percorre todos os índices da tabela hash
        for item in self.table:
            current_node = item
            # percorre a lista ligada de cada índice, adicionando as chaves e valores à lista de tuplas
            while current_node is not None:
                items_list.append((current_node.key, current_node.value))
                current_node = current_node.next
        return items_list

# leitura do arquivo "sequences.fasta" com o genoma do coronavírus
with open('sequences.fasta', 'r') as f:
    genome = f.read().replace('\n', '')

# cria a tabela hash
hash_table = HashTable()

# ler os blocos de 6 bases nitrogenadas e inserir na tabela hash
for i in range(0, len(genome) - 5, 6):
    block = genome[i:i+6]  # obter o bloco de 6 bases nitrogenadas
    hash_table.insert(block)  # inserir o bloco na tabela hash

# contar a quantidade de blocos repetidos
repeated_blocks = {}
for i in range(0, len(genome) - 5, 6):
    block = genome[i:i+6]  # obter o bloco de 6 bases nitrogenadas
    count = hash_table.search(block)  # obter a contagem de ocorrências do bloco na tabela hash
    if count > 1:  # se o bloco se repetir mais de uma vez
        repeated_blocks[block] = count  # adicionar o bloco e a contagem no dicionário repeated_blocks

# Imprimi os blocos repetidos e suas contagens em ordem crescente
# Este "for" serve APENAS para mostrar o resultado na IDE, caso queira visualiza-lo, só tirar o # do comando
#for block, count in sorted(repeated_blocks.items(), key=lambda x: x[1]):
#    print(f'O bloco {block} se repete {count} vezes no genoma.')  

# escreve o arquivo "count_blocos_genomas_covid.txt" em ordem crescente
with open("count_blocos_genomas_covid.txt", "w") as file:
    file.write('Bloco\tOcorrências\n')  # escreve a primeira linha no arquivo
    for key, value in sorted(hash_table.items(), key=lambda x: x[1]):  # itera sobre os itens da tabela hash em ordem crescente
        file.write(f"{key}\t{value}\n")  # escreve o bloco e sua contagem no arquivo
