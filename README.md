# Movie-Recommended-System
Content Based Recommender System recommends movies similar to the movie user likes and analyses the sentiments on the reviews given by the user for that movie.
I used IMDB 5000 Movie Dataset to built this. Link to dataset :
  https://www.kaggle.com/datasets/rakkesharv/imdb-5000-movies-multiple-genres-dataset

# Similarity Score:

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

# How Cosine Similarity works?

Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.
![cosine](https://github.com/user-attachments/assets/ffc8936a-4279-4227-b8ae-0bc2c3ff31d5)
