from sistema import SistemaPlaylist

def exibir_menu():
    """Exibe o menu principal."""
    print("\n" + "=" * 40)
    print("     SISTEMA DE PLAYLIST")
    print("=" * 40)
    print("1. Adicionar música à biblioteca")
    print("2. Remover música da biblioteca")
    print("3. Buscar música")
    print("4. Listar biblioteca completa")
    print("5. Montar filas de reprodução por humor")
    print("6. Reproduzir próxima")
    print("7. Exibir fila de humor")
    print("8. Exibir histórico de reproduções")
    print("9. Estatísticas")
    print("10. Sair")
    print("=" * 40)

def ler_inteiro(mensagem):
    while True:
        entrada = input(mensagem)
        
        if len(entrada) == 0:
            print("Erro: Digite um número inteiro válido.")
            continue
        
        if entrada[0] == '-':
            if len(entrada) == 1:
                print("Erro: Digite um número inteiro válido.")
                continue
            parte_num = entrada[1:]
        else:
            parte_num = entrada
        
        valido = True
        for char in parte_num:
            if char < '0' or char > '9':
                valido = False
                break
        
        if valido:
            return int(entrada)
        else:
            print("Erro: Digite um número inteiro válido.")

def ler_bpm():
    """
    Lê o BPM do usuário.
    Valida se é número positivo.
    """
    while True:
        bpm = ler_inteiro("BPM: ")
        if bpm > 0:
            return bpm
        print("Erro: BPM deve ser maior que zero.")


def menu_busca(sistema):
    """Submenu para escolher tipo de busca."""
    print("\nBuscar por:")
    print("1. ID")
    print("2. Título")
    opcao = ler_inteiro("Escolha: ")
    
    if opcao == 1:
        id_busca = ler_inteiro("Digite o ID: ")
        musica = sistema.buscar_musica(id_busca, por_id=True)
    elif opcao == 2:
        titulo = input("Digite o título: ")
        musica = sistema.buscar_musica(titulo, por_id=False)
    else:
        print("Opção inválida.")
        return
    
    if musica is not None:
        print("\nMúsica encontrada:")
        print(musica)
    else:
        print("Música não encontrada.")


def menu_fila_humor():
    """Exibe opções de filas de humor."""
    print("\nFilas de humor:")
    print("1. Relaxar (até 80 BPM)")
    print("2. Focar (81-120 BPM)")
    print("3. Animar (121-160 BPM)")
    print("4. Treinar (acima de 160 BPM)")
    return ler_inteiro("Escolha a fila: ")


def main():
    """Função principal que executa o sistema."""
    sistema = SistemaPlaylist()
    
    while True:
        exibir_menu()
        opcao = ler_inteiro("Escolha uma opção: ")
        
        if opcao == 1:
            # Adicionar música
            print("\n--- Adicionar Música ---")
            titulo = input("Título: ")
            artista = input("Artista: ")
            genero = input("Gênero: ")
            bpm = ler_bpm()
            
            musica = sistema.adicionar_musica(titulo, artista, genero, bpm)
            print(f"\nMúsica adicionada com sucesso!")
            print(musica)
        
        elif opcao == 2:
            # Remover música
            print("\n--- Remover Música ---")
            id_remover = ler_inteiro("Digite o ID da música: ")
            
            if sistema.remover_musica(id_remover):
                print("Música removida com sucesso!")
            else:
                print("Erro: Música não encontrada.")
        
        elif opcao == 3:
            # Buscar música
            print("\n--- Buscar Música ---")
            menu_busca(sistema)
        
        elif opcao == 4:
            # Listar biblioteca
            print("\n--- Biblioteca Completa ---")
            print(sistema.listar_biblioteca())
        
        elif opcao == 5:
            # Montar filas de humor
            sistema.montar_filas_humor()
            print("\nFilas de humor montadas com sucesso!")
            print(f"Relaxar: {sistema.fila_relaxar.tamanho} músicas")
            print(f"Focar: {sistema.fila_focar.tamanho} músicas")
            print(f"Animar: {sistema.fila_animar.tamanho} músicas")
            print(f"Treinar: {sistema.fila_treinar.tamanho} músicas")
        
        elif opcao == 6:
            # Reproduzir próxima
            print("\n--- Reproduzir Próxima ---")
            numero_fila = menu_fila_humor()
            
            if numero_fila < 1 or numero_fila > 4:
                print("Fila inválida.")
            else:
                musica = sistema.reproduzir_proxima(numero_fila)
                if musica is not None:
                    nome_fila = sistema.obter_nome_fila(numero_fila)
                    print(f"\n♪ Reproduzindo da fila {nome_fila}:")
                    print(musica)
                else:
                    print("Fila vazia. Nenhuma música para reproduzir.")
        
        elif opcao == 7:
            # Exibir fila de humor
            print("\n--- Exibir Fila de Humor ---")
            numero_fila = menu_fila_humor()
            
            if numero_fila < 1 or numero_fila > 4:
                print("Fila inválida.")
            else:
                nome_fila = sistema.obter_nome_fila(numero_fila)
                print(f"\nFila {nome_fila}:")
                print(sistema.exibir_fila_humor(numero_fila))
        
        elif opcao == 8:
            # Exibir histórico
            print("\n--- Histórico de Reproduções ---")
            print(sistema.exibir_historico())
        
        elif opcao == 9:
            # Estatísticas
            print("\n" + sistema.obter_estatisticas())
        
        elif opcao == 10:
            # Sair
            print("\nAté logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
