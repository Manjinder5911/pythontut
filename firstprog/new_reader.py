import requests
import json
url = ('https://newsapi.org/v2/everything?'
       'language=en&'
       'sources=bbc-news&'
       'sortBy=relevancy&'
       'pageSize=10&'
       'apiKey=d739d1cd0e5d4b50876a8e5a4a2ef536')
response = requests.get(url)

a = response.json()
b = a['articles']
c = 1

def speak(str):
       from win32com.client import Dispatch
       speak = Dispatch("SAPI.SpVoice")
       speak.speak(str)

if __name__ == '__main__':
       for i in b:
              print(f"News No. {c} ,{i['title']}")
              speak(f"News No. {c} ,{i['title']}")
              c += 1
