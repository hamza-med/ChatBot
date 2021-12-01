#import libraries
from flask import Flask, render_template, request
import pred


my_story = "John left the kitchen . Sandra dropped the football in the garden ."
my_question = "Is the football in the garden ?"


# k, accuracy = predict("the football is in the bathroom .",
#                       "Is the football in the kitchen ?")
# print(k)
# print(accuracy)
# App
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == "POST":
        story = request.form["story"]
        question = request.form["question"]
        k, accuracy = pred.predict(story, question)
        answer = k
    return render_template("predict.html", my_answer=answer)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
