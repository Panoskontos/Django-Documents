from .filters import MessageFilter
# get min and max
from django.db.models import Avg, Max, Min




@login_required(login_url='login')
def test(request):
    messages = Message.objects.all()
    # grab min and max
    phonemin = messages.aggregate(Min('receiver_phone'))
    phonemax = messages.aggregate(Max('receiver_phone'))
    myFilter = MessageFilter(request.GET, queryset=messages)
    messages = myFilter.qs
    print(phonemin['receiver_phone__min'])
    print(phonemax['receiver_phone__max'])

    my_context= {
        'myFilter':myFilter,
        'messages':messages,
        'phonemin':phonemin['receiver_phone__min'],
        'phonemax':phonemax['receiver_phone__max'],
    }
    return render(request, 'sms/test.html', my_context)

