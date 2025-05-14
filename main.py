# -*- coding: utf-8 -*-
#All comentaries was made by me (not chatbot) for better understanding of the code by myself either.
#It's on english, because i think it's better get used to using English only.
import networkx as nx
import matplotlib.pyplot as plt

#Returning a new array of arrays that jumps over a certain number of elements.
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

#This function is used to get the positions of the nodes in the graph.
def get_positions(lenghts):
    pos = {}
    addiction = 0
    if len(lenghts) % 2 == 0:
        addiction = 1
    pos["e"] = (len(lenghts)//2+1,-5)
        
    for i in range(len(lenghts)):
        if i >= len(lenghts)//2:
            pos["a_"+str(i+1)] = (1+i+addiction,lenghts[i])
        else:
            pos["a_"+str(i+1)] = (1+i,lenghts[i])
    return pos
#Same as the function above, but for the second graph that is straight.
def get_positions_straight(lenghts):
    lenghs_checkout = []
    pos = {}
    for lenght in lenghts:
        if lenght not in lenghs_checkout:
            lenghs_checkout.append(lenght)
    lenghs_checkout.sort()
    for i in range(len(lenghs_checkout)):
        pos[str(lenghs_checkout[i])] = (i, 0)
    return pos

#Returns the edges of the graph.
def get_edges(lenghts):
    edges = []
    edges.append(("e", "a_1"))
    edges.append(("e", "a_"+str(len(lenghts))))
    for i in range(len(lenghts)-1):
        edges.append(("a_"+str(i+1), "a_"+str(i+2)))
    return edges
#Returns the edges of the second graph that is straight.
def get_edges_straight(lenghts):
    edges = []
    lenghts_checkout = []
    for lenght in lenghts:
        if lenght not in lenghts_checkout:
            lenghts_checkout.append(lenght)
    if len(lenghts_checkout) == 2:
        return [("0", "0")]
    lenghts_checkout.sort()
    lenghts_checkout.pop()
    for i in range(len(lenghts_checkout)-1):
        edges.append((str(lenghts_checkout[i]), str(lenghts_checkout[i+1])))
    return edges

if __name__ == "__main__":
    number = int(input("please enter a number of elements: "))
    array = []

    for i in range(number):
        array.append(i)

    arrays = [[array]]

    lenghts = [len(array)]

    for i in range(1, number):
        arrays.append(array_offset(array, i))
        lenghts.append(len(arrays[-1][-1]))
    lenghts.pop()

    #Building first graph
    G = nx.Graph()
    edges = get_edges(lenghts)
    G.add_edges_from(edges)
    pos = get_positions(lenghts)
    
    plt.figure(figsize=(10, 6))
    plt.xlim(0, len(lenghts)+2)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000)

    #Y coordinates for better visualization
    y_coords = sorted(set(y for x, y in pos.values()), reverse=True)

    for y in y_coords:
        if y == -5:
            plt.text(0, y, f"e-", fontsize=8, color='black', ha='right', va='center')    
        else:
            plt.text(0, y, f"{y}-", fontsize=8, color='black', ha='right', va='center')
    
    #building a second graph
    straight_pos = get_positions_straight(lenghts)
    straight_edges = get_edges_straight(lenghts)

    #it's will not happe if we have only one element
    if straight_edges != [("0", "0")]:
        plt.figure(figsize=(8, 4))
        G2 = nx.Graph()
        G2.add_edges_from(straight_edges)
        nx.draw(G2, straight_pos, with_labels=True, node_color='red', node_size=1000)
    #Showing the graph(s)
    plt.grid(True)
    plt.show()
