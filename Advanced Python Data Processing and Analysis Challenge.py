import re
from collections import Counter

def analyze_blog_sentiments(blog_file):
    # List of positive and negative words for sentiment analysis
    positive_words = ["amazing", "enjoy", "beautiful", "wonderful", "breathtaking", "stunning", "memorable", "excellent", "fantastic", "unique"]
    negative_words = ["bad", "disappointing", "poor", "lackluster", "scarce", "overcrowded"]
    
    pos_count = 0
    neg_count = 0
    
    try:
        # Open the file and read its content
        with open(blog_file, 'r') as file:
            text = file.read().lower()  # Convert text to lowercase to ensure case-insensitive matching
            # Find all words using regex
            words = re.findall(r'\b\w+\b', text)
            # Count occurrences of each word
            word_counts = Counter(words)
            
            # Count positive words
            for word in positive_words:
                pos_count += word_counts[word]
            
            # Count negative words
            for word in negative_words:
                neg_count += word_counts[word]
                
    except FileNotFoundError:
        print(f"The file '{blog_file}' does not exist.")
    except PermissionError:
        print(f"Permission denied to read the file '{blog_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Return the counts of positive and negative words
    return pos_count, neg_count

if __name__ == "__main__":
    blog_file = 'travel_blogs.txt'  # Specify the file name
    pos_count, neg_count = analyze_blog_sentiments(blog_file)
    print(f"Positive words count: {pos_count}")
    print(f"Negative words count: {neg_count}")

import os

def read_weather_data(file):
    temperatures = []
    
    try:
        # Open the file and read line by line
        with open(file, 'r') as f:
            for line in f:
                # Split each line into date and temperature
                date, temp = line.strip().split(',')
                # Convert temperature to integer after removing '°C'
                temp = int(temp.replace('°C', ''))
                # Append the temperature to the list
                temperatures.append(temp)
                
    except FileNotFoundError:
        print(f"The file '{file}' does not exist.")
    except PermissionError:
        print(f"Permission denied to read the file '{file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    # Return the list of temperatures
    return temperatures

def calculate_average_temperatures(files):
    yearly_averages = {}
    
    # Process each file to calculate yearly average temperatures
    for file in files:
        year = file.split('_')[1].split('.')[0]  # Extract the year from the filename
        temperatures = read_weather_data(file)
        if temperatures:
            # Calculate the average temperature for the year
            yearly_averages[year] = sum(temperatures) / len(temperatures)
    
    return yearly_averages

if __name__ == "__main__":
    # List of weather data files
    weather_files = ['weather_2020.txt', 'weather_2021.txt']  # Add more files as needed
    yearly_averages = calculate_average_temperatures(weather_files)
    
    # Print the average temperature for each year
    for year, avg_temp in yearly_averages.items():
        print(f"Average temperature for {year}: {avg_temp:.2f}°C")
    
    # Identify and print the year with the highest average temperature
    if yearly_averages:
        warmest_year = max(yearly_averages, key=yearly_averages.get)
        print(f"The year with the highest average temperature is {warmest_year} with an average of {yearly_averages[warmest_year]:.2f}°C")
