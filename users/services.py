import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(obj):
    """Создание продукта в stripe."""
    product_name = obj.course if obj.course else obj.lesson
    stripe_product = stripe.Product.create(name=product_name)
    return stripe_product


def create_stripe_price(product, amount):
    """Создание цены в stripe."""
    return stripe.Price.create(currency="rub", unit_amount=amount * 100, product=product.get("id"))


def create_stripe_session(price):
    """Создание сессии в stripe."""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
