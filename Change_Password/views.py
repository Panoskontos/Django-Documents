from django.contrib.auth.forms import PasswordChangeForm


@ login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()

            user = authenticate(request, username=request.user.username,
                                password=form.cleaned_data.get('new_password2'))

            login(request, user)
            message = 'You have successfully changed your password'
            return HttpResponseRedirect('/library/success/'+message+'/')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'library/change_password.html', {'form': form})