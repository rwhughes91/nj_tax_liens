from django import template
from new_jersey.models import Lien

register = template.Library()


@register.filter("currency")
def currency(dollar_value):
    """Will take in a decimal/int datatype and return a string resembling currency"""
    dollar_value = "${0}".format(dollar_value)
    return dollar_value


@register.filter("percentage")
def percentage(decimal):
    """Will convert a number to a percentage"""
    percent = format(decimal, '%')
    decimal_index = percent.find('.')
    before_decimal = percent[:decimal_index]
    percent_sign = percent[-1]
    after_decimal = percent[decimal_index:]
    return before_decimal + after_decimal[:3] + percent_sign
