import graph


def main():
    base_input = input().split(' ')  # le o input do usuario
    numero_cidades = int(base_input[0])
    destino = int(base_input[1])
    origem = int(base_input[2])
    gp = graph.Graph()
    for i in range(1, numero_cidades+1):
        gp.add_vertex(str(i))

    # numero_pares = int(base_input[1])
    for i in range(numero_cidades - 1):
        base_input = input().split(' ')
        gp.add_edge(gp.get_vertex(base_input[0]), gp.get_vertex(base_input[1]), value=int(base_input[2]))
    distance = gp.dijkistra(gp.get_vertex(str(destino)))
    print(distance[gp.get_vertex(str(origem))])
main()