from distutils.util import change_root
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

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

# Events and changes
events = [
    {'time': 5, 'changes': [('First Witch', 'Macbeth', 'Tricked', 'Enemies'),
                            ('Second Witch', 'Macbeth', 'Tricked', 'Enemies'),
                            ('Third Witch', 'Macbeth', 'Tricked', 'Enemies')]},
    {'time': 10, 'changes': [('Lady Macbeth', 'Macbeth', 'Despise', 'Enemies'), ('Macbeth', 'Self', 'Evil')]},
    {'time': 15, 'changes': [('Macbeth', 'Duncan', 'Murdered', 'Enemies')]},
    {'time': 20, 'changes': [('Macbeth', 'Chamberlains', 'Murdered', 'Enemies')]},
    {'time': 25, 'changes': [('Hecate', 'Macbeth', 'Tricked', 'Enemies'), ('Macbeth', 'Hecate', 'Tricked', 'Enemies')]},
    {'time': 30, 'changes': [('Macbeth', 'Banquo', 'Murdered', 'Enemies'), ('Lady Macbeth', 'Self', 'Insane')]},
    {'time': 35, 'changes': [('Macduff', 'Macbeth', 'Murdered', 'Enemies'),
                             ('Lady Macbeth', 'Self', 'Insane', 'Dies')]}
]


# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph with initial relationships 
# Add 'Macbeth' as a node to the graph



# Update layout of the graph
pos = nx.spring_layout(G, seed=42)

for source, target, rel_type in starting_relationships:
    G.add_edge(source, target, relationship_type=rel_type, weight=1)  # Adding weight as 1

# Create layout of the graph
pos = nx.spring_layout(G, seed=42)

# Extract unique relationships from edges
unique_relationships = list(set(nx.get_edge_attributes(G, 'relationship_type').values()))

# Create a colormap for relationships
cmap = plt.cm.get_cmap('tab10', len(unique_relationships))

# Create a legend for relationships
legend_data = []
for idx, rel in enumerate(unique_relationships):
    legend_data.append(go.Scatter(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(size=0, color=cmap(idx)),
        legendgroup=rel,
        name=rel
    ))

# Create edge trace
edge_trace = []
cmap = plt.cm.get_cmap('tab10', len(unique_relationships))
color_dict = {rel: cmap(idx) for idx, rel in enumerate(unique_relationships)}

for edge in G.edges(data=True):
    source, target, data = edge
    x0, y0 = pos[source]
    x1, y1 = pos[target]
    rel_type = data['relationship_type']

    color = color_dict[rel_type]
    color_hex = f"#{int(color[0] * 255):02X}{int(color[1] * 255):02X}{int(color[2] * 255):02X}"

    edge_trace.append(go.Scatter(x=(x0, x1, None), y=(y0, y1, None), mode='lines',
                                line=dict(width=data['weight'], color=color_hex),
                                hoverinfo='none', legendgroup=rel_type, name=f'Relationship Type: {rel_type}'))

if G.has_node(source) and G.has_node(target):
    if G.has_edge(source, target):
        # Define new_rel_type here
        new_rel_type = 'YourDefaultValue'  # Change 'YourDefaultValue' to the appropriate value
        G[source][target]['relationship_type'] = new_rel_type
    else:
        print(f"Edge between {source} and {target} does not exist.")
else:
    print(f"One or both of the nodes {source} and {target} do not exist in the graph.")

# Create node trace
node_trace = go.Scatter(
    x=[pos[node][0] for node in G.nodes()],
    y=[pos[node][1] for node in G.nodes()],
    mode='markers+text',
    hoverinfo='text',
    marker=dict(
        showscale=False,
        color=['red' if 'gender' in G.nodes[node] and G.nodes[node]['gender'] == 'Female' else 'blue' for node in
               G.nodes()]
    ),
    text=[node for node in G.nodes()],
    textposition='bottom center',
    customdata=[[f"Character: {node}<br>Weighted Degree: {nx.degree_centrality(G)[node]:.2f}"] for node in G.nodes()]
)

# Create Plotly graph
fig = go.Figure(legend_data + edge_trace + [node_trace])
fig.update_traces(
    hovertemplate='%{customdata}',  # Show attributes on hover
)

# Update layout
fig.update_layout(
    title="Starting Relationships with Colored Edges",
    showlegend=True,
    margin=dict(b=20, t=40, l=0, r=0),
)

# Update graph at each event and add frames for animation
frames = []
for event in events:
    for change in event['changes']:
        source, target, rel_type, new_rel_type = change
        G[source][target]['relationship_type'] = new_rel_type
    edge_trace_frame = []
    for edge in G.edges(data=True):
        source, target, data = edge
        x0, y0 = pos[source]
        x1, y1 = pos[target]
        rel_type = data['relationship_type']
        edge_trace = []
        color_dict = {rel: plt.cm.get_cmap('tab10', len(unique_relationships))(idx) for idx, rel in enumerate(unique_relationships)}
        color = color_dict[rel_type]
        color_hex = f"#{int(color[0] * 255):02X}{int(color[1] * 255):02X}{int(color[2] * 255):02X}"

        edge_trace_frame.append(
            go.Scatter(x=(x0, x1, None), y=(y0, y1, None), mode='lines',
                       line=dict(width=data['weight'], color=color_hex),
                       hoverinfo='none', legendgroup=rel_type, name=f'Relationship Type: {rel_type}'))

    frames.append(go.Frame(data=edge_trace_frame, name=f"Time {event['time']}"))

# Update frames and layout for animation
fig.frames = frames
fig.update_layout(
    updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                                                        method='animate',
                                                                        args=[None,
                                                                              dict(frame=dict(duration=1000, redraw=True),
                                                                                   fromcurrent=True)])])],
    sliders=[dict(steps=[dict(args=[[f"Time {event['time']}"]], label=f"Time {event['time']}", method='animate') for
                        event in events],
                   active=0, transition=dict(duration=1000))],
)

# Show the plot
fig.show()
