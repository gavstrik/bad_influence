import numpy as np
import json
import networkx as nx
from networkx.readwrite import json_graph
from operator import itemgetter
import matplotlib.pyplot as plt
import random
from random import sample
random.seed(52)

num_players = 20
fraction_hub = 0.25
timesteps = 50

# scoring rules


G = nx.generators.powerlaw_cluster_graph(20, 2, 0.2)
node_and_degree = sorted(G.degree(), key=itemgetter(1), reverse=True)
hubs_in_graph, _ = map(list, zip(*node_and_degree[:int(num_players * fraction_hub)]))
normal_in_graph, _ = map(list, zip(*node_and_degree[int(num_players * fraction_hub):]))
print('hubs: ', hubs_in_graph)


# set attributes:
for p in range(num_players):
    if p in hubs_in_graph:
        G.node[p]['stubborness'] = np.random.uniform(0,1,1)[0]
        G.node[p]['preference'] = True
        G.node[p]['color'] = 'orange'
    else:
        G.node[p]['stubborness'] = np.random.uniform(0,1,1)[0]
        G.node[p]['preference'] = False
        G.node[p]['color'] = 'blue'
    print(p, G.node[p]['stubborness'])

# print(json.dumps(json_graph.node_link_data(G)))
colors = nx.get_node_attributes(G, 'color')
print('color: ', colors.values())


for timestep in range(timesteps):
    player = sample(G.nodes(),1)[0]  # choose a random player
    ego_net = nx.ego_graph(G, player) # get ego network
    pref = G.node[player]['preference']
    color = G.node[player]['color']
    stub = G.node[player]['stubborness']
    ego_net_prefs = nx.get_node_attributes(ego_net, 'preference').values()
    if pref == True:
        if sum(ego_net_prefs) < len(ego_net_prefs)/2: # if in minority
            if np.random.uniform(0,1,1)[0] < stub:
                G.node[player]['color'] = 'blue'
    else:
        if sum(ego_net_prefs) > len(ego_net_prefs)/2: # if in minority
            if np.random.uniform(0,1,1)[0] > stub:
                G.node[player]['color'] = 'orange'
    print(timestep, player, pref, color, stub, G.node[player]['color'])
    colors = nx.get_node_attributes(G, 'color')
nx.draw(G, node_color=colors.values(), with_labels = True)
plt.show()
