def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        print("ENTRE XD")
        for key, value in request.session["carro"].items():
            total = total + (float(value["precio"]) * float(value["cantidad"]))

    return {"importe_total_carro": total}
