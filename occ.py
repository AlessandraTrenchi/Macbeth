import networkx as nx
import matplotlib.pyplot as plt
from allmac import scenes

# Initialize a directed graph
G = nx.DiGraph()

# Iterate through scenes and add edges based on character co-participation
for scene in scenes:
    for i, character1 in enumerate(scene):
        for character2 in scene[i+1:]:
            if G.has_edge(character1, character2):
                G[character1][character2]['weight'] += 1
            else:
                G.add_edge(character1, character2, weight=1)

# Draw the graph
pos = nx.spring_layout(G)
edge_labels = {(char1, char2): G[char1][char2]['weight'] for (char1, char2) in G.edges()}
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1000, font_size=10, font_color='black', font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Show the plot
plt.show()

# Calculate the weight of nodes
node_weights = {node: sum(G[node][neighbor]['weight'] for neighbor in G.neighbors(node)) for node in G.nodes()}

# Print node weights
print("Node Weights:")
for node, weight in node_weights.items():
    print(f"{node}: {weight}")
