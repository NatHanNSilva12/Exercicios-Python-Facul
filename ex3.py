import sqlite3  # Importa a biblioteca para trabalhar com SQLite
import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa a biblioteca Matplotlib para visualizações
import seaborn as sns  # Importa a biblioteca Seaborn para visualizações aprimoradas

# Passo 1: Conectar ao banco de dados SQLite e criar uma tabela
# Passo 1.1: Conectar ao banco de dados (ou criar, se não existir)
conexao = sqlite3.connect('dados_vendas.db')

# Passo 1.2: Criar um cursor
cursor = conexao.cursor()

# Passo 1.3: Criar uma tabela (se não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
''')

# Passo 1.4: Inserir alguns dados (se a tabela estiver vazia)
cursor.execute('''
SELECT COUNT(*) FROM vendas1
''')
if cursor.fetchone()[0] == 0:  # Verifica se a tabela está vazia antes de inserir dados
    cursor.execute('''
    INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
    ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
    ('2023-01-05', 'Produto B', 'Roupas', 350.00),
    ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
    ('2023-03-15', 'Produto D', 'Livros', 200.00),
    ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),
    ('2023-10-05', 'Produto L', 'Roupas', 450.00),
    ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
    ('2023-12-20', 'Produto N', 'Livros', 250.00);
    ''')
    
# Passo 1.5: Confirmar as mudanças
conexao.commit()

# Passo 2: Explorar e preparar os dados
# Carrega os dados da tabela vendas1 em um DataFrame do Pandas
df_vendas = pd.read_sql_query('SELECT * FROM vendas1', conexao)

# Exibe as primeiras linhas do DataFrame para inspeção
print(df_vendas.head())

# Passo 3: Análise dos dados
# Calcula o total de vendas por categoria
total_vendas_categoria = df_vendas.groupby('categoria')['valor_venda'].sum().reset_index()
print("\nTotal de vendas por categoria:")
print(total_vendas_categoria)

# Calcula o total de vendas por mês
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])  # Converte a coluna de data para o tipo datetime
df_vendas['mes'] = df_vendas['data_venda'].dt.to_period('M')  # Cria uma nova coluna para o mês
total_vendas_mensal = df_vendas.groupby('mes')['valor_venda'].sum().reset_index()
print("\nTotal de vendas por mês:")
print(total_vendas_mensal)

# Passo 4: Visualização dos dados
# Gráfico de vendas por categoria
plt.figure(figsize=(10, 5))
sns.barplot(data=total_vendas_categoria, x='categoria', y='valor_venda', palette='viridis')
plt.title('Total de Vendas por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Total de Vendas (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico de vendas mensais
plt.figure(figsize=(10, 5))
# Convert the 'mes' column to strings before plotting
sns.lineplot(data=total_vendas_mensal, x='mes'.astype(str), y='valor_venda', marker='o')
plt.title('Total de Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Total de Vendas (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Passo 5: Conclusão e análise de insights
# Exibir insights a partir das análises
print("Insights:")
print("1. A categoria 'Eletrônicos' teve o maior total de vendas.")
print("2. As vendas variaram ao longo do ano, com meses específicos apresentando picos.")
print("3. Recomenda-se um foco maior em promoções para a categoria 'Roupas', pois apresenta vendas mais baixas.")

# Fechar a conexão com o banco de dados
conexao.close()