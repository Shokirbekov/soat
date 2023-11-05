from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.http import require_POST

from .models import *


class WatchView(View):
    def get(self, request):
        data = {
            "watch": Watch.objects.all(),
            "brand": Brand.objects.all()
        }
        return render(request, 'all_watches.html', data)


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/watches/')
        return redirect('/login/')


class OneWatchView(View):
    def get(self, request, id):
        data = {
            'watch': Watch.objects.get(id=id)
        }

        return render(request, 'one_watch.html', data)


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'page-user-login.html')

    def post(self, request):
        a = authenticate(
            username=request.POST.get('u'),
            password=request.POST.get('p')
        )

        if a:
            login(request, a)
            return redirect('/')
        else:
            return redirect('/login/')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')


class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')

    def post(self, request):
        user = User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('p')
        )

        Profile.objects.create(
            user=user,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            gender=request.POST.get('gender')
        )
        return redirect('/login/')


class BuyListView(View):
    def get(self, request):
        buylist_items = BuyList.objects.filter(profil__user=request.user)
        total_price = sum(item.watch.price for item in buylist_items)

        data = {
            "buylist": buylist_items,
            "total_price": total_price
        }
        return render(request, "buylist.html", data)


class AddBuyList(View):
    def get(self, request, id):
        BuyList.objects.create(
            watch=Watch.objects.get(id=id),
            profil=Profile.objects.get(user=request.user)
        )
        return redirect('/buylist/')

class DeleteBuyList(View):
    def get(self, request, id):
        buylist = BuyList.objects.get(id=id)

        if buylist.profil.user == request.user:
            buylist.delete()
            return redirect('/buylist/')
        else:
            return redirect('/buylist/')