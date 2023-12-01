import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from macbeth import param
from matplotlib.colors import rgb2hex
import plotly.express as px

# Define kinship relationships with weights
kinship_relations = [
    ("Macduff", "Malcolm", "cousins", 2),
    ("Macduff", "Lennox", "cousins", 2),
    ("Ross", "Macduff", "cousins", 2),
    ("Macduff", "Ross", "cousins", 2),
    ("Macduff", "Menteith", "cousins", 2),
    ("Macduff", "Angus", "cousins", 2),
    ("Macduff", "Caithness", "cousins", 2),
    ("Malcolm", "Old Siward", "nephew", "uncle", 2),
    ("Malcolm", "Young Siward", "cousins", 2),
    ("Menteith", "Caithness", "cousins", 2),
    ("Menteith", "Angus", "cousins", 2),
    ("Angus", "Lennox", "cousins", 2),
    ("Lennox", "Ross", "cousins", 2),
    ("Lady Macbeth", "Duncan", "host", "subject", 1),
    ("Duncan", "Donalbain", "father", "son", 3),
    ("Donalbain", "Malcolm", "brothers", 3),
    ("Lady Macbeth", "Macbeth", "wife", "husband", 3),
    ("Duncan", "Lady Macbeth", "lost father", "lost child", 2),
    ("Old Siward", "Seyton", "son", "father", 3),
    ("Banquo", "Fleance", "father", "son", 3),
    ("Young Siward", "Old Siward", "son", "father", 2),
    ("Macduff", "Porter", "master", "servant", 1),
    ("Old Siward", "Malcolm", "uncle", "nephew", 2),
    ("Old Siward", "Duncan", "brothers", 3)
]


# Add edges with attributes
# Add edges with attributes
G = nx.DiGraph()
for relation in kinship_relations:
    if len(relation) == 4:
        G.add_edge(relation[0], relation[1], relationship=(relation[2], relation[3]))
    else:
        G.add_edge(relation[0], relation[1], relationship=relation[2])

# Add nodes with attributes
for idx, character in enumerate(param['Character']):
    gender = param['Gender'][idx]
    place = param['Place of belonging'][idx]
    description = param['Description'][idx]
    role = param['Role'][idx]
    G.add_node(character, gender=gender, place=place, description=description, role=role)

# Extract unique relationships from edges
unique_relationships = list(set(nx.get_edge_attributes(G, 'relationship').values()))

# Create layout of the graph using Spring layout
pos = nx.spring_layout(G, k=400, scale=50)

# Calculate degree centrality for each node
degree_centrality = nx.degree_centrality(G)

# Scale node sizes based on degree centrality
node_sizes = [500 * degree_centrality[node] for node in G.nodes()]

# Create edge trace
edge_trace = []

# Create a colormap for relationships
cmap = px.colors.qualitative.Plotly

for idx, edge in enumerate(G.edges(data=True)):
    rel_type = edge[2]['relationship']
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_trace.append(go.Scatter(x=(x0, x1, None), y=(y0, y1, None), mode='lines', line=dict(width=2, color=rgb2hex(cmap[idx % len(cmap)])), hoverinfo='none', legendgroup=f"edge_{idx}"))  # Update to use the index of the relationship

# Create node trace
node_trace = go.Scatter(
    x=[pos[node][0] for node in G.nodes()],
    y=[pos[node][1] for node in G.nodes()],
    mode='markers+text',
    hoverinfo='text',
    marker=dict(
        showscale=False,
        size=node_sizes,
        color=['red' if 'gender' in G.nodes[node] and G.nodes[node]['gender'] == 'Female' else 'blue' for node in G.nodes()]
    ),
    text=[node for node in G.nodes()],
    textposition='bottom center',
    textfont=dict(size=10),
    customdata=[[f"Character: {node}<br>Gender: {G.nodes[node].get('gender', 'N/A')}<br>Place: {G.nodes[node].get('place', 'N/A')}<br>Description: {G.nodes[node].get('description', 'N/A')}<br>Role: {G.nodes[node].get('role', 'N/A')}"] for node in G.nodes()]
)

# Create Plotly graph
fig = go.Figure(edge_trace + [node_trace])
fig.update_traces(
    hovertemplate='%{customdata}',  # Show attributes on hover
)

# Create relationship legends
for idx, rel in enumerate(set(nx.get_edge_attributes(G, 'relationship').values())):
    rel_str = ', '.join(map(str, rel))
    fig.add_trace(go.Scatter(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(size=0, color=px.colors.qualitative.Plotly[idx % len(px.colors.qualitative.Plotly)]),
        legendgroup=str(rel),  # Convert the tuple to a string
        name=rel_str
    ))

# Update layout
fig.update_layout(
    showlegend=True,
    title="Kinship Relations in Macbeth",
    legend=dict(orientation="v", x=1, y=0.6),
    margin=dict(b=30, t=30, l=0, r=0),
)

fig.update_xaxes(showgrid=False, zeroline=False)
fig.update_yaxes(showgrid=False, zeroline=False)

fig.show()