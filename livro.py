#
# autor: Michel
# data: 26/08/2025


# Crie uma Classe `Livro`
# Defina uma classe `Livro` com um atributo `titulo` e um método `ler()` que imprima "Lendo [titulo do livro]".

# 1. Definição da Classe Livro e seu Método ler()

class Livro:
    """
    Representa um livro com um título e a capacidade de ser lido.
    """
    
    def __init__(self, titulo):
        """
        Construtor da classe. É chamado quando um novo objeto Livro é criado.
        
        Parâmetros:
            titulo (str): O título do livro.
        """
        self.titulo = titulo  # Atributo que armazena o título de cada livro

    def ler(self):
        """
        Simula a ação de ler o livro, imprimindo uma mensagem com seu título.
        """
        print(f"Lendo {self.titulo}")