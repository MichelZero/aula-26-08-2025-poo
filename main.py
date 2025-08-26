#
# autor: Michel
# data: 26/08/2025

# Instancie e Use Objetos `Livro`
#Crie dois objetos diferentes da classe `Livro`, um para "O Pequeno Príncipe" e outro para "Dom Casmurro". Chame o método `ler()` para cada um deles.

# importando a classe livro
from livro import Livro

# 2. Instanciando e Usando os Objetos

# Cria o primeiro objeto (instância) da classe Livro
livro_principe = Livro("O Pequeno Príncipe")

# Cria o segundo objeto (instância) da classe Livro
livro_casmurro = Livro("1984")


# 3. Chamando o método ler() para cada objeto

# Chama o método para o primeiro livro
livro_principe.ler()

# Chama o método para o segundo livro
livro_casmurro.ler()

