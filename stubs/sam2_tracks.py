import json
import pickle

# Load the existing tracks.pkl file
with open('C:/Users/conta/Desktop/football_analysis/stubs/original_08fd33_4/track_stubs.pkl', 'rb') as file:
    tracks = pickle.load(file)

del tracks["ball"]

# Load the ball_bboxes.json file
with open('C:/Users/conta/Desktop/football_analysis/stubs/sam2_08fd33_4/ball_bboxes_08fd33_4.json', 'r') as file:
    ball_bboxes = json.load(file)

# Add the ball_bboxes to the tracks dictionary with the key "ball"
tracks["ball"] = ball_bboxes

# Save the updated dictionary back to tracks.pkl
with open('tracks.pkl', 'wb') as file:
    pickle.dump(tracks, file)

print("Updated dictionary saved to tracks.pkl")