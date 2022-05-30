from flask_admin.contrib.sqla import ModelView

from .offer import OfferInlineAdmin
from .models import Offer


class ProviderView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    column_list = ('name', 'email', 'phone_number')

    inline_models = (OfferInlineAdmin(Offer),)
