from django.shortcuts import render


def divide(request):
    x = request.GET.get('x')
    y = request.GET.get('y')

    if x is None or y is None:
        return render(request, 'calculator/divide.html')

    x = int(x)
    y = int(y)

    return render(request, 'calculator/divide.html', {'result': x / y, 'x': x, 'y': y})
