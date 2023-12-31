# -*- coding: utf-8 -*-
"""Copie de GOFAR_part_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/150N3NjZq8J_AvB35iz0sEjx8UoAkTTm-

# **In this first part, we want to generate some top companies in Morocco and create their embedding (vectorisation) as well as their location coordinates**
"""

pip install openai

import openai
openai.api_key = "Unfortunately, I need to keep this secret"

def GPT(prompt):
        response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=2048, n=1, stop=None, temperature=0.5)
        response_text = response["choices"][0]["text"]
        return(response_text)



"""# **Generating companies database**"""

companies_list = ['Office Chérifien des Phosphates (OCP)', 'OCP Africa', 'Foundation OCP', 'International Water Resources Institute (IWRI)', 'Moroccan Foundation for Advanced Science (MASCIR)', 'Research Institute for Solar Energy and New (IRESEN)', 'Agri Edge Solutions', 'Banque Populaire du Maroc', 'BMCE Bank', 'Attijariwafa Bank', 'Inwi', 'Maroc Telecom', 'Méditel', 'Label\'Vie', 'Ynna Holding', 'Maghreb Oxygène', 'Lesieur Cristal', 'Afriquia', 'Cosumar', 'Centrale Danone', 'Marsa Maroc', 'Managem', 'Addoha Group', 'ONCF', 'Royal Air Maroc', 'Office National de l\'Electricité et de l\'Eau Potable (ONEE)', 'Société Nationale d\'Investissement (SNI)', 'Saham Assurance', 'Wafa Assurance', 'Atlanta Sanitaire', 'La Samir', 'Mutandis', 'Label\'Vie', 'SNEP', 'Sopriam', 'Holmarcom Group', 'Cosumar', 'Les Eaux Minérales d\'Oulmès (LEMO)', 'Lesieur Cristal', 'La Société Marocaine d\'Electrolyse et de Chemie (SMEC)', 'Maroc Telecom', 'Med Paper', 'Plastima', 'SNEP', 'Société Marocaine des Tabacs (SMT)', 'Sopriam', 'Timar', 'Ynna Holding', 'Renault Tanger-Med', 'Société d\'Articles Hygiéniques (SAH)', 'Société Maghrébine de Monétique (S2M)', 'Patisserie Amandine', 'Chaabi Lil Iskane', 'CNIA Saada', 'Delta Holding', 'Douja Promotion Groupe Addoha', 'Eqdom', 'Holmarcom Group', 'Maghrebail', 'M2M Group', 'Onapar', 'Redal', 'Salafin', 'Société Générale Marocaine de Banques (SGMB)', 'Société Marocaine d\'Ingénierie Touristique (SMIT)', 'Société Marocaine des Hydrocarbures et de la Chimie (SMHC)', 'Somed', 'Sonasid', 'Sonasid Algérie', 'Sopriam', 'Total Maroc', 'TMSA', 'Wafa Immobilier', 'Zellidja S.A', 'Zellidja S.A. Maroc', 'Zellidja S.A. Congo', 'Auto Nejma', 'Auto Hall', 'Auto Réseau', 'Bricoma', 'Ciments du Maroc', 'Compagnie Générale Immobilière (CGI)', 'Dislog Group', 'Enda Inter-Arabe', 'Label\'Vie', 'Les Dérivés Résiniques et Terpéniques (DRT)', 'Managem', 'M2M Group', 'Marwa', 'MedZ', 'Mena Media Consulting', 'Mutandis', 'Oulmès', 'Petroserv', 'Samir', 'SNEP', 'Sopriam', 'STROC Industrie', 'Timar','Ynna Holding','Zellidja S.A.','Zellidja S.A. Algérie','Zellidja S.A. Gabon','Afriquia Gaz','Al Omrane', 'Auto Hall', 'BCI Bank (Banque Centrale Internationale)', 'Centrale Danone', 'CIMR (Caisse Interprofessionnelle Marocaine de Retraites)', 'City Club', 'CIH Bank (Crédit Immobilier et Hôtelier)', 'CTM (Compagnie de Transport au Maroc)', 'CTM Immobilier', 'Delattre Levivier Maroc', 'Delta Holding', 'Diac Salaf', 'Douja Promotion Groupe Addoha', 'HPS (Hightech Payment Systems)', 'Involys', 'La Marocaine Vie', 'Label','Vie', 'Les Domaines Agricoles', 'Lesieur Cristal', 'Maghrebail', 'Managem', 'Méditel', 'Mutandis', 'Nareva Holding', 'Novec', 'OCP Group (Office Chérifien des Phosphates)', 'ONDA (Office National des Aéroports)', 'ONHYM (Office National des Hydrocarbures et des Mines)']

companies = companies_list[:50]
len(companies)

import pandas as pd

import openai


# openai.api_key = "YOUR_API_KEY"
model_engine = "text-davinci-002"

#companies = ["OCP Group", "Inwi", "Maroc Telecom"]
company_info = {}

# Generate values for the "Culture" column
for company in companies:
    prompt = f"Generate the culture of {company}"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text.strip()
    company_info[company] = {"Culture": message}

# Generate values for the "Main Job Opportunities for UM6P students" column
for company in companies:
    prompt = f"Generate the main job opportunities for UM6P students at {company}"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=40,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text.strip()
    company_info[company]["Job_Opportunities"] = message

# Generate values for the "Location in Morocco" column
for company in companies:
    prompt = f"Generate only the name of the city where the company {company} is located in Morocco in only one word"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text.strip()
    company_info[company]["Location"] = message

# Convert the dictionary to a pandas DataFrame
df2 = pd.DataFrame.from_dict(company_info, orient="index")

df2.head()

df2["Location"].value_counts()

df2["Comapany_name"] = df2.index

df2.reset_index(inplace = True)

df2.head()

df2.drop(columns="Location", inplace=True)

df2 = df2.rename(columns={"Location2":"Location"})

# to export the data and download it
from google.colab import files
df2.to_csv('companies_dataset.csv', encoding = 'utf-8-sig') 
files.download('companies_dataset.csv')

"""# **Embedding**"""

import pandas as pd
import numpy as np

df = pd.read_csv("companies_dataset.csv")

df.head(5)

def adaEmbedding(string):
        response = openai.Embedding.create(input=string, model="text-embedding-ada-002")
        embeddings = response['data'][0]['embedding']
        return(embeddings)

df["Culture"][0]

df.columns

# Embedding culture and job opportunies
culture_embedding_list = []
job_embedding_list = []

for i in range(len(df)):
  culture = df["Culture"][i]
  embedding_output = adaEmbedding(culture)
  culture_embedding_list.append(embedding_output)

  job = df["Job_Opportunities"][i]
  embedding_output = adaEmbedding(job)
  job_embedding_list.append(embedding_output)

# Adding new columns for the embedding results
df["embedding_culture"] = culture_embedding_list
df["embedding_job"] = job_embedding_list

df["embedding_culture"].head(5)

# Getting an encoding for each location
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="Chrome/58.0.3029.110")

# Get the latitude and longitude of the first location
location_code_list = []

for i in range(len(df)):
  location = df["Location"][i]
  location1 = geolocator.geocode(location)
  lat1, lon1 = location1.latitude, location1.longitude
  list_code = [lat1, lon1] 
  location_code_list.append(list_code)

df["coordinates_location"] = location_code_list
df["coordinates_location"].head(5)

# to export the new data and download it
from google.colab import files
df.to_csv('updated_companies_dataset.csv', encoding = 'utf-8-sig') 
files.download('updated_companies_dataset.csv')

"""End of the part 1
