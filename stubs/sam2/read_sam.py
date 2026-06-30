import pickle

# Replace 'your_file.pkl' with the path to your .pkl file
with open('C:/Users/conta/Desktop/football_analysis/stubs/sam2/track_stubs_sam.pkl', 'rb') as file:
    data = pickle.load(file)

# Now you can use 'data' as needed
#print(data)
first_two_players = data['referees'][:2]

# Print the first two players
print(first_two_players)

