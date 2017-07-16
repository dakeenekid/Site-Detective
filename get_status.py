from urllib.request import urlopen

def get_status():
    site = input("Which website do you want to check the status of?")
    print("You are finding the status of "+site+".")

    page = urlopen("http://www."+site+".com").getcode()

    if page == 200:
        print(page)
        return 'The page is up!'


    elif page == 404:
        print(page)
        return 'Page is down!'

    elif page == 503:
        print(page)
        return 'Page is down!'
    elif page == 429:
        print('Please stop spamming this server with requests')

    else:
        print(page)
        return 'Page is down!'


get_status()