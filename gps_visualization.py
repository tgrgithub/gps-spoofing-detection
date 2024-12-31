import pandas as pd
import matplotlib.pyplot as plt

# Load data
spoofed_data = pd.read_csv('spoofed_gps_data.csv')

# Plot spoofed GPS coordinates
plt.scatter(spoofed_data.index, spoofed_data['latitude'], label='Spoofed Latitude', color='red')
plt.scatter(spoofed_data.index, spoofed_data['longitude'], label='Spoofed Longitude', color='blue')
plt.legend()
plt.title("GPS Spoofing Visualization")
plt.xlabel("Data Points")
plt.ylabel("Coordinates")
plt.savefig('gps_spoofing_visualization.png')
plt.show()
