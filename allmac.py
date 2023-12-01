import numpy as np
import networkx as nx
import numpy as np

G = nx.DiGraph()

# Export the co-participation network to GEXF format
# Iterate through scenes and add edges based on character co-participation
# Define the characters
characters = [ #do they correspond to the list in macbeth.py? 
    "First Witch", "Second Witch", "Third Witch", "Macbeth", "Banquo",
    "Duncan", "Malcolm", "Captain", "Ross", "Lennox",
    "Lady Macbeth", "Macduff", "Hecate", "Son", "Fleance", "Porter",
    "Lady Macduff", "Donalbain", "Old Man", "Doctor", "Seyton",
    "Menteith", "Caithness", "Angus", "Young Siward", "Old Siward", "First Apparition", "Second Apparition", "Third Apparition"
]


# Define relationships according to the changes during Acts!!!
relations = [ 
    ("First Witch", "Second Witch", "Third Witch", "friendship"),
    ("Macbeth", "Macduff", "friendship"),
    ("Macbeth", "Duncan", "cousins"),
    ("Macbeth", "Banquo", "friendship"),
    ("Macbeth", "Malcolm", "friendship"),
    ("Ross", "Duncan", "friendship"),
    ("Duncan", "Banquo", "friendship"),
    ("Banquo", "Fleance", ("father", "son")),
    ("Duncan", "Malcolm", ("father", "son")),
    ("Lady Macbeth", "Duncan", ("host", "subject")),
    ("Duncan", "Donalbain", ("father", "son")),
    ("Lady Macbeth", "Macbeth", ("wife", "husband")),
    ("Duncan", "Lady Macbeth", ("lost father", "lost child")),
    ("Lady Macbeth", "Duncan", ("murderer", "murdered")),
    ("Macbeth", "Duncan", ("murderer", "murdered")),
    ("Ross", "Macduff", "cousins"),
    ("Macduff", "Porter", ("master", "servant")),
    ("Old Siward", "Malcolm", ("supporter", "supported")),
    ("Young Siward", "Old Siward", ("son", "father")),
    ("Old Siward", "Seyton", ("father", "son")),
    ("First Witch", "Macbeth", ("trickster", "tricked")),
    ("Second Witch", "Macbeth", ("trickster", "tricked")),
    ("Third Witch", "Macbeth", ("trickster", "tricked")),
    ("Hecate", "Macbeth", ("trickster", "tricked")),
    ("Duncan", "Malcolm", ("father", "son")),
    ("Macbeth", "Banquo", ("murderer", "murdered")),
    ("Macduff", "Macbeth", ("murderer", "murdered")),
    ("Lady Macduff", "Son", ("mother", "son"))
    # Add more relationships based on your information
]


# Define co-occurrences based on scenes
scenes = [ #co-participation in events
    ["First Witch", "Second Witch", "Third Witch"],
    ["Duncan", "Malcolm", "Donalbain", "Lennox"],
    ["Ross", "Duncan"],
    ["First Witch", "Second Witch", "Third Witch"],
    ["First Witch", "Second Witch", "Third Witch", "Macbeth", "Banquo"],
    ["Macbeth", "Banquo"],
    ["Macbeth", "Banquo", "Ross", "Angus"],
    ["Duncan", "Malcolm", "Donalbain", "Lennox", "Attendants"], 
    ["Lady Macbeth", "Messanger"],
    ["Duncan", "Malcolm", "Donalbain", "Banquo", "Lennox", "Macduff", "Ross", "Angus", "Attendants", "Lady Macbeth"],
    ["Macbeth", "Lady Macbeth"],
    ["Banquo", "Fleance"],
    ["Macbeth", "Banquo", "Fleance", "Servant"],
    ["Macbeth", "Lady Macbeth"],
    ["Macduff", "Porter"],
    ["Lennox", "Macbeth", "Macduff"],
    ["Lady Macbeth", "Macduff"],
    ["Macduff", "Banquo", "Lady Macbeth"],
    ["Malcolm", "Donalbain", "Macbeth", "Lennox", "Macduff", "Lady Macbeth"],
    ["Malcolm", "Donalbain"],
    ["Ross", "Old Man"],
    ["Macduff", "Ross"],
    ["Banquo", "Macbeth", "Lady Macbeth", "Lennox", "Ross", "Ladies", "Attendants"], #MACBETH, as king, LADY MACBETH, as queen, LENNOX,ROSS, Lords, Ladies, and Attendants
    ["Attendant", "Macbeth"],
    ["Attendant", "First Murderer", "Second Murderer", "Macbeth"],
    ["Lady Macbeth", "Servant"],
    ["Lady Macbeth", "Macbeth"],
    [ "First Murderer",  "Second Murderer", "Third Murderer"],
    [ "First Murderer",  "Second Murderer", "Third Murderer", "Banquo", "Fleance"],
    [ "Macbeth",  "Lady Macbeth", "Ross", "Lennox"],
    [ "Macbeth",  "Lady Macbeth", "Ross", "Lennox", "Banquo's ghost"],
    [ "Macbeth",  "Lady Macbeth", "Ross", "Lennox", "Banquo's ghost", "First murderer"],
    [ "Macbeth",  "Lady Macbeth", "Ross", "Lennox"],
    [ "Macbeth",  "Lady Macbeth", "Ross", "Lennox", "Banquo's ghost"],
    ["Macbeth", "Lady Macbeth"],
    ["First Witch", "Second Witch", "Third Witch", "Hecate"],
    ["Lennox", "Lord"],
    ["First Witch", "Second Witch", "Third Witch"], #devo includere i famigli?
    ["First Witch", "Second Witch", "Third Witch", "Hecate"],
    ["First Witch", "Second Witch", "Third Witch", "Macbeth"],
    ["First Witch", "Second Witch", "Third Witch", "Macbeth", "First Apparition"],
    ["First Witch", "Second Witch", "Third Witch", "Macbeth", "Second Apparition"],
    ["First Witch", "Second Witch", "Third Witch", "Macbeth", "Third Apparition"],
    ["Lennox", "Macbeth"],
    ["Lady Macduff", "Son", "Ross"],
    ["Malcolm", "Macduff"],
    ["Malcolm", "Macduff", "Doctor"],
    ["Malcolm", "Macduff", "Ross"],
    ["Doctor of Physic", "Waiting-Gentlewoman"],
    ["Doctor of Physic", "Waiting-Gentlewoman", "Lady Macbeth"],
    ["Menteith", "Caithness", "Angus", "Lennox", "Soldiers"],
    ["Macbeth", "Doctor", "Attendants"],
    ["Seyton", "Macbeth"],
    ["Malolm", "Siward", "Young Siward", "Macduff"],
    ["Menteith", "Caithness", "Angus", "Lennox", "Ross", "Soldiers"],
    ["Macbeth", "Seyton", "Soldiers"],
    ["Malcolm", "Siward", "Macduff"],
    ["Young Siward", "Macbeth"],
    ["Malcolm", "Siward"],
    ["Macbeth", "Macduff"],
    ["Malcolm", "Ross", "Thanes and Soldiers"],
    ["Macduff", "Malcolm", "Lennox", "Ross", "Menteth", "Caithness"] #add all remaining character names!!!!
    #not self cited nodes here because it is about the presence of people in the scene 
    # Add more scenes based on your information
]

# Define interactions based on dialogues
dialogues = [
    ("First Witch", "Second Witch", "Third Witch", "flow", "discussing the prophecy of Macbeth's fate"),
    ("Lady Macbeth", "Macbeth", "transaction", "conspiring to murder Duncan"),
    ("Lady Macbeth", "Servant", "flow", "discussing the upcoming banquet"),
    ("Duncan", "Malcolm", "Donalbain", "Lennox", "Attendants", "Sergeant", "flow", "inquiring about the bleeding sergeant's report"),
    ("Malcolm", "Sergeant", "flow", "thanking the sergeant for his bravery"),
    ("Sergeant", "Duncan", "flow", "providing information about the battle with macdonwald"),
    ("Duncan", "Sergeant", "flow", "expressing gratitude for the sergeant's service"),
    ("Duncan", "Ross", "Lennox", "flow", "welcoming ross and inquiring about the news from fife"),
    ("Ross", "Duncan", "Report","flow", "reporting on the victory over the norweyan forces and the thane of cawdor"),
    ("Duncan", "Ross", "transaction", "promoting macbeth to the thane of cawdor"),
    ("Duncan", "Malcolm", "Donalbain", "Lennox", "Attendants", "Sergeant", "flow", "inquiring about the bleeding sergeant's report"),
    ("Malcolm", "Sergeant", "flow", "thanking the sergeant for his bravery"),
    ("Sergeant", "Duncan", "Report","flow", "providing information about the battle with Macdonwald"),
    ("Duncan", "Sergeant", "Gratitude", "flow","expressing gratitude for the sergeant's service"),
    ("Duncan", "Ross", "Lennox", "flow", "welcoming Ross and inquiring about the news from Fife"),
    ("Ross", "Duncan", "flow", "reporting on the victory over the Norweyan forces and the thane of Cawdor"),
    ("Duncan", "Ross", "transaction", "promoting Macbeth to the thane of Cawdor"),
    ("First Witch", "Second Witch", "Third Witch", "flow", "discussing the prophecy of Macbeth's fate"),
    ("First Witch", "Second Witch", "Third Witch", "flow", "witches conversing about their recent activities"),
    ("First Witch", "Second Witch", "Third Witch", "flow", "first witch recounting an encounter with a sailor's wife"),
    ("Second Witch", "First Witch", "transaction", "second witch offering wind to the first witch"),
    ("Third witch", "First witch", "flow", "third witch describing her own activities"),
    ("First witch", "Second witch", "Third witch", "transaction", "witches chanting a spell"),
    ("Macbeth", "First witch", "Second witch", "Third witch", "transaction", "macbeth receiving prophecies from the witches"),
    ("Banquo", "First witch", "Second witch", "Third witch", "transaction", "banquo questioning the witches about his own future"),
    ("Ross", "Angus", "Macbeth", "Banquo", "flow", "Ross and Angus informing macbeth and banquo of king duncan's gratitude"),
    ("Macbeth", "Banquo", "Ross", "flow", "Macbeth and Banquo expressing their thoughts on the prophecies"),
    ("Duncan", "Malcolm", "Donalbain", "Lennox", "Attendants", "flow", "inquiring about execution on cawdor", "interaction"),
    ("Macbeth", "Duncan", "flow", "reflecting on the title of prince of cumberland"),
    ("Lady Macbeth", "Macbeth", "flow", "expressing fear about macbeth's nature"),
    ("Messenger", "Lady Macbeth", "transaction", "delivering news about duncan's visit"),
    ("Lady Macbeth", "Macbeth", "transaction", "encouraging macbeth to commit the king's murder"),
    ("Macbeth", "Lady Macbeth", "flow", "expressing doubts about the plan"),
    ("Lady Macbeth", "Macbeth", "transaction", "encouraging macbeth to follow through with the plan"),
    ("Duncan", "Malcolm", "Donalbain", "Banquo", "Lennox", "Macduff", "Ross", "Angus", "Lady Macbeth", "Sewer", "Servants", "flow", "welcoming duncan to macbeth's castle"),
    ("Macbeth", "Macbeth", "flow", "reflecting on the assassination"),
    ("Lady Macbeth", "Macbeth", "flow", "inquiring about why macbeth left the chamber"),
    ("Macbeth", "Lady Macbeth", "flow", "expressing hesitation about the murder", "interaction"),
    ("Lady_macbeth", "Macbeth", "transaction", "persuading macbeth to proceed with the plan"),
    ("Macbeth", "Lady Macbeth", "transaction", "committing to the murder"),
    ("Lady Macbeth", "Macbeth", "transaction", "planning to drug duncan' chamberlains"),
    ("Macbeth", "Lady Macbeth", "flow", "expressing resolve to proceed with the murder"),
    ("Macbeth", "Macbeth", "flow","reflecting on the murder"),
    ("Macbeth", "Duncan", "transaction", "committing the murder"),
    ("Macbeth", "Chamberlains", "transaction", "committing the murder"),
    ("Lady Macbeth", "Macbeth", "flow", "inquiring about why macbeth left the chamber"),
    ("Messenger", "Lady Macbeth", "flow", "delivering news about duncan's visit"),
    ("Lady Macbeth", "Lady Macbeth", "transaction", "summoning the evil spirits to help in committing the murder"),
    ("Duncan", "Malcolm", "Donalbain", "Banquo", "Lennox", "Macduff", "Ross", "Angus", "Sewer", "Servants", "flow", "welcoming duncan to macbeth's castle"),
    ("Macbeth", "Macbeth", "flow", "reflecting on the murder"),
    ("Banquo", "Fleance", "transaction", "giving sword to fleance"),
    ("Messenger", "Lady Macbeth", "flow", "delivering news about duncan's visit"),
    ("Lady Macbeth", "Macbeth", "flow", "discussing plan to kill duncan"),
    ("Macbeth", "Lady Macbeth", "flow", "expressing doubts about committing murder"),
    ("Lady Macbeth", "Macbeth", "transaction", "persuading macbeth to commit murder"),
    ("Macbeth", "Lady Macbeth", "transaction", "committing to commit murder"),
    ("Lady Macbeth", "Macbeth", "transaction", "planning to drug duncan's chamberlains"),
    ("Macbeth", "flow", "reflecting on murder"),
    ("Lady Macbeth", "Macbeth", "flow", "inquiring about macbeth's whereabouts"),
    ("Duncan", "Malcolm", "Donalbain", "Banquo", "Lennox", "Macduff", "Ross", "Angus", "Sewer", "flow", "welcoming duncan to macbeth's castle"),
    ("Ross", "Macduff" "flow", "news of murder"),
    ("Macbeth", "First Murderer", "transaction", "ordering Banquo and Fleance's murder"),
    ("Macbeth", "Second Murderer", "transaction", "ordering Banquo and Fleance's murder"),
    ("Macbeth", "Macbeth", "flow" "reflecting on murder"),
    ("Hecate", "First Witch", "Second Witch", "Third Witch", "transaction", "plot to trick macbeth"),
    ("Macbeth", "First Witch", "Second Witch", "Third Witch", "transaction", "Macbeth receiving prophecies from the witches"),
    ("Ross", "Lady Macduff", "flow", "information on a possible attack"),
    ("Lady Macduff", "Son", "flow", "talk about betrayal"),
    ("Messenger", "Lady Macduff", "flow", "warning of danger"),
    ("Murderers", "Lady Macduff", "flow", "Macduff's location"),
    ("First Murderer", "Son", "flow", "insulting the Son"),
    ("First Murderer", "Son", "transaction", "murder"),
    ("Macduff", "Malcolm", "flow", "resolving to take action"),
    ("Malcolm", "Macduff", "flow", "warning about Macbeth"),
    ("Doctor", "Gentlewoman", "flow", "Lady Macbeth's health"),
    ("Lady Macbeth", "Doctor", "flow", "confused confessions"),
    ("Caithness", "Lennox", "flow", "comment on Macbeth's actions"),
    ("Caithness", "Lennox", "transaction", "resolving to march"),
    ("Servant", "Macbeth", "flow", "reporting on soldiers"),
    ("Macbeth", "Seyton", "flow", "declaring intention to fight"),
    ("Doctor", "Macbeth", "flow", "reporting on Lady Macbeth's condition"),
    ("Macbeth", "Doctor", "transaction", "commanding to cure Lady Macbeth"),
    ("Malcolm", "Soldiers", "transaction", "commanding to cut boughs"),
    ("Macbeth", "Macbeth", "flow", "reflecting on past fears"),
    ("Seyton", "Macbeth", "flow", "reporting on queen's death"),
    ("Messenger", "Macbeth", "flow", "reporting on Birnam wood movement"),
    ("Macbeth", "Young Siward", "transaction", "murder"),
    ("Ross", "Macduff", "flow", "informs of his son's murder"),
    ("Macduff", "Macbeth", "transaction", "murder"),
    ("Macduff", "Malcolm", "transaction", "offers him Macbeth's head")
]

# Define the relationships based on the provided information
occur = [
    ('First Witch', 'Macbeth'),
    ('First Witch', 'Banquo'),
    ('Second Witch', 'Macbeth'),
    ('Second Witch', 'Banquo'),
    ('Third Witch', 'Macbeth'),
    ('Third Witch', 'Banquo'),
    ('Witches', 'Macbeth'),
    ('Witches', 'Banquo'),
    ('Macbeth', 'Ross'),
    ('Duncan', 'Malcolm'),
    ('Duncan', 'Macbeth'),
    ('Duncan', 'Banquo'),
    ('Lady Macbeth', 'Macbeth'),
    ('Lady Macbeth', 'Servant'),
    ('Lady Macbeth', 'Duncan'),
    ('Banquo', 'Fleance'),
    ('Banquo', 'Macbeth'),
    ('Macbeth', 'Servant'),
    ('Porter', 'Macbeth'),
    ('Macduff', 'Porter'),
    ('Macbeth', 'Lennox'),
    ('Lady Macbeth', 'Macduff'),
    ('Lady Macbeth', 'Macbeth'),
    ('Lady Macbeth', 'Servant'),
    ('Macbeth', 'First Murderer'),
    ('Macbeth', 'Second Murderer'),
    ('Macbeth', 'Third Murderer'),
    ('First Murderer', 'Second Murderer'),
    ('First Murderer', 'Third Murderer'),
    ('Banquo', 'Fleance'),
    ('Lady Macbeth', 'Second Murderer'),
    ('Malcolm', 'Donalbain'),
    ('Duncan', 'Lady Macbeth'),
    ('Banquo', 'Fleance'),
    ('Macbeth', 'Lennox'),
    ('Hecate', 'First Witch'),
    ('Hecate', 'Second Witch'),
    ('Hecate', 'Third Witch'),
    ('Macbeth', 'Lennox'),
    ('Macbeth', 'Ross'),
    ('Lady Macbeth', 'Doctor'),
    ('Malcolm', 'Macduff'),
    ('Ross', 'Macduff'),
    ('Malcolm', 'Doctor'),
    ('Ross', 'Malcolm'),
    ('Lady Macbeth', 'Ross'),
    ('Doctor', 'Gentlewoman'),
    ('Lady Macbeth', 'Macbeth'),
    ('Macbeth', 'Seyton'),
    ('Macbeth', 'Doctor'),
    ('Doctor', 'Gentlewoman'),
    ('Ross', 'Macduff'),
    ('Malcolm', 'Macduff'),
    ('Malcolm', 'Old Siward'),
    ('Macbeth', 'Seyton'),
    ('Macbeth', 'Messenger'),
    ('Macbeth', 'Soldiers'),
    ('Macbeth', 'Young Siward'),
    ('Old Siward', 'Malcolm'),
    ('Macduff', 'Malcolm')
]

for scene in scenes:
    for i, character1 in enumerate(scene):
        for character2 in scene[i+1:]:
            if G.has_edge(character1, character2):
                G[character1][character2]['weight'] += 1
            else:
                G.add_edge(character1, character2, weight=1)

nx.write_gexf(G, "co_participation_network.gexf")
# Initialize matrices
relation_matrix = np.zeros((len(characters), len(characters)), dtype=int)
co_occurrence_matrix = np.zeros((len(characters), len(characters)), dtype=int)
interaction_matrix = np.zeros((len(characters), len(characters)), dtype=int)

# Fill in the matrices based on relationships, co-occurrences, and interactions
for rel in relations:
    char1, char2, rel_type = rel
    char1_idx = characters.index(char1)
    char2_idx = characters.index(char2)

    if rel_type == "friends":
        relation_matrix[char1_idx, char2_idx] = 1
        relation_matrix[char2_idx, char1_idx] = 1
    # Add more relationship types if needed

for scene in scenes:
    for i in range(len(scene)):
        for j in range(i + 1, len(scene)):
            char1_idx = characters.index(scene[i])
            char2_idx = characters.index(scene[j])
            co_occurrence_matrix[char1_idx, char2_idx] += 1
            co_occurrence_matrix[char2_idx, char1_idx] += 1

for interaction in dialogues:
    char1, char2, interaction_type, _ = interaction
    char1_idx = characters.index(char1)
    char2_idx = characters.index(char2)
    interaction_matrix[char1_idx, char2_idx] += 1
    interaction_matrix[char2_idx, char1_idx] += 1

# Distinguish relationships in their acts
for relation in relations:
    character1, character2, *relationship = relation

    # Find the index of characters
    index1, index2 = characters.index(character1), characters.index(character2)

    # Update the relation_matrix based on the relationship type
    if isinstance(relationship[0], str):
        relation_type = relationship[0]
        if relation_type == "friendship":
            relation_matrix[index1, index2] = 1
            relation_matrix[index2, index1] = 1
        elif relation_type == "cousins":
            relation_matrix[index1, index2] = 2
            relation_matrix[index2, index1] = 2
        elif relation_type == "host_subject":
            relation_matrix[index1, index2] = 3
            relation_matrix[index2, index1] = 3
        elif relation_type == "wife_husband":
            relation_matrix[index1, index2] = 4
            relation_matrix[index2, index1] = 4
        elif relation_type == "lost_parent_child":
            relation_matrix[index1, index2] = 5
            relation_matrix[index2, index1] = 5
        elif relation_type == "murderer_murdered":
            relation_matrix[index1, index2] = 6
            relation_matrix[index2, index1] = 6
        elif relation_type == "trickster_tricked":
            relation_matrix[index1, index2] = 7
            relation_matrix[index2, index1] = 7
        elif relation_type == "father_son":
            relation_matrix[index1, index2] = 8
            relation_matrix[index2, index1] = 8
        elif relation_type == "mother_son":
            relation_matrix[index1, index2] = 9
            relation_matrix[index2, index1] = 9
    elif isinstance(relationship[0], tuple):
        relation_type = relationship[0][0]
        if relation_type == "father_son":
            relation_matrix[index1, index2] = 8
            relation_matrix[index2, index1] = 8
        elif relation_type == "mother_son":
            relation_matrix[index1, index2] = 9
            relation_matrix[index2, index1] = 9

nx.write_gexf(nx.from_numpy_matrix(relation_matrix), "relation_matrix.gexf")
nx.write_gexf(nx.from_numpy_matrix(co_occurrence_matrix), "co_occurrence_matrix.gexf")
nx.write_gexf(nx.from_numpy_matrix(interaction_matrix), "interaction_matrix.gexf")

# Print the matrices
print("Relation Matrix:")
print(relation_matrix)

print("\nCo-occurrence Matrix:")
print(co_occurrence_matrix)

print("\nInteraction Matrix:")
print(interaction_matrix)
