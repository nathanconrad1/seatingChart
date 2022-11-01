from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('heyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')

def seatingChartView(request) :
    return HttpResponse('beautiful seating chart')
