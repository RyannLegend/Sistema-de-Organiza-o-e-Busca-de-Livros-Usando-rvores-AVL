class No:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        if not no:
            return 0
        return no.altura

    def rotacao_direita(self, raiz):
        nova_raiz = raiz.esquerda
        raiz.esquerda = nova_raiz.direita
        nova_raiz.direita = raiz
        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))
        nova_raiz.altura = 1 + max(self.altura(nova_raiz.esquerda), self.altura(nova_raiz.direita))
        return nova_raiz

    def rotacao_esquerda(self, raiz):
        nova_raiz = raiz.direita
        raiz.direita = nova_raiz.esquerda
        nova_raiz.esquerda = raiz
        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))
        nova_raiz.altura = 1 + max(self.altura(nova_raiz.esquerda), self.altura(nova_raiz.direita))
        return nova_raiz

    def balanceamento(self, no):
        if not no:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def inserir(self, raiz, titulo, autor, isbn):
        if not raiz:
            return No(titulo, autor, isbn)

        if isbn < raiz.isbn:
            raiz.esquerda = self.inserir(raiz.esquerda, titulo, autor, isbn)
        else:
            raiz.direita = self.inserir(raiz.direita, titulo, autor, isbn)

        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))

        balanceamento = self.balanceamento(raiz)

        if balanceamento > 1 and isbn < raiz.esquerda.isbn:
            return self.rotacao_direita(raiz)
        if balanceamento < -1 and isbn > raiz.direita.isbn:
            return self.rotacao_esquerda(raiz)
        if balanceamento > 1 and isbn > raiz.esquerda.isbn:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)
        if balanceamento < -1 and isbn < raiz.direita.isbn:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

    def buscar(self, raiz, isbn):
        if raiz is None or raiz.isbn == isbn:
            return raiz

        if isbn < raiz.isbn:
            return self.buscar(raiz.esquerda, isbn)

        return self.buscar(raiz.direita, isbn)

    def exibir_em_ordem(self, raiz):
        if raiz:
            self.exibir_em_ordem(raiz.esquerda)
            print(f'{raiz.titulo}, {raiz.autor}, {raiz.isbn}')
            self.exibir_em_ordem(raiz.direita)
