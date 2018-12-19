from flask import Blueprint

from .company_list_views import get_companies, index
from .database_update_views import main_update


api = Blueprint('companylist', __name__)

api.add_url_rule('/', view_func=index)
api.add_url_rule('/companies', view_func=get_companies)
api.add_url_rule('/db_update', view_func=main_update)
