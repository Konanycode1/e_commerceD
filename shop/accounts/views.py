from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login

User = get_user_model()
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.create(username=username, password=password)

        login(request,user)
        return redirect('shop:index')
    return render(request, 'accounts/signup.html')
