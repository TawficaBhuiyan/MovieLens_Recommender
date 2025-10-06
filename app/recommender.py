
# app/recommender.py
import pandas as pd
import joblib

# Load ratings
ratings = pd.read_csv("data/ratings.csv")

# Load movies metadata
movies_df = pd.read_csv("data/movies.csv")
movies_dict = pd.Series(movies_df.title.values, index=movies_df.movieId).to_dict()

# Load trained model
model = joblib.load("app/model.pkl")

def recommend_movies(user_id, N=5):
    """Return Top-N movie titles for a given user_id"""
    all_movies = ratings['movieId'].unique()
    user_rated = ratings[ratings['userId'] == user_id]['movieId'].values

    movies_to_predict = [m for m in all_movies if m not in user_rated]

    predictions = []
    for movie in movies_to_predict[:1000]:  # limit for speed
        pred = model.predict(user_id, movie)
        predictions.append((movie, pred.est))

    top_movies = sorted(predictions, key=lambda x: x[1], reverse=True)[:N]

    # Convert movieIds to titles
    top_titles = [movies_dict.get(mid, f"Movie {mid}") for mid, _ in top_movies]

    return top_titles

if __name__ == "__main__":
    user_id = 1
    top_n = 5
    recs = recommend_movies(user_id, top_n)
    print(f"Top {top_n} recommendations for user {user_id}:")
    for idx, title in enumerate(recs, 1):
        print(f"{idx}. {title}")
