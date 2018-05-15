from app import application


# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>Traffic message generator</title> </head>\n<body>'''
instructions = '''<img src="/static/traffic.jpg"/>
    <p><em>Hint</em>: This is a RESTful web service! Call the service by appending <code>
    /traffic</code> to the url.
    This will generate a single message.</p><p>Add the request parameter
    <code>count=</code> to specify the number of messages to generate.</p>\n
    <p>Add the request parameter <code>randomlocation=true</code> to specify to generate a random location.</p>\n
    <p>Add the request parameter <code>roadnumber=</code> to specify to the road number to choose from 
    (eg. &amp;roadnumber=A12).</p>\n
    <p>Add the request parameter <code>starttime=</code> to specify the timestamp to start at (format: 
    YYYY-MM-DDTHH:MM:SSZ).</p>\n
    <p>Example: .../traffic?count=100 to generate 100 messages.</p>\n
    <p>Example: .../traffic?count=100&amp;randomlocation=true to generate 100 messages with a random location.</p>
    <p>Example: .../traffic?count=10&amp;stepsize=5000 to generate 100 messages with 5 seconds between each generated message timestamp.</p>\n
    '''
footer_text = '</body>\n</html>'

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text + instructions + footer_text))


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host='', port=8080)
