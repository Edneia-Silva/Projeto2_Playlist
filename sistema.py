from musica import Musica
from biblioteca import Biblioteca
from fila import Fila

class SistemaPlaylist:
    """ Gerencia toda a lógica do sistema de playlist.
    Conecta a biblioteca, as filas de humor e o histórico. """
    
    def __init__(self):
        self.biblioteca = Biblioteca()
        
        # Filas de humor (uma para cada faixa de BPM)
        self.fila_relaxar = Fila()      # até 80 BPM
        self.fila_focar = Fila()        # 81 a 120 BPM
        self.fila_animar = Fila()       # 121 a 160 BPM
        self.fila_treinar = Fila()      # acima de 160 BPM
        
        self.historico = Fila()
        
        # Contador para gerar IDs únicos (nunca reutilizado)
        self.proximo_id = 1
    
    def adicionar_musica(self, titulo, artista, genero, bpm):        
        nova_musica = Musica(self.proximo_id, titulo, artista, genero, bpm)
        self.biblioteca.inserir_no_final(nova_musica)
        self.proximo_id = self.proximo_id + 1  # Incrementa para próxima música
        return nova_musica
    
    def remover_musica(self, id_musica):     
        return self.biblioteca.remover_por_id(id_musica)
    
    def buscar_musica(self, termo, por_id=True):       
        if por_id:
            return self.biblioteca.buscar_por_id(termo)
        else:
            return self.biblioteca.buscar_por_titulo(termo)
    
    def listar_biblioteca(self):
        # Retorna texto com todas as músicas da biblioteca.
        return self.biblioteca.listar_todas()
    
    def montar_filas_humor(self):
        # Distribui músicas da biblioteca nas filas de humor conforme o BPM.
        self.fila_relaxar.limpar()
        self.fila_focar.limpar()
        self.fila_animar.limpar()
        self.fila_treinar.limpar()
        
        # Percorre a biblioteca
        atual = self.biblioteca.cabeca
        
        while atual is not None:
            musica = atual.musica
            bpm = musica.bpm
            
            # Decide qual fila baseado no BPM
            if bpm <= 80:
                self.fila_relaxar.enqueue(musica)
            elif bpm <= 120:
                self.fila_focar.enqueue(musica)
            elif bpm <= 160:
                self.fila_animar.enqueue(musica)
            else:
                self.fila_treinar.enqueue(musica)
            
            atual = atual.proximo
    
    def obter_fila_por_numero(self, numero):
        # Retorna a fila correspondente ao número escolhido.    
        if numero == 1:
            return self.fila_relaxar
        elif numero == 2:
            return self.fila_focar
        elif numero == 3:
            return self.fila_animar
        elif numero == 4:
            return self.fila_treinar
        else:
            return None
    
    def obter_nome_fila(self, numero):
        # Retorna o nome da fila pelo número.
        nomes = {1: "Relaxar", 2: "Focar", 3: "Animar", 4: "Treinar"}
        if numero in nomes:
            return nomes[numero]
        return "Desconhecida"
    
    def reproduzir_proxima(self, numero_fila):
        # Remove a música do topo da fila escolhida e adiciona ao histórico.
        fila = self.obter_fila_por_numero(numero_fila)
        
        if fila is None:
            return None
        
        musica = fila.dequeue()
        
        if musica is not None:
            self.historico.enqueue(musica)
        
        return musica
    
    def exibir_fila_humor(self, numero_fila):
        # Retorna texto com músicas da fila de humor escolhida.       
        fila = self.obter_fila_por_numero(numero_fila)
        
        if fila is None:
            return "Fila inválida."
        
        return fila.listar()
    
    def exibir_historico(self):
        # Retorna texto com todas as músicas reproduzidas.
        return self.historico.listar()
    
    def obter_estatisticas(self):
        # Retorna texto com estatísticas do sistema.
        texto = "=== ESTATÍSTICAS ===\n"
        texto = texto + f"Total na biblioteca: {self.biblioteca.tamanho}\n"
        texto = texto + f"Fila Relaxar: {self.fila_relaxar.tamanho}\n"
        texto = texto + f"Fila Focar: {self.fila_focar.tamanho}\n"
        texto = texto + f"Fila Animar: {self.fila_animar.tamanho}\n"
        texto = texto + f"Fila Treinar: {self.fila_treinar.tamanho}\n"
        texto = texto + f"Total reproduzidas: {self.historico.tamanho}\n"
        return texto
