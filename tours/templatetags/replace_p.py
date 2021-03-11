from django import template

register = template.Library()


@register.filter(is_safe=True)
def replace_two_parts(value, arg):
    first = ""
    second = ""
    array = value.split("\n")

    for i in range(len(array)):
        if i < arg:
            first += '<p>' + array[i] + '</p>'
        else:
            second += '<p>' + array[i] + '</p>'

    return {'first': first, 'second': second}
