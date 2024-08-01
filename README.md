# NYC Housing Price Prediction
By Brianna Trigueros-Pericone, Kyle Keegan, Sarah Arif, Darshan Patel

Project Objective
The objective of this project is to predict the residence value of properties where the price per square foot was greater than $1550/sq ft in the five boroughs of New York City: Manhattan (New York County), Brooklyn (Kings County), The Bronx (Bronx County), Staten Island (Richmond County), and Queens (Queens County). 
The home value will be predicted based off of factors such as number of bedrooms/bathrooms, the property size, and which borough it is in.

The dataset we used for this project was the property values in the five boroughs of New York City from Kaggle. The dataset included property size, number of rooms, availability, addresses, and more. 
We primarily looked at Condos, Co-ops, Multi-family homes, Houses, and Townhouses.

Source: https://www.kaggle.com/datasets/nelgiriyewithana/new-york-housing-market

Code Overview
- First cleaned dataset to remove redundant and unnecessary information, as well as add a price per square foot column based on the sale of the property and the square footage. 
- Target variable is price per square foot greater than 15$/sqft
- Data was scaled and run through a Linear Regression model
- Mean square error was .2015, R^2 = .8132, property size has greatest coefficient of .5881
- We then ran a Logistical Regression model that had a classification accuracy of 95%
- We also ran a RandomForest and Decision Tree classifier to test the different accuracies. The two models had accuracies of 94% and 93% respectively. 

Conclusion:
BAsed on the assessment of home prices that were evaluated, we've discovered that of all the factors include in the dataset, that the SQ footage of the residence no matter the type places the biggest importance in price for NYC. The locations and bedrooms did not have as much of impact as we had orrignally assumed. 
