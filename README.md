# Movie-Recommender-System using NLP

This project builds a content-based movie recommender system using Python libraries like pandas, NumPy, Matplotlib, Seaborn, BeautifulSoup, string, nltk, sklearn, and pickle.

## Data Preprocessing

- Merged two datasets (movies and credits) based on the "title" column.
- Dropped unnecessary columns.
- Cleaned and preprocessed text data in various columns like genres, keywords, cast, and overview.
- Removed HTML tags, punctuations, numbers, and applied lemmatization.

## Vectorization and Similarity Calculation

- Used CountVectorizer to convert textual data into numerical vectors.
- Calculated cosine similarity between each pair of movie vectors.

## Recommendation Generation

- Defined a function to recommend movies based on a given input movie title.
- The function retrieves the input movie index, calculates similarity scores with other movies, and returns the top 5 most similar movies.

## Additional Features

- Created a list of all available movie titles in the dataset.
- Saved the processed data frame as a pickle file for future use.

## Usage

1. Run the provided Python code to generate the "all_movies_list.html" file containing a list of available movies.
2. Enter the name of a movie you like from the list.
3. The system will recommend the top 5 most similar movies based on your input.

## Conclusion

This content-based movie recommender system offers personalized recommendations based on the textual similarities between movies. It utilizes various data preprocessing techniques and calculates cosine similarity to provide relevant suggestions.
