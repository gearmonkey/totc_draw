'''A Really simple web app to serve as an emulator of the random process for 
Zach Weinersmith's Trial of the Clones
'''

import os
from random import sample
from flask import Flask


app = Flask(__name__)

page_frame = """
<head>

</head>
<body style="width:600px;margin:auto;margin-top:1.5em">
    {body}
    <div class='footer' style="font-size:small;margin-top:1em"><a href="/">home</a> | <a href="/draw/1">Draw one?</a> | <a href="/draw/3">Draw three?</a> | <a href="/draw/big">Biggest draw is best draw?</a>
</body>"""

@app.route('/draw/big')
def biggest():
    return page_frame.format(body=3)

@app.route('/draw/<int:num_draws>')
def draw(num_draws):
    possible_outcomes = [3]*53 + [2]*67 + [1]*71 + [0]*56
    all_draws=''
    for _ in xrange(num_draws):
        all_draws += '{0}<br/>'.format(sample(possible_outcomes,1)[0])
    all_draws += '<a href="">Same draw again?</a><br/>'
    return page_frame.format(body=all_draws)

@app.route('/')
def hello():
    return page_frame.format(body='''Hello! This is a random draw emulator for <a href="http://www.kickstarter.com/projects/999790007/trial-of-the-clone-a-choosable-path-gamebook-by-za">The Trial of the Clone</a> a choosable path gamebook by <a href="http://www.theweinerworks.com/">Zach Weinersmith</a>. While the book is great, the eBook verion lacks a good way to do the random draw, so <a href="http://benfields.net">I</a> made this. It's written in <a href='http://pyhton.org'>Python</a> using <a href='http://flask.pocoo.org/'>Flask</a>, and you can fork it on <a href='https://github.com/gearmonkey/totc_draw'>github</a>, if you're into that sort of thing. <br/><br/>Pick a draw type to proceed:''' )

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

