import requests  #испортируем библиотеку
from config import API_KEY #импортируем наш эти кей для ссылки 

def search_places(city, query): #делаем функцию с аргуентами 
    url = "https://places.googleapis.com/v1/places:searchText" #задаем переменную url

    headers  = { # делаем словарь с параметрами запроса
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.nationalPhoneNumber,places.rating,places.websiteUri"
    }

    body = {
        "textQuery": f"{query}{city}",
        "languageCode": "uk"
    }

    response = requests.post(url, headers=headers, json=body)  
    #вызываем функцию post из библиотеки requests с 
    #переменными которые мы задали выше
    #она отправляет HTTP запрос к API и возвращает ответ, который мы сохраняем в переменную response.

    data = response.json()   #задаем переменную  data и в нее передаем то что получится в response 

    return data #на выходе получаем json код 