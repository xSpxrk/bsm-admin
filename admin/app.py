from typing import cast

import flask
from flask import Flask, render_template, request
from flask_admin import Admin, AdminIndexView

from .db.session import current_session
from .views.models import Provider, Order, Offer, Customer, Review, Material
from flask_admin.form import form


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.secret_key = 'secret_key'

    @app.route('/', methods=['GET', 'POST'])
    def login():
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':
            return flask.redirect('/admin')

        return render_template('index.html')

    admin = Admin(app, name='Биржа строительных материалов',
                  index_view=AdminIndexView(name='Главная страница', url='/admin'),
                  template_mode='bootstrap4')

    from .views.provider import ProviderView
    from .views.offer import OfferView
    from .views.order import OrderView
    from .views.customer import CustomerView
    from .views.review import ReviewView
    from .views.material import MaterialView

    admin.add_view(CustomerView(Customer, current_session, name="Заказчики"))
    admin.add_view(OrderView(Order, current_session, name='Заказы'))
    admin.add_view(OfferView(Offer, current_session, name="Предложения"))
    admin.add_view(ProviderView(Provider, current_session, name='Поставщики'))
    admin.add_view(ReviewView(Review, current_session, name='Отзывы'))
    admin.add_view(MaterialView(Material, current_session, name='Материалы'))

    return cast(Flask, admin.app)


app = create_app()


def create_app():
    return app
