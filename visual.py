import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('macbeth.csv')

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph with gender and place attributes
for _, row in df.iterrows():
    character = row['Character']
    gender = row['Gender']
    place = row['Place of belonging']
    role = row['Role']

    # Add nodes with gender and place attributes
    G.add_node(character, gender=gender, place=place, role=role)

# Add edges based on the condition that nodes should have an edge between them if they all come from the same place
places = set(df['Place of belonging'])
for place in places:
    characters_in_place = df[df['Place of belonging'] == place]['Character'].tolist()
    for i in range(len(characters_in_place)):
        for j in range(i + 1, len(characters_in_place)):
            G.add_edge(characters_in_place[i], characters_in_place[j])

# Calculate and print various measures
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("Density:", nx.density(G))
print("Average clustering coefficient:", nx.average_clustering(G))
print("In-degree centrality:", nx.in_degree_centrality(G))
print("Out-degree centrality:", nx.out_degree_centrality(G))
print("PageRank:", nx.pagerank(G))
print("Hubs and authorities (hits):", nx.hits(G))
print("Closeness centrality:", nx.closeness_centrality(G))
print("Betweenness centrality:", nx.betweenness_centrality(G))
# Other measures can be added based on your specific requirements

# Create a color mapping based on gender
color_mapping = {
    'Female': 'red',
    'Male': 'blue',
}

# Assign colors to nodes based on the gender attribute
node_colors = [color_mapping.get(gender, 'gray') for gender in df['Gender']]

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, node_color=node_colors, font_size=8, font_color="black", font_weight="bold", edge_color="green", linewidths=0.3, arrowsize=10)

plt.title("Character Network - Macbeth")
nx.write_gexf(G, 'visual.gexf')
plt.show()
