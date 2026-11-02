import turtle


# CONFIGURAÇÕES DO PROJETO
COMPRIMENTO_INICIAL = 100
ANGULO = 30
REDUCAO = 0.7
LIMITE = 5


def desenhar_arvore(t, comprimento):
    """
    Desenha uma árvore fractal utilizando recursividade.

    Parâmetros:
    t: objeto responsável pelo desenho.
    comprimento: tamanho do galho atual.
    """

    # Condição de parada da recursividade
    if comprimento < LIMITE:
        return

    # Desenha o galho principal
    t.forward(comprimento)

    # Primeira ramificação
    t.left(ANGULO)
    desenhar_arvore(t, comprimento * REDUCAO)

    # Segunda ramificação
    t.right(ANGULO * 2)
    desenhar_arvore(t, comprimento * REDUCAO)

    # Retorna à posição e direção anteriores
    t.left(ANGULO)
    t.backward(comprimento)


def main():

    # Configuração da janela
    tela = turtle.Screen()
    tela.title("Árvore Fractal - Python")
    tela.setup(width=1000, height=700)
    tela.bgcolor("white")

    # Configuração da caneta
    t = turtle.Turtle()
    t.speed(0)
    t.color("#263238")
    t.pensize(1)

    # Posicionamento inicial
    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()

    # Execução do algoritmo
    desenhar_arvore(t, COMPRIMENTO_INICIAL)

    # Oculta a tartaruga
    t.hideturtle()

    turtle.done()


if __name__ == "__main__":
    main()
