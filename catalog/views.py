from django.shortcuts import render


def homepage(request):
    return render(request, "index.html")


def contacts(request):
    if request.method == "POST":
        user_name = request.POST.get("name")
        phone = request.POST.get("phone")
        user_message = request.POST.get("message")
        filename = f"сообщение_от_{user_name}.txt"
        message = f"Пользователь: {user_name} (телефон: {phone}) оставил сообщение '{user_message}'"
        file = open(filename, "w", encoding="utf-8")
        file.write(message)
        file.close()
    return render(request, "contacts.html")
