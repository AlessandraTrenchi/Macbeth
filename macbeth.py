import pandas as pd

# Creating the dataset
param = {
    'Character': ['GentleWoman','First Witch', 'Second Witch', 'Third Witch', 'Macbeth', 'Banquo', 'Ross', 'Duncan', 'Malcolm', 'Captain', 'Angus', 'Lennox', 'Lady Macbeth', 'Fleance', 'Porter', 'Donalbain', 'Old man', 'First murderer', 'Second murderer', 'Third murderer' , 'Ghost of Banquo', 'Hecate', 'Lady Macduff', 'Son', 'Doctor', 'First Apparition', 'Second Apparition', 'Third Apparition', 'Menteith', 'Caithness', 'Seyton', 'Old Siward', 'Young Siward', 'Macduff'],
    'Gender': ['Female','Female', 'Female', 'Female', 'Male',  'Male',  'Male',  'Male',  'Male',  'Male',  'Male', 'Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male'],
    'Place of belonging': ['Uknown','Unknown', 'Unknown', 'Unknown', 'Glamis', 'Scotland', 'Scotland', 'Scotland', 'Scotland', 'Scotland', 'Scotland', 'Scotland','Scotland', 'Scotland', 'Scotland', 'Scotland', 'Scotland', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Scotland', 'Scotland', 'Scotland', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Scotland', 'Scotland', 'Scotland', 'Scotland', 'Scotland'],
    'Role': ['Minor Character','Antagonist', 'Antagonist', 'Antagonist', 'Protagonist/Antihero', 'Confidant', 'Minor Character', 'Henchman', 'Antagonist', 'Minor Character', 'Minor Character', 'Minor Character', 'Confidant', 'Antagonist', 'Minor character', 'Antagonist', 'Minor Character', 'Henchman', 'Henchman', 'Henchman', 'Antagonist', 'Antagonist', 'Minor character', 'Minor character', 'Minor Character', 'Antagonist', 'Antagonist', 'Antagonist', 'Minor Character', 'Minor Character', 'Henchman', 'Antagonist', 'Antagonist', 'Antagonist'],
    'Description': [
        'The companion of Lady Macbeth',
        'Mysterious and supernatural',
        'Mysterious and supernatural',
        'Mysterious and supernatural',
        'Thane of Glamis, Thane of Cawdor and then king of Scotland',
        'Scottish nobleman, friend of Macbeth, his descendants will inherit the throne.',
        'A Scottish nobleman and ally to Macbeth',
        'The King of Scotland',
        'Duncan\'s son and heir to the throne, target for Macbeth\'s ambition.',
        'A soldier in Duncan\'s army, reporting on Macbeth\'s heroism in battle.',
        'A Scottish nobleman who supports Malcolm\'s cause against Macbeth.',
        'Another Scottish nobleman and supporter of Malcolm.',
        'The wife of Macbeth',
        'Banquo\'s son.',
        'The gatekeeper at Macbeth\'s castle',
        'Duncan\'s younger son, who flees to Ireland after his father\'s murder.',
        'An old man who witnesses the unnatural events occurring in Scotland.',
        'Assassin hired by Macbeth to carry out murders.',
        'Assassin hired by Macbeth to carry out murders.',
        'Assassin hired by Macbeth to carry out murders.',
        'The supernatural manifestation of Banquo, haunting Macbeth as a ghost.',
        'The goddess of witchcraft.',
        'The wife of Macduff, who becomes a victim of Macbeth\'s tyranny.',
        'The son of Lady Macduff, who also falls victim to the violence in Scotland.',
        'A doctor attending to Lady Macbeth.',
        'An apparition for Macbeth.',
        'An apparition for Macbeth.',
        'An apparition for Macbeth.',
        'Scottish noblemen supporting Malcolm\'s cause against Macbeth.',
        'Scottish noblemen supporting Malcolm\'s cause against Macbeth.',
        'Seyton is a servant and attendant to Macbeth.',
        'Earl of Northumberland, is a veteran soldier of the English king.',
        'Son of the English Commander',
        'Thane of Fife'
    ]
}

# Remove Macdonald, Sweno, and Sinel from the 'Character' and 'Gender' lists
characters_to_remove = ['Macdonald', 'Sweno', 'Sinel']
param = {key: [val for val in values if val not in characters_to_remove] for key, values in param.items()}

# Check the lengths of the lists in the 'param' dictionary
lengths = {key: len(value) for key, value in param.items()}

# Print lengths and lists
for key, value in param.items():
    print(f"{key}: {len(value)} - {value}")

# Verifica che tutte le liste abbiano la stessa lunghezza
if len(set(lengths.values())) == 1:
    # Creating the dataframe
    df = pd.DataFrame(param)
    print("DataFrame created successfully.")

    # Saving to a CSV file
    df.to_csv('macbeth.csv', index=False)

    # Displaying the dataframe
    print(df)
else:
    print("Error: All lists must have the same length.")
    print("Lengths:", lengths)