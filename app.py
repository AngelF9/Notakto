from flask import Flask, render_template, request, session, redirect, url_for
from notakto import draw_board, has_line, place_x

app = Flask(__name__)
app.secret_key = 'your secret key'

@app.route('/', methods=['GET', 'POST'])
def home(): # this home functin will replace our main.py file. Home function is designed to handle the individual HTTP requests that are coming in.

    if 'board' not in session: # if board is not in session then initialize a 3X3 board and set as empty {}
        session['board'] = [[''] * 3 for _ in range(3)]
    board = session['board'] # if board is in session then set board to session board

    message = ""
    winner = None
    turn = 0

    if request.method == 'POST': # if req is post then user has entered a location(submit button)
        # get the user input from the form
        user_input = int(request.form.get('location'))

        if place_x(board, user_input): # if place_x is true then will func will place x (true) 
            # we can then update the turn 
            turn += 1
            if has_line(board):
                winner = turn % 2 + 1            
        else:
            # will not print but instead pass along a message to html file
            message = "Location invalid or already taken. Please try again."
        
    session['board'] = board # set session board to board
    return render_template('index.html', board=session['board'], message=message, winner=winner)

@app.route('/reset')
def reset():
    session.pop('board', None)          # if board is in session then pop it out
    session.modified = True             # set session to modified
    return redirect(url_for('home'))    # redirect to home

if __name__ == '__main__':
    app.run(debug=True)