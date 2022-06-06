from flask_admin.contrib.sqla import ModelView


def owner_formatter(owner):
    if owner == 0:
        return 'Заказчик'
    else:
        return 'Поставщик'


class ReviewView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True
    column_list = ('description', 'customer_id', 'owner', 'provider', 'customer')

    column_formatters = {'owner': owner_formatter}


