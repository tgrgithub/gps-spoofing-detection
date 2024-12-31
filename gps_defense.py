import pandas as pd

# Load original and spoofed datasets
original_data = pd.read_csv('gps_data.csv')
spoofed_data = pd.read_csv('spoofed_gps_data.csv')

# Detect inconsistencies (e.g., large differences in coordinates)
threshold = 0.001
discrepancies = (abs(original_data['latitude'] - spoofed_data['latitude']) > threshold) | \
                (abs(original_data['longitude'] - spoofed_data['longitude']) > threshold)

spoofed_data['is_spoofed'] = discrepancies

# Save results
spoofed_data.to_csv('defense_results.csv', index=False)
print("Defense analysis completed. Results saved to defense_results.csv")
