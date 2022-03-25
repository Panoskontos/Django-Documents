from django.shortcuts import render, redirect


# Success and fail views


def success(request, message=None):
    return render(request, 'dishes/success.html', {'message': message})


def fail(request, message=None):
    return render(request, 'dishes/fail.html', {'message': message})

# use them with " return redirect('success', message='blah blah')
