from flask_admin.contrib.sqla import ModelView
from typing import Any, cast

from flask_admin.model import InlineFormAdmin

from .models import Offer
from markupsafe import Markup


def provider_name_formatter(view: 'OfferView', context: Any, model: Offer, name: str) -> Markup:
    return cast(Markup, model.provider.name)


def provider_email_formatter(view: 'OfferView', context: Any, model: Offer, name: str) -> Markup:
    return cast(Markup, model.provider.email)


def order_formatter(view: 'OfferView', context: Any, model: Offer, name: str) -> Markup:
    return cast(Markup, model.order.name)


class OfferView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    column_list = ('order', 'quantity', 'price', 'provider', 'email')

    column_formatters = {'order': order_formatter, 'provider': provider_name_formatter,
                         'email': provider_email_formatter}


class OfferInlineAdmin(InlineFormAdmin):
    form_columns = ('quantity', 'price', 'offer_id')
