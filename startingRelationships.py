from distutils.util import change_root
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from macbeth import param
import matplotlib.cm as cm

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
        marker=dict(size=0, color=cmap(idx)),
        legendgroup=rel,
        name=rel
    ))

# Create edge trace
edge_trace = []
color_dict = {rel: cmap(idx) for idx, rel in enumerate(unique_relationships)}

for edge in G.edges(data=True):
    source, target, data = edge
    x0, y0 = pos.get(source, (0, 0))
    x1, y1 = pos.get(target, (0, 0))
    rel_type = data['relationship_type']

    # Handle the case where the relationship type is not in color_dict
    if rel_type not in color_dict:
        color_dict[rel_type] = cmap(len(color_dict))

    color = color_dict[rel_type]
    color_hex = f"#{int(color[0] * 255):02X}{int(color[1] * 255):02X}{int(color[2] * 255):02X}"

    edge_trace.append(go.Scatter(x=(x0, x1, None), y=(y0, y1, None), mode='lines',
                                line=dict(width=data['weight'], color=color_hex),
                                hoverinfo='none', legendgroup=rel_type, name=f'Relationship Type: {rel_type}'))

# Define new_rel_type here
new_rel_type = 'YourDefaultValue'  # Change 'YourDefaultValue' to the appropriate value

if G.has_node(source) and G.has_node(target):
    if G.has_edge(source, target):
        G[source][target]['relationship_type'] = new_rel_type
    else:
        print(f"Edge between {source} and {target} does not exist. Adding the edge.")
        G.add_edge(source, target, relationship_type=new_rel_type, weight=1)
else:
    print(f"One or both of the nodes {source} and {target} do not exist in the graph. Adding the nodes and edge.")
    G.add_node(source)
    G.add_node(target)
    G.add_edge(source, target, relationship_type=new_rel_type, weight=1)

# ... (rest of the code)

# Update graph at each event and add frames for animation
frames = []
# Inside the loop where you update the graph at each event
# Add new relationship types encountered during events to unique_relationships
for event in events:
    for changes in event['changes']:
        source, target, rel_type, _ = changes
        if rel_type not in unique_relationships:
            unique_relationships.append(rel_type)

        # Ensure that both source and target nodes exist in the graph
        if not G.has_node(source):
            G.add_node(source)
        if not G.has_node(target):
            G.add_node(target)

        if G.has_edge(source, target):
            # Update the relationship type
            G[source][target]['relationship_type'] = new_rel_type
        else:
            print(f"Edge between {source} and {target} does not exist. Adding the edge.")
            G.add_edge(source, target, relationship_type=new_rel_type, weight=1)
# Create node trace
node_trace = go.Scatter(
    x=[pos[node][0] if node in pos else 0 for node in G.nodes()],  # Adjust the default value as needed
    y=[pos[node][1] if node in pos else 0 for node in G.nodes()],  # Adjust the default value as needed
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
# Inside the loop where you update the graph at each event
# Inside the loop where you update the graph at each event
# Add new relationship types encountered during events to unique_relationships
for event in events:
    for changes in event['changes']:
        source, target, rel_type, _ = changes
        if rel_type not in unique_relationships:
            unique_relationships.append(rel_type)

        # Ensure that both source and target nodes exist in the graph
        if not G.has_node(source):
            G.add_node(source)
        if not G.has_node(target):
            G.add_node(target)

        if G.has_edge(source, target):
            # Update the relationship type
            G[source][target]['relationship_type'] = new_rel_type
        else:
            print(f"Edge between {source} and {target} does not exist. Adding the edge.")
            G.add_edge(source, target, relationship_type=new_rel_type, weight=1)

edge_trace = []
cmap = plt.cm.get_cmap('tab10', len(unique_relationships)) if len(unique_relationships) > 0 else None
color_dict = {rel: cmap(idx) for idx, rel in enumerate(unique_relationships)}

for edge in G.edges(data=True):
    source, target, data = edge
    x0, y0 = pos[source]
    x1, y1 = pos[target]
    rel_type = data['relationship_type']
    color = color_dict.get(rel_type, 'YourDefaultValue')
   # print(f"Color for {rel_type}: {color}")

# Add this line to identify the problematic color values
#print(f"Color values: {color[0]}, {color[1]}, {color[2]}")
#print(f"Color for {rel_type}: {color}")

# Add this line to identify the problematic color values
#print(f"Color values: {color}")
print(f"Color for {rel_type}: {color}")

# Add this line to identify the problematic color values
print(f"Color values: {color}")

color_hex = f"#{int(color[0] * 255):02X}{int(color[1] * 255):02X}{int(color[2] * 255):02X}"

edge_trace.append(go.Scatter(x=(x0, x1, None), y=(y0, y1, None), mode='lines',
                                line=dict(width=data['weight'], color=color_hex),
                                hoverinfo='none', legendgroup=rel_type, name=f'Relationship Type: {rel_type}'))

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

# Inside the loop where you update the graph at each event
for event in events:
    edge_trace_frame = []  # Define edge_trace_frame here

    for change in event['changes']:
        source, target, rel_type, new_rel_type = change  # Define new_rel_type here for each change

        # Ensure that both source and target nodes exist in the graph
        if G.has_node(source) and G.has_node(target):
            if G.has_edge(source, target):
                # Update the relationship type
                G[source][target]['relationship_type'] = new_rel_type
            else:
                print(f"Edge between {source} and {target} does not exist. Adding the edge.")
                G.add_edge(source, target, relationship_type=new_rel_type, weight=1)
        else:
            print(f"One or both of the nodes {source} and {target} do not exist in the graph.")

    # Extract unique relationships from edges after the changes
    unique_relationships = list(set(nx.get_edge_attributes(G, 'relationship_type').values()))


# Inside the loop where you create edge_trace_frame
edge_trace_frame = []  # Reinitialize edge_trace_frame
for edge in G.edges(data=True):
    source, target, data = edge
    rel_type = data['relationship_type']
    
    # Get the coordinates of the source and target nodes
    x0, y0 = pos.get(source, (0, 0))  # Adjust the default values as needed
    x1, y1 = pos.get(target, (0, 0))

    if rel_type in color_dict:
        color = color_dict[rel_type]
    else:
        # Provide a fallback color for the default value
        color = (0.8, 0.8, 0.8, 1.0)  # Adjust these values as needed

    color_hex = f"#{int(color[0] * 255):02X}{int(color[1] * 255):02X}{int(color[2] * 255):02X}"

    edge_trace_frame.append(go.Scatter(x=(x0, x1, None), y=(y0, y1, None), mode='lines',
                                      line=dict(width=data['weight'], color=color_hex),
                                      hoverinfo='none', legendgroup=rel_type,
                                      name=f'Relationship Type: {rel_type}'))
frames.append(go.Frame(data=edge_trace_frame, name=f"Time {event['time']}"))
