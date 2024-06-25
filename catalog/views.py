from django.shortcuts import render


def homepage(request):
    return render(request, "index.html")


def contacts(request):
    if request.method == "POST":
        user_name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        user_message = request.POST.get("message")
        filename = f"{user_name}_information.txt"
        message = f"пользователь {user_name} (почта: {email}, телефон: {phone}) оставил сообщение '{user_message}'"
        file = open(filename, "w")
        file.write(message)
        file.close()
    return render(request, "contacts.html")
