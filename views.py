import requests
import json
import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post, Comentario
from django.http import JsonResponse, HttpResponse

def index(request):
    context1 = {
        "name": "6G atinge taxa de transmissão 5.000 vezes maior que 5G",
        "data": {
            "texto": "A University College de Londres (UCL) conseguiu atingir uma taxa de transmissão de dados de 938 Gb/s com a rede 6G. Esse valor é 5.000 vezes maior que a taxa atingida pelo 5G...",
            "pub_date": "11/11/2024",
            "img": "https://network-king.net/wp-content/uploads/2024/07/6G-769x450.jpg",
            "comentarios": [
                {
                    "comment": "Para o consumidor final no BR (quando chegar): velocidade vai ser próxima a do 4G. Isso quando funcionar."
                },
                {
                    "comment": "Top!"
                }
            ]
        },
    }
    
    context2 = {
        "name": "Snapdragon 8 Elite é o novo chip da Qualcomm para celulares avançados",
        "data": {
            "texto": "Snapdragon 8 Elite é o nome do novo chip da Qualcomm para celulares de alto desempenho. A novidade chega com a missão de suceder o Snapdragon 8 Gen 3.",
            "pub_date": "12/11/2024",
            "img": "https://files.tecnoblog.net/wp-content/uploads/2024/10/snapdragon-8-elite-celular-768x432.jpg",
            "comentarios": [
                {
                    "comment": "Para o consumidor final no BR (quando chegar): velocidade vai ser próxima a do 4G. Isso quando funcionar."
                },
                {
                    "comment": "Top!"
                }
            ]
        },
    }
    
    response1 = requests.post("https://api.restful-api.dev/objects", json=context1)
    response2 = requests.post("https://api.restful-api.dev/objects", json=context2)
    post_data = [response1.json(), response2.json()]

    return render(request, 'index.html', {'posts_template': post_data})

def detalhe(request, id_post):
    context1 = {
        "name": "6G atinge taxa de transmissão 5.000 vezes maior que 5G",
        "data": {
            "texto": "A University College de Londres (UCL) conseguiu atingir uma taxa de transmissão de dados de 938 Gb/s com a rede 6G. Esse valor é 5.000 vezes maior que a taxa atingida pelo 5G",
            "pub_date": "11/11/2024",
            "img": "https://www.acidadeon.com/tudoep/wp-content/uploads/sites/10/2024/05/WhatsApp-Image-2024-05-29-at-18.07.29_2024-05-30_16-38-52_jpeg_2024-05-30_16-38-53-1280x700.webp",
            "comentarios": [
                {
                    "comment": "Para o consumidor final no BR (quando chegar): velocidade vai ser próxima a do 4G. Isso quando funcionar."},
                {
                    "comment": "Top!"
                }
            ]
        },
    }
    
    response1 = requests.post("https://api.restful-api.dev/objects", json=context1)
    post_data = [response1.json()]
    
    with open("responses.txt", "w") as file:
        file.write(json.dumps(post_data, indent=4))
        

    return render(request, 'detalhe.html', {'post_template': post_data})

def editar_comentario(request):
    # Estrutura para atualização dos comentários
    
    context1 = {
        "name": "6G atinge taxa de transmissão 5.000 vezes maior que 5G",
        "data": {
            "texto": "A University College de Londres (UCL) conseguiu atingir uma taxa de transmissão de dados de 938 Gb/s com a rede 6G. Esse valor é 5.000 vezes maior que a taxa atingida pelo 5G",
            "pub_date": "11/11/2024",
            "img": "https://www.acidadeon.com/tudoep/wp-content/uploads/sites/10/2024/05/WhatsApp-Image-2024-05-29-at-18.07.29_2024-05-30_16-38-52_jpeg_2024-05-30_16-38-53-1280x700.webp",
            "comentarios": [
                {
                    "comment": "Comentário Atualizado: Para o consumidor final no BR (quando chegar): velocidade vai ser próxima a do 4G. Isso quando funcionar."
                },
                {
                    "comment": "Comentário Atualizado: Top!"
                },
                {
                    "comment": "Testando PUT!"
                }
            ]
        },
    }
    
    respose = requests.put("https://api.restful-api.dev/objects/ff808181932badb601932d7b79da05ee", json=context1)
    comments = respose.json()
    
    return JsonResponse(comments, safe=False)
