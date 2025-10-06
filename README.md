# 🎬 **MovieLens Recommender System**

A **Movie Recommendation System** built with **Python**, leveraging **collaborative filtering** via `scikit-surprise` and `scikit-learn`.  
It predicts user preferences and suggests personalized movies interactively through **Gradio** and **FastAPI**.

---

## 🖼️ **Project Preview**

![UI Screenshot](Screenshot%202025-10-04%20062237.png)
![API Screenshot](Screenshot%202025-10-04%20064027.png)
![Results Screenshot](Screenshot%202025-10-04%20064054.png)

---

## ⚙️ **Installation & Setup**

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/TawficaBhuiyan/MovieLens_Recommender.git
cd MovieLens_Recommender

2️⃣ Create and Activate Virtual Environment
py -3.12 -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt

🧱 Project Structure
MovieLens_Recommender/
│
├── data/                 # dataset files
├── app/
│   ├── train_model.py    # trains and saves model
│   ├── recommender.py    # generates recommendations
│   ├── evaluation.py     # evaluates model performance
│   ├── main.py           # FastAPI backend
│   └── ui.py             # Gradio interface
├── requirements.txt
└── README.md

🚀 Usage
| **Action**              | **Command**                     |
| ----------------------- | ------------------------------- |
| 🧠 Train the model      | `python -m app.train_model`     |
| 📊 Evaluate performance | `python -m app.evaluation`      |
| 🌐 Run API backend      | `uvicorn app.main:app --reload` |
| 💻 Launch Gradio UI     | `python -m app.ui`              |


FastAPI:
http://127.0.0.1:8000
 → API home
http://127.0.0.1:8000/recommend/1?top_n=5
 → Example recommendations

Gradio:
http://127.0.0.1:7860
 → Interactive interface

 🧩 Main Dependencies
 | Library         | Purpose                    |
| --------------- | -------------------------- |
| pandas          | Data manipulation          |
| numpy           | Numerical operations       |
| scikit-learn    | Machine learning utilities |
| scikit-surprise | Collaborative filtering    |
| gradio          | Interactive web UI         |
| FastAPI         | RESTful API service        |
| joblib          | Model saving/loading       |
| matplotlib      | Visualization              |
| tqdm            | Progress bars              |

📊 Example Evaluation Results
RMSE: 0.8807
MAE:  0.6780
Precision@10: 0.7449
Recall@10: 0.5095
NDCG@10: 0.7935

👤 Author

| **Name**                  | **Details**                                         |
| ------------------------- | --------------------------------------------------- |
| 👨‍💻 **Tawfica Bhuiyan** | ProblemSolver & MLEnthuthiast                 |
| 🌐 GitHub                 | [TawficaBhuiyan](https://github.com/TawficaBhuiyan) |

```
