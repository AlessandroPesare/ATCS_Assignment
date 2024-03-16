Group Recommendations Project

This project aims to implement existing approaches for producing group
recommendations and propose your own ideas and implement them for the same
topic using Python.
A group recommender system analyses the interests of every member in the
group and provides a final decision which would be accepted by all the members.
Recommending to groups is a tedious task as we have to keep in mind each person’s
likes and dislikes in the group before giving any recommendations

Project Goals

Assignment 2: Group Recommendations
The goal of the second assignment is to implement existing approaches for producing
group recommendations and propose your own ideas and implement them for the same
topic.
The assignment may be completed in pairs. Both students are expected to understand,
be able to explain, and be able to modify the implementation.
(a) For producing group recommendation, we will use the user-based collaborative
filtering approach as this implemented in Assignment 1. Specifically, for producing group
recommendations, we will first compute the movies recommendations for each user in
the group, and then we will aggregate the lists of the individual users, so as to produce a
single list of movies for the group.
You will implement two well established aggregation methods for producing the group
recommendations.
The first aggregation approach is the average method. The main idea behind this
approach is that all members are considered equals. So, the rating of an item for a group
of users will be given be averaging the scores of an item across all group members.
The second aggregation method is the least misery method, where one member can act
as a veto for the rest of the group. In this case, the rating of an item for a group of users is
computed as the minimum score assigned to that item in all group members
recommendations.
Produce a group of 3 users, and for this group, show the top-10 recommendations, i.e.,
the 10 movies with the highest prediction scores that (i) the average method suggests,
and (ii) the least misery method suggest. Use the MovieLens 100K rating dataset.
(b) The methods employed in part (a) of Assignment 2, do not consider any
disagreements between the users in the group.
In part (b) of Assignment 2, define a way for counting the disagreements between the
users in a group, and propose a method that takes disagreements into account when
computing suggestions for the group.
Implement your method and explain why it is useful when producing group
recommendations.
Use again the group of 3 users, and for this group, show the top-10 recommendations,
i.e., the 10 movies with the highest prediction scores that your method suggests. Use the
MovieLens 100K rating dataset.
Any programming language for your assignment is acceptable. Please explain any
assumptions you made.

Required Libraries

To run the project code, make sure you have the following Python libraries installed:
Python 3.11.8
NumPy 1.26.4
Pandas 2.2.1
tabulate 0.9.0

python -m pip install -f requirements.txt

These libraries are used for data manipulation, computing similarities between users

Code Structure

The project is organized into the following modules:

folder dataset: contains data in csv format
collaborative_filtering.ipynb: implements a collaborative filtering approach (user-based) utilizing functions provided in the script collaborative_filtering.py
collaborative_filtering.py: contains functions for implementing user-based collaborative filtering, a technique used in recommendation systems. These functions facilitate the computation of user similarities and the generation of recommendations based on those similarities
similarity_metrics_evaluation.ipynb: Evaluates the performance of two different similarity metrics, Pearson similarity and ITR (Improved Triangle Similarity) similarity
download_movielens.py: Read the dataset and display the first few rows to understand it