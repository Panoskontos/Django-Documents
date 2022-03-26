from django.contrib.auth import authenticate, login

# object create


# Author Regisration
# Author Regisration
def author_registration(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()

            # Get data to craete author in DB
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            age = form.cleaned_data.get('age')
            user = User.objects.get(username=username)
            author = Author(user=user, email=email, age=age)
            author.save()

            # Authenticate User
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')

    else:
        form = AuthorForm()

    # print(username)
    context = {
        'form': form,
    }
    return render(request, 'library/author_registration.html', context)
