import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from macbeth import param
from matplotlib.colors import rgb2hex
import plotly.express as px

# Define relationships for each category with weights
feelings_relations = [
    ("First Witch", "Second Witch", "Third Witch", "friendship", 2),
    ("Macbeth", "Macduff", "friendship", 2),
    ("Macbeth", "Banquo", "friendship", 2),
    ("Macbeth", "Malcolm", "friendship", 2),
    ("Ross", "Duncan", "friendship", 2),
    ("Duncan", "Banquo", "friendship", 2),
    ("Lady Macbeth", "Duncan", "murderer, murdered", 1),
    ("Macbeth", "Duncan", "murderer, murdered", 1),
    ("Old Siward", "Malcolm", "supporter, supported", 2)]

kinship_relations = [
    ("Macduff", "Malcolm", "cousins", 2),
    ("Macduff", "Lennox", "cousins", 2),
    ("Ross", "Macduff", "cousins", 2),
    ("Macduff", "Ross", "cousins", 2),
    ("Macduff", "Menteith", "cousins", 2),
    ("Macduff", "Angus", "cousins", 2),
    ("Macduff", "Caithness", "cousins", 2),
    ("Malcolm", "Old Siward", "nephew, uncle", 2),
    ("Malcolm", "Young Siward", "cousins", 2),
    ("Menteith", "Caithness", "cousins", 2),
    ("Menteith", "Angus", "cousins", 2),
    ("Angus", "Lennox", "cousins", 2),
    ("Lennox", "Ross", "cousins", 2),
    ("Lady Macbeth", "Duncan", "host, subject", 1),
    ("Duncan", "Donalbain", "father, son", 3),
    ("Lady Macbeth", "Macbeth", "wife, husband", 3),
    ("Duncan", "Lady Macbeth", "lost father, lost child", 2),
    ("Old Siward", "Seyton", "son, father", 3),
    ("Young Siward", "Old Siward", "son, father", 2),
    ("Macduff", "Porter", "master, servant", 1),
]

actions_relations = [
    ("Banquo", "Fleance", "murderer, murdered", 4),
    ("Duncan", "Malcolm", "murderer, murdered", 4),
    ("Macbeth", "Banquo", "murderer, murdered", 4),
    ("Macduff", "Macbeth", "murderer, murdered", 4),
    ("Lady Macduff", "Son", "murderer, murdered", 4),
    ("First Witch", "Macbeth", "trickster, tricked", 3),
    ("Second Witch", "Macbeth", "trickster, tricked", 3),
    ("Third Witch", "Macbeth", "trickster, tricked", 3),
    ("Hecate", "Macbeth", "trickster, tricked", 3)]

# Function to create a graph based on a list of relations
def create_graph(relations):
    G = nx.Graph()

    for relation in relations:
        if len(relation) == 4:
            G.add_edge(relation[0], relation[1], relationship=relation[2], weight=relation[3])
        else:
            G.add_edge(relation[0], relation[1], relationship=relation[2], weight=1)

    return G

# Function to create traces based on a graph and its layout
def create_trace(G, pos, cmap, node_sizes):
    edge_trace = []
    for idx, edge in enumerate(G.edges(data=True)):
        rel_type = edge[2].get('relationship', '')
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_trace.append(go.Scatter(x=(x0, x1, None), y=(y0, y1, None), mode='lines', line=dict(width=2, color=rgb2hex(cmap(idx))), hoverinfo='none', legendgroup=f"edge_{idx}"))

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
        customdata=[
            f"Character: {node}<br>"
            f"Gender: {G.nodes[node].get('gender', '')}<br>"
            f"Place: {G.nodes[node].get('place', '')}<br>"
            f"Description: {G.nodes[node].get('description', '')}<br>"
            f"Relationship: {G.edges[node].get('relationship', '')}<br>" if node in G.edges else ''
            for node in G.nodes()
        ]
    )
    
    return edge_trace, node_trace


# Create Plotly graph
G = create_graph(feelings_relations)  # You can choose any relation list for the initial graph
pos = nx.spring_layout(G, seed=42)
degree_centrality = nx.degree_centrality(G)
node_sizes = [3000 * degree_centrality[node] for node in G.nodes()]

edge_trace, node_trace = create_trace(G, pos, plt.cm.get_cmap('tab10', len(set(nx.get_edge_attributes(G, 'relationship').values()))), node_sizes)

fig = go.Figure(edge_trace + [node_trace])
fig.update_traces(
    hovertemplate='%{customdata}',
)
fig.update_layout(showlegend=False, title=f"Network dei Personaggi di Macbeth - Kinship")
fig.update_xaxes(showgrid=False, zeroline=False)
fig.update_yaxes(showgrid=False, zeroline=False)

fig.show()