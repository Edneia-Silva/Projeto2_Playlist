class Musica:  
    def __init__(self, id_musica, titulo, artista, genero, bpm):
        # Armazena os dados da música como atributos do objeto
        self.id = id_musica
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm
    
    def __str__(self):
        # Método especial que define como a música será exibida como texto
        return (
            f"[ID: {self.id}] {self.titulo} - {self.artista}"
            f"| Gênero: {self.genero} | BPM: {self.bpm}"
        )
    


