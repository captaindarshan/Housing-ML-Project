import pandas as pd
import json
import os

# Define the path to your Downloads/Leaflet_Heatmap_Project directory
downloads_path = os.path.expanduser("~/Downloads/Leaflet_Heatmap_Project")
csv_file_path = os.path.join(downloads_path, 'clean_NY_Housing_data.csv')

# Load the CSV data
df = pd.read_csv(csv_file_path)

# Define a dictionary with localities and their corresponding lat/long
locality_coordinates = {
    "Kings County": [40.6782, -73.9442],
    "Bronx County": [40.8448, -73.8648],
    "Richmond County": [40.5795, -74.1502],
    "New York County": [40.7128, -74.0060],
    "Queens County": [40.7282, -73.7949]
}

# Function to add lat/long based on locality
def add_coordinates(row):
    locality = row['LOCALITY']
    coordinates = locality_coordinates.get(locality, [0.0, 0.0])
    return coordinates + list(row[['PRICE', 'BEDS', 'BATH', 'PROPERTYSQFT', 'TYPE', 'LOCALITY']]) + [row['Price_Above_Threshold']]

# Add a new column 'Price_Above_Threshold' to classify properties based on the threshold price
threshold_price = 500000
df['Price_Above_Threshold'] = (df['PRICE'] > threshold_price).astype(int)

# Apply the function to each row in the DataFrame to add coordinates
df_with_coords = df.apply(add_coordinates, axis=1)

# Convert DataFrame to JSON
json_data = df_with_coords.tolist()
json_file_path = os.path.join(downloads_path, 'filtered_heatmap_data_with_predictions_corrected.json')
with open(json_file_path, 'w') as json_file:
    json.dump(json_data, json_file)

print(f"JSON data saved to {json_file_path}")
