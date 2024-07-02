from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f"/media/{path}"
    return "#"


@register.inclusion_tag("product_card.html")
def render_product_card(product, card):
    return {"product": product,
            "card": card
        }