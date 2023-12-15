import networkx as nx
import matplotlib.pyplot as plt

class MacbethPlacesGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_scene(self, scene_name, characters):
        # Add nodes and edges for characters in the scene
        for character1 in characters:
            for character2 in characters:
                if character1 != character2:
                    # Add nodes and edges to the graph
                    self.graph.add_node(character1, scene=scene_name)
                    self.graph.add_node(character2, scene=scene_name)
                    self.graph.add_edge(character1, character2, scene=scene_name)

    def export_to_gephi(self, filename='macbeth_graph.gexf'):
        nx.write_gexf(self.graph, filename)

    def plot_graph(self):
        # Create node lists based on scene names
        scenes = list(set(nx.get_edge_attributes(self.graph, 'scene').values()))

        # Draw the graph
        pos = nx.spring_layout(self.graph)
        for scene in scenes:
            scene_nodes = [node for node, data in self.graph.nodes(data=True) if data['scene'] == scene]
            nx.draw_networkx_nodes(self.graph, pos, nodelist=scene_nodes, node_size=500, alpha=0.8, label=scene)
            nx.draw_networkx_labels(self.graph, pos, labels={n: n for n in scene_nodes}, font_size=8)

        nx.draw_networkx_edges(self.graph, pos, width=1.0, alpha=0.5)
        plt.title('Character Co-occurrence Network in Macbeth')
        plt.legend(scenes)
        plt.show()

# Usage example
macbeth_graph = MacbethPlacesGraph()

# Add scenes with characters
macbeth_graph.add_scene("A desert place", ["First Witch", "Second Witch", "Third Witch"])
macbeth_graph.add_scene("A camp near Forres", ["DUNCAN", "MALCOLM", "DONALBAIN", "LENNOX", "Sergeant", "MACBETH", "BANQUO", "ROSS"])
# Add the new scene to the existing MacbethPlacesGraph
macbeth_graph.add_scene("A heath near Forres", ["First Witch", "Second Witch", "Third Witch", "MACBETH", "BANQUO", "ROSS", "ANGUS", "DUNCAN", "MALCOLM"])
macbeth_graph.add_scene("Inverness. Macbeth's castle.", ["LADY MACBETH", "Messenger", "DUNCAN", "MALCOLM", "DONALBAIN", "BANQUO", "LENNOX", "MACDUFF", "ROSS", "ANGUS", "Sewer", "MACBETH"])
macbeth_graph.add_scene("Before Macbeth's castle.", ["DUNCAN", "MALCOLM", "DONALBAIN", "BANQUO", "LENNOX", "MACDUFF", "ROSS", "ANGUS", "LADY MACBETH", "Sewer", "MACBETH"])
macbeth_graph.add_scene("Macbeth's castle.", ["LADY MACBETH", "Servant", "BANQUO", "FLEANCE", "MACBETH"])
macbeth_graph.add_scene("Court of Macbeth's castle.", ["BANQUO", "FLEANCE", "MACBETH", "Servant"])
macbeth_graph.add_scene("Outside Macbeth's castle.", ["ROSS", "Old Man", "MACDUFF"])
macbeth_graph.add_scene("Forres. The palace.", ["BANQUO", "MACBETH", "LADY MACBETH", "LENNOX", "ROSS", "Lords", "Ladies", "Attendants", "Servant", "First Murderer", "Second Murderer"])
macbeth_graph.add_scene("The palace.", ["LADY MACBETH", "Servant", "MACBETH"])
macbeth_graph.add_scene("A park near the palace.", ["First Murderer", "Third Murderer", "Second Murderer", "BANQUO", "FLEANCE"])
macbeth_graph.add_scene("Hall in the palace.", ["MACBETH", "LADY MACBETH", "ROSS", "LENNOX", "Lords", "Attendants", "First Murderer", "GHOST OF BANQUO"])
macbeth_graph.add_scene("A Heath.", ["First Witch", "HECATE"])
macbeth_graph.add_scene("Forres. The palace.", ["LENNOX", "Lord"])
macbeth_graph.add_scene("A cavern. In the middle, a boiling cauldron.", ["First Witch", "Second Witch", "Third Witch", "HECATE"])
macbeth_graph.add_scene("A cavern. In the middle, a boiling cauldron.", ["MACBETH", "First Apparition", "Second Apparition", "Third Apparition", "GHOST OF BANQUO", "LENNOX"])
macbeth_graph.add_scene("Fife. Macduff's castle.", ["LADY MACDUFF", "Son", "ROSS", "Messenger", "First Murderer", "Second Murderer", "Third Murderer"])
macbeth_graph.add_scene("England. Before the King's palace.", ["MALCOLM", "MACDUFF", "Doctor", "Waiting-Gentlewoman", "ROSS"])
macbeth_graph.add_scene("The country near Dunsinane.", ["MENTEITH", "CAITHNESS", "ANGUS", "LENNOX", "Soldiers"])
macbeth_graph.add_scene("Dunsinane. A room in the castle.", ["MACBETH", "Doctor", "Attendants", "Servant", "SEYTON"])
macbeth_graph.add_scene("Country near Birnam wood.", ["MALCOLM", "SIWARD", "YOUNG SIWARD", "MACDUFF", "MENTEITH", "CAITHNESS", "ANGUS", "LENNOX", "ROSS", "Soldiers"])
macbeth_graph.add_scene("Dunsinane. Within the castle.", ["MACBETH", "SEYTON", "Soldiers", "Drum", "Colours"])
macbeth_graph.add_scene("Another part of the field.", ["MACBETH", "MACDUFF", "YOUNG SIWARD", "Messenger"])

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
macbeth_graph.export_to_gephi('occurrences.gexf')

# Plot the graph (optional)
macbeth_graph.plot_graph()
