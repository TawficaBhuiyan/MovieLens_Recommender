from surprise import accuracy
from surprise.model_selection import train_test_split
from surprise import Dataset, Reader, SVD
import pandas as pd
import numpy as np

# Load data
ratings = pd.read_csv("data/ratings.csv")
reader = Reader(rating_scale=(0.5, 5.0))
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

# Train model
model = SVD()
model.fit(trainset)
predictions = model.test(testset)

# Basic RMSE/MAE
print("RMSE:", accuracy.rmse(predictions))
print("MAE:", accuracy.mae(predictions))

# Precision@K, Recall@K, NDCG
def precision_recall_ndcg_at_k(predictions, k=10, threshold=3.5):
    user_est_true = {}
    for uid, _, true_r, est, _ in predictions:
        user_est_true.setdefault(uid, []).append((est, true_r))

    precisions, recalls, ndcgs = [], [], []
    for uid, ratings in user_est_true.items():
        ratings.sort(key=lambda x: x[0], reverse=True)
        top_k = ratings[:k]

        n_rel = sum((true_r >= threshold) for (_, true_r) in ratings)
        n_rec_k = sum((est >= threshold) for (est, _) in top_k)
        n_rel_and_rec_k = sum(((true_r >= threshold) and (est >= threshold)) for (est, true_r) in top_k)

        precisions.append(n_rel_and_rec_k / n_rec_k if n_rec_k != 0 else 0)
        recalls.append(n_rel_and_rec_k / n_rel if n_rel != 0 else 0)

        dcg = sum([(2**true_r - 1) / np.log2(idx+2) for idx, (est, true_r) in enumerate(top_k)])
        idcg = sum([(2**true_r - 1) / np.log2(idx+2) for idx, (est, true_r) in enumerate(sorted(ratings, key=lambda x: x[1], reverse=True)[:k])])
        ndcgs.append(dcg / idcg if idcg > 0 else 0)

    return np.mean(precisions), np.mean(recalls), np.mean(ndcgs)

p, r, n = precision_recall_ndcg_at_k(predictions, k=10)
print(f"Precision@10: {p:.4f}")
print(f"Recall@10: {r:.4f}")
print(f"NDCG@10: {n:.4f}")
