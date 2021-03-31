from tours.models import Tour, Rate, Variable


def get_prices_for_tour(tour: Tour):
    variables = Variable.objects.filter(tour=tour)

    children = Rate.objects.none()
    rate = Rate.objects.none()
    group = Rate.objects.none()

    for variable in variables:
        if variable.type == "c":
            children = Rate.objects.filter(variable=variable)

        if variable.type == "r":
            rate = Rate.objects.filter(variable=variable)

        if variable.type == "g":
            group = Rate.objects.filter(variable=variable)

    if not children.exists():
        children = None

    if not rate.exists():
        rate = None

    if not group.exists():
        group = None

    result = {
        "children": children,
        "rate": rate,
        "group": group
    }

    print(result)

    return result
