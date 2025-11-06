from django.shortcuts import render, redirect
from .forms import UserForm

# Create your views here.
def register_page(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/success.html', {'message': 'Message sent successfully!'})
        
    else:
        form = UserForm()
    return render(request, 'users/register_page.html', {'form': form})