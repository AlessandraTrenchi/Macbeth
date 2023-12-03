import networkx as nx
import plotly.graph_objects as go
from macbeth import param
from matplotlib.colors import rgb2hex
import plotly.express as px

# Events and changes data
events = [
    {'time': 5, 'changes': [
        ('First Witch', 'Macbeth', 'Tricked', 'Enemies'),
        ('Second Witch', 'Macbeth', 'Tricked', 'Enemies'),
        ('Third Witch', 'Macbeth', 'Tricked', 'Enemies')
    ]},
    {'time': 10, 'changes': [
        ('Lady Macbeth', 'Macbeth', 'Despise', 'Enemies'),
        ('Macbeth', 'Self', 'Evil', None)
    ]},
    {'time': 15, 'changes': [
        ('Macbeth', 'Duncan', 'Murdered', 'Enemies')
    ]},
    {'time': 20, 'changes': [
        ('Macbeth', 'Chamberlains', 'Murdered', 'Enemies')
    ]},
    {'time': 25, 'changes': [
        ('Hecate', 'Macbeth', 'Tricked', 'Enemies'),
        ('Macbeth', 'Hecate', 'Tricked', 'Enemies')
    ]},
    {'time': 30, 'changes': [
        ('Macbeth', 'Banquo', 'Murdered', 'Enemies'),
        ('Lady Macbeth', 'Self', 'Insane', None)  # Set status to None if not available
    ]},
    {'time': 35, 'changes': [
        ('Macduff', 'Macbeth', 'Murdered', 'Enemies'),
        ('Lady Macbeth', 'Self', 'Insane', 'Dies')
    ]}
]

# Create a directed graph for events
G_events = nx.DiGraph()

# Add nodes and edges based on events and changes
for event in events:
    for change in event['changes']:
        source, target, action, status = change

        # Handle "Self" as a special case for gender assignment
        if source == 'Self':
            source_gender = 'Male'  # or 'Female' depending on your preference
        else:
            source_gender = 'Female' if param['Gender'][param['Character'].index(source)] == 'Female' else 'Male'

        try:
            # Try to find the target character in param data
            target_index = param['Character'].index(target)
            target_gender = 'Female' if param['Gender'][target_index] == 'Female' else 'Male'
        except ValueError:
            # If the target is not found, use default values or handle it as needed
            target_gender = 'Unknown'  # You can set a default gender or handle it differently

        if target not in param['Character']:
            param['Character'].append(target)
            param['Gender'].append(target_gender)
            param['Place of belonging'].append('')
            param['Role'].append('')
            param['Description'].append('')

        G_events.add_node(source, gender=source_gender, place='Scotland', role='Character', description='Description')
        G_events.add_node(target, gender=target_gender, place='Scotland', role='Character', description='Description')
        G_events.add_edge(source, target, action=action, status=status, time=event['time'])

# Create layout of the graph for events
pos_events = nx.spring_layout(G_events, k=400, seed=42)

# Add degree centrality as node attribute for events
degree_centrality_events = nx.degree_centrality(G_events)
nx.set_node_attributes(G_events, degree_centrality_events, 'degree_centrality')

# Extract unique actions from edges for events
unique_actions = list(set(nx.get_edge_attributes(G_events, 'action').values()))

# Create edge trace with hover information for events
edge_trace_events = []
color_dict_events = {act: rgb2hex(px.colors.qualitative.Plotly[i % len(px.colors.qualitative.Plotly)]) for i, act in enumerate(unique_actions)}

for act in unique_actions:
    edges = [(source, target, data) for source, target, data in G_events.edges(data=True) if data['action'] == act]
    x_coords = []
    y_coords = []
    hover_texts = []

    for source, target, data in edges:
        x_coords.extend([pos_events[source][0], pos_events[target][0], None])
        y_coords.extend([pos_events[source][1], pos_events[target][1], None])
        hover_texts.append(f"Action: {data['action']}<br>Status: {data['status']}<br>Time: {data['time']}")

    edge_trace_events.append(go.Scatter(
        x=x_coords,
        y=y_coords,
        line=dict(width=2, color=color_dict_events[act]),
        hoverinfo='text',
        text=hover_texts,
        mode='lines',
        marker=dict(
            size=8,
            color=color_dict_events[act],
            line=dict(width=0),
            symbol='arrow-up'  # Use 'arrow-up' symbol for arrowheads
        ),
        name=act
    ))

# Create node trace with hover information for events
node_trace_events = go.Scatter(
    x=[pos_events[node][0] for node in G_events.nodes()],
    y=[pos_events[node][1] for node in G_events.nodes()],
    mode='markers',
    hoverinfo='text',
    marker=dict(
        color=['red' if G_events.nodes[node]['gender'] == 'Female' else 'blue' for node in G_events.nodes()],
        size=[300 * G_events.nodes[node]['degree_centrality'] for node in G_events.nodes()],
    ),
    text=[f"Character: {node}<br>Gender: {G_events.nodes[node]['gender']}<br>Place: {G_events.nodes[node]['place']}<br>Role: {G_events.nodes[node]['role']}<br>Description: {param['Description'][param['Character'].index(node)]}" for node in G_events.nodes()],
)

# Create Plotly graph for events
fig_events = go.Figure(edge_trace_events + [node_trace_events])

# Update layout for events
fig_events.update_layout(
    showlegend=True,
    title="Events and Changes",
    margin=dict(b=0, t=30, l=0, r=0),
)

fig_events.update_xaxes(showgrid=False, zeroline=False)
fig_events.update_yaxes(showgrid=False, zeroline=False)

# Show the graph for events
fig_events.show()
