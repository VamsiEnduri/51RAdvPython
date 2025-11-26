from django.urls import path
from .views import home,about,contact,todos
# urlpatterns=[
#     path("",home),
#     path("about/",about),
#     path("contact/",contact)
# ]


urlpatterns=[
    path("",home),
    path("about/",about),
    path("contact/",contact),
    path("todos/",todos),
]