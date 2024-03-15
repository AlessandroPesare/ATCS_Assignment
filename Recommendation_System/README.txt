Collaborative Filtering Project

This project aims to implement collaborative filtering algorithms for recommendation systems using Python.
Collaborative filtering is a commonly used technique to generate personalized recommendations to users based on
their past behaviors and the behavior patterns of other users.

Project Goals

Implement collaborative filtering algorithms for recommending movies.
Evaluate the performance of collaborative filtering algorithms on MovieLens datasets.

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
collaborative_filtering.ipynb: implements a collaborative filtering approach (user-based) utilizing functions provided in the script collaborative_filtering.py: contains functions for implementing user-based collaborative filtering, a technique used in recommendation systems. These functions facilitate the computation of user similarities and the generation of recommendations based on those similarities
similarity_metrics_evaluation.ipynb: evaluates the performance of two different similarity metrics, Pearson similarity and ITR (Improved Triangle Similarity) similarity
download_movielens.py:  Read the dataset and display the first few rows to understand it
