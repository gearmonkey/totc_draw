'''A Really simple web app to serve as an emulator of the random process for 
Zach Weinersmith's Trial of the Clones
'''

import os
from random import sample
from flask import Flask


app = Flask(__name__)

page_frame = """<head></head><body>{body}</body>"""

@app.route('/draw/<int:num_draws>')
def draw(num_draws):
    possible_outcomes = [3]*53 + [2]*67 + [1]*71 + [0]*56
    all_draws=''
    for _ in xrange(num_draws):
        all_draws += '{0}<br/>'.format(sample(possible_outcomes,1)[0])
    all_draws += '<a href="">Same draw again?</a>'
    return page_frame.format(body=all_draws)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

