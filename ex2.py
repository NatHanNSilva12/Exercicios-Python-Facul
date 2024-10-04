import matplotlib.pyplot as plt  # Importa a biblioteca Matplotlib para criar gráficos

# Passo 1: Definindo a classe Livro
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo        # Atributo para o título do livro
        self.autor = autor          # Atributo para o autor do livro
        self.genero = genero        # Atributo para o gênero do livro
        self.quantidade = quantidade  # Atributo para a quantidade disponível

# Passo 2: Inicializando uma lista vazia para armazenar os livros
livros = []

# Passo 3: Implementando funções para gerenciar os livros
def cadastrar_livro():
    # Solicita informações do livro ao usuário
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o gênero do livro: ")
    quantidade = int(input("Digite a quantidade disponível: "))
    
    # Cria uma instância da classe Livro e adiciona à lista
    livro = Livro(titulo, autor, genero, quantidade)
    livros.append(livro)
    print(f'Livro "{titulo}" cadastrado com sucesso!')

def listar_livros():
    # Verifica se há livros cadastrados
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    # Exibe todos os livros cadastrados
    print("\nLivros cadastrados:")
    for livro in livros:
        print(f'Título: {livro.titulo}, Autor: {livro.autor}, Gênero: {livro.genero}, Quantidade: {livro.quantidade}')

def buscar_livro():
    # Solicita o título do livro a ser buscado
    titulo_busca = input("Digite o título do livro que deseja buscar: ")
    # Procura o livro na lista
    for livro in livros:
        if livro.titulo.lower() == titulo_busca.lower():
            print(f'Livro encontrado: Título: {livro.titulo}, Autor: {livro.autor}, Gênero: {livro.genero}, Quantidade: {livro.quantidade}')
            return
    print("Livro não encontrado.")

def gerar_grafico_genero():
    # Dicionário para contar a quantidade de livros por gênero
    genero_count = {}
    
    # Conta a quantidade de livros por gênero
    for livro in livros:
        if livro.genero in genero_count:
            genero_count[livro.genero] += livro.quantidade
        else:
            genero_count[livro.genero] = livro.quantidade
    
    # Gera o gráfico
    plt.bar(genero_count.keys(), genero_count.values())
    plt.xlabel('Gênero')
    plt.ylabel('Quantidade de Livros')
    plt.title('Quantidade de Livros por Gênero')
    plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x para melhor legibilidade
    plt.tight_layout()  # Ajusta o layout para evitar sobreposição
    plt.show()  # Exibe o gráfico

# Passo 5: Função principal para testar o sistema
def main():
    while True:
        print("\nMenu:")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Buscar livro pelo título")
        print("4. Gerar gráfico de livros por gênero")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            buscar_livro()
        elif opcao == '4':
            gerar_grafico_genero()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()  # Chama a função principal para iniciar a execução