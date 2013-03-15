import webapp2
import cgi
import urllib,json

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("""
              <html>
                 <head>
                  <link type="text/css" rel="stylesheet" href="/stylesheets/main.css" />
                 </head>   
                <title>Twetter App</title>
                
                <body>
                <center>
                  <h1> YOUR RECENT TWEETS !!! </h1>
                  <img src = /stylesheets/images/twitter03.png />   
                  <p><h2>Your Twitter Name:</h2></p>
                  <form action="/sign" method = "post"
                  <p><input type="text" name="name" value="Your twitter user name" /></p>
                  <p><input type="submit" /> <input type="reset" /></p>

                 </form>
                </center>
                </body>
              </html 
                    """)

class Tweets(webapp2.RequestHandler):
    def post(self):
        name = (cgi.escape(self.request.get('name')))
        self.response.headers['Content-Type'] = 'text/plain'
       	tweets = urllib.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?screen_name="+name)	
        tweets = tweets.read()
        tweets = json.loads(tweets)
        count = 0
        for tweet in tweets:
            if tweet["text"][0] != 'R' and count<10:
               self.response.out.write(tweet['text'])
               self.response.out.write("\n")
               count += 1
app = webapp2.WSGIApplication([('/', MainPage),('/sign', Tweets)], debug=True)
