# # #app/ui.py

# import gradio as gr
# from app.recommender import recommend_movies

# def recommend_ui(user_id, top_n):
#     recs = recommend_movies(int(user_id), int(top_n))
#     return "\n".join(recs)  # Display nicely as list

# demo = gr.Interface(
#     fn=recommend_ui,
#     inputs=[gr.Number(label="User ID"), gr.Number(label="Top N")],
#     outputs="text",
#     title="🎬 MovieLens Recommender",
#     description="Enter a User ID to get personalized recommendations."
# )

# if __name__ == "__main__":
#     demo.launch()
# app/ui.py
import gradio as gr
from app.recommender import recommend_movies

def recommend_ui(user_id, top_n):
    recs = recommend_movies(int(user_id), int(top_n))
    return "\n".join(recs)

demo = gr.Interface(
    fn=recommend_ui,
    inputs=[gr.Number(label="User ID"), gr.Number(label="Top N")],
    outputs="text",
    title="🎬 MovieLens Recommender",
    description="Enter a User ID to get personalized recommendations."
)

if __name__ == "__main__":
    demo.launch()
