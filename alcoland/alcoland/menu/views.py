from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib import messages
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .forms import *
from .serializers import *


def Menu(request):
    q1 = request.GET.get('q1') if request.GET.get('q1') != None else ''
    drinks = Alcogol.objects.filter(related_to_name__slug__contains=q1)
    alc_list_names = MenuList.objects.all()
    #alc_list = Alcogol.objects.all()

    paginator = Paginator(drinks, 15)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'alc_list_names': alc_list_names,
        # 'alc_list': alc_list,
        'drinks': drinks,
        'page_obj': page_obj,
        'q1': q1,
    }
    return render(request, 'menu/menu.html', context=context)


def AlcogolSolo(request, slug, pk):
    alcogol_item = get_object_or_404(Alcogol, related_to_name__slug=slug, pk=pk)
    alcogol = Alcogol.objects.get(related_to_name__slug=slug, pk=pk)
    vino = True if alcogol.related_to_name.name == 'Вино' else False
    pivo = True if alcogol.related_to_name.name == 'Пиво' else False
    cognak = True if alcogol.related_to_name.name == 'Коньяк' else False
    vodka = True if alcogol.related_to_name.name == 'Водка' else False
    tekila = True if alcogol.related_to_name.name == 'Текила' else False
    rom = True if alcogol.related_to_name.name == 'Ром' else False
    context = {
        'alcogol_item': alcogol_item,
        'alcogol': alcogol,
        'pivo': pivo,
        'vino': vino,
        'cognak': cognak,
        'vodka': vodka,
        'tekila': tekila,
        'rom': rom,
    }
    return render(request, 'menu/alcogol_solo.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['text'])
            sending = send_mail(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['text'], ['4918bolia@ogasa.org.ua'])
            if sending:
                messages.success(request, 'Комментарий отправлен')
                return redirect('contact')
            else:
                messages.error(request, 'Не удалось отправить')
        else:
            messages.error(request, 'Ошибка отправки')
    else:
        form = ContactForm()
    return render(request, 'menu/contact.html', {"form": form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'menu/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = UserLoginForm()
    return render(request, 'menu/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')




class AlcogolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Alcogol.objects.all()
    serializer_class = AlcogolSerializer

    @action(methods=['get'], detail=False)
    def names(self, request):
        alcogol_names = MenuList.objects.all()
        return Response({'alcogol_names': [item.name for item in alcogol_names]})

    @action(methods=['get'], detail=False)
    def types(self, request):
        alcogol_types = Type.objects.all()
        return Response({'alcogol_types': [item.name for item in alcogol_types]})

    @action(methods=['get'], detail=False)
    def characters(self, request):
        alcogol_characters = Characters.objects.all().values()
        return Response({'alcogol_characters': [value for value in alcogol_characters]})

    @action(methods=['get'], detail=False)
    def snacks(self, request):
        alcogol_snacks = Snacks.objects.all()
        return Response({'alcogol_snacks': [item for item in alcogol_snacks]})


