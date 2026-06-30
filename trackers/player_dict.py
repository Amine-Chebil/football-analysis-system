import os
import pickle

stub_path = "C:/Users/conta/Desktop/football_analysis/stubs/track_stubs.pkl"

if os.path.exists(stub_path):
    with open(stub_path, 'rb') as f:
        tracks = pickle.load(f)

