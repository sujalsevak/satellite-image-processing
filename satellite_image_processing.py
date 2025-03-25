import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
#Below code is for mini project satellite-image-processing in python

# Step 1: Simulating satellite image data (Red and Infrared bands)
# Normally, you would load actual satellite data using libraries like rasterio or geopandas.

# Simulating a 100x100 image
image_height, image_width = 100, 100

# Random values for Red and Infrared bands (normally you'd load these from an actual dataset)
red_band = np.random.rand(image_height, image_width) * 0.6  # Simulating Red band data
infrared_band = np.random.rand(image_height, image_width) * 0.8  # Simulating Infrared band data

# Step 2: Calculating NDVI (Normalized Difference Vegetation Index)
# NDVI = (Infrared - Red) / (Infrared + Red)
def calculate_ndvi(red, infrared):
    return (infrared - red) / (infrared + red)

ndvi_image = calculate_ndvi(red_band, infrared_band)

# Step 3: Generate Visualizations

# 1. NDVI Heatmap
plt.figure(figsize=(8, 6))
plt.imshow(ndvi_image, cmap='YlGn', interpolation='nearest')
plt.colorbar(label='NDVI Value')
plt.title('NDVI Heatmap')
plt.xlabel('Pixel X')
plt.ylabel('Pixel Y')
plt.savefig('ndvi_heatmap.png')
plt.show()
# 2. Histogram of NDVI values
plt.figure(figsize=(8, 6))
plt.hist(ndvi_image.flatten(), bins=50, color='green', edgecolor='black')
plt.title('Histogram of NDVI Values')
plt.xlabel('NDVI')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('ndvi_histogram.png')
plt.show()
# 3. Plotting Time Series (Simulated)
# Simulating NDVI values over time for a specific region (e.g., 5 months of data)
time_points = pd.date_range(start='2023-01-01', periods=5, freq='M')
ndvi_time_series = np.random.rand(5)  # Simulated NDVI values over time

# Creating DataFrame to organize the time series data
time_series_df = pd.DataFrame({
    'Date': time_points,
    'NDVI': ndvi_time_series
})
# Plot the Time Series
plt.figure(figsize=(8, 6))
plt.plot(time_series_df['Date'], time_series_df['NDVI'], marker='o', color='b', linestyle='-')
plt.title('NDVI Time Series')
plt.xlabel('Date')
plt.ylabel('NDVI')
plt.grid(True)
plt.xticks(rotation=45)
plt.savefig('ndvi_timeseries.png')
plt.show()

# Step 4: Save Processed Image
# Save the processed NDVI image (as a PNG)
plt.figure(figsize=(8, 6))
plt.imshow(ndvi_image, cmap='YlGn', interpolation='nearest')
plt.colorbar(label='NDVI Value')
plt.title('Processed NDVI Image')
plt.savefig('processed_ndvi_image.png')
plt.show()  # This will display the image
plt.close()  # Now you can safely close the plot after showing it
