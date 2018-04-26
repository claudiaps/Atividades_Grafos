import graph


def main():
    base_input = input().split(' ')  # le o input do usuario

    no_teste = 1
    gp = {}  # cria uma estrutura para armazenar todos os testes

    while(base_input[0] != '0' or base_input[1] != '0'):  # le novos inputs até digitar um 0
        gp[no_teste] = graph.Graph()  # grafo para o novo teste
        for i in range(1, int(base_input[0]) + 1):  # le todos os autores de todos os artigos
            gp[no_teste].add_vertex(str(i))

        for i in range(int(base_input[1])):
            estacao = input().split(' ')
            gp[no_teste].add_edge(gp[no_teste].get_vertex(estacao[0]), gp[no_teste].get_vertex(estacao[1]))

        base_input = input().split(' ')  # le o novo input
        no_teste += 1

    for key in gp:
        print("")
        print("Teste", key)

        distancia = gp[key].breadth_search(
            gp[key].get_vertex('1'))

        normal = True
        for i in distancia:
            if distancia[i] == float('inf') and normal:
                normal = False
        if normal:
            print('normal')
        else:
            print('falha')
        print('')

main()