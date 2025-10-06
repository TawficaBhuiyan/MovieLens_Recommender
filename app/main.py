# # # app/main.py
# import pandas as pd
# from fastapi import FastAPI
# from app.recommender import recommend_movies

# app = FastAPI()

# # Load movie titles
# movies_df = pd.read_csv("data/movies.csv")  # make sure movies.csv is in your data folder
# movies_dict = pd.Series(movies_df.title.values, index=movies_df.movieId).to_dict()
# app/main.py
from fastapi import FastAPI
from app.recommender import recommend_movies

app = FastAPI()

@app.get("/")
def root():
    return {"message": "MovieLens Recommender API is running!"}

@app.get("/recommend/{user_id}")
def get_recommendations(user_id: int, top_n: int = 5):
    recs = recommend_movies(user_id, top_n)
    return {"user_id": user_id, "recommendations": recs}
