from django import template

register = template.Library()


@register.filter
def next(value, arg):
    try:
        t = value[int(arg) + 1]
        print(t)
        print(t.name)

        return value[int(arg) + 1]
    finally:
        return None
