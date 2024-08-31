from flask import Blueprint
from controllers.login import login,login_required
from controllers.home import home
from controllers.property import properties

app_bp = Blueprint('app_bp', __name__)

app_bp.route('/login', methods= ['POST','GET'])(login)
app_bp.route('/', methods= ['GET'])(home)
app_bp.route('/property', methods =['GET','POST'])(properties)