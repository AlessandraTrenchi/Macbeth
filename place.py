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

# Create a color mapping based on place and gender
color_mapping = {
    'Unknown_Female': 'red',
    'Unknown_Male': 'blue',
    'Glamis_Male': 'green',
    'Scotland_Female': 'purple',
    'Scotland_Male': 'orange',
}

# Assign colors to nodes based on the color mapping
node_colors = [color_mapping.get(f"{place}_{gender}", 'gray') for place, gender in zip(df['Place of belonging'], df['Gender'])]

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, node_color=node_colors, font_size=8, font_color="black", font_weight="bold", edge_color="green", linewidths=0.3, arrowsize=10)

plt.title("Character Network - Macbeth")
plt.show()
