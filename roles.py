import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

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
        # Antagonist goes against the protagonist
        G.add_edge(character, 'Macbeth', role=role)
    elif role == 'Confidant':
        # Confidant is deeply trusted by the protagonist
        G.add_edge('Macbeth', character, role=role)
    elif role == 'Henchman':
        # Henchman helps the protagonist
        G.add_edge('Macbeth', character, role=role)

# Create a color mapping based on the role attribute for edges
edge_color_mapping = {
    'Antagonist': 'red',
    'Confidant': 'green',
    'Henchman': 'blue',
}

# Assign colors to edges based on the role attribute
edge_colors = [edge_color_mapping.get(G[ed[0]][ed[1]]['role'], 'gray') for ed in G.edges()]

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, node_color=['red' if g == 'Female' else 'blue' for g in df['Gender']], font_size=8, font_color="black", font_weight="bold", edge_color=edge_colors, linewidths=2, arrowsize=10)

# Create a legend for relationship types
legend_labels = {role: color for role, color in edge_color_mapping.items()}
legend_labels['Other'] = 'gray'  # For edges with roles not in the mapping
legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label) for label, color in legend_labels.items()]
plt.legend(handles=legend_handles, title="Relationship Types", loc='upper left')

plt.title("Character Network - Macbeth")
plt.show()
