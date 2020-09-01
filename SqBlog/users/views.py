from django.shortcuts import render,redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    form=UserRegisterForm()
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account Successfully Created for {username}')
            return redirect('login')


        else:
            form = UserRegisterForm()

    return render(request,'users/register.html',{'form':form})


@login_required()
def profile(request):
    if request.method=="POST":
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,
                                 request.FILES,
                                 instance=request.user.profile)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your Personal Info has been successfully Updated !')
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your Profile Image has been successfully Updated !')


            return redirect('profile')
        # else:
        #     messages.error(request,f'Please Fill Carefully with Instructions ')


    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context={
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'users/profile.html',context)





def change_password(request):
    if request.method=='POST':
        form =PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'password changed')
            return redirect('profile')
        else:
            messages.error(request,'try again')
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'users/change.html',{'form':form})