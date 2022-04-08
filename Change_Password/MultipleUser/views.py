def change_password(request):
    form = ChangePasswordForm()
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)

        # get user and passwords
        user = CustomUser.objects.get(username=request.user)
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        repeat_password = request.POST.get('repeat_password')

        if form.is_valid() and repeat_password == new_password and user.password == old_password:
            print('all valid')
            CustomUser.objects.filter(
                username=request.user).update(password=new_password)

            return redirect('login')
        else:
            return redirect('change_password')

    return render(request, 'myapp/create-book.html', {
        'form': form
    })
