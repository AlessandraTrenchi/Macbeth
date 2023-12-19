import networkx as nx
import plotly.graph_objects as go
from macbeth import param
from matplotlib.colors import rgb2hex
import plotly.express as px

# Sample data for starting relationships
starting_relationships = [
    ('First Witch', 'Second Witch', 'Professional Bond'),
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
    
]

# Create a directed graph
G = nx.DiGraph()

# Extract unique nodes from relationships
unique_nodes = set()
# Add edges to the graph with initial relationships and assign weights based on relationship type
for source, target, rel_type in starting_relationships:
    weight = 1  # default weight
    if rel_type == 'Best Friends':
        weight = 2
    elif rel_type == 'Love':
        weight = 3

    G.add_edge(source, target, relationship_type=rel_type, weight=weight)

# Add nodes to the graph with additional attributes
for node in unique_nodes:
    G.add_node(node, gender='Female' if param['Gender'][param['Character'].index(node)] == 'Female' else 'Male',
               place='Scotland', role='Character', description='Description')

## Add edges to the graph with initial relationships and assign weights based on relationship type
for source, target, rel_type in starting_relationships:
    weight = 1  # default weight
    if rel_type == 'Best Friends':
        weight = 2
    elif rel_type == 'Love':
        weight = 3

    G.add_edge(source, target, relationship_type=rel_type, weight=weight)

    # Add nodes to the graph with additional attributes
    G.add_node(source, gender='Female' if param['Gender'][param['Character'].index(source)] == 'Female' else 'Male',
               place='Scotland', role='Character', description='Description')
    G.add_node(target, gender='Female' if param['Gender'][param['Character'].index(target)] == 'Female' else 'Male',
               place='Scotland', role='Character', description='Description')

# Create layout of the graph
pos = nx.spring_layout(G, k=400, scale=50, seed=42)

# Add degree centrality as node attribute
degree_centrality = nx.degree_centrality(G)
nx.set_node_attributes(G, degree_centrality, 'degree_centrality')

# Extract unique relationships from edges
unique_relationships = list(set(nx.get_edge_attributes(G, 'relationship_type').values()))

# Create edge trace with hover information
edge_trace = []
color_dict = {rel: rgb2hex(px.colors.qualitative.Plotly[i % len(px.colors.qualitative.Plotly)]) for i, rel in enumerate(unique_relationships)}

for rel_type in unique_relationships:
    edges = [(source, target, data) for source, target, data in G.edges(data=True) if data['relationship_type'] == rel_type]
    x_coords = []
    y_coords = []
    hover_texts = []

    for source, target, data in edges:
        x_coords.extend([pos[source][0], pos[target][0], None])
        y_coords.extend([pos[source][1], pos[target][1], None])
        hover_texts.append(f"Type: {data['relationship_type']}<br>Weight: {data['weight']}")

    edge_trace.append(go.Scatter(
        x=x_coords,
        y=y_coords,
        line=dict(width=data['weight'], color=color_dict[rel_type]),
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
    text=[f"Character: {node}<br>Gender: {G.nodes[node]['gender']}<br>Place: {G.nodes[node]['place']}<br>Role: {G.nodes[node]['role']}<br>Description: {param['Description'][param['Character'].index(node)]}" for node in G.nodes()],
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
nx.write_gexf(G, 'relationships1.gexf')

fig.show()
