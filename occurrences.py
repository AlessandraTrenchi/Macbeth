import networkx as nx 

# Create a directed graph
G = nx.Graph()

class SceneCharacterCooccurrences:
    def __init__(self):
        self.cooccurrences = {}

    def add_cooccurrence(self, character1, character2):
        pair = tuple(sorted([character1, character2]))
        self.cooccurrences[pair] = self.cooccurrences.get(pair, 0) + 1
        # Ensure that nodes and edges are added to the graph
        G.add_nodes_from(pair)
        
        # Add +1 to the weight of the edge
        if G.has_edge(*pair):
            G[character1][character2]['weight'] += 1
        else:
            G.add_edge(*pair, weight=1)

    def display_cooccurrences(self):
        for pair, count in self.cooccurrences.items():
            print(f"{pair[0]} and {pair[1]}: {count} times")

# Example usage
all_scenes_cooccurrences = SceneCharacterCooccurrences()

# Adding co-occurrences based on the provided information
all_scenes_cooccurrences.add_cooccurrence("First Witch", "Second Witch")
all_scenes_cooccurrences.add_cooccurrence("First Witch", "Third Witch")
all_scenes_cooccurrences.add_cooccurrence("Second Witch", "Third Witch")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Donalbain")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Malcolm", "Donalbain")
all_scenes_cooccurrences.add_cooccurrence("Malcolm", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Donalbain", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Malcolm", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Banquo")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "First Witch")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Second Witch")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Third Witch")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Angus")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Banquo")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Angus")
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Ross", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Angus", "Lady Macbeth")
# Adding co-occurrences from the latest scene
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Duncan")
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Duncan")
# Adding co-occurrences from Act II, Scene 1
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Banquo")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Fleance")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Fleance")

# Adding co-occurrences from Act II, Scene 2
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Macbeth")

# Adding co-occurrences from Act II, Scene 3
all_scenes_cooccurrences.add_cooccurrence("Porter", "Macduff")
all_scenes_cooccurrences.add_cooccurrence("Porter", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Porter", "Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Banquo")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Donalbain")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Donalbain")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Banquo")
# Adding co-occurrences from Act II, Scene 4
all_scenes_cooccurrences.add_cooccurrence("Ross", "Old Man")
all_scenes_cooccurrences.add_cooccurrence("Ross", "Macduff")
all_scenes_cooccurrences.add_cooccurrence("Old Man", "Macduff")
# Adding co-occurrences from Act III, Scene 1
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Lords")
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Lords")
all_scenes_cooccurrences.add_cooccurrence("Ross", "Lords")
# Adding co-occurrences from Act III, Scene 1
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "First Murderer")
all_scenes_cooccurrences.add_cooccurrence("First Murderer", "Second Murderer")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Second Murderer")
# Adding co-occurrences from Act III, Scene 2
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Macbeth")
# Adding co-occurrences from Act III, Scene 3
all_scenes_cooccurrences.add_cooccurrence("First Murderer", "Third Murderer")
all_scenes_cooccurrences.add_cooccurrence("First Murderer", "Second Murderer")
all_scenes_cooccurrences.add_cooccurrence("Third Murderer", "Second Murderer")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "First Murderer")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Second Murderer")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Third Murderer")
all_scenes_cooccurrences.add_cooccurrence("Banquo", "Fleance")
# Adding co-occurrences from Act III, Scene 4
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Lords")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "First Murderer")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Second Murderer")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Third Murderer")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Ghost of Banquo")
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "First Murderer")
# Adding co-occurrences from Act III, Scene 5
all_scenes_cooccurrences.add_cooccurrence("First Witch", "Second Witch")
all_scenes_cooccurrences.add_cooccurrence("First Witch", "Third Witch")
all_scenes_cooccurrences.add_cooccurrence("Second Witch", "Third Witch")
all_scenes_cooccurrences.add_cooccurrence("First Witch", "Hecate")
all_scenes_cooccurrences.add_cooccurrence("Second Witch", "Hecate")
all_scenes_cooccurrences.add_cooccurrence("Third Witch", "Hecate")
# Adding co-occurrences from Act III, Scene 6
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Lord")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Duncan")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Donalbain")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Banquo")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Fleance")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Macduff")
all_scenes_cooccurrences.add_cooccurrence("Lord", "Duncan")
all_scenes_cooccurrences.add_cooccurrence("Lord", "Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Lord", "Fleance")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Duncan")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Banquo")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Duncan", "Donalbain")
all_scenes_cooccurrences.add_cooccurrence("Malcolm", "Donalbain")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Edward")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Siward")
# Adding co-occurrences from Act IV, Scene 1
all_scenes_cooccurrences.add_cooccurrence("First Witch", "Second Witch")
all_scenes_cooccurrences.add_cooccurrence("First Witch", "Third Witch")
all_scenes_cooccurrences.add_cooccurrence("Second Witch", "Third Witch")
all_scenes_cooccurrences.add_cooccurrence("First Witch", "Hecate")
all_scenes_cooccurrences.add_cooccurrence("Second Witch", "Hecate")
all_scenes_cooccurrences.add_cooccurrence("Third Witch", "Hecate")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "First Witch")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Second Witch")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Third Witch")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Hecate")
all_scenes_cooccurrences.add_cooccurrence("Macbeth", "Lennox")
# Adding co-occurrences from Act IV, Scene 2
all_scenes_cooccurrences.add_cooccurrence("Lady Macduff", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Lady Macduff", "Son")
all_scenes_cooccurrences.add_cooccurrence("Lady Macduff", "First Murderer")
all_scenes_cooccurrences.add_cooccurrence("Son", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Son", "First Murderer")
all_scenes_cooccurrences.add_cooccurrence("Ross", "First Murderer")
# Adding co-occurrences from Act V, Scene 3
all_scenes_cooccurrences.add_cooccurrence("Macduff", "MALCOLM")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Doctor")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "ROSS")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Lady Macduff")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Children")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "Heaven")
all_scenes_cooccurrences.add_cooccurrence("Macduff", "King")
all_scenes_cooccurrences.add_cooccurrence("Malcolm", "Doctor")
all_scenes_cooccurrences.add_cooccurrence("Malcolm", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Malcolm", "Heaven")
all_scenes_cooccurrences.add_cooccurrence("Doctor", "Ross")
all_scenes_cooccurrences.add_cooccurrence("Doctor", "Heaven")
all_scenes_cooccurrences.add_cooccurrence("Ross", "Lady Macduff")
all_scenes_cooccurrences.add_cooccurrence("Ross", "Children")
all_scenes_cooccurrences.add_cooccurrence("Wife", "Children")
all_scenes_cooccurrences.add_cooccurrence("Doctor", "Gentlewoman")
all_scenes_cooccurrences.add_cooccurrence("Doctor", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Doctor", "Banquo")
all_scenes_cooccurrences.add_cooccurrence("Doctor", "God")
all_scenes_cooccurrences.add_cooccurrence("Gentlewoman", "Lady Macbeth")
all_scenes_cooccurrences.add_cooccurrence("Gentlewoman", "Banquo")
all_scenes_cooccurrences.add_cooccurrence("Gentlewoman", "God")
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Banquo")
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "God")
all_scenes_cooccurrences.add_cooccurrence("Lady Macbeth", "Arabia")
all_scenes_cooccurrences.add_cooccurrence("Menteith", "Caithness")
all_scenes_cooccurrences.add_cooccurrence("Menteith", "Angus")
all_scenes_cooccurrences.add_cooccurrence("Menteith", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Menteith", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Menteith", "Siward")
all_scenes_cooccurrences.add_cooccurrence("Menteith", "Macduff")
all_scenes_cooccurrences.add_cooccurrence("Caithness", "Angus")
all_scenes_cooccurrences.add_cooccurrence("Caithness", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Caithness", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Caithness", "Siward")
all_scenes_cooccurrences.add_cooccurrence("Caithness", "Macduff")
all_scenes_cooccurrences.add_cooccurrence("Angus", "Lennox")
all_scenes_cooccurrences.add_cooccurrence("Angus", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Angus", "Siward")
all_scenes_cooccurrences.add_cooccurrence("Angus", "Macduff")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Malcolm")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Siward")
all_scenes_cooccurrences.add_cooccurrence("Lennox", "Macduff")
all_scenes_cooccurrences.add_cooccurrence('Macbeth', 'Doctor')
all_scenes_cooccurrences.add_cooccurrence('Macbeth', 'Seyton')
all_scenes_cooccurrences.add_cooccurrence('Macbeth', 'Seyton')
all_scenes_cooccurrences.add_cooccurrence('Doctor', 'Macbeth')
all_scenes_cooccurrences.add_cooccurrence('Doctor', 'Seyton')
all_scenes_cooccurrences.add_cooccurrence('Seyton', 'Macbeth')
# Act V, Scene 4
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Siward')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Young Siward')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Macduff')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Menteith')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Caithness')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Angus')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Lennox')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Ross')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Soldiers')
all_scenes_cooccurrences.add_cooccurrence('Menteith', 'Siward')
all_scenes_cooccurrences.add_cooccurrence('Menteith', 'Caithness')
all_scenes_cooccurrences.add_cooccurrence('Menteith', 'Angus')
all_scenes_cooccurrences.add_cooccurrence('Menteith', 'Lennox')
all_scenes_cooccurrences.add_cooccurrence('Menteith', 'Ross')
all_scenes_cooccurrences.add_cooccurrence('Menteith', 'Soldiers')
all_scenes_cooccurrences.add_cooccurrence('Siward', 'Caithness')
all_scenes_cooccurrences.add_cooccurrence('Siward', 'Angus')
all_scenes_cooccurrences.add_cooccurrence('Siward', 'Lennox')
all_scenes_cooccurrences.add_cooccurrence('Siward', 'Ross')
all_scenes_cooccurrences.add_cooccurrence('Siward', 'Soldiers')
all_scenes_cooccurrences.add_cooccurrence('Caithness', 'Angus')
all_scenes_cooccurrences.add_cooccurrence('Caithness', 'Lennox')
all_scenes_cooccurrences.add_cooccurrence('Caithness', 'Ross')
all_scenes_cooccurrences.add_cooccurrence('Angus', 'Lennox')
all_scenes_cooccurrences.add_cooccurrence('Angus', 'Ross')
all_scenes_cooccurrences.add_cooccurrence('Lennox', 'Ross')

# Act V, Scene 5
all_scenes_cooccurrences.add_cooccurrence('Macbeth', 'Seyton')
all_scenes_cooccurrences.add_cooccurrence('Doctor', 'Macbeth')
all_scenes_cooccurrences.add_cooccurrence('Doctor', 'Seyton')
all_scenes_cooccurrences.add_cooccurrence('Seyton', 'Macbeth')
# Act V, Scene 6
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Siward')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Macduff')
all_scenes_cooccurrences.add_cooccurrence('Siward', 'Macduff')

# Act V, Scene 7
all_scenes_cooccurrences.add_cooccurrence('Macbeth', 'Young Siward')
all_scenes_cooccurrences.add_cooccurrence('Young Siward', 'Macbeth')
all_scenes_cooccurrences.add_cooccurrence('Macduff', 'Macbeth')
# Act V, Scene 8
all_scenes_cooccurrences.add_cooccurrence('Macbeth', 'Macduff')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Siward')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Ross')
all_scenes_cooccurrences.add_cooccurrence('Siward', 'Ross')
all_scenes_cooccurrences.add_cooccurrence('Malcolm', 'Macduff')

# Export the graph to Gephi
nx.write_gexf(G, 'occurrences.gexf')

# Calculate and add centrality measures
centrality_measures = {
    'degree_centrality': nx.degree_centrality(G),
    'betweenness_centrality': nx.betweenness_centrality(G),
    'closeness_centrality': nx.closeness_centrality(G),
    'eigenvector_centrality': nx.eigenvector_centrality(G, max_iter=1000)
}

for measure, values in centrality_measures.items():
    nx.set_node_attributes(G, values, measure)

# Export the graph to Gephi
nx.write_gexf(G, 'weighted_occurrences.gexf')

# Calculate and add clique measures
cliques = list(nx.find_cliques(G))

# Flatten the list of cliques to create a list of nodes in each clique
flattened_cliques = [node for clique in cliques for node in clique]

# Create a dictionary to map each node to its clique index
clique_dict = {node: idx for idx, nodes in enumerate(cliques) for node in nodes}
nx.set_node_attributes(G, clique_dict, 'clique_membership')