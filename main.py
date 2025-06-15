from arvore_avl import ArvoreAVL
from livros_class import carregar_livros, salvar_livros
from sistema_busca import buscar_livro

def main():
    arvore = ArvoreAVL()

    livros = carregar_livros()  


    for livro in livros:
        arvore.raiz = arvore.inserir(arvore.raiz, livro["titulo"], livro["autor"], livro["isbn"])

    while True:
        print("Sistema de Biblioteca")
        print("1. Inserir livro manualmente")
        print("2. Exibir todos os livros")
        print("3. Buscar livro por ISBN")
        print("4. Buscar livro por Título")
        print("5. Buscar livro por Autor")
        print("6. Excluir livro")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            isbn = input("Digite o ISBN do livro: ")

            livro_existente = arvore.buscar(arvore.raiz, isbn)
            if livro_existente:
                print(f"Livro '{titulo}' já está na árvore.")
            else:
                arvore.raiz = arvore.inserir(arvore.raiz, titulo, autor, isbn)
                print(f"Livro '{titulo}' inserido com sucesso!")
                novos_livros = {"titulo": titulo, "autor": autor, "isbn": isbn}
                livros.append(novos_livros)  
                salvar_livros(livros)  

        elif opcao == '2':
            print("Livros cadastrados:")
            arvore.exibir_em_ordem(arvore.raiz)
        elif opcao == '3':
            isbn = input("Digite o ISBN do livro para busca: ")
            buscar_livro(arvore, isbn, tipo_busca='isbn')
        elif opcao == '4':
            titulo = input("Digite o título do livro para busca: ")
            buscar_livro(arvore, titulo, tipo_busca='titulo')
        elif opcao == '5':
            autor = input("Digite o autor do livro para busca: ")
            buscar_livro(arvore, autor, tipo_busca='autor')
        elif opcao == '6':
            isbn = input("Digite o ISBN do livro para excluir: ")
          
            livros = [livro for livro in livros if livro["isbn"] != isbn]

            arvore = ArvoreAVL()
            for livro in livros:
                arvore.raiz = arvore.inserir(arvore.raiz, livro["titulo"], livro["autor"], livro["isbn"])

            salvar_livros(livros)

            print(f"Livro com ISBN {isbn} removido com sucesso.")
        elif opcao == '7':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
