from .models import Cart  # Update with your actual model

def cart_count(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        cart_count = cart_items.count()
    else:
        cart_count = 0

    return {'cart_count': cart_count}