from django.contrib.auth import login
from django.shortcuts import render, redirect

from .froms import SignUpForm

# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')  # name='frontpage' for frontapge() view in urls so redirecting it there
    else:
        form = SignUpForm()
        
    return render(request, 'core/signup.html', {'form': form})