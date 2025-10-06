import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import joblib

# Load ratings
ratings = pd.read_csv("data/ratings.csv")

# Load movies
movies = pd.read_csv("data/movies.csv")


# Reader for Surprise
reader = Reader(rating_scale=(0.5, 5.0))
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

# Train-test split
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

# Train SVD model
model = SVD(n_factors=20)  # smaller model, less memory
model.fit(trainset)

# Save model
joblib.dump(model, "app/model.pkl")
print(" Model trained and saved at app/model.pkl")
