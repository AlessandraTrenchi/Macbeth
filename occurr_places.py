import networkx as nx
import matplotlib.pyplot as plt
from macbeth import param

class MacbethPlacesGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.interaction_weights = {}  # Dictionary to store interaction weights

    def add_scene(self, scene_name, characters):
        # Add nodes and edges for characters in the scene
        for character1 in characters:
            for character2 in characters:
                if character1 != character2:
                    # Update edge weight
                    edge = (character1, character2)
                    self.interaction_weights[edge] = self.interaction_weights.get(edge, 0) + 1

                    # Add nodes and edges to the graph
                    self.graph.add_node(character1, scene=scene_name, gender=self.get_gender(character1))
                    self.graph.add_node(character2, scene=scene_name, gender=self.get_gender(character2))
                    self.graph.add_edge(character1, character2, scene=scene_name, weight=self.interaction_weights[edge])

    def get_gender(self, character):
        # This function should return the gender of the character based on your data
        # For simplicity, assuming 'gender' attribute is present in your data
        try:
            character_data = param[param['Character'] == character]
            if not character_data.empty:
                return character_data['Gender'].values[0]
            else:
                # Handle the case when character is not found in the data
                print(f"No data found for character: {character}")
                return 'Unknown'
        except KeyError as e:
            print(f"KeyError: {e}")
            print("Check if 'Character' column exists in your data.")
            return 'Unknown'

    def export_to_gephi(self, filename='macbeth_graph.gexf'):
        # Create a copy of the graph to modify attributes for exporting
        export_graph = self.graph.copy()

        # Add edge weights to the graph
        for edge, weight in self.interaction_weights.items():
            export_graph[edge[0]][edge[1]]['weight'] = weight
            nx.write_gexf(export_graph, filename)
    def plot_graph(self):
    # Create node lists based on scene names
        scenes = list(set(nx.get_edge_attributes(self.graph, 'scene').values()))

    # Draw the graph
        pos = nx.spring_layout(self.graph)
        for scene in scenes:
            scene_nodes = [node for node, data in self.graph.nodes(data=True) if data['scene'] == scene and data['gender'] != 'Unknown']
            node_colors = [data['gender'] for node, data in self.graph.nodes(data=True) if data['scene'] == scene and data['gender'] != 'Unknown']
            weighted_edges = [(edge[0], edge[1]) for edge, data in self.graph.edges(data=True) if isinstance(edge, tuple) and len(edge) == 2 and data.get('scene') == scene] + [edge for edge, data in self.graph.edges(data=True) if not isinstance(edge, tuple) and data.get('scene') == scene]
            edge_weights = [data['weight'] for edge, data in self.graph.edges(data=True) if data.get('scene') == scene]
            nx.draw_networkx_nodes(self.graph, pos, nodelist=scene_nodes, node_size=500, alpha=0.8,
                               node_color=node_colors, cmap=plt.cm.Paired, label=scene)
            nx.draw_networkx_labels(self.graph, pos, labels={n: n for n in scene_nodes}, font_size=8)
            nx.draw_networkx_edges(self.graph, pos, edgelist=weighted_edges, width=edge_weights, alpha=0.5, edge_color=edge_weights)
            plt.title('Character Co-occurrence Network in Macbeth')
            plt.legend(scenes)
            plt.show()




# Usage example
macbeth_graph = MacbethPlacesGraph()

# Add scenes with characters
macbeth_graph.add_scene("A desert place", ["First Witch", "Second Witch", "Third Witch"])
macbeth_graph.add_scene("A camp near Forres", ["Duncan", "Malcolm", "Donalbain", "Lennox", "Sergeant", "Macbeth", "Banquo", "Ross"])
# Add the new scene to the existing MacbethPlacesGraph
macbeth_graph.add_scene("A heath near Forres", ["First Witch", "Second Witch", "Third Witch", "Macbeth", "Banquo", "Ross", "Angus", "Duncan", "Malcolm"])
macbeth_graph.add_scene("Inverness. Macbeth's castle.", ["Lady Macbeth", "Messenger", "Duncan", "Malcolm", "Donalbain", "Banquo", "Lennox", "Macduff", "Ross", "Angus", "Sewer", "Macbeth"])
macbeth_graph.add_scene("Before Macbeth's castle.", ["Duncan", "Malcolm", "Donalbain", "Banquo", "Lennox", "Macduff", "Ross", "Angus", "Lady Macbeth", "Sewer", "Macbeth"])
macbeth_graph.add_scene("Macbeth's castle.", ["Lady Macbeth", "Servant", "Banquo", "Fleance", "Macbeth"])
macbeth_graph.add_scene("Court of Macbeth's castle.", ["Banquo", "Fleance", "Macbeth", "Servant"])
macbeth_graph.add_scene("Outside Macbeth's castle.", ["Ross", "Old Man", "Macduff"])
macbeth_graph.add_scene("Forres. The palace.", ["Banquo", "Macbeth", "Lady Macbeth", "Lennox", "Ross", "Lords", "Ladies", "Attendants", "Servant", "First Murderer", "Second Murderer"])
macbeth_graph.add_scene("The palace.", ["Lady Macbeth", "Servant", "Macbeth"])
macbeth_graph.add_scene("A park near the palace.", ["First Murderer", "Third Murderer", "Second Murderer", "Banquo", "Fleance"])
macbeth_graph.add_scene("Hall in the palace.", ["Macbeth", "Lady Macbeth", "Ross", "Lennox", "Lords", "Attendants", "First Murderer", "Ghost of Banquo"])
macbeth_graph.add_scene("A Heath.", ["First Witch", "Hecate"])
macbeth_graph.add_scene("Forres. The palace.", ["Lennox", "Lord"])
macbeth_graph.add_scene("A cavern. In the middle, a boiling cauldron.", ["First Witch", "Second Witch", "Third Witch", "Hecate"])
macbeth_graph.add_scene("A cavern. In the middle, a boiling cauldron.", ["Macbeth", "First Apparition", "Second Apparition", "Third Apparition", "Ghost of Banquo", "Lennox"])
macbeth_graph.add_scene("Fife. Macduff's castle.", ["LADY Macduff", "Son", "Ross", "Messenger", "First Murderer", "Second Murderer", "Third Murderer"])
macbeth_graph.add_scene("England. Before the King's palace.", ["Malcolm", "Macduff", "Doctor", "Gentlewoman", "Ross"])
macbeth_graph.add_scene("The country near Dunsinane.", ["Menteith", "Caithness", "Angus", "Lennox", "Soldiers"])
macbeth_graph.add_scene("Dunsinane. A room in the castle.", ["Macbeth", "Doctor", "Attendants", "Servant", "Seyton"])
macbeth_graph.add_scene("Country near Birnam wood.", ["Malcolm", "Siward", "Young Siward", "Macduff", "Menteith", "Caithness", "Angus", "Lennox", "Ross", "Soldiers"])
macbeth_graph.add_scene("Dunsinane. Within the castle.", ["Macbeth", "Seyton", "Soldiers"])
macbeth_graph.add_scene("Another part of the field.", ["Macbeth", "Macduff", "Young Siward", "Messenger"])

# Calculate and print various measures
print("Number of nodes:", macbeth_graph.graph.number_of_nodes())
print("Number of edges:", macbeth_graph.graph.number_of_edges())
print("Density:", nx.density(macbeth_graph.graph))
print("Average clustering coefficient:", nx.average_clustering(macbeth_graph.graph))
print("Degree centrality:", nx.degree_centrality(macbeth_graph.graph))
print("Betweenness centrality:", nx.betweenness_centrality(macbeth_graph.graph))
print("Closeness centrality:", nx.closeness_centrality(macbeth_graph.graph))

# Convert the graph to undirected and find cliques
undirected_graph = macbeth_graph.graph.to_undirected()
cliques = list(nx.find_cliques(undirected_graph))
print("All cliques:", cliques)
print("Size of the largest clique:", len(max(cliques, key=len)))

# Write the graph to GEXF file
macbeth_graph.export_to_gephi('weighted_interactions.gexf')

# Plot the graph (optional)
macbeth_graph.plot_graph()
