import pickle
import numpy as np

# Load names data
names_path = r'data/names.pkl'
with open(names_path, 'rb') as f:
    names = pickle.load(f)

# Load faces data
faces_data_path = r'data/faces_data.pkl'
with open(faces_data_path, 'rb') as f:
    faces = pickle.load(f)

# Check initial lengths
print(f"Initial number of faces: {faces.shape[0]}")
print(f"Initial number of names: {len(names)}")

# Assume you want to remove the fifth person (index 4)
person_to_remove_index = 2

# Determine the indices for the block of faces and names to delete
start_index = person_to_remove_index * 100
end_index = start_index + 100

# Remove the face data and corresponding names for the specified person
faces = np.concatenate((faces[:start_index], faces[end_index:]), axis=0)
names = names[:start_index] + names[end_index:]

# Check the lengths after deletion
print(f"Number of faces after deletion: {faces.shape[0]}")
print(f"Number of names after deletion: {len(names)}")

# Save the modified names data
with open(names_path, 'wb') as f:
    pickle.dump(names, f)

# Save the modified faces data
with open(faces_data_path, 'wb') as f:
    pickle.dump(faces, f)
