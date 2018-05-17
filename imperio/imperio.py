import graph


def main():
    base_input = input() # le o input do usuario
    numero_vetex = int(base_input)
    gp = graph.Graph()
    for i in range(1, numero_vetex+1):
        gp.add_vertex(str(i))

    # numero_pares = int(base_input[1])
    for i in range(numero_vetex - 1):
        base_input = input().split(' ')
        gp.add_edge(gp.get_vertex(base_input[0]), gp.get_vertex(base_input[1]))
    inicial, final, anterior = gp.deep_first_search()
    particao = [1 for i in range(numero_vetex+1)]
    while len(final) != 0:
        menor= list(final.keys())[0]
        for key in final:
            if (final[key] < final[menor]):
                menor = key
        prev = anterior[menor]
        if prev:
            particao[int(prev.get_name())] += particao[int(menor.get_name())]
        final.pop(menor, None)
    menor = numero_vetex
    for i in particao:
        diferenca = abs(i*2 - numero_vetex)
        if (diferenca < menor):
            menor = diferenca
    
    print(menor)


main()