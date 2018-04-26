import graph


def main():
    first_input = input().split(' ')
    n_ilhas = int(first_input[0])
    n_pontes = int(first_input[1])
    n_sede = int(first_input[2])
    gp = graph.Graph()
    for i in range(1, n_ilhas + 1):
        gp.add_vertex(str(i))

    for i in range(n_pontes):
        ponte = input().split(' ')
        gp.add_edge(gp.get_vertex(ponte[0]), gp.get_vertex(
            ponte[1]), value=int(ponte[2]))

    sedes = {}
    for i in range(n_sede):
        sede_deposito = input().split(' ')
        sedes[i] = [sede_deposito[0], sede_deposito[1]]

    tree = graph.Graph()
    edges = gp.get_all_edges()
    edges.sort(key=lambda x: x.get_value(), reverse=True)
    
    for edge in edges:
        if not tree.get_vertex(edge.get_source().get_name()):
            tree.add_edge(edge.get_source(), edge.get_destination(), value=edge.get_value())
        elif not tree.get_vertex(edge.get_destination().get_name()):
            tree.add_edge(edge.get_source(), edge.get_destination(), value=edge.get_value())
    
    for sede in sedes:
        deposito = sedes[sede][1]
        distancia = tree.breadth_first_search(tree.get_vertex(sedes[sede][0]))
        print(distancia[tree.get_vertex(deposito)])


main()
