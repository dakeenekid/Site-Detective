from flask import Flask
from flask_ask import Ask, statement, question, session
import urllib
import json
import requests

app = Flask(__name__)
ask = Ask(app, "/")

@ask.launch
def start_skill():
    message = "Hello there, what web page do you need checking today?"
    return question(message)


@ask.intent("WhatIsMyStatusIntent")
def what_is_my_status(site):

    if " " in site:
        msg = "Sorry, web pages cannot have a space. I heard you say {}. Please repeat the site name and try again.".format(site)
        return statement(msg)


    page = urllib.urlopen("http://www."+site.lower()+".com").getcode()


    if page == 200:
        msg = "The page {} is up!".format(site)
        return statement(msg).simple_card("Okay, {}".format(site), msg)


    elif page == 404:
        print page
        msg = "The page {} is down!".format(site)
        return statement(msg)

    elif page == 403:
        msg = "The page {} is forbidden, or returned code 403. Please try a different website.".format(site)
        return statement(msg)

    elif page == 503:
        print page
        msg = "The page {} is down!".format(site)
        return statement(msg).simple_card("Okay, {}".format(site), msg)


    elif page == 429:
        print page
        msg = "The page {} is not avaliable, but could be up!".format(site)
        return statement(msg).simple_card("Okay, {}".format(site), msg)

    else:
        print page
        msg = "The page {} is down!".format(site)
        return statement(msg).simple_card("Okay, {}".format(site), msg)

if __name__ == '__main__':
    app.run(debug=True)

