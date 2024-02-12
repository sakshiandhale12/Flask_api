# app.py
import os
from flask import Flask
from flask_restful import Api
from models import db
from resources import EcodeCatgLnkResource, EppsBusinessZoneMstResource,EmployeeMstResource,EmployeeMstResource3,EmployeeMstResource2
# from schemas import VDivIdSchema
from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI') + "?options=-c%20search_path%3Depps_admin"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)
swagger = Swagger(app)

@app.route('/apidocs/')
def apidocs():
    return redirect('/apidocs/index.html')
# Add routes
api.add_resource(EcodeCatgLnkResource, '/ecode/catg/lnk/v1')
api.add_resource(EppsBusinessZoneMstResource, '/bussiness/zone/tree/v1')
api.add_resource(EmployeeMstResource, '/employeeget/v1')
api.add_resource(EmployeeMstResource2, '/employeecreate/v1')
api.add_resource(EmployeeMstResource3, '/employeeupdate/v1')

if __name__ == '__main__':
    app.run(debug=True)


