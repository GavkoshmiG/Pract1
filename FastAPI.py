from fastapi import FastAPI
from typing import Union

app = FastAPI() #создание экземпляра приложения

mentors = [
    {
        "id": 1,
        "name": "Beber Abeber",
        "tags": ["JS", "FaastAPI", "Pytn"]
    },
    {
        "id": 2,
        "name": "Galkov",
        "tags": ["JS", "FaastAPI", "Pytn"]
    },
    {
        "id": 3,
        "name": "Aboba",
        "tags": ["JS", "FaastAPI", "Pytn"]
    }
]

@app.get("/mentors") #показывает какой путь должен быть прописан в строке, чтобы выполнить функцию (указывает маршрут )
def get_mentors():      # возвращает массив со всеми менторами
    return mentors 

@app.get("/PathMentors/{mentor_id}") #берем переменную из URL 
def get_mentors(mentor_id: int):      #передаем пер-ю из URL в ф-ю
    for mentor in mentors:      #пробегаем по всему массиву с менторами и ищем ментора с нужным нам id
        if(mentor["id"] == mentor_id):
            return mentor 


