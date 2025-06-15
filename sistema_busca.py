def buscar_livro(arvore, valor, tipo_busca):
    if tipo_busca == 'isbn':
        livro = arvore.buscar(arvore.raiz, valor)
        if livro:
            print(f"Livro encontrado por ISBN: {livro.titulo}, {livro.autor}, {livro.isbn}")
        else:
            print("Livro não encontrado por ISBN.")
    
    elif tipo_busca == 'titulo':
        livros_encontrados = []

        def buscar_por_titulo_recursivo(no):
            if no:
                if valor.lower() in no.titulo.lower():  
                    livros_encontrados.append(no)
                buscar_por_titulo_recursivo(no.esquerda)  
                buscar_por_titulo_recursivo(no.direita)  

        buscar_por_titulo_recursivo(arvore.raiz)

        if livros_encontrados:
            print(f"Livros encontrados com o título '{valor}':")
            for livro in livros_encontrados:
                print(f"{livro.titulo}, {livro.autor}, {livro.isbn}")
        else:
            print(f"Nenhum livro encontrado com o título '{valor}'.")

    elif tipo_busca == 'autor':
        livros_encontrados = []

        def buscar_por_autor_recursivo(no):
            if no:
                if valor.lower() in no.autor.lower():  
                    livros_encontrados.append(no)
                buscar_por_autor_recursivo(no.esquerda)  
                buscar_por_autor_recursivo(no.direita)  

        buscar_por_autor_recursivo(arvore.raiz)

        if livros_encontrados:
            print(f"Livros encontrados com o autor '{valor}':")
            for livro in livros_encontrados:
                print(f"{livro.titulo}, {livro.autor}, {livro.isbn}")
        else:
            print(f"Nenhum livro encontrado com o autor '{valor}'.")
