from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .form import PurchaseForm
from .models import Product
from users.models import Profile
from order.models import Order
# Create your views here.

# Purchase form
def purchase_view(request, *args, **kwargs):
    obj = Product.objects.all()

    purchase_form = PurchaseForm()
    if request.method == "POST":
        purchase_form = PurchaseForm(request.POST)

        # get user object
        u = Profile.objects.get(id=request.user.id)

        # get all available stocks
        flower_stock = 'stock'
        field_value = []
        flower_id = []

        for flower in obj:
            qty = getattr(flower, flower_stock)
            # only append if the flower is not sold out
            if qty != 0:
                field_value.append(qty)

                # get flower id user selected
                flower_id.append(flower.id)
            else:
                continue

        # get list of quantity entered by user 
        user_input_list = request.POST.getlist('qty') 
                
        save_counter = 0
        order_bulk_list = []

        # if input are all valid and there is something to buy
        if purchase_form.is_valid():
            for i in user_input_list:

                # Save multiple order by looping over list of data collected from form
                product_fk = Product.objects.get(id=flower_id[save_counter])
                flower_qty = int(i)
                order_subtotal = product_fk.price * flower_qty
                # print("Subtotal:", order_subtotal)

                if order_subtotal != 0.00:
                    order_bulk_list.append(Order(user_id=u, product=product_fk, qty=flower_qty, subtotal=order_subtotal))
                else: 
                    pass
                
                # update flower stock
                product_fk.stock -= flower_qty
                product_fk.save()

                save_counter += 1

            Order.objects.bulk_create(order_bulk_list)
            return HttpResponseRedirect('.') # will redirect to receipt page
    else:
        purchase_form = PurchaseForm()
    
    flowers = {
        "flower"     : obj,
        "form"       : purchase_form
    }
    # return HttpResponse("<h1>Flowers</h1>")
    return render(request, "purchase.html", flowers)


# Details
def flower_details(request, my_id):
    obj = Product.objects.get(id = my_id)

    context = { 'flower': obj }

    return render(request, 'details.html', context)

    