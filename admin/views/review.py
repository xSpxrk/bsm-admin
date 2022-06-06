from flask_admin.contrib.sqla import ModelView
from .models import Review
from markupsafe import Markup
from typing import Any, cast


def provider_name_formatter(view: 'ReviewView', context: Any, model: Review, name: str):
    return cast(Markup, model.provider.name)


def customer_name_formatter(view: 'ReviewView', context: Any, model: Review, name: str):
    return cast(Markup, model.customer.name)


def owner_name_formatter(view: 'ReviewView', context: Any, model: Review, name: str):
    if model.owner == 0:
        return cast(Markup, 'Заказчик')
    else:
        return cast(Markup, 'Поставщик')


class ReviewView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True
    column_list = ('description', 'rating', 'provider', 'customer', 'owner', )

    column_formatters = {'owner': owner_name_formatter, 'provider': provider_name_formatter,
                         'customer': customer_name_formatter}
