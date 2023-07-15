# -*- coding: utf-8 -*-
"""
Created on Sun May 28 09:13:19 2023

@author: HP
"""

#!pip install geopy
#!pip install openai

#=========================================================================
# Run this code in a single block to test the platform (run the hole file)
#=========================================================================

import datetime
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np
import ast
from sklearn.metrics.pairwise import cosine_similarity
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Load the DataFrame from the CSV file
df = pd.read_csv("C:/Users/HP\Downloads/updated_companies_dataset.csv")

# Convert certain columns to lists
df['embedding_job'] = df['embedding_job'].apply(ast.literal_eval)
df['embedding_culture'] = df['embedding_culture'].apply(ast.literal_eval)
df['coordinates_location'] = df['coordinates_location'].apply(ast.literal_eval)

# Create the main application window
window = tk.Tk()
window.title("Job Search Tool")

# Create a Text widget for displaying the search results
results_textbox = tk.Text(window, height=20, width=120)
results_textbox.pack()



# Create labels and entry fields for user input
name_label = tk.Label(window, text="Full Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

job_desc_label = tk.Label(window, text="Job Description (max 250 words):")
job_desc_label.pack()
job_desc_entry = tk.Entry(window)
job_desc_entry.pack()

culture_desc_label = tk.Label(window, text="Job Culture (max 250 words):")
culture_desc_label.pack()
culture_desc_entry = tk.Entry(window)
culture_desc_entry.pack()

location_label = tk.Label(window, text="Location in Morocco :['CASABLANCA', 'RABAT', 'AGADIR', 'OULMES', 'TANGER']")
location_label.pack()
location_entry = tk.Entry(window)
location_entry.pack()

# Function to handle the search button click event
#results_textbox = None

def search_jobs():
    global results_textbox  # Add this line
    
    # Get the user inputs
    user_name = name_entry.get()
    job_desc_input = job_desc_entry.get()
    culture_desc_input = culture_desc_entry.get()
    location_input = location_entry.get()

    # Validate inputs
    if not user_name or not job_desc_input or not culture_desc_input or not location_input:
        messagebox.showwarning("Error", "Please fill in all the fields.")
        return
    
    # Get valid locations
    valid_locations = ['CASABLANCA', 'RABAT', 'AGADIR', 'OULMES', 'TANGER']

    # Validate inputs
    if location_input.upper() not in valid_locations:
        messagebox.showwarning("Please enter a valid location in Morocco: ")
        return
    
    
    # Perform the job search
    try:
        # Perform the necessary calculations (similar to the original code)

        # Set OpenAI API key
        import openai
        openai.api_key = "Unfortunately, I need to keep this secret"
        
        def adaEmbedding(string):
            response = openai.Embedding.create(input=string, model="text-embedding-ada-002")
            embeddings = response['data'][0]['embedding']
            return(embeddings)

        # Calculate embeddings
        embedding_1 = adaEmbedding(job_desc_input)
        embedding_2 = adaEmbedding(culture_desc_input)

        # Get location coordinates
        geolocator = Nominatim(user_agent="Chrome/58.0.3029.110")
        location1 = geolocator.geocode(location_input)
        input_lat, input_lon = location1.latitude, location1.longitude
        input_coordinates = (input_lat, input_lon)

        # Calculate cosine similarity for job embeddings
        embedding_jobs = np.array(df['embedding_job'].tolist())
        embedding_1 = np.array(embedding_1).reshape(1, -1)
        similarities = cosine_similarity(embedding_1, embedding_jobs)

        # Calculate cosine similarity for culture embeddings
        embedding_culture = np.array(df['embedding_culture'].tolist())
        embedding_2 = np.array(embedding_2).reshape(1, -1)
        similarities_2 = cosine_similarity(embedding_2, embedding_culture)

        # Calculate distance and inverse distance
        df['distance'] = df['coordinates_location'].apply(lambda x: geodesic(input_coordinates, x).km)

        # Calculate the inverse of the distance (add 1 to avoid division by zero)
        df['Inverse Distance'] = 1 / (df['distance'] + 1)

        # Create a new DataFrame with the desired features
        new_df = pd.DataFrame()
        new_df['Company Name'] = df['Comapany_name']
        new_df['Job Description'] = similarities[0]
        new_df['Job Culture'] = similarities_2[0]
        new_df['Inverse Distance'] = df['Inverse Distance']
        new_df['user_name'] = user_name

        def is_dominated(row, df):
          criteria_values = row[['Job Description', 'Job Culture', 'Inverse Distance']].values
          better_in_at_least_one = (df[['Job Description', 'Job Culture', 'Inverse Distance']].values > criteria_values).any(axis=1)
          at_least_as_well_in_all = (df[['Job Description', 'Job Culture', 'Inverse Distance']].values >= criteria_values).all(axis=1)
          return (better_in_at_least_one & at_least_as_well_in_all).any()

        pareto_front = new_df[~new_df.apply(lambda row: is_dominated(row, new_df), axis=1)]

        # Create an empty DataFrame to store the matching company rows
        company_row = pd.DataFrame()

        # Iterate over each company name in the pareto_front dataset
        for company_name in pareto_front['Company Name']:
          # Find the corresponding row in the df dataset based on the company name
          matching_rows = df[df['Comapany_name'] == company_name]
          # Append the matching rows to the company_row DataFrame
          company_row = company_row.append(matching_rows)

        # Create a string to store the results for display
        results_text = ""

        # Iterate over the matching company rows
        for index, row in company_row.iterrows():
          company_name = row['Comapany_name']
          culture = row['Culture']
          job_opportunities = row['Job_Opportunities']
          location = row['Location']

          # Add the company information to the results string
          results_text += f"Company Name: {company_name}\n"
          results_text += f"Culture: {culture}\n"
          results_text += f"Job Opportunities: {job_opportunities}\n"
          results_text += f"Location: {location}\n"
          results_text += "------------------------------\n\n\n"

        
        # Update the results_textbox with the search results
        results_textbox.delete(1.0, tk.END)
        results_textbox.insert(tk.END, results_text)
        # Show the results in a messagebox
        #Pmessagebox.showinfo("Search Results", "Here are the matching job opportunities:\n\n" + results_text)

        # Save company_row to CSV
        
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"company_results_{user_name}_{current_datetime}.csv"
        company_row.to_csv(filename, index=False)
        #messagebox.showinfo("Success", f"Search results saved to '{filename}'.")        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during the search: {str(e)}")

    

# Create the search button
search_button = tk.Button(window, text="Search", command=search_jobs)
search_button.pack()

# Create labels and entry fields for rating and comments
rating_label = tk.Label(window, text="Rating (out of 5):")
rating_label.pack()
rating_entry = tk.Entry(window)
rating_entry.pack()

comments_label = tk.Label(window, text="Comments or suggestions of companies that match to your preferences?:")
comments_label.pack()
comments_entry = tk.Entry(window)
comments_entry.pack()


# Function to handle saving to CSV
def save_to_csv():
    # Get the input values
    user_name = name_entry.get()
    job_desc_input = job_desc_entry.get()
    culture_desc_input = culture_desc_entry.get()
    location_input = location_entry.get()
    rating = rating_entry.get()
    comments = comments_entry.get()

    # Validate inputs
    if not user_name or not job_desc_input or not culture_desc_input or not location_input or not rating:
        messagebox.showwarning("Error", "Please fill in all the fields.")
        return
    """
    # Validate inputs
    if rating>5:
        messagebox.showwarning("Error", "Please, give a rate less not more than 5.")
        return
    """
    # Save to CSV
    data = {
        'User Name': [user_name],
        'Job Description': [job_desc_input],
        'Job Culture': [culture_desc_input],
        'Location': [location_input],
        'Rating': [rating],
        'Comments': [comments]
    }
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    df_feed = pd.DataFrame(data)
    df_feed.to_csv(f'user_feedback_{user_name}_{current_datetime}.csv', index=False)
    
    messagebox.showinfo("Success", "Thank you for giving us your feedback.")

# Create the save button
save_button = tk.Button(window, text="Save Feedback", command=save_to_csv)
save_button.pack()



# Start the main event loop
window.mainloop()

