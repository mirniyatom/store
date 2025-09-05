from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

mainmenu_dict ={
    'katalog' : 'Bu yerda katolog boladi',
    'sale': 'Bu yerda aksiyalar boladi',
    'brend': 'Bu yerda brendlar boladi',
    'formen': 'Bu yerda erkaklar uchun tovarlar boladi boladi',
    'forwomen' : 'Bu yerda ayollar uchun tovarlar boladi boladi',
    'makeup': 'Bu yerda makeup uchun tovarlar boladi boladi',
    'skincare': 'Bu yerda yuz uchun tovarlar boladi boladi',
    'gifts': 'Bu yerda sovgalar boladi boladi boladi',
}

def get_main_menu(request, main_menu:str ):
    desc = mainmenu_dict.get(main_menu)
    if desc:
        return HttpResponse(desc)
    else:
        return HttpResponseNotFound(f'{main_menu} bunday bolim yoq')
