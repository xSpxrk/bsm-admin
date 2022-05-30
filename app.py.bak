from typing import cast
from flask import Flask
from flask_admin import Admin, AdminIndexView

from db.session import current_session
from views.models import Provider, Order, Offer, Customer


def create_app() -> Flask:
    app = Flask(__name__)

    app.config['FLASK_ADMIN_SWATCH'] = 'Cosmo'
    app.secret_key = 'secret_key'

    admin = Admin(app, name='Биржа строительных материалов',
                  index_view=AdminIndexView(name='Главная страница', url='/'),
                  template_mode='bootstrap4')

    from views.provider import ProviderView
    from views.offer import OfferView
    from views.order import OrderView
    from views.customer import CustomerView

    admin.add_view(CustomerView(Customer, current_session, name="Заказчики"))
    admin.add_view(OrderView(Order, current_session, name='Заказы'))
    admin.add_view(OfferView(Offer, current_session, name="Предложения"))
    admin.add_view(ProviderView(Provider, current_session, name='Поставщики'))

    return cast(Flask, admin.app)


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
