'''A Really simple web app to serve as an emulator of the random process for 
Zach Weinersmith's Trial of the Clones
'''

import os
from random import sample
from flask import Flask


app = Flask(__name__)

page_frame = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
   "http://www.w3.org/TR/html4/loose.dtd">
<html lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="author" content="Benjamin Fields">
<meta name="robots" content="index,follow" />
<link rel="copyright" href="http://www.gnu.org/copyleft/fdl.html" />
<title>{title}</title>
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-35572122-1']);
  _gaq.push(['_trackPageview']);

  (function() {{
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  }})();

</script>
</head>
<body style="width:600px;margin:auto;margin-top:1.5em">
    {body}
    <div class='footer' style="font-size:small;margin-top:1em"><a href="/">home</a> | <a href="/draw/1">Draw one?</a> | <a href="/draw/3">Draw three?</a> | <a href="/draw/big">Biggest draw is best draw?</a>
</body>'''

@app.route('/draw/big')
def biggest():
    return page_frame.format(title='TotC Draw|Biggest Draw is Best Draw', body='3<br/><a href="">Same draw again?</a><br/>')

@app.route('/draw/<int:num_draws>')
def draw(num_draws):
    possible_outcomes = [3]*53 + [2]*67 + [1]*71 + [0]*56
    all_draws=''
    for _ in xrange(num_draws):
        all_draws += '{0}<br/>'.format(sample(possible_outcomes,1)[0])
    all_draws += '<a href="">Same draw again?</a><br/>'
    return page_frame.format(title='TotC Draw|Draw {0}'.format(num_draws),body=all_draws)

@app.route('/')
def hello():
    return page_frame.format(title='TotC Draw|Home', body='''Hello! This is a random draw emulator for <a href="http://www.kickstarter.com/projects/999790007/trial-of-the-clone-a-choosable-path-gamebook-by-za">The Trial of the Clone</a> a choosable path gamebook by <a href="http://www.theweinerworks.com/">Zach Weinersmith</a>. While the book is great, the eBook verion lacks a good way to do the random draw, so <a href="http://benfields.net">I</a> made this. It's written in <a href='http://python.org'>Python</a> using <a href='http://flask.pocoo.org/'>Flask</a>, and you can fork it on <a href='https://github.com/gearmonkey/totc_draw'>github</a>, if you're into that sort of thing. <br/><br/>Pick a draw type to proceed:''' )

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

