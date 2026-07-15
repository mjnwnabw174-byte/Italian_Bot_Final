import requests
from config import WEB_APP_URL

def add_user_to_sheet(user, link):
    params = {'action': 'addAccount', 'link': link, 'user': user}
    requests.get(WEB_APP_URL, params=params)

def get_next_user():
    return "سيتم تفعيل رابط التبادل قريباً!"
