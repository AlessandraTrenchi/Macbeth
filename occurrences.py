class SceneCharacterCooccurrences:
    def __init__(self):
        self.cooccurrences = {}

    def add_cooccurrence(self, character1, character2):
        pair = tuple(sorted([character1, character2]))
        self.cooccurrences[pair] = self.cooccurrences.get(pair, 0) + 1

    def display_cooccurrences(self):
        for pair, count in self.cooccurrences.items():
            print(f"{pair[0]} and {pair[1]}: {count} times")

# Example usage
scene_cooccurrences = SceneCharacterCooccurrences()

# Adding co-occurrences based on the provided information
scene_cooccurrences.add_cooccurrence("First Witch", "Second Witch")
scene_cooccurrences.add_cooccurrence("First Witch", "Third Witch")
scene_cooccurrences.add_cooccurrence("Second Witch", "Third Witch")
scene_cooccurrences.add_cooccurrence("First Witch", "Second Witch")
scene_cooccurrences.add_cooccurrence("First Witch", "Third Witch")
scene_cooccurrences.add_cooccurrence("Second Witch", "Third Witch")
scene_cooccurrences.add_cooccurrence("First Witch", "Second Witch")
scene_cooccurrences.add_cooccurrence("First Witch", "Third Witch")

# Displaying the results
scene_cooccurrences.display_cooccurrences()
