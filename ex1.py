# Função para adicionar notas dos alunos
def adicionar_notas():
    # Lista para armazenar as notas
    notas = []
    while True:
        try:
            # Solicita ao usuário que insira uma nota
            nota = float(input("Digite a nota do aluno (ou -1 para finalizar): "))
            # Verifica se o usuário deseja finalizar a entrada
            if nota == -1:
                break
            # Verifica se a nota está dentro do intervalo válido (0 a 10)
            if 0 <= nota <= 10:
                # Adiciona a nota à lista
                notas.append(nota)
            else:
                # Informa ao usuário que a nota é inválida
                print("Por favor, insira uma nota válida entre 0 e 10.")
        except ValueError:
            # Trata exceções caso a entrada não seja um número válido
            print("Entrada inválida! Por favor, insira um número.")
    return notas  # Retorna a lista de notas

# Função para calcular a média das notas
def calcular_media(notas):
    # Se não houver notas, retorna 0
    if len(notas) == 0:
        return 0
    # Calcula a média somando as notas e dividindo pela quantidade
    return sum(notas) / len(notas)

# Função para determinar a situação do aluno baseado na média
def determinar_situacao(media):
    # Se a média for maior ou igual a 7, o aluno está aprovado
    if media >= 7:
        return "Aprovado"
    else:
        # Caso contrário, o aluno está reprovado
        return "Reprovado"

# Função para exibir o relatório final com notas, média e situação
def exibir_relatorio(notas, media, situacao):
    print("\nRelatório Final:")
    print("Notas inseridas:", notas)  # Exibe as notas
    print("Média:", media)            # Exibe a média calculada
    print("Situação do aluno:", situacao)  # Exibe a situação do aluno

# Função principal que executa o programa
def main():
    print("Sistema de Gestão de Notas")  # Cabeçalho do sistema
    notas = adicionar_notas()           # Chama a função para adicionar notas
    media = calcular_media(notas)       # Chama a função para calcular a média
    situacao = determinar_situacao(media)  # Determina a situação do aluno
    exibir_relatorio(notas, media, situacao)  # Exibe o relatório final

# Ponto de entrada do programa
if __name__ == "__main__":
    main()  # Chama a função principal para iniciar a execução