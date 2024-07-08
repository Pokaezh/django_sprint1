from django.shortcuts import render


def about(request):
    """Функция для отображения страницы о проекте"""
    return render(request, "pages/about.html")


def rules(request):
    """Функция для отображения страницы с правилами проекта"""
    return render(request, "pages/rules.html")
