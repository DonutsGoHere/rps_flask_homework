from flask import render_template

from app import app
from models.player import Player
from models.game import *

@app.route('/')
def index():
  return render_template('index.html')

# @app.route('/<player_1_choice>/<player_2_choice>')
# def result():
#    return render_template('game_result')


@app.route('/rock')
def rock():
   return render_template('rock.html')

@app.route('/paper')
def paper():
   return render_template('paper.html')

@app.route('/scissors')
def scissors():
   return render_template('scissors.html')

@app.route('/rock/rock')
def rock_rock():
   return render_template('draw.html')

@app.route('/rock/paper')
def rock_paper():
   return render_template('player_2_wins.html')

@app.route('/rock/scissors')
def rock_scissors():
   return render_template('player_1_wins.html')

@app.route('/paper/rock')
def paper_rock():
   return render_template('player_1_wins.html')

@app.route('/paper/paper')
def paper_paper():
   return render_template('draw.html')

@app.route('/paper/scissors')
def paper_scissors():
   return render_template('player_2_wins.html')

@app.route('/scissors/rock')
def scissors_rock():
   return render_template('player_2_wins.html')

@app.route('/scissors/paper')
def scissors_paper():
   return render_template('player_1_wins.html')

@app.route('/scissors/scissors')
def scissors_scissors():
   return render_template('draw.html')



