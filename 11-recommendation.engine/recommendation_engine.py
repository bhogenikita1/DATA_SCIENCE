# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 09:39:23 2024

@author: HP
"""

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Load the .csv file
data = pd.read_csv("Entertainment.csv")
data.head()

# Step 1: Normalize the review scores
# We use MinMaxScaler to scale the reviews between 0 and 1.
scaler = MinMaxScaler()
data['Normalized_reviews'] = scaler.fit_transform(data[['Reviews']])

# Step 2: Compute the cosine similarity for normalized reviews
cosine_sim_reviews = cosine_similarity(data[['Normalized_reviews']])

# Step 3: Create a function to recommend titles based on similarity
def get_recommendation(title, cosine_sim=cosine_sim_reviews):
    # Get the index of the title that matches the input title
    idx = data[data['Titles'] == title].index[0]

    # Get the pairwise similarity scores of all titles with that title
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the titles based on the similarity scores in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices of the most similar titles
    sim_indices = [i[0] for i in sim_scores[1:6]]  # Exclude the first as it is the title itself

    # Return the top 5 most similar titles
    return data['Titles'].iloc[sim_indices]

# Test the recommendation system with an example title
example_title = "Toy Story (1995)"
collaborative_recommended_titles = get_recommendation(example_title)

# Print the recommendations
print(f"Collaborative Recommendations for '{example_title}':")
for title in collaborative_recommended_titles:
    print(title)
