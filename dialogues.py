import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Define the data
act_1_data = {
    'SCENE 1': ["First Witch, Second Witch, Third Witch", "Discussing the place and time of the event."],
    'SCENE 2': ["Duncan, Malcolm, Donalbain, Lennox, Attendants, Sergeant", "Inquiring about the bleeding sergeant's report"],
    'SCENE 3': ["First Witch, Second Witch, Third Witch", "Conspiring"],
    'SCENE 4': ["DUNCAN, MALCOLM, DONALBAIN, LENNOX, and Attendants", "Talk about the execution of the previous thane of Cawdor."],
    'SCENE 5': ["LADY MACBETH, SERVANT", "News that the king is coming."],
    'SCENE 6': ["DUNCAN, LADY MACBETH", "He thanks her for the hospitality."],
    'SCENE 7': ["MACBETH, MACBETH", "Reflects on the possibility of murder."],
}

act_2_data = {
    'SCENE 1': ["BANQUO, FLEANCE", "Talk about the time."],
    'SCENE 2': ["LADY MACBETH, LADY MACBETH", "Give him the daggers."],
    'SCENE 3': ["PORTER, MACDUFF", "Talk about getting drunk."],
    'SCENE 4': ["MACBETH, LORDS", "Tells them to sit according to their rank."],
    'SCENE 5': ["HECATE, FIRST WITCH, SECOND WITCH, THIRD WITCH", "Hecate scolds them because they did not involve her."],
    'SCENE 6': ["LENNOX, LORD", "They talk about the fate of Macduff."],
}

act_3_data = {
    'SCENE 1': ["BANQUO, BANQUO", "Afraid about Macbeth and the prophecy."],
    'SCENE 2': ["MACBETH, LADY MACBETH, BANQUO", "Talk about Malcolm and Donalbain being murderers. Talk about Macbeth's crowning the day after. Banquo tells him he is going riding."],
    'SCENE 3': ["MACBETH, SERVANT", "Macbeth tells him to get the murderers."],
    'SCENE 4': ["MACBETH, FIRST MURDERER, SECOND MURDERER", "They talk about Banquo and Fleance's murder."],
    'SCENE 5': ["MACBETH, LORDS", "Tells them to sit according to their rank."],
    'SCENE 6': ["LADY MACBETH, LENNOX, ROSS, LORDS", "She tells them the king has a sickness."],
}

act_4_data = {
    'SCENE 1': ["FIRST WITCH, SECOND WITCH, THIRD WITCH", "Talk about the coming of Macbeth"],
    'SCENE 2': ["LENNOX, MACBETH", "Talk about Macduff's disappearance."],
}

act_5_data = {
    'SCENE 1': ["DOCTOR, GENTLEWOMAN", "Talk about Lady Macbeth's craziness"],
    'SCENE 2': ["MENTEITH, ANGUS, CAITHNESS, LENNOX", "Organize to meet near Birnam Wood."],
    'SCENE 3': ["MACBETH, DOCTOR", "Macbeth asks about Malcolm's origin"],
    'SCENE 4': ["SERVANT, MACBETH", "Tells him there are ten thousand men at his castle's gate."],
    'SCENE 5': ["MALCOLM , OLD SIWARD , MACDUFF, MENTEITH", "Malcolm advises that everyone should hide behind a wood bough so the enemy will not know how many soldiers there are."],
    'SCENE 6': ["OLD SEYTON, MACBETH", "He tells him Lady Macbeth is dead."],
    'SCENE 7': ["MESSANGER, MACBETH", "He tells him the wood began moving."],
    'SCENE 8': ["MALCOLM, SIWARD, MACDUFF", "Malcolm promises to fight with Siward for Macduff until they cannot anymore."],
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

# Define the network for Scene 2
scene_2_network = {
    "Duncan": ["Malcolm", "Donalbain", "Lennox", "Attendants", "Sergeant"],
    "Malcolm": ["Duncan", "Donalbain", "Lennox", "Attendants", "Sergeant"],
    "Donalbain": ["Duncan", "Malcolm", "Lennox", "Attendants", "Sergeant"],
    "Lennox": ["Duncan", "Malcolm", "Donalbain", "Attendants", "Sergeant"],
    "Attendants": ["Duncan", "Malcolm", "Donalbain", "Lennox", "Sergeant"],
    "Sergeant": ["Duncan", "Malcolm", "Donalbain", "Lennox", "Attendants"],
    "Ross": ["Angus", "Macbeth", "Banquo"],
    "Angus": ["Ross", "Macbeth", "Banquo"],
    "Macbeth": ["Ross", "Angus", "Banquo"],
    "Banquo": ["Ross", "Angus", "Macbeth"]
}

# Create a directed graph
G = nx.DiGraph(scene_2_network)
# Specify the layout using spring_layout and adjust the k parameter for distance
pos = nx.spring_layout(G, k=5.5)

# Plot the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", edge_color="green", linewidths=0.3, arrowsize=10)
plt.title("Character Network - Scene 2")
plt.show()
