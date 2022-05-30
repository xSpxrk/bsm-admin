from flask_admin.contrib.sqla import ModelView
from typing import Any, cast

from flask_admin.model import InlineFormAdmin

from .offer import OfferInlineAdmin
from .models import Order, Offer
from markupsafe import Markup


def customer_name_formatter(view: 'OfferView', context: Any, model: Order, name: str) -> Markup:
    return cast(Markup, model.customer.name)


def customer_email_formatter(view: 'OfferView', context: Any, model: Order, name: str) -> Markup:
    return cast(Markup, model.customer.email)


class OrderView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    column_list = ('name', 'description', 'materials', 'quantity', 'customer', 'email')

    column_formatters = {'customer': customer_name_formatter, 'email': customer_email_formatter}

    inline_models = (OfferInlineAdmin(Offer), )


class OrderInlineAdmin(InlineFormAdmin):
    form_columns = ('name', 'description', 'materials', 'quantity', 'order_id')
