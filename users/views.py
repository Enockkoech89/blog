from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from.forms import SignUpForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, f'Your account has been created. Log in Here')
            # login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
    
@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES ,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        

    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'profile.html', context)



# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm

# def register(request):

# 	if request.method == "POST":
# 		form = UserCreationForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username= form.cleaned_data.get('username')
# 			messages.success(request, f'account created for {username}')
# 			return redirect('blog-home')
# 	else:
# 		form = UserCreationForm()

# 	return render(request, "register.html", {'form': form})

