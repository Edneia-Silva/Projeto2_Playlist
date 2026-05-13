### 🎧 Sistema de Playlist de Músicas por BPM

Um sistema de gerenciamento de músicas e playlists baseado em listas encadeadas 
e filas FIFO, organizado por humor conforme o BPM das músicas. O projeto permite 
adicionar, remover, buscar e reproduzir músicas, além de manter um histórico e estatísticas.

⚠️ Importante: este projeto é uma simulação — ele não reproduz músicas de verdade, 
apenas organiza e exibe informações (no terminal) como se fosse um player.

### 📌 Objetivos Acadêmicos

Aplicar conceitos fundamentais de:
* Estruturas de Dados
* Lista Encadeada Simples
* Filas FIFO (First In, First Out)
* Manipulação de nós
* Organização modular em Python
* Encapsulamento e separação de responsabilidades

### 🚀 Funcionalidades 

* Gestão de biblioteca: adição, remoção e listagem de músicas com IDs únicos.
* Busca flexível: localização de faixas por ID ou título.
* Filas por BPM (Humor): classificação automática em 4 categorias:

    * Relaxar: Até 80 BPM.
    * Focar: 81-120 BPM.
    * Animar: 121-160 BPM.
    * Treinar: Acima de 160 BPM.

* Fluxo de reprodução: simulação de "dar play" que move o objeto de uma fila para um histórico, demonstrando o funcionamento de estruturas FIFO.
* Histórico de reprodução: registro de todas as músicas ouvidas durante a sessão.
* Estatísticas: painel com o total de músicas na biblioteca e o status de cada fila.
* Interface via terminal: menu interativo para interação direta com o back-end.

### 🛠️ Estruturas de Dados

O projeto utiliza implementações manuais para otimizar o desempenho e o controle de memória:

* Lista Encadeada Simples: utilizada na biblioteca principal para inserções dinâmicas e buscas (por ID ou Título) sem necessidade de realocação de memória.

* Filas Dinâmicas (FIFO): implementadas para gerenciar Filas de Humor e o Histórico, garantindo complexidade (O(1)) para inserção e remoção. 

* Encapsulamento: separação rígida entre a lógica de gerenciamento da biblioteca e o fluxo de reprodução do usuário.

### 🧩 Tecnologias Utilizadas

* Python 3
* Estruturas de Dados: lista encadeada e filas FIFO 
* Programação Orientada a Objetos (POO)

### 🏗️ Estrutura do Projeto

```bash
📦 projeto2_playlist
 ┣ 📜 main.py
 ┣ 📜 sistema.py
 ┣ 📜 biblioteca.py
 ┣ 📜 fila.py
 ┣ 📜 musica.py
 ┗ 📜 nodos.py
```

* main.py: ponto de entrada com o menu interativo.
* sistema.py: orquestrador que conecta a biblioteca às filas e gerencia a lógica de negócio.
* biblioteca.py: implementação da lista encadeada principal.
* fila.py: implementação da lógica de filas (Início/Fim).
* musica.py: classe modelo para o objeto Música.
* nodos.py: definição dos nós (nodes) para as estruturas encadeadas.

### 💻 Como Executar

1. Certifique-se de ter o Python instalado.
2. Faça o download dos arquivos ou clone o repositório do projeto.
3. Nenhuma biblioteca externa é necessária. 
4. Execute o arquivo principal: 

```bash
python main.py
```

### 📝 Exemplo de Uso

Ao iniciar o sistema, você pode adicionar músicas informando o título, artista e BPM. Após montar as filas (opção 5), o sistema distribuirá as músicas automaticamente, permitindo que você escolha o "humor" desejado para reproduzir a próxima faixa. Ao rodar o programa, você verá o menu principal:

========================================
 SISTEMA DE PLAYLIST
========================================
1. Adicionar música à biblioteca
2. Remover música da biblioteca
3. Buscar música
4. Listar biblioteca completa
5. Montar filas de reprodução por humor
6. Reproduzir próxima
7. Exibir fila de humor
8. Exibir histórico de reproduções
9. Estatísticas
10. Sair
========================================

### 🧪 Exemplo Real de Execução

```text
Escolha uma opção: 1

--- Adicionar Música ---
Título: Cálice
Artista: Chico Buarque
Gênero: MPB
BPM: 75

✔ Música adicionada com sucesso!
[ID: 1] Cálice - Chico Buarque | Gênero: MPB | BPM: 75
```

### 🚫 Restrições do Projeto

As estruturas foram implementadas manualmente com nós encadeados, sem utilização de estruturas prontas da linguagem Python, conforme exigência acadêmica.

### 📄 Licença

Projeto desenvolvido para fins acadêmicos.

### 👨‍💻 Autora

Ednéia Silva
Estudante de Inteligência Artificial (IA) - Fatec Rio Claro
Projeto desenvolvido para fins acadêmicos como parte da disciplina "Estrutura de Dados".


