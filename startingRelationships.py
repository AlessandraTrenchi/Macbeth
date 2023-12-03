from distutils.util import change_root
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from macbeth import param
import matplotlib.cm as cm
from matplotlib.colors import rgb2hex

# Sample data for starting relationships
starting_relationships = [
    ('First Witch', 'Second Witch', 'Friendship'),
    ('Second Witch', 'Third Witch', 'Friendship'),
    ('Third Witch', 'First Witch', 'Friendship'),
    ('Hecate', 'Third Witch', 'Friendship'),
    ('Hecate', 'Second Witch', 'Friendship'),
    ('First Witch', 'Hecate', 'Friendship'),
    ('First Witch', 'First Apparition', 'Friendship'),
    ('First Witch', 'Second Apparition', 'Friendship'),
    ('First Witch', 'Third Apparition', 'Friendship'),
    ('Second Witch', 'Third Apparition', 'Friendship'),
    ('Second Witch', 'Second Apparition', 'Friendship'),
    ('Second Witch', 'Third Apparition', 'Friendship'),
    ('Third Witch', 'First Apparition', 'Friendship'),
    ('Third Witch', 'Second Apparition', 'Friendship'),
    ('Third Witch', 'Third Apparition', 'Friendship'),
    ('Malcolm', 'Captain', 'Friendship'),
    ('Banquo', 'Macbeth', 'Best Friends'),
    ('Duncan', 'Macbeth', 'Friendship'),
    ('Macduff', 'Macbeth', 'Friendship'),
    ('Lady Macbeth', 'Macbeth', 'Love')
]
# Create a directed graph
G = nx.DiGraph()

# Extract unique nodes from relationships
unique_nodes = set()
for source, target, _ in starting_relationships:
    unique_nodes.add(source)
    unique_nodes.add(target)

# Add nodes to the graph
for node in unique_nodes:
    G.add_node(node)  # You may want to provide additional attributes if needed

# Add edges to the graph with initial relationships
for source, target, rel_type in starting_relationships:
    G.add_edge(source, target, relationship_type=rel_type, weight=1)

# Now you can update the layout of the graph
# Create layout of the graph
pos = nx.spring_layout(G, seed=42)

# Ensure that 'Self' node is in the layout
if 'Self' not in pos:
    pos['Self'] = (0, 0)

for source, target, rel_type in starting_relationships:
    G.add_edge(source, target, relationship_type=rel_type, weight=1)  # Adding weight as 1

# Create layout of the graph
pos = nx.spring_layout(G, seed=42)

# Extract unique relationships from edges
unique_relationships = list(set(nx.get_edge_attributes(G, 'relationship_type').values()))

# Create a colormap for relationships
cmap = cm.get_cmap('tab10', len(unique_relationships))

# Create a legend for relationships
legend_data = []
for idx, rel in enumerate(unique_relationships):
    legend_data.append(go.Scatter(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(size=0, color=rgb2hex(cmap(idx))),
        legendgroup=rel,
        name=rel
    ))

# Create edge trace
edge_trace = []
color_dict = {rel: rgb2hex(cmap(idx % cmap.N)) for idx, rel in enumerate(unique_relationships)}

for edge in G.edges(data=True):
    source, target, data = edge
    edge_trace.append(go.Scatter(
        x=[pos[source][0], pos[target][0]],
        y=[pos[source][1], pos[target][1]],
        line=dict(width=data['weight'], color=color_dict[data['relationship_type']]),
        hoverinfo='none',
        mode='lines'
    ))

# Create node trace
node_trace = go.Scatter(
    x=[pos[node][0] for node in G.nodes()],
    y=[pos[node][1] for node in G.nodes()],
    mode='markers+text',
    hoverinfo='text',
    marker=dict(
        showscale=False,
        color=['red' if 'gender' in G.nodes[node] and G.nodes[node]['gender'] == 'Female' else 'blue' for node in G.nodes()]
    ),
    text=[node for node in G.nodes()],
    textposition='bottom center',
    textfont=dict(size=10),
    customdata=[[f"Character: {node}<br>Gender: {G.nodes[node].get('gender', 'N/A')}"] for node in G.nodes()]
)

# Create Plotly graph
fig = go.Figure(edge_trace + [node_trace])
fig.update_traces(
    hovertemplate='%{customdata}',  # Show attributes on hover
)

# Create relationship legends
for idx, rel in enumerate(unique_relationships):
    rel_str = rel
    fig.add_trace(go.Scatter(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(size=0, color=color_dict[rel]),
        legendgroup=rel,
        name=rel_str
    ))

# Update layout
fig.update_layout(
    showlegend=True,
    title="Starting Relationships",
    margin=dict(b=0, t=30, l=0, r=0),
)

fig.update_xaxes(showgrid=False, zeroline=False)
fig.update_yaxes(showgrid=False, zeroline=False)

fig.show()
