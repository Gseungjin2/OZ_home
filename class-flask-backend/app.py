# {
#  "cells": [
#   {
#    "cell_type": "code",
#    "execution_count": 1,
#    "metadata": {},
#    "outputs": [
#     {
#      "name": "stderr",
#      "output_type": "stream",
#      "text": [
#       "UsageError: Line magic function `%poetry` not found.\n"
#      ]
#     }
#    ],
#    "source": []
#   }
#  ],
#  "metadata": {
#   "kernelspec": {
#    "display_name": "Python 3",
#    "language": "python",
#    "name": "python3"
#   },
#   "language_info": {
#    "codemirror_mode": {
#     "name": "ipython",
#     "version": 3
#    },
#    "file_extension": ".py",
#    "mimetype": "text/x-python",
#    "name": "python",
#    "nbconvert_exporter": "python",
#    "pygments_lexer": "ipython3",
#    "version": "3.12.4"
#   }
#  },
#  "nbformat": 4,
#  "nbformat_minor": 2
# }


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {"username": "traveler", "name": "Alex"},
        {"username": "photographer", "name": "Sam"},
        {"username": "gourmet", "name": "Chris"}
    ]
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
