from flask_admin.contrib.sqla import ModelView


class MaterialView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    column_list = ('name',)
