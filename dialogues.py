import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import community
import igraph
from macbeth import param
# Define the data
act_1_data = {
    'SCENE 1': ["First Witch, Second Witch, Third Witch", "The play opens with three witches gathering amidst thunder and lightening. They plan to meet with Macbeth that evening, ‘when the battle’s lost and won’ at ‘the set of sun’."],
    'SCENE 2': ["Duncan, Malcolm, Donalbain, Lennox", "At King Duncan’s camp, a wounded captain tells the king that 'brave Macbeth' fought well against the rebel forces led by Macdonald. He also reports that there was 'a fresh assault' from Norwegian troops after they had defeated Macdonald, but Macbeth and Banquo ‘doubly redoubled strokes upon the foe’ and pushed them back as well. Duncan thanks the Captain for the ‘honour’ of his words and his wounds and sends him to be treated by a surgeon. Ross arrives from Fife with further news of victory. The Norwegian king is pleading for a peace treaty and has paid a ransom, while the rebellious Thane of Cawdor has been captured. Duncan sentences Cawdor to 'present death' and tells Ross to 'greet Macbeth' with his 'former title'."],
    'SCENE 3': ["First Witch, Second Witch, Third Witch", "The witches meet on the heath. One has been killing pigs. Another has been insulted by a sailor’s wife so they plot to cast a spell which will disrupt the sailor’s next sea journey to Aleppo. They hear Macbeth and Banquo approaching and cast a spell. The men encounter the witches ‘that look not like th’inhabitants o’th’earth’. The witches hail Macbeth firstly by his title Thane of Glamis, then as Thane of Cawdor and finally as ‘king hereafter!’ Banquo says there is no need to ‘fear things that sound so fair’, and asks the witches for his future. They predict that his children will be 'kings, though thou be none’. Macbeth demands to know how their prediction about him can be true when the Thane of Cawdor is still alive but the witches vanish. Ross and Angus arrive to tell Macbeth that he has been given the title Thane of Cawdor by Duncan to thank him for his valiant efforts in the battle. Macbeth considers ‘this supernatural soliciting’. He realises that to become king, Duncan would have to die but he thinks this is a ‘horrid image’. Then he adds in an aside that ‘chance may crown me, without my stir’. Banquo and Macbeth decide to discuss the witches’ prophecies at a later time."],
    'SCENE 4': ["Duncan, Malcolm, Donalbain, Lennox", "King Duncan asks about the execution of Cawdor. King Duncan's son Malcolm reports that he confessed and died nobly. Macbeth and Banquo, along with Ross and Angus, join the rest of Duncan’s party. Duncan thanks them both for their part in the battle and announces that his eldest son, Malcolm, will inherit the throne from him when he dies. Duncan then says they will visit Macbeth’s castle as they travel ‘from hence to Inverness’ and will celebrate there. Macbeth decides to go on ahead to tell his wife. He remarks to himself that Malcolm is now ‘a step on which I must fall down, or else o’erleap’ to get to the throne."],
    'SCENE 5': ["Lady Macbeth", "Lady Macbeth reads a letter from her husband about his encounter with the witches. She fears that her husband is ‘too full o’th’milk of human kindness to catch the nearest way’ of achieving the throne. She wants him to come home quickly so that she can ‘pour’ her words of ambition into his ears. She is interrupted by news that the king is coming to the castle that evening and that Macbeth is already on his way. She celebrates the ‘fatal entrance’ of Duncan into their home. She calls on the spirits to ‘unsex’ her and make her capable of murder. Macbeth arrives home and Lady Macbeth immediately plants the seed of her murderous intentions. She advises him to hide their plans with innocence, but be a ‘serpent’ underneath."],
    'SCENE 6': ["Duncan, Lady Macbeth", "Duncan and the thanes arrive at Macbeth’s castle and enjoy the ‘gentle’ surroundings. Duncan is delighted to see the ‘honoured hostess’ Lady Macbeth. She welcomes him into their home, taking him to see Macbeth."],
    'SCENE 7': ["Macbeth, Macbeth", "Outside the banqueting hall, Macbeth considers his complex thoughts about killing Duncan. He struggles with his conscience and decides not to go through with it because it is only his ‘vaulting ambition’ that is pushing him onwards. Lady Macbeth tells him off for leaving the hall. When Macbeth tells her that he has decided against killing Duncan, she is furious, calling him a coward and a ‘beast’. She goads him by saying that she would have ‘dash’d the brains out’ of her own baby if she had promised it to him. Macbeth is further persuaded by the strength of their plan. She will give Duncan’s two guards so much wine that they ‘lie as in death’, allowing Duncan to be an unguarded target for Macbeth to attack in the night. They will frame the guards for Duncan’s murder by covering their daggers in Duncan’s blood. The final step of the plan is for Lady Macbeth and Macbeth to act horrified on the discovery of the murder and ‘clamour roar / Upon his death’. Macbeth is ‘settled’ to kill Duncan."],
}


act_2_data = {
    'SCENE 1': ["Banquo, Fleance", "Talk about the time."],
    'SCENE 2': ["Lady Macbeth, Lady Macbeth", "Give him the daggers."],
    'SCENE 3': ["Porter, Macduff", "Talk about getting drunk."],
    'SCENE 4': ["Ross, Macduff", "Reports that Macbeth has been named king and he plans to go to Scone for his coronation."],
    'SCENE 5': ["Hecate, First Witch, Second Witch, Third Witch", "Hecate scolds them because they did not involve her."],
}

act_3_data = {
    'SCENE 1': ["Banquo, Banquo", "Afraid about Macbeth and the prophecy."],
    'SCENE 2': ["Macbeth, Lady Macbeth, Banquo", "Talk about Malcolm and Donalbain being murderers. Talk about Macbeth's crowning the day after. Banquo tells him he is going riding."],
    'SCENE 3': ["Macbeth, Old Siward", "Macbeth tells him to get the murderers."],
    'SCENE 4': ["Macbeth, First murderer, Second murderer", "They talk about Banquo and Fleance's murder."],
    'SCENE 5': ["Hecate, First Witch, Second Witch, Third Witch", "Hecate is angry with the witches for giving prophecies to Macbeth without consulting her."],
    'SCENE 6': ["Lady Macbeth, Lennox, Ross", "She tells them the king has a sickness."],
}

act_4_data = {
    'SCENE 1': ["First Witch, Second Witch, Third Witch, Hecate", "The witches cast a spell around a cauldron. Hecate congratulates them. Macbeth visits the witches, and they show him three apparitions. Firstly, an armed head appears, saying that Macbeth should ‘beware Macduff’. Secondly, a bloody child appears, saying ‘none of woman born shall harm Macbeth’. Thirdly, a crowned child holding a tree appears, saying that he will never be defeated ‘until Great Birnam Wood to high Dunsinane hill shall come against him’. Macbeth is reassured but asks if Banquo’s descendants will ever reign. The witches advise against his question, but he demands that they answer. An apparition of eight kings appears following Banquo’s ghost. Macbeth is terrified and angry, but the witches disappear. Lennox arrives with word that Macduff has fled to England. Privately, Macbeth vows to kill all of Macduff’s family, including ’his wife, his babes, and all unfortunate souls that trace him in his line'."],
    'SCENE 2': ["Lady Macduff, Ross", "Lady Macduff worries about why her husband has fled to England. Ross reassures her that Macduff is ‘noble, wise, judicious’ but dares not tell her any more and leaves. Lady Macduff tells her son that his father is dead and was a traitor, but he teases her and knows it is not true. A messenger advises Lady Macduff to flee with her family, but she does not go, saying she has ‘done no harm’. Murderers arrive seeking Macduff and, finding him gone, they kill both his son and wife."],
    'SCENE 3': ["Macduff, Malcolm, Old Siward, Doctor", "In England, Macduff tells Malcolm of how Scotland is suffering under the ‘tyrant’ Macbeth. Malcolm is suspicious of Macduff and tests his loyalty by saying that if Malcolm became king, his own ‘vices’ would be worse than Macbeth's. Macduff excuses several of Malcolm’s flaws. However, when Malcolm claims that he will bring chaos to Scotland were he to rule, Macduff condemns him, saying his ‘hope ends here’. Seeing Macduff’s response, Malcolm’s suspicions are gone, and he tells Macduff that he was ‘false speaking’ and is, in fact, devoted to his country and people. Malcolm is ready with Old Siward and 10,000 men to invade Scotland. A doctor tells how King Edward cures people through touch, which is a gift bestowed on true kings. Ross arrives to tell Macduff the terrible news about the death of his wife and children. Malcolm comforts Macduff, advising that they ‘make us medicines of our great revenge to cure this deadly grief'."],
}


act_5_data = {
    'SCENE 1': ["Doctor, GentleWoman", "Talk about Lady Macbeth's craziness"],
    'SCENE 2': ["Menteith, Angus, Caithness, Lennox", "Organize to meet near Birnam Wood."],
    'SCENE 3': ["Macbeth, Doctor", "Macbeth asks about Malcolm's origin"],
    'SCENE 4': ["Old Siward, Macbeth", "Tells him there are ten thousand men at his castle's gate."],
    'SCENE 5': ["Malcolm , Old Siward , Macduff, Menteith", "Malcolm advises that everyone should hide behind a wood bough so the enemy will not know how many soldiers there are."],
    'SCENE 6': ["Seyton, Macbeth", "He tells him Lady Macbeth is dead."],
    'SCENE 7': ["Seyton, Macbeth", "He tells him Lady Macbeth is dead."],
    'SCENE 8': ["Malcolm, Old Siward, Macduff", "Malcolm promises to fight with Siward for Macduff until they cannot anymore."],
    'SCENE 9': ["Malcolm, Old Siward, Ross, Macduff", "Macduff arrives with Macbeth’s severed head. He hails Malcolm the new King of Scotland."],

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
