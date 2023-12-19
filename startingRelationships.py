import networkx as nx
import plotly.graph_objects as go
from macbeth import param
from matplotlib.colors import rgb2hex
import plotly.express as px

# Sample data for starting relationships
starting_relationships = [
    ('First Witch', 'Second Witch', 'Professional Bond'),
    ('Second Witch', 'First Apparition', 'Professional Bond'),
    ('Second Witch', 'Third Witch', 'Professional Bond'),
    ('Third Witch', 'First Witch', 'Professional Bond'),
    ('Hecate', 'Third Witch', 'Professional Bond'),
    ('Hecate', 'Second Witch', 'Professional Bond'),
    ('First Witch', 'Hecate', 'Professional Bond'),
    ('First Witch', 'First Apparition', 'Professional Bond'),
    ('First Witch', 'Second Apparition', 'Professional Bond'),
    ('First Witch', 'Third Apparition', 'Professional Bond'),
    ('Second Witch', 'Third Apparition', 'Professional Bond'),
    ('Second Witch', 'Second Apparition', 'Professional Bond'),
    ('Second Witch', 'Third Apparition', 'Professional Bond'),
    ('Third Witch', 'First Apparition', 'Professional Bond'),
    ('Third Witch', 'Second Apparition', 'Professional Bond'),
    ('Third Witch', 'Third Apparition', 'Professional Bond'),
    ('Malcolm', 'Captain', 'Friendship'),
    ('Banquo', 'Macbeth', 'Friendship'),
    ('Duncan', 'Macbeth', 'Friendship'),
    ('Macduff', 'Macbeth', 'Friendship'),
    ('Lady Macbeth', 'Macbeth', 'Marriage'),
    ('Lady Macduff', 'Macduff', 'Marriage'),
    ('First Witch', 'Macbeth', 'Competitors'),
    ('Second Witch', 'Macbeth', 'Competitors'),
    ('Third Witch', 'Macbeth', 'Competitors'),
    ('Lady Macbeth', 'Macbeth', 'Competitors'),
    ('Macbeth', 'Macbeth', 'Competitors'),
    ('Macbeth', 'Duncan', 'Competitors'),
    ('Macbeth', 'Banquo', 'Competitors'),
    ('Macbeth', "Lady Macbeth", "Competitors"),
    ('Hecate', 'Macbeth', 'Competitors'),
    ('Macbeth', 'Young Siward', 'Competitors'),
    ('Macduff', 'Macbeth', 'Competitors'),
     ("Macduff", "Malcolm", "Kinship"),
    ("Macduff", "Lennox", "Kinship"),
    ("Ross", "Macduff", "Kinship"),
    ("Macduff", "Ross", "Kinship"),
    ("Macduff", "Menteith", "Kinship"),
    ("Macduff", "Angus", "Kinship"),
    ("Macduff", "Caithness", "Kinship"),
    ("Malcolm", "Old Siward", "Kinship"),
    ("Malcolm", "Young Siward", "Kinship"),
    ("Menteith", "Caithness", "Kinship"),
    ("Menteith", "Angus", "Kinship"),
    ("Angus", "Lennox", "Kinship"),
    ("Lennox", "Ross", "Kinship"),
    ("Lady Macbeth", "Duncan", "Hospitality Bond"),
    ("Duncan", "Donalbain", "Paternal Bond"),
    ("Donalbain", "Malcolm", "Kinship"),
    ("Old Siward", "Seyton", "Paternal Bond"),
    ("Banquo", "Fleance", "Paternal Bond"),
    ("Young Siward", "Old Siward", "Paternal Bond"),
    ("Old Siward", "Malcolm", "Kinship"),
    ("Old Siward", "Duncan", "Kinship"),
    ("Lady Macduff", "Son", "Maternal Bond"),
    ("Macduff", "Porter", "Professional Bond"),
    ("Macbeth", "Seyton", "Professional Bond"),
    ("Macbeth", "First murderer", "Professional Bond"),
    ("Macbeth", "Second murderer", "Professional Bond"),
    ("Macbeth", "Third murderer", "Professional Bond"),

    
]

 #Create a directed graph
G = nx.DiGraph()

# Extract unique nodes from relationships
unique_nodes = set()

# Add nodes to the graph with additional attributes
for node in param['Character']:
    G.add_node(node, gender='Female' if param['Gender'][param['Character'].index(node)] == 'Female' else 'Male',
               place='Scotland', role='Character', description='Description')

# Add edges to the graph with initial relationships
for source, target, rel_type in starting_relationships:
    G.add_edge(source, target, relationship_type=rel_type)

    # Add nodes to the graph with additional attributes (if not already added)
    if source not in unique_nodes:
        G.add_node(source, gender='Female' if param['Gender'][param['Character'].index(source)] == 'Female' else 'Male',
                   place='Scotland', role='Character', description='Description')
        unique_nodes.add(source)

    if target not in unique_nodes:
        G.add_node(target, gender='Female' if param['Gender'][param['Character'].index(target)] == 'Female' else 'Male',
                   place='Scotland', role='Character', description='Description')
        unique_nodes.add(target)

# Calculate centrality measures
closeness_centrality = nx.closeness_centrality(G)
degree_centrality = nx.degree_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)
katz_centrality = nx.katz_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
average_clustering = nx.average_clustering(G)
density = nx.density(G)
modularity = nx.algorithms.community.modularity_max.greedy_modularity_communities(G)
components = nx.number_weakly_connected_components(G)

# Extract unique relationships from edges
unique_relationships = list(set(nx.get_edge_attributes(G, 'relationship_type').values()))

# Update node attributes with centrality measures
nx.set_node_attributes(G, closeness_centrality, 'closeness_centrality')
nx.set_node_attributes(G, degree_centrality, 'degree_centrality')
nx.set_node_attributes(G, eigenvector_centrality, 'eigenvector_centrality')
nx.set_node_attributes(G, katz_centrality, 'katz_centrality')
nx.set_node_attributes(G, betweenness_centrality, 'betweenness_centrality')

# Create layout of the graph
pos = nx.spring_layout(G, k=400, scale=50, seed=42)

# Create edge trace with hover information
edge_trace = []
color_dict = {rel: rgb2hex(px.colors.qualitative.Plotly[i % len(px.colors.qualitative.Plotly)]) for i, rel in enumerate(unique_relationships)}

for rel_type in unique_relationships:
    edges = [(source, target, data) for source, target, data in G.edges(data=True) if data.get('relationship_type') == rel_type]
    x_coords = []
    y_coords = []
    hover_texts = []

    for source, target, data in edges:
        x_coords.extend([pos[source][0], pos[target][0], None])
        y_coords.extend([pos[source][1], pos[target][1], None])
        hover_texts.append(f"Type: {data.get('relationship_type', 'Unknown')}")

    edge_trace.append(go.Scatter(
        x=x_coords,
        y=y_coords,
        line=dict(width=1, color=color_dict.get(rel_type, 'black')),
        hoverinfo='text',
        text=hover_texts,
        mode='lines',
        name=rel_type
    ))

# Create node trace with hover information
node_trace = go.Scatter(
    x=[pos[node][0] for node in G.nodes()],
    y=[pos[node][1] for node in G.nodes()],
    mode='markers',
    hoverinfo='text',
    marker=dict(
        color=['red' if G.nodes[node]['gender'] == 'Female' else 'blue' for node in G.nodes()],
        size=[300 * G.nodes[node]['degree_centrality'] for node in G.nodes()],
    ),
    text=[f"Character: {node}<br>Gender: {G.nodes[node]['gender']}<br>Place: {G.nodes[node]['place']}<br>Role: {G.nodes[node]['role']}<br>Description: {param['Description'][param['Character'].index(node)]}"
          f"<br>Closeness Centrality: {G.nodes[node].get('closeness_centrality', 'N/A')}"
          f"<br>Degree Centrality: {G.nodes[node].get('degree_centrality', 'N/A')}"
          f"<br>Eigenvector Centrality: {G.nodes[node].get('eigenvector_centrality', 'N/A')}"
          f"<br>Katz Centrality: {G.nodes[node].get('katz_centrality', 'N/A')}"
          f"<br>Betweenness Centrality: {G.nodes[node].get('betweenness_centrality', 'N/A')}"
          for node in G.nodes()],
)

# Create Plotly graph
fig = go.Figure(edge_trace + [node_trace])

# Update layout
fig.update_layout(
    showlegend=True,
    title="Starting Relationships",
    margin=dict(b=0, t=30, l=0, r=0),
)

fig.update_xaxes(showgrid=False, zeroline=False)
fig.update_yaxes(showgrid=False, zeroline=False)

# Calculate the diameter for the largest strongly connected component
largest_scc = max(nx.strongly_connected_components(G), key=len)
diameter_scc = nx.diameter(G.subgraph(largest_scc))
print(f"Diameter of the largest strongly connected component: {diameter_scc}")

nx.write_gexf(G, 'relations.gexf')

fig.show()