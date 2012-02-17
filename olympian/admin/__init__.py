from flask import Blueprint

admin = Blueprint('admin', __name__)

@admin.route('/clients')
def index():
    return 'List and create clients'
