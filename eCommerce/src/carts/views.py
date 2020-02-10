from django.shortcuts import render

from .models import Cart


def cart_creator(user=None):
    cart_obj = Cart.objects.create(user=user)
    print("New looser created")
    return cart_obj


def cart_home(request):
    # print(request.session)                # session
    # print(dir(request.session))           # prints vars
    # request.session.set_expiry(300)     # 5 minutes
    # key = request.session.session_key
    # print(key)
    # print(request.session.get("first_name", "Unknown ( instead of None )"))       # GETTER
    cart_id = request.session.get("cart_id", None)
    # request.session['cart_id'] = "10"
    print(cart_id)
    """
    if cart_id is None:
        print("EYYYY ITS NONE")
        cart_obj = cart_creator()
        request.session['cart_id'] = cart_obj.id     # SETTER
    else:
    """
    qs = Cart.objects.filter(id=cart_id)
    if qs.count() == 1:
        cart_obj = qs.first()
    else:
        cart_obj = cart_creator()
        request.session['cart_id'] = cart_obj.id
    # print(cart_id)
    # cart_obj = Cart.objects.get(id=cart_id)
    # request.session['user'] = request.user.username     # CAN STORY ONLY STRING / INT ETC. NOT AN OBJECT
    return render(request, "carts/home.html", {})
