from flask import Flask
from flask_ask import Ask, statement, question

import urllib

app = Flask(__name__)
ask = Ask(app, "/")

@ask.launch
def start_skill():
    message = "Hello there, welcome to site detective. Is there a webpage you need checking?"
    return question(message)

@ask.intent("LeaveIntent")
def leave_skill():
    message = "Oh, I see that I have wasted your time. You have asked me to leave. I'm sorry. Goodbye"
    return statement(message)


@ask.intent("HelpIntent")
def help_skill():
        msg = "Site Detective is an alexa skill used to confirm if a website or web service is currently unavailable. It uses python to get the status code response from a page, then identifies if the page is running or not. Would you like to search for a site now?"
        return question(msg)


@ask.intent("YesIntent")
def yes_skill():
    msg = "What is the name of the website? Please include the dot com or the dot net suffix at the end, okay?"
    return question(msg)


@ask.intent("NoIntent")
def no_skill():
    msg = "Oh, okay. I thought you needed a webpage checked. If you need help, please say, alexa, ask site detective to help me."
    return statement(msg)


@ask.intent("WhatIsMyStatusIntent")
def what_is_my_status(site):
    try:

        if " " in site:
            site = site.replace(" ", "")

        if "dot" in site:
            site = site.replace("dot", ".")

        if not site:
            msg = "I'm sorry, I must not have heard you correctly. Can you repeat that?"
            return question(msg)

        add = urllib.urlopen("http://www." + site.lower())
        if "xbox" in add:
            add = "http://www.xbox.com/en-US/"
        elif "playstation" in add:
            add = "https://www.playstation.com/en-us/"
        page = add.getcode()

        if page == 200:
            msg = "The page {} is up! Would you like to ask again?".format(site)
            return question(msg).simple_card("Looking at, {}".format(site), msg)

        elif page == 404:
            msg = "The page {} is down, or does not exist! Would you like to ask again?".format(site)
            return question(msg)

        elif page == 403:
            msg = "The page {} is forbidden, and returned code 403. Would you like to ask again?".format(site)
            return question(msg)

        elif page == 503:
            msg = "The page {} is down! Would you like to ask again?".format(site)
            return question(msg).simple_card("Looking at, {}".format(site), msg)


        elif page == 429:
            msg = "The page {} is not avaliable, but could be up! Returned code 429 from server. Would you like to ask again?".format(site)
            return question(msg).simple_card("Looking at, {}".format(site), msg)

        else:
            msg = "The page {} is down! Would you like to ask again?".format(site)
            return question(msg).simple_card("Looking at, {}".format(site), msg)
    except:
        msg = "Sorry, I must have misunderstood you. Can you repeat that?"
        return question(msg)

if __name__ == '__main__':
    app.run(debug=True)
