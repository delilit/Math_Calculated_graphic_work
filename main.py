import networkx as nx
import matplotlib.pyplot as plt

def array_offset(array, offset):
    new_array = []
    result = []
    addiction = 0
    for i in range(0, len(array)):
        if array[(i + addiction + offset*(i))%len(array)] in new_array:
            result.append(new_array)
            new_array = []
            addiction += 1
        new_array.append(array[(i + addiction + offset*(i))%len(array)])
    result.append(new_array)
    return result

def get_positions(lenghts):
    pos = {}
    addiction = 0
    if len(lenghts) % 2 == 0:
        addiction = 1
        pos["e"] = (len(lenghts)/2,-5)
    else:
        pos["e"] = (len(lenghts)/2, -5)
    for i in range(len(lenghts)):
        if i >= len(lenghts)//2:
            pos["a_"+str(i+1)] = (i+addiction,lenghts[i])
        else:
            pos["a_"+str(i+1)] = (i,lenghts[i])
    return pos
def get_positions_straight(lenghts):
    lenghs = set(lenghts)


def get_edges(lenghts):
    edges = []
    edges.append(("e", "a_1"))
    edges.append(("e", "a_"+str(len(lenghts))))
    for i in range(len(lenghts)-1):
        edges.append(("a_"+str(i+1), "a_"+str(i+2)))
    return edges

if __name__ == "__main__":
    number = int(input())
    array = []

    for i in range(number):
        array.append(i)

    arrays = [[array]]

    lenghts = [len(array)]

    for i in range(1, number):
        arrays.append(array_offset(array, i))
        lenghts.append(len(arrays[-1][-1]))
    lenghts.pop()

    #making a graph
    G = nx.Graph()
    edges = get_edges(lenghts)
    G.add_edges_from(edges)
    pos = get_positions(lenghts)
    
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000)

    y_coords = sorted(set(y for x, y in pos.values()), reverse=True)
    min_x = min(x for x, y in pos.values())

    for y in y_coords:
        plt.text(min_x - 1, y, f"{y}", fontsize=8, color='black', ha='right', va='center')
    #making a second graph
    plt.figure(figsize=(8, 4))
    G2 = nx.Graph()
    

    plt.grid(True)
    plt.show()
