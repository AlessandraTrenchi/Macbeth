import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import community
import igraph
from macbeth import param
# Define the data
act_1_data = {
    'SCENE 1': ["First Witch, Second Witch, Third Witch", "Discussing the place and time of the event."],
    'SCENE 2': ["Duncan, Malcolm, Donalbain, Lennox", "Inquiring about the bleeding sergeant's report"],
    'SCENE 3': ["First Witch, Second Witch, Third Witch", "Conspiring"],
    'SCENE 4': ["Duncan, Malcolm, Donalbain, Lennox" , "Talk about the execution of the previous thane of Cawdor."],
    'SCENE 5': ["Lady Macbeth", "News that the king is coming."],
    'SCENE 6': ["Duncan, Lady Macbeth", "He thanks her for the hospitality."],
    'SCENE 7': ["Macbeth, Macbeth", "Reflects on the possibility of murder."],
}

act_2_data = {
    'SCENE 1': ["Banquo, Fleance", "Talk about the time."],
    'SCENE 2': ["Lady Macbeth, Lady Macbeth", "Give him the daggers."],
    'SCENE 3': ["Porter, Macduff", "Talk about getting drunk."],
    'SCENE 5': ["Hecate, First Witch, Second Witch, Third Witch", "Hecate scolds them because they did not involve her."],
}

act_3_data = {
    'SCENE 1': ["Banquo, Banquo", "Afraid about Macbeth and the prophecy."],
    'SCENE 2': ["Macbeth, Lady Macbeth, Banquo", "Talk about Malcolm and Donalbain being murderers. Talk about Macbeth's crowning the day after. Banquo tells him he is going riding."],
    'SCENE 3': ["Macbeth, Old Siward", "Macbeth tells him to get the murderers."],
    'SCENE 4': ["Macbeth, First murderer, Second murderer", "They talk about Banquo and Fleance's murder."],
    'SCENE 6': ["Lady Macbeth, Lennox, Ross", "She tells them the king has a sickness."],
}

act_4_data = {
    'SCENE 1': ["First Witch, Second Witch, Third Witch", "Talk about the coming of Macbeth"],
    'SCENE 2': ["Lennox, Macbeth", "Talk about Macduff's disappearance."],
}

act_5_data = {
    'SCENE 1': ["Doctor, GentleWoman", "Talk about Lady Macbeth's craziness"],
    'SCENE 2': ["Menteith, Angus, Caithness, Lennox", "Organize to meet near Birnam Wood."],
    'SCENE 3': ["Macbeth, Doctor", "Macbeth asks about Malcolm's origin"],
    'SCENE 4': ["Old Siward, Macbeth", "Tells him there are ten thousand men at his castle's gate."],
    'SCENE 5': ["Malcolm , Old Siward , Macduff, Menteith", "Malcolm advises that everyone should hide behind a wood bough so the enemy will not know how many soldiers there are."],
    'SCENE 6': ["Seyton, Macbeth", "He tells him Lady Macbeth is dead."],
    'SCENE 8': ["Malcolm, Old Siward, Macduff", "Malcolm promises to fight with Siward for Macduff until they cannot anymore."],
}

# Create DataFrames
act_1_df = pd.DataFrame.from_dict(act_1_data, orient='index', columns=['Characters', 'Dialogue'])
act_2_df = pd.DataFrame.from_dict(act_2_data, orient='index', columns=['Characters', 'Dialogue'])
act_3_df = pd.DataFrame.from_dict(act_3_data, orient='index', columns=['Characters', 'Dialogue'])
act_4_df = pd.DataFrame.from_dict(act_4_data, orient='index', columns=['Characters', 'Dialogue'])
act_5_df = pd.DataFrame.from_dict(act_5_data, orient='index', columns=['Characters', 'Dialogue'])

# Export to CSV
act_1_df.to_csv('csv/dialogues/act1.csv')
act_2_df.to_csv('csv/dialogues/act2.csv')
act_3_df.to_csv('csv/dialogues/act3.csv')
act_4_df.to_csv('csv/dialogues/act4.csv')
act_5_df.to_csv('csv/dialogues/act5.csv')

# Load the CSV files into DataFrames
act_1_df = pd.read_csv('csv/dialogues/act1.csv', index_col=0)
act_2_df = pd.read_csv('csv/dialogues/act2.csv', index_col=0)
act_3_df = pd.read_csv('csv/dialogues/act3.csv', index_col=0)
act_4_df = pd.read_csv('csv/dialogues/act4.csv', index_col=0)
act_5_df = pd.read_csv('csv/dialogues/act5.csv', index_col=0)

# Combine all DataFrames into a single DataFrame
combined_df = pd.concat([act_1_df, act_2_df, act_3_df, act_4_df, act_5_df])

# Create a directed graph
G = nx.DiGraph()

# Add nodes from param
all_characters = param['Character']
gender_mapping = dict(zip(param['Character'], param['Gender']))

for character in all_characters:
    G.add_node(character)
    G.nodes[character]['gender'] = gender_mapping.get(character, 'Unknown')

# Add nodes and edges to the graph based on the combined DataFrame
for _, row in combined_df.iterrows():
    characters = [char.strip() for char in row['Characters'].split(',')]
    dialogue = row['Dialogue']

    for i in range(len(characters)):
        for j in range(i + 1, len(characters)):
            source = characters[i]
            target = characters[j]

            # Add nodes and edge
            G.add_node(source)
            G.add_node(target)
            if G.has_edge(source, target):
                G[source][target]['weight'] += 1  # Increment the weight if the edge already exists
            else:
                G.add_edge(source, target, weight=1)  # Add a new edge with weight 1
# Add gender information to nodes
param_dict = dict(zip(param['Character'], param['Gender']))

for node in G.nodes:
    gender = param_dict.get(node, 'Unknown')
    G.nodes[node]['gender'] = gender

# Map gender to numerical values
gender_mapping = {'Male': 0, 'Female': 1, 'Unknown': 2}
node_colors = [gender_mapping[G.nodes[node]['gender']] for node in G.nodes]

# Specify the layout using spring_layout and adjust the k parameter for distance
pos = nx.spring_layout(G, k=4.0)
# Draw the graph with edge weights
edge_labels = {(source, target): f"{G[source][target]['weight']}" for source, target in G.edges()}
# Calculate centrality measures
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

# Add centrality measures as node attributes
nx.set_node_attributes(G, degree_centrality, 'degree_centrality')
nx.set_node_attributes(G, closeness_centrality, 'closeness_centrality')
nx.set_node_attributes(G, betweenness_centrality, 'betweenness_centrality')

# Community detection using Girvan-Newman algorithm
communities = list(nx.community.girvan_newman(G))
best_community = max(communities, key=len)

# Flatten the list of sets to create a list of nodes in each community
flattened_communities = [node for community in communities for node in community]

# Create a dictionary to map each node to its community index
community_dict = {node: idx for idx, nodes in enumerate(flattened_communities) for node in nodes}
nx.set_node_attributes(G, community_dict, 'girvan_newman_community')

# Use Girvan-Newman community as node colors
node_colors = [community_dict[node] for node in G.nodes()]

# Create an undirected graph for k-clique community detection
G_undirected = G.to_undirected()

# Community detection using k-clique method
k_cliques = list(nx.community.k_clique_communities(G_undirected, k=3))
k_clique_dict = {node: idx for idx, nodes in enumerate(k_cliques) for node in nodes}
nx.set_node_attributes(G, k_clique_dict, 'k_clique_community')

# Create an undirected graph for label propagation community detection
G_undirected_lp = G.to_undirected()

# Community detection using label propagation
label_propagation_communities = nx.community.label_propagation_communities(G_undirected_lp)
label_propagation_dict = {node: idx for idx, nodes in enumerate(label_propagation_communities) for node in nodes}
nx.set_node_attributes(G, label_propagation_dict, 'label_propagation_community')

# Draw the graph with different colors for each community
nx.draw(G, pos, with_labels=True, node_size=500, node_color=node_colors, font_size=8, font_color="black", font_weight="bold", edge_color="green", linewidths=0.3, arrowsize=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red", font_size=8)

plt.title("Character Network - All Dialogues")
# Export the graph to Gephi
nx.write_gexf(G, 'dialogues.gexf')
plt.show()
