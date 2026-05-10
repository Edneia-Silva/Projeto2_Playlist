from nodos import NodoLista

class Biblioteca:
    """Gerencia a coleção principal usando uma lista encadeada simples."""   
    
    def __init__(self):
        self.cabeca = None    # Primeiro nó da lista
        self.tamanho = 0      # Contador de músicas
    
    def esta_vazia(self):  
        return self.cabeca is None    
    
    def inserir_no_final(self, musica):
        """Insere um novo registro no final da lista (Complexidade O(n))."""        
        novo_nodo = NodoLista(musica)
        
        if self.esta_vazia():
            # Lista vazia: novo nó é a cabeça
            self.cabeca = novo_nodo
        else:
            # Percorre até encontrar o último nó
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            # Conecta o novo nó no final
            atual.proximo = novo_nodo
        
        self.tamanho = self.tamanho + 1
    
    def remover_por_id(self, id_musica): 
        """Remove um nodo por ID e ajusta os ponteiros adjacentes."""      
        if self.esta_vazia():
            return False        

        if self.cabeca.musica.id == id_musica:
            self.cabeca = self.cabeca.proximo
            self.tamanho = self.tamanho - 1
            return True
        
        # Procura o nó anterior ao que será removido
        anterior = self.cabeca
        atual = self.cabeca.proximo
        
        while atual is not None:
            if atual.musica.id == id_musica:
                # Se encontrou, pula o nó atual na corrente
                anterior.proximo = atual.proximo
                self.tamanho = self.tamanho - 1
                return True
            # Avança para o próximo
            anterior = atual
            atual = atual.proximo
        
        # Não encontrou
        return False
    
    def buscar_por_id(self, id_musica):     
        atual = self.cabeca
        
        while atual is not None:
            if atual.musica.id == id_musica:
                return atual.musica
            atual = atual.proximo
        
        return None
    
    def buscar_por_titulo(self, titulo):      
        atual = self.cabeca
        titulo_busca = titulo.lower()  
        
        while atual is not None:
            if atual.musica.titulo.lower() == titulo_busca:
                return atual.musica
            atual = atual.proximo
        
        return None
    
    def listar_todas(self):      
        if self.esta_vazia():
            return "Biblioteca vazia."
        
        resultado = ""
        atual = self.cabeca
        
        while atual is not None:
            resultado = resultado + str(atual.musica) + "\n"
            atual = atual.proximo
        
        return resultado


