from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
def signup(request):
 
    if request.user.is_authenticated:
        return redirect('djangobin:profile', username=request.user.username)
 
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('signup')
 
    else:
        f = UserCreationForm()
 
    return render(request, 'djangobin/signup.html', {'form': f})
