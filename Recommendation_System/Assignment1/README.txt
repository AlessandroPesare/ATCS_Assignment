Collaborative Filtering Project

This project aims to implement collaborative filtering algorithms for recommendation systems using Python.
Collaborative filtering is a commonly used technique to generate personalized recommendations to users based on
their past behaviors and the behavior patterns of other users.

Project Goals

Assignment 1: User-based Collaborative Filtering Recommendations
The goal of the first assignment is to implement a user-based collaborative filtering
approach.
The assignment may be completed in pairs. Both students are expected to understand,
be able to explain, and be able to modify the implementation.
(a) Download the MovieLens 100K rating dataset from https://grouplens.org/datasets/
movielens/ (the small dataset recommended for education and development). Read the
dataset, display the first few rows to understand it, and display the count of ratings (rows)
in the dataset to be sure that you download it correctly.
--->script download_movielens.py
(b) Implement the user-based collaborative filtering approach, using the Pearson
correlation function for computing similarities between users, and
(c) the prediction function presented in class for predicting movies scores.
---> script collaborative_filtering.py + notebook collaborative_filtering.ipynb
(d) Select a user from the dataset, and for this user, show the 10 most similar users and
the 10 most relevant movies that the recommender suggests.
---> script collaborative_filtering.py + notebook collaborative_filtering.ipynb
(e) Design and implement a new similarity function for computing similarities between
users. Explain why this similarity function is useful for the collaborative filtering approach.
Hint: Exploiting ideas from related works are highly encouraged.
---> script collaborative_filtering.py + notebook collaborative_filtering.ipynb + notebook similarity_metrics_evaluation.ipynb
Any programming language for your assignment is acceptable.
Please explain any assumptions you made. Some instructions on how to run your codes
are necessary.

Required Libraries

To run the project code, make sure you have the following Python libraries installed:
Python 3.11.8
NumPy 1.26.4
Pandas 2.2.1
tabulate 0.9.0

These libraries are used for data manipulation, computing similarities between users

Code Structure

The project is organized into the following modules:

folder dataset: contains data in csv format
collaborative_filtering.ipynb: implements a collaborative filtering approach (user-based) utilizing functions provided in the script collaborative_filtering.py
collaborative_filtering.py: contains functions for implementing user-based collaborative filtering, a technique used in recommendation systems. These functions facilitate the computation of user similarities and the generation of recommendations based on those similarities
similarity_metrics_evaluation.ipynb: Evaluates the performance of two different similarity metrics, Pearson similarity and ITR (Improved Triangle Similarity) similarity
download_movielens.py: Read the dataset and display the first few rows to understand it