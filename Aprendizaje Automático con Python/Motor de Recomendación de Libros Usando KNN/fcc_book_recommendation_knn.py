# import libraries (you may add additional imports but you may not have to)
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt

# get data files
books_filename = 'BX-Books.csv'
ratings_filename = 'BX-Book-Ratings.csv'

# import csv data into dataframes
df_books = pd.read_csv(
    books_filename,
    encoding = "ISO-8859-1",
    sep=";",
    header=0,
    names=['isbn', 'title', 'author'],
    usecols=['isbn', 'title', 'author'],
    dtype={'isbn': 'str', 'title': 'str', 'author': 'str'})

df_ratings = pd.read_csv(
    ratings_filename,
    encoding = "ISO-8859-1",
    sep=";",
    header=0,
    names=['user', 'isbn', 'rating'],
    usecols=['user', 'isbn', 'rating'],
    dtype={'user': 'int32', 'isbn': 'str', 'rating': 'float32'})

# START CODE -->

# get counts of each user and isbn
ratingsCountByUser = df_ratings['user'].value_counts()
ratingsCountByIsbn = df_ratings['isbn'].value_counts()

# remove ratings with less than 200 users and less than 100 isbn
df_ratings = df_ratings.loc[
    (~df_ratings['user'].isin(ratingsCountByUser[ratingsCountByUser < 200].index)) &
    (~df_ratings['isbn'].isin(ratingsCountByIsbn[ratingsCountByIsbn < 100].index))]

# merge ratings with books and remove duplicates to pivot
df_merged = pd.merge(right=df_ratings, left=df_books, on='isbn')
df_merged = df_merged.drop_duplicates(['title', 'user'])

df_pivot = pd.pivot_table(df_merged, values="rating", index="title", columns="user", fill_value =0)

# transform values to matrix
df_csrMatrix = csr_matrix(df_pivot.values)

# create model and get titles
neighbors = NearestNeighbors(metric='cosine', algorithm='brute', p=2).fit(df_csrMatrix)
titles = df_pivot.index.values

# function to return recommended books - this will be tested
def get_recommends(book = ""):
  if book == "":
    return 'Empty book'

  neigh_dist, neigh_ind = neighbors.kneighbors(df_pivot.loc[book].values.reshape(1, -1), len(titles), True)
  neigh_distFlatten = neigh_dist.flatten()
  neigh_indFlatten = neigh_ind.flatten()

  recommendedBooks = []
  for i in range(5, 0, -1):
    recommendedBooks.append([df_pivot.index[neigh_indFlatten[i]], neigh_distFlatten[i]])

  return [book, recommendedBooks]

# <-- END CODE

books = get_recommends("Where the Heart Is (Oprah's Book Club (Paperback))")
print(books)

def test_book_recommendation():
  test_pass = True
  recommends = get_recommends("Where the Heart Is (Oprah's Book Club (Paperback))")
  if recommends[0] != "Where the Heart Is (Oprah's Book Club (Paperback))":
    test_pass = False
  recommended_books = ["I'll Be Seeing You", 'The Weight of Water', 'The Surgeon', 'I Know This Much Is True']
  recommended_books_dist = [0.8, 0.77, 0.77, 0.77]
  for i in range(2): 
    if recommends[1][i][0] not in recommended_books:
      test_pass = False
    if abs(recommends[1][i][1] - recommended_books_dist[i]) >= 0.05:
      test_pass = False
  if test_pass:
    print("You passed the challenge! 🎉🎉🎉🎉🎉")
  else:
    print("You haven't passed yet. Keep trying!")

test_book_recommendation()