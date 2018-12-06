import random
import sys


def create_graph(graph_size=4096, density=100, max_dist=1000, file_name="graph.txt"):

    file = open(file_name, 'w')
    file.write("{}\n".format(graph_size))

    for i in range(1, graph_size+1):
        for j in range(1, graph_size+1):
            if i != j and random.randint(1, 100) > (100 - density):
                file.write("{} {} {}\n".format(i, j, random.randint(1, max_dist)))
                
    file.close()

    return


if __name__ == '__main__':


    args = sys.argv

    if len(args) > 1:
        print("creating graph of size {}".format(args[1]))
        create_graph(graph_size=int(args[1]), file_name="g{}.txt".format(args[1]))

    else:
        for i in range(1,11):
            create_graph(i*100, 100, 1000, "g{}.txt".format(i))

