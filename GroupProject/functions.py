import matplotlib.pyplot as plt
import numpy as np

# Function to plot the total deaths by state
def plot_deaths_by_state(data, save_path=None):
    
    # Group data by 'state' and sum up the 'abs' column to get total deaths per state
    deaths_by_state = data.groupby('state')['abs'].sum()
    
    # Create a new figure with specified size
    plt.figure(figsize=(10, 8))
    
    # Plot the total deaths by state as a bar chart
    deaths_by_state.plot(kind='bar')
    
    # Set the title and labels for the chart
    plt.title('Total Deaths by State')
    plt.xlabel('State')
    plt.ylabel('Total Deaths')
    
    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    
    # Adjust the bottom margin to prevent label cutoff
    plt.subplots_adjust(bottom=0.25)
    
    # Print the top 5 states with the highest total deaths
    print("Total deaths by state (Top 5):")
    print(deaths_by_state.head())
    
    # Save the plot to the specified path if provided
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', pad_inches=0.2, dpi=300)
    
    # Display the plot
    plt.show()

# Function to plot the total deaths by gender
def plot_deaths_by_gender(data, save_path=None):
    # Group data by 'sex' and sum up the 'abs' column to get total deaths per gender
    deaths_by_gender = data.groupby('sex')['abs'].sum()
    
    # Create a new figure with specified size
    plt.figure(figsize=(8, 6))
    
    # Plot the total deaths by gender as a bar chart with custom colors
    deaths_by_gender.plot(kind='bar', color=['#99ff99','#ff9999','#66b3ff']) 
    
    # Set the title and labels for the chart
    plt.title('Total Deaths by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Total Deaths')
    
    # Keep x-axis labels horizontal
    plt.xticks(rotation=0)
    
    # Print the total deaths for each gender
    print("Total deaths by gender:")
    print(deaths_by_gender)
    
    # Save the plot to the specified path if provided
    if save_path:
        plt.savefig(save_path)
    
    # Display the plot
    plt.show()

# Function to plot the trend of deaths over time
def plot_deaths_over_time(data, save_path=None):
    # Group data by 'date' and sum up the 'abs' column to get total deaths per day
    deaths_over_time = data.groupby('date')['abs'].sum()
    
    # Create a new figure with specified size
    plt.figure(figsize=(14, 7))
    
    # Plot the total deaths over time as a line chart
    deaths_over_time.plot(color='red')
    
    # Set the title and labels for the chart
    plt.title('Trend of Deaths Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Deaths')
    
    # Add a grid to the chart for better readability
    plt.grid(True)
    
    # Print the first 5 dates with the corresponding total deaths
    print("Total deaths over time (First 5 dates):")
    print(deaths_over_time.head())
    
    # Save the plot to the specified path if provided
    if save_path:
        plt.savefig(save_path)
    
    # Display the plot
    plt.show()