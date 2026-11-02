# 🌳 Árvore Fractal com Python

Projeto desenvolvido em Python para demonstrar a construção de uma árvore fractal utilizando recursividade e a biblioteca Turtle Graphics.

A aplicação gera uma estrutura de ramificações progressivamente menores, explorando conceitos de lógica de programação, matemática e visualização computacional.

## 📸 Demonstração

![Árvore Fractal](assets/arvore_fractal.png)

## 🎯 Objetivo

Desenvolver uma representação gráfica de uma árvore fractal por meio de um algoritmo recursivo, explorando a repetição de padrões e a aplicação de conceitos matemáticos na programação.

## 🛠️ Tecnologias utilizadas

- Python 3
- Turtle Graphics
- Recursividade
- Matemática e geometria

## ⚙️ Funcionalidades

- Geração automática de uma árvore fractal.
- Criação de ramificações utilizando recursividade.
- Redução progressiva do comprimento dos galhos.
- Configuração dos ângulos de ramificação.
- Personalização do comprimento inicial e do limite de profundidade.
- Renderização gráfica utilizando Turtle Graphics.

## 🧠 Conceitos aplicados

### Recursividade

A recursividade consiste em uma função que chama a si mesma para executar determinada tarefa.

Neste projeto, cada galho gera duas novas ramificações, seguindo o mesmo padrão de construção até atingir uma condição de parada.

### Caso-base

O caso-base determina quando a função deve interromper as chamadas recursivas.

Neste projeto, a execução termina quando o comprimento da ramificação fica abaixo do limite estabelecido.

### Fractais

Fractais são estruturas matemáticas que apresentam padrões semelhantes em diferentes escalas.

A árvore fractal representa esse comportamento por meio de ramificações progressivamente menores.

## 📂 Estrutura do projeto

```text
arvore-fractal-python/
│
├── README.md
├── arvore_fractal.py
│
└── assets/
    └── arvore_fractal.png
```

## 🚀 Como executar

### Pré-requisitos

- Python 3 instalado.
- Visual Studio Code ou outro ambiente de desenvolvimento.
- Suporte gráfico para execução do Turtle.

A biblioteca Turtle faz parte da biblioteca padrão do Python, não sendo necessária instalação adicional.

### Executando o projeto

Clone o repositório:

```bash
git clone https://github.com/carlosaugustosoares/arvore-fractal-python.git
```

Entre na pasta:

```bash
cd arvore-fractal-python
```

Execute o programa:

```bash
python arvore_fractal.py
```

## 🔧 Parâmetros de configuração

O comportamento da árvore pode ser modificado por meio dos seguintes parâmetros:

| Parâmetro | Descrição |
|---|---|
| `COMPRIMENTO_INICIAL` | Define o tamanho inicial do tronco. |
| `ANGULO` | Controla o ângulo das ramificações. |
| `REDUCAO` | Determina a proporção de redução dos galhos. |
| `LIMITE` | Define a condição de parada da recursividade. |

## 📈 Possibilidades de evolução

- Personalização das cores das ramificações.
- Criação de diferentes padrões fractais.
- Controle da profundidade da recursividade.
- Desenvolvimento de novas formas geométricas.

## 📚 Aprendizados

O projeto proporcionou a aplicação prática de conceitos de lógica de programação, funções recursivas, estruturas matemáticas e visualização gráfica utilizando Python.

---

**Autor:** Carlos Augusto

**Tecnologias:** Python | Turtle Graphics | Recursividade
