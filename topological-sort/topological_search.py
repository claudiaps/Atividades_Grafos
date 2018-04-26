'''
    Erdos Number Class
'''

import graph
import copy

def main():
    qtdInput = int(input())  # le o input do usuario

    no_teste = 1
    gp = {}  # cria uma estrutura para armazenar todos os testes

    while(qtdInput != 0):  # le novos inputs até digitar um 0
        gp[no_teste] = graph.Graph(directed=True)  # grafo para o novo teste
        nodes = input()
        nodes_array = nodes.split(' ')
        for node in nodes_array:
            gp[no_teste].add_vertex(node)
        for i in range(qtdInput):  # le todos os autores de todos os artigos
            requirements = input().split(' ')
            for requirement in requirements[2:]:
                gp[no_teste].add_edge(gp[no_teste].get_vertex(requirements[0]), gp[no_teste].get_vertex(requirement))


        qtdInput = int(input())  # le o novo input
        no_teste += 1

    for key in gp:
        print("")
        print("Teste", key)
        no_requirements = []
        for people in gp[key].get_all_vertex():
            if (gp[key].in_degree_vertex(people) == 0):
                no_requirements.append(people)
        
        sorted_list = []
        while(len(no_requirements) > 0):
            n = no_requirements.pop()
            sorted_list.append(n)
            adjacents = gp[key].adjacents_vertex(n)[:]
            for adjacent in adjacents:
                gp[key].remove_edge(gp[key].get_edge_from_souce_destination(n, adjacent))
                if gp[key].in_degree_vertex(adjacent) == 0:
                    no_requirements.append(adjacent)
     
        if len(gp[key].get_all_edges()) != 0:
            print("impossivel", end="")
        else:
            for item in reversed(sorted_list):
                print(item, end=" ")
        print("")





if __name__ == '__main__':
    main()
