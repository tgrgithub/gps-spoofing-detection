# GPS Spoofing Detection Project

## Overview
This project simulates GPS spoofing attacks, implements anomaly detection, and visualizes spoofed GPS data to demonstrate cybersecurity defense mechanisms.

## Features
- Simulates GPS spoofing by altering coordinate data.
- Detects spoofed entries using threshold-based anomaly detection.
- Visualizes genuine vs. spoofed GPS data for analysis.

## Results
- **Accuracy**: Detected 100% of spoofed entries.
- **Visualization**: Scatter plot showing deviations in GPS coordinates.

## Files
- `gps_data.csv`: Original GPS dataset.
- `spoofed_gps_data.csv`: Spoofed GPS dataset.
- `defense_results.csv`: Anomaly detection results.
- `gps_spoofing_visualization.png`: Visualization of spoofed data.

## How to Run
1. Clone the repository:
   
   git clone https://github.com/yourusername/gps-spoofing-detection.git
   cd gps-spoofing-detection

2. Install Dependencies:
   Ensure you have Python 3.x installed.
   Install the required Python libraries:

   pip install pandas matplotlib
3.Run the Scripts:
  Execute each script in the following order:
    1.Simulate GPS Spoofing:
     python gps_spoofing.py
  This creates a spoofed GPS dataset: spoofed_gps_data.csv
    2.Detect Spoofing:
     python gps_defense.py
  This compares the original and spoofed datasets, marking anomalies   
  defense_results.csv.
    3.Visualize Results:
     python gps_visualization.py
  This generates a visualization of spoofed vs. genuine GPS data and saves it as     gps_spoofing_visualization.png.
    Review the Outputs:

    4.Check the generated files for results and insights:
  spoofed_gps_data.csv: Contains the spoofed GPS data.
  defense_results.csv: Flags spoofed entries.
  gps_spoofing_visualization.png: A scatter plot visualizing GPS spoofing.

     
