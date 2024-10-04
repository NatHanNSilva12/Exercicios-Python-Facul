# Passo 1: Importar Bibliotecas e Carregar Dados
import tensorflow as tf  # Importa a biblioteca TensorFlow
import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados
from sklearn.datasets import load_iris  # Importa o conjunto de dados Iris do scikit-learn
from sklearn.model_selection import train_test_split  # Importa a função para dividir dados em treino e teste
from sklearn.preprocessing import StandardScaler  # Importa o escalador para normalização dos dados

# Carregar conjunto de dados Iris
iris = load_iris()  # Carrega o conjunto de dados
X = iris.data  # Atributos (comprimento e largura das sépalas e pétalas)
y = iris.target  # Classes (espécies das flores)

# Passo 2: Pré-processamento dos Dados
# Dividir o conjunto de dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar os dados
scaler = StandardScaler()  # Cria um objeto StandardScaler
X_train = scaler.fit_transform(X_train)  # Ajusta e transforma os dados de treinamento
X_test = scaler.transform(X_test)  # Transforma os dados de teste

# Passo 3: Construir o Modelo
# Criar um modelo sequencial
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(X_train.shape[1],)),  # Camada oculta com 10 neurônios
    tf.keras.layers.Dense(3, activation='softmax')  # Camada de saída com 3 neurônios (uma para cada classe)
])

# Compilar o modelo
model.compile(optimizer='adam',  # Otimizador Adam
              loss='sparse_categorical_crossentropy',  # Função de perda para classificação
              metrics=['accuracy'])  # Métrica de precisão

# Passo 4: Treinar o Modelo
model.fit(X_train, y_train, epochs=100)  # Treina o modelo por 100 épocas

# Passo 5: Avaliar o Modelo
loss, accuracy = model.evaluate(X_test, y_test)  # Avalia o modelo com os dados de teste
print(f'Accuracy: {accuracy:.2f}')  # Exibe a precisão do modelo

# Passo 6: Fazer Previsões
predictions = model.predict(X_test)  # Faz previsões com os dados de teste
predicted_classes = tf.argmax(predictions, axis=1)  # Obtém a classe prevista para cada exemplo

# Exibe as previsões
print("Predictions:", predicted_classes.numpy())  # Converte para numpy e exibe
print("True Labels:", y_test)  # Exibe as classes verdadeiras
