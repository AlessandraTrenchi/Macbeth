import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import community

# Load the dataset
df = pd.read_csv('macbeth.csv')

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph with gender, place, and role attributes
for _, row in df.iterrows():
    character = row['Character']
    gender = row['Gender']
    place = row['Place of belonging']
    role = row['Role']

    # Add nodes with gender, place, and role attributes
    G.add_node(character, gender=gender, place=place, role=role)

# Add edges based on the specified relationships
for _, row in df.iterrows():
    character = row['Character']
    role = row['Role']

    # Add edges based on the role attribute
    if role == 'Antagonist':
        G.add_edge(character, 'Macbeth', role=role)
    elif role == 'Confidant':
        G.add_edge('Macbeth', character, role=role)
    elif role == 'Henchman':
        G.add_edge('Macbeth', character, role=role)

# Create a color mapping based on the role attribute for edges
edge_color_mapping = {'Antagonist': 'red', 'Confidant': 'green', 'Henchman': 'blue'}
edge_colors = [edge_color_mapping.get(G[ed[0]][ed[1]]['role'], 'gray') for ed in G.edges()]

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, node_color=['red' if g == 'Female' else 'blue' for g in df['Gender']],
        font_size=8, font_color="black", font_weight="bold", edge_color=edge_colors, linewidths=2, arrowsize=10,
        cmap=plt.cm.tab10)

# Create a legend for relationship types
legend_labels = {role: color for role, color in edge_color_mapping.items()}
legend_labels['Other'] = 'gray'  # For edges with roles not in the mapping
legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label)
                  for label, color in legend_labels.items()]
plt.legend(handles=legend_handles, title="Relationship Types", loc='upper left')

plt.title("Character Network - Macbeth")

# Calculate and add centrality measures as node attributes
centrality_measures = {
    'degree_centrality': nx.degree_centrality(G),
    'betweenness_centrality': nx.betweenness_centrality(G),
    'closeness_centrality': nx.closeness_centrality(G),
    'eigenvector_centrality': nx.eigenvector_centrality(G, max_iter=1000)
}

for measure, values in centrality_measures.items():
    nx.set_node_attributes(G, values, measure)

# Convert the directed graph to an undirected graph
G_undirected = G.to_undirected()

# Apply Louvain community detection algorithm
partition = community.best_partition(G_undirected)


# Add community information as node attribute
nx.set_node_attributes(G, partition, 'community')

# Draw the graph with different colors for each community
node_colors_community = list(partition.values())
nx.draw(G, pos, with_labels=True, node_size=500, node_color=node_colors_community,
        font_size=8, font_color="black", font_weight="bold", edge_color=edge_colors, linewidths=2, arrowsize=10,
        cmap=plt.cm.tab10)

# Convert the directed graph to an undirected graph
G_undirected = G.to_undirected()

# Detect and add cliques as node attributes
cliques = list(nx.find_cliques(G_undirected))

# Flatten the list of cliques to create a list of nodes in each clique
flattened_cliques = [node for clique in cliques for node in clique]

# Create a dictionary to map each node to its clique index
clique_dict = {node: idx for idx, nodes in enumerate(cliques) for node in nodes}
nx.set_node_attributes(G, clique_dict, 'clique_membership')

# Draw the graph with different colors for each clique
clique_colors = [clique_dict[node] for node in G.nodes()]
nx.draw(G, pos, with_labels=True, node_size=500, node_color=clique_colors,
        font_size=8, font_color="black", font_weight="bold", edge_color=edge_colors, linewidths=2, arrowsize=10,
        cmap=plt.cm.tab10)
# Save the graph in GEXF format
nx.write_gexf(G, 'roles.gexf')
# Show plot
plt.show()
