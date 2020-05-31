# -*- coding: utf-8 -*-
"""
NETWORK ANALYSIS OF GAME OF THRONES CHARACTERS
Created on Sun May 24 13:02:22 2020
@author: Stanislav "Stas" Lukashevich
"""

# Importing modules
import pandas as pd
from IPython.display import display
# Reading in datasets/book1.csv
# Printing out the head of the dataset
book1 = pd.read_csv('book1.csv')
display(book1.head())
# Importing modules
import networkx as nx
# Creating an empty graph object
G_book1 = nx.Graph()
# Iterating through the DataFrame to add edges
for _, edge in book1.iterrows():
    G_book1.add_edge(edge['Source'], edge['Target'], weight=edge['weight'])
# Creating a list of networks for all the books
books = [G_book1]
book_fnames = ['datasets/book2.csv', 'datasets/book3.csv', 'datasets/book4.csv', 'datasets/book5.csv']
for book_fname in book_fnames:
    book = pd.read_csv(book_fname)
    G_book = nx.Graph()
    for _, edge in book.iterrows():
        G_book.add_edge(edge['Source'], edge['Target'], weight=edge['weight'])
    books.append(G_book)

nx.draw(G_book)





#------------------------------------------------------------
#Finding the most important character using DEGREE CENTRALITY
#------------------------------------------------------------
    
# Calculating the degree centrality of book 1-5
deg_cen_book1 = nx.degree_centrality(books[0])
deg_cen_book2 = nx.degree_centrality(books[1])
deg_cen_book3 = nx.degree_centrality(books[2])
deg_cen_book4 = nx.degree_centrality(books[3])
deg_cen_book5 = nx.degree_centrality(books[4])
# Sorting the dictionaries according to their degree centrality and storing the top 10
sorted_deg_cen_book1 = sorted(deg_cen_book1.items(), key=lambda x:x[1], reverse = True)[0:10]
sorted_deg_cen_book2 = sorted(deg_cen_book2.items(), key=lambda x:x[1], reverse = True)[0:10]
sorted_deg_cen_book3 = sorted(deg_cen_book3.items(), key=lambda x:x[1], reverse = True)[0:10]
sorted_deg_cen_book4 = sorted(deg_cen_book4.items(), key=lambda x:x[1], reverse = True)[0:10]
sorted_deg_cen_book5 = sorted(deg_cen_book5.items(), key=lambda x:x[1], reverse = True)[0:10]
# Printing out the top 10 of book 1-5
print("TOP 5 characters in Book 1 (acc. Degree Centrality)")
print(sorted_deg_cen_book1[0:5])
print("\n")
print("TOP 5 characters in Book 2 (acc. Degree Centrality)")
print(sorted_deg_cen_book2[0:5])
print("\n")
print("TOP 5 characters in Book 3 (acc. Degree Centrality)")
print(sorted_deg_cen_book3[0:5])
print("\n")
print("TOP 5 characters in Book 4 (acc. Degree Centrality)")
print(sorted_deg_cen_book4[0:5])
print("\n")
print("TOP 5 characters in Book 5 (acc. Degree Centrality)")
print(sorted_deg_cen_book5[0:5])
print("\n")


#iterate thought the results (dictionaries) to make one aggregate list of all books
top_characters_all_books = {}
listoflists = [sorted_deg_cen_book1,sorted_deg_cen_book2,sorted_deg_cen_book3,sorted_deg_cen_book4,sorted_deg_cen_book5]

for book in listoflists :
    for character,value in book :
        if character in top_characters_all_books :
            top_characters_all_books[character] += value
        else :
            top_characters_all_books[character] = value
            
top_five_degree_centrality = sorted(top_characters_all_books.items(), key=lambda x:x[1], reverse = True)[0:10]
print("\n")
print("TOP 5 characters in ALL BOOKS (acc. Degree Centrality)")
print(top_five_degree_centrality[0:5])

#Let's document this into a CSV file (in Case we want a visualization in Tableau)
import csv
with open('got_top_characters_degree_centraility.csv', 'w', newline="") as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in top_five_degree_centrality:
       writer.writerow([key, value])
      
        
       
       
       
       
       
       
       
#------------------------------------------------------------
#Finding the most important character using BETWEENNESS CENTRALITY
#------------------------------------------------------------
       
# Calculating the betweenness centrality of book 1-5
bet_cen_book1 = nx.betweenness_centrality(books[0])
bet_cen_book2 = nx.betweenness_centrality(books[1])
bet_cen_book3 = nx.betweenness_centrality(books[2])
bet_cen_book4 = nx.betweenness_centrality(books[3])
bet_cen_book5 = nx.betweenness_centrality(books[4])
# Sorting the dictionaries according to their betweenness centrality and storing the top 10
sorted_bet_cen_book1 = sorted(bet_cen_book1.items(), key=lambda x:x[1], reverse = True)[0:10]
sorted_bet_cen_book2 = sorted(bet_cen_book2.items(), key=lambda x:x[1], reverse = True)[0:10]
sorted_bet_cen_book3 = sorted(bet_cen_book3.items(), key=lambda x:x[1], reverse = True)[0:10]
sorted_bet_cen_book4 = sorted(bet_cen_book4.items(), key=lambda x:x[1], reverse = True)[0:10]
sorted_bet_cen_book5 = sorted(bet_cen_book5.items(), key=lambda x:x[1], reverse = True)[0:10]
# Printing out the top 10 of book 1-5
print("\n")
print("TOP 5 characters in Book 1 (acc. Betweenness Centrality)")
print(sorted_bet_cen_book1[0:5])
print("\n")
print("TOP 5 characters in Book 2 (acc. Betweenness Centrality)")
print(sorted_bet_cen_book2[0:5])
print("\n")
print("TOP 5 characters in Book 3 (acc. Betweenness Centrality)")
print(sorted_bet_cen_book3[0:5])
print("\n")
print("TOP 5 characters in Book 4 (acc. Betweenness Centrality)")
print(sorted_bet_cen_book4[0:5])
print("\n")
print("TOP 5 characters in Book 5 (acc. Betweenness Centrality)")
print(sorted_bet_cen_book5[0:5])
print("\n")

#iterate thought the results (dictionaries) to make one aggregate list of all books
top_characters_all_books2 = {}
listoflists2 = [sorted_bet_cen_book1,sorted_bet_cen_book2,sorted_bet_cen_book3,sorted_bet_cen_book4,sorted_bet_cen_book5]

for book in listoflists2 :
    for character,value in book :
        if character in top_characters_all_books2 :
            top_characters_all_books2[character] += value
        else :
            top_characters_all_books2[character] = value
            
top_five_betweenness_centrality = sorted(top_characters_all_books2.items(), key=lambda x:x[1], reverse = True)[0:10]
print("\n")
print("TOP 5 characters in ALL BOOKS (acc. Betweenness Centrality)")
print(top_five_betweenness_centrality[0:5])

#Let's document this into a CSV file (in Case we want a visualization in Tableau)
with open('got_top_characters_betweenness_centraility.csv', 'w', newline="") as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in top_five_betweenness_centrality:
       writer.writerow([key, value])
       
       
       
       
       
       
       
#------------------------------------------------------------
#Finding the most important character using GOOGLE PAGE RANK
#------------------------------------------------------------
       
       
# Calculating the page rank of book 1-5
page_rank_book1 = nx.pagerank(books[0])
page_rank_book2 = nx.pagerank(books[1])
page_rank_book3 = nx.pagerank(books[2])
page_rank_book4 = nx.pagerank(books[3])
page_rank_book5 = nx.pagerank(books[4])
# Sorting the dictionaries according to their pagerank and storing the top 10
sorted_page_rank_book1 = sorted(page_rank_book1.items(), key=lambda x:x[1], reverse = True)[0:10]
sorted_page_rank_book2 = sorted(page_rank_book2.items(), key=lambda x:x[1], reverse = True)[0:10]
sorted_page_rank_book3 = sorted(page_rank_book3.items(), key=lambda x:x[1], reverse = True)[0:10]
sorted_page_rank_book4 = sorted(page_rank_book4.items(), key=lambda x:x[1], reverse = True)[0:10]
sorted_page_rank_book5 = sorted(page_rank_book5.items(), key=lambda x:x[1], reverse = True)[0:10]
# Printing out the top 10 of book 1-5
print("\n")
print("TOP 5 characters in Book 1 (acc. Page Rank)")
print(sorted_page_rank_book1[0:5])
print("\n")
print("TOP 5 characters in Book 2 (acc. Page Rank)")
print(sorted_page_rank_book2[0:5])
print("\n")
print("TOP 5 characters in Book 3 (acc. Page Rank)")
print(sorted_page_rank_book3[0:5])
print("\n")
print("TOP 5 characters in Book 4 (acc. Page Rank)")
print(sorted_page_rank_book4[0:5])
print("\n")
print("TOP 5 characters in Book 5 (acc. Page Rank)")
print(sorted_page_rank_book5[0:5])
print("\n")

#iterate thought the results (dictionaries) to make one aggregate list of all books
top_characters_all_books3 = {}
listoflists3 = [sorted_page_rank_book1,sorted_page_rank_book2,sorted_page_rank_book3,sorted_page_rank_book4,sorted_page_rank_book5]

for book in listoflists3 :
    for character,value in book :
        if character in top_characters_all_books3 :
            top_characters_all_books3[character] += value
        else :
            top_characters_all_books3[character] = value
            
top_five_page_rank = sorted(top_characters_all_books3.items(), key=lambda x:x[1], reverse = True)[0:10]
print("\n")
print("TOP 5 characters in ALL BOOKS (acc. Page Rank)")
print(top_five_page_rank[0:5])

#Let's document this into a CSV file (in Case we want a visualization in Tableau)
with open('got_top_characters_page_rank.csv', 'w', newline="") as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in top_five_page_rank:
       writer.writerow([key, value])


            
    