from nodos import NodoFila

class Fila:
    """Implementação de fila FIFO com 
    referências de início e fim (O(1) para inserção)."""    
    def __init__(self):
        self.inicio = None    
        self.fim = None      
        self.tamanho = 0
    
    def esta_vazia(self):
        # Verifica se a fila está vazia.
        return self.inicio is None
    
    def enqueue(self, musica):
        # Adiciona uma música no final da fila.
        novo_nodo = NodoFila(musica)
        
        if self.esta_vazia():
            # Fila vazia: o novo é o início e o fim
            self.inicio = novo_nodo
            self.fim = novo_nodo
        else:
            # Conecta o novo no final
            self.fim.proximo = novo_nodo
            self.fim = novo_nodo
        
        self.tamanho = self.tamanho + 1
    
    def dequeue(self):
        # Remove e retorna a música do início da fila.   
        if self.esta_vazia():
            return None
        
        # Guarda a música que será removida
        musica_removida = self.inicio.musica
        
        # Avança o início para o próximo
        self.inicio = self.inicio.proximo
        
        # Se a fila ficou vazia, atualiza o fim também
        if self.inicio is None:
            self.fim = None
        
        self.tamanho = self.tamanho - 1
        return musica_removida
    
    def limpar(self):
        # Remove todos os elementos da fila.
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def listar(self):
        # Retorna texto com todas as músicas da fila, sem removê-las.
        if self.esta_vazia():
            return "Fila vazia."
        
        resultado = ""
        atual = self.inicio
        posicao = 1
        
        while atual is not None:
            resultado = resultado + f"{posicao}. {atual.musica}\n"
            atual = atual.proximo
            posicao = posicao + 1
        
        return resultado

