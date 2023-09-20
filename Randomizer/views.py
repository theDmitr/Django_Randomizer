from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseBadRequest
from random import randint


def main(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


def myRandom(request: HttpRequest) -> HttpResponse:
    start: str = request.GET.get('start', '')
    end: str = request.GET.get('end', '')

    if not start.isdigit() or not end.isdigit():
        return HttpResponseBadRequest('Incorrect arguments!')

    random_digit: int = randint(int(start), int(end))
    data = {'random_digit': random_digit}
    return JsonResponse(data)
