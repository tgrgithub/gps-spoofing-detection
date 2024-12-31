import pandas as pd

# Load the GPS dataset
gps_data = pd.read_csv('gps_data.csv')

# Introduce spoofing by modifying latitude and longitude
gps_data['latitude'] += 0.002  # Add an offset
gps_data['longitude'] += 0.002

# Save spoofed data
gps_data.to_csv('spoofed_gps_data.csv', index=False)

print("Spoofing completed. Saved as spoofed_gps_data.csv")
