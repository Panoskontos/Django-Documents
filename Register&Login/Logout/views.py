from django.contrib.auth import logout


def signout(request):
    logout(request)
    # return redirect('/')
    context = {}
    return render(request, 'library/logout.html', context)
