Group Recommendations Project

This project aims to design and implement a method for producing sequential group recommendations based on existing approaches.
The method involves simple modifications to improve group satisfaction over iterations.
The implementation is demonstrated using the MovieLens 100K rating dataset, where recommendations are generated 
for a group of 3 users in 3 different sequences.

Project Goals

Assignment 3: Sequential Recommendations
Motivated by the sequential methods we discussed in class, the goal of the third
assignment is to design and implement a new method for producing sequential group
recommendations. Also, provide detailed explanations and clarifications about why the
method you propose works well for the case of sequential group recommendations.
Hint: There is no need to design a method from scratch. For the needs of this assignment,
you can suggest simple modifications of the existing approach, e.g., by proposing and
using alternatives for group aggregation that ensure good results for the group.
Produce a group of 3 users, and for this group, show the top-10 recommendations in 3
different sequences, i.e., the 10 movies with the highest prediction scores in 3 rounds,
using the MovieLens 100K rating dataset.
Any programming language for your assignment is acceptable. Please explain any
assumptions you made.
The assignment may be completed in pairs. Both students are expected to understand,
be able to explain, and be able to modify the implementation.

Required Libraries

To run the project code, make sure you have the following Python libraries installed:
Python 3.11.8
NumPy 1.26.4
Pandas 2.2.1
tabulate 0.9.0
matplotlib 3.8.3

python -m pip install -f requirements.txt

These libraries are used for data manipulation, computing similarities between users

Code Structure

The project is organized into the following modules:

folder dataset: contains data in csv format
src: This directory contains all the source code of the project:
    utils: This subdirectory contains utility functions that support various aspects of the project.
    group_recommendation: This subdirectory contains implementations of strategies for group recommendation and sequential group recommendation.
    Sequential_Group_Recommendation.ipynb: This Jupyter notebook facilitates the visualization of results obtained by invoking the two approaches for sequential group recommendation.
folder results: contains results of some experiments 