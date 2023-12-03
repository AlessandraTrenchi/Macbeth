import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from macbeth import param

# Creazione grafo
G = nx.Graph()

# Aggiunta dei nodi (personaggi) con attributi di genere, luogo e descrizione
for idx, character in enumerate(param['Character']):
    gender = param['Gender'][idx]
    place = param['Place of belonging'][idx]
    description = param['Description'][idx]
    G.add_node(character, gender=gender, place=place, description=description)

# Creazione layout del grafo
pos = nx.spring_layout(G, seed=42)

# Creazione del tracciato degli archi
edge_trace = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_trace.append(go.Scatter(x=(x0, x1, None), y=(y0, y1, None), mode='lines', line=dict(width=0.5), hoverinfo='none'))

# Creazione del tracciato dei nodi
node_trace = go.Scatter(
    x=[pos[node][0] for node in G.nodes()],
    y=[pos[node][1] for node in G.nodes()],
    mode='markers+text',
    hoverinfo='text',
    marker=dict(
        showscale=False,
        color=['red' if G.nodes[node]['gender'] == 'Female' else 'blue' for node in G.nodes()],
        size=10  # Adjust the size of the nodes as needed
    ),
    text=[node for node in G.nodes()],
    textposition='bottom center',
    textfont=dict(size=10),
    customdata=[[f"Character: {node}<br>Gender: {G.nodes[node]['gender']}<br>Place: {G.nodes[node]['place']}<br>Description: {G.nodes[node]['description']}"] for node in G.nodes()]
)

# Creazione del grafico Plotly
fig = go.Figure(edge_trace + [node_trace])
fig.update_traces(
    hovertemplate='%{customdata}',  # Visualizza gli attributi al passaggio del mouse
)

fig.update_layout(showlegend=False, title="Network dei Personaggi di Macbeth")
fig.update_xaxes(showgrid=False, zeroline=False)
fig.update_yaxes(showgrid=False, zeroline=False)

fig.show()
