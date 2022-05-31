from typing import cast

import flask
from flask import Flask, render_template, request
from flask_admin import Admin, AdminIndexView

from .db.session import current_session
from admin.views.models import Provider, Order, Offer, Customer
from flask_admin.form import form


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['FLASK_ADMIN_SWATCH'] = 'Cosmo'
    app.secret_key = 'secret_key'

    @app.route('/', methods=['GET', 'POST'])
    def login():
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':
            return flask.redirect('/admin')
        return '''
        <form action="" method="post">
        <p>
	    <label for="username">Username</label>
	    <input type="text" name="username">
	</p>
	<p>
	    <label for="password">Password</label>
	    <input type="password" name="password">
	</p>
	<p>
	    <input type="submit">
	</p>
    </form>'''

    admin = Admin(app, name='Биржа строительных материалов',
                  index_view=AdminIndexView(name='Главная страница', url='/admin'),
                  template_mode='bootstrap4')

    from admin.views.provider import ProviderView
    from admin.views.offer import OfferView
    from admin.views.order import OrderView
    from admin.views.customer import CustomerView

    admin.add_view(CustomerView(Customer, current_session, name="Заказчики"))
    admin.add_view(OrderView(Order, current_session, name='Заказы'))
    admin.add_view(OfferView(Offer, current_session, name="Предложения"))
    admin.add_view(ProviderView(Provider, current_session, name='Поставщики'))

    return cast(Flask, admin.app)


app = create_app()

app.run()
