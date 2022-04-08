from .models import Wishlist

# Logic


def home(request):
    # .....

    wishlist = Wishlist.objects.all()
    # create empty dictionary
    mydict = dict()
    # O(n)complexity
    # create empty sets
    for i in wishlist:
        mydict[i.user.username] = set()
    # add to arrays
    for i in wishlist:
        mydict[i.user.username].add(i.book.title)
    print(mydict)
    context = {
        'mydict': mydict,
    }

    # return render . . . .
