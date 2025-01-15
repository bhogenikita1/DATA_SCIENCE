# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:05:24 2025

@author: HP
"""


import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
#Load the CSV file
data=pd.read_csv("game.csv")
data.head()
userId	game
'''	rating
0	3	The Legend of Zelda: Ocarina of Time	4.0
1	6	Tony Hawk's Pro Skater 2	5.0
2	8	Grand Theft Auto IV	4.0
3	10	SoulCalibur	4.0
4	11	Grand Theft Auto IV	4.5
'''
#Step 1: Create a user-item matrix(rows:users,columns: games,values: rating)
user_item_matrix=data.pivot_table(index='userId',columns='game',values='rating')
'''
pivot_table:This function reshapes the DataFrame into a matrix where:
Each row represents a user(identified by userId)
Each column represents a game(identified by game).
The valuses in the matrix represents the ratings that user gave to the games.
'''
'\npivot_table:This function reshapes the DataFrame into a matrix where:\nEach row represents a user(identified by userId)\nEach column represents a game(identified by game).\nThe valuses in the matrix represents the ratings that user gave to the games.\n'
user_item_matrix
game	'Splosion Man	007: The World is Not Enough	10 Second Ninja X	1001 Spikes	1701 A.D.	1979 Revolution: Black Friday	2002 FIFA World Cup	2010 FIFA World Cup South Africa	3D After Burner II	3D Gunstar Heroes	...	echochrome	echochrome ii	escapeVektor: Chapter 1	flower	ilomilo	inFamous	inFamous 2	inFamous: Festival of Blood	inFamous: Second Son	page not found
userId																					
1	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
2	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
3	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
5	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
6	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
7110	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
7116	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
7117	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
7119	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
7120	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
3261 rows × 3438 columns

#Step 2:Fill NaN values with 0(assuming no rating means the game has not)
user_item_matrix_filled=user_item_matrix.fillna(0)

'''
This Line replaces any missing values (NaNs)
in the user-item matrix with 0,
indicating that the user did not rate that perticular game.
'''
'\nThis Line replaces any missing values (NaNs)\nin the user-item matrix with 0,\nindicating that the user did not rate that perticular game.\n'
#Step 3:Compute the cosine similarity between users bases on raw ratings
user_similarity=cosine_similarity=cosine_similarity(user_item_matrix_filled)

#Convert similarity matrix to a DataFrame for easy reference
user_similarity_df=pd.DataFrame(user_similarity,index=user_item_matrix.index,columns=user_item_matrix.index)
#Step 4:Function to get game recommendations for a specific user based on sililarity.
def get_recomm_user_info(user_id,num_recommendations=5):
    #Get the similarity scores for the input user with all other user
    similar_users=user_similarity_df[user_id].sort_values(ascending=False)
    
    #Get the most similar users(exclusing the user themselves)
    similar_users=similar_users.drop(user_id)
    
    #Select the top N similar users to limit noise(e.g,top 50 users)
    top_similar_users=similar_users.head(50)
    #This selects the top 50 most similar users to limit noise in the recommendation
    #Get ratings of these similar users,weightd by there similarity score
    weighted_ratings=np.dot(top_similar_users.values,user_item_matrix_filled.loc[top_similar_users.index])
    #np.dot:This computes the dot product between the
    #Similarity scores of the top similar users and
    #their corresponding ratings in the user-item matrix.
    #The result is an array of the weighted ratings for each game.
    #Normalize by the sum of similarities
    sum_of_similarities=top_similar_users.sum()
    
    if sum_of_similarities > 0:
        weighted_ratings/= sum_of_similarities
        
    #This weighted ratings are normalized by dividing by the 
    #sum of similarities to avoid biasing toward user with higher ratings.
    
    #Recommend games that the user hasn't rated yet
    user_ratings=user_item_matrix_filled.loc[user_id]
    unrated_games=user_ratings[user_ratings==0]
    #This identifies game that the target user has not rated(i.e,rated 0)
    
    #Get the weighted scores for unrated games
    game_recommendations=pd.Series(weighted_ratings,index=user_item_matrix_filled.columns).loc[unrated_games.index]
    
    #This creats a pandas Series from the weighted ratings
    #and filters it to include only the unrated games.
    #Finally,it sorts the recommendations in decreasing order
    #and returns the top specificied number of recommendations.
    
    #Return the top 'num_recommendations' game recommendations
    return game_recommendations.sort_values(ascending=False).head(num_recommendations)
#Example usage:Get recommendations for a user with ID 3
recommendad_games=get_recomm_user_info(user_id=22)

#Print the recommended games
print("Recommended games for user 3:")
print(recommendad_games)
Recommended games for user 3:
game
Alan Wake: The Writer                 0.728709
Command & Conquer 3: Tiberium Wars    0.666940
World of Tanks                        0.666940
'Splosion Man                         0.000000
Retro City Rampage                    0.000000
dtype: float64
 