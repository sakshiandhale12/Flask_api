from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flasgger import Swagger
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os
from sqlalchemy import ForeignKey, UniqueConstraint
from datetime import datetime
from werkzeug.exceptions import HTTPException
from flask_restful import fields, marshal_with
from flask import Flask
from flask_restful import Api, Resource, reqparse
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

employee_response_fields = {
    'message': fields.String,
}

load_dotenv()
engine = create_engine(os.getenv('DATABASE_URI') + "?options=-c%20search_path%3Depps_admin")
Base = declarative_base()
Session = sessionmaker(bind=engine)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI') + "?options=-c%20search_path%3Depps_admin"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Base = declarative_base()
# Swagger configuration
swagger = Swagger(app)
ma = Marshmallow(app)
Base.metadata.create_all(engine)

class EppsEcodeCatgLnk(db.Model):
    __tablename__ = 'epps_ecode_catg_lnk'
    __table_args__ = {'schema': 'epps_admin'}

    comp_cd = db.Column(db.Integer, primary_key=True)
    div_cd = db.Column(db.SmallInteger)
    ecode = db.Column(db.String(10))
    item_category = db.Column(db.String(50))
    created_by = db.Column(db.String(10), nullable=True)
    updated_by = db.Column(db.String(10), nullable=True)
    terminal_id = db.Column(db.String(100), nullable=True)
    active_yn = db.Column(db.String(1), nullable=True)
    creator_role_cd = db.Column(db.SmallInteger, nullable=True)
    updator_role_cd = db.Column(db.SmallInteger, nullable=True)


class EppsBusinessZoneMst(db.Model):
    __tablename__ = 'epps_business_zone_mst'
    __table_args__ = {'schema': 'epps_admin'}

    comp_cd = db.Column(db.Integer, primary_key=True)
    div_cd = db.Column(db.SmallInteger, primary_key=True)
    bus_zone_cd = db.Column(db.String(25), primary_key=True)
    bus_zone_disp_name = db.Column(db.String(50))
    bus_zone_long_name = db.Column(db.String(100), nullable=True)
    parent_bus_zone_cd = db.Column(db.String(25), nullable=True)
    bus_level_flag = db.Column(db.String(1))
    address_details = db.Column(db.String(255), nullable=True)
    city_cd = db.Column(db.SmallInteger, nullable=True)
    state_cd = db.Column(db.SmallInteger, nullable=True)
    country_cd = db.Column(db.SmallInteger, nullable=True)
    created_dt = db.Column(db.DateTime)
    created_by = db.Column(db.String(10))
    updated_dt = db.Column(db.DateTime, nullable=True)
    updated_by = db.Column(db.String(10), nullable=True)
    active_yn = db.Column(db.String(1), nullable=True)
    terminal_id = db.Column(db.String(100), nullable=True)
    creator_role_cd = db.Column(db.SmallInteger, nullable=True)
    updator_role_cd = db.Column(db.SmallInteger, nullable=True)

    def __repr__(self):
        return f"<EppsBusinessZoneMst(comp_cd={self.comp_cd}, div_cd={self.div_cd}, bus_zone_cd={self.bus_zone_cd})>"

class EppsEmpLocLnk(db.Model):
    __tablename__ = 'epps_emp_loc_lnk'
    __table_args__ = {'schema': 'epps_admin'}    
    comp_cd = db.Column(db.Integer, ForeignKey('epps_role_mst.id'), primary_key=True)
    div_cd = db.Column(db.SmallInteger, primary_key=True)
    loc_cd = db.Column(db.SmallInteger, primary_key=True)
    role_cd = db.Column(db.SmallInteger, primary_key=True)
    emp_cd = db.Column(db.String(50), primary_key=True)
    sal_loc_flag = db.Column(db.String(1), nullable=True)
    created_by = db.Column(db.String(10))
    created_dt = db.Column(db.DateTime)
    updated_by = db.Column(db.String(10), nullable=True)
    updated_dt = db.Column(db.DateTime, nullable=True)
    terminal_id = db.Column(db.String(100), nullable=True)
    active_yn = db.Column(db.String(1), nullable=True)
    creator_role_cd = db.Column(db.SmallInteger, nullable=True)
    updator_role_cd = db.Column(db.SmallInteger, nullable=True)
    rep2_emp_cd = db.Column(db.String(10), nullable=True)
    auto_created_entry = db.Column(db.SmallInteger, nullable=True)

    __table_args__ = (UniqueConstraint('comp_cd', 'div_cd', 'loc_cd', 'role_cd', 'emp_cd', name='_comp_div_loc_role_emp_uc'),)
class EppsRoleMst(db.Model):
    __tablename__ = 'epps_role_mst'
    __table_args__ = {'schema': 'epps_admin'}
    comp_cd = db.Column(db.Integer, db.ForeignKey('epps_division_mst.comp_cd'), primary_key=True)
    div_cd = db.Column(db.SmallInteger, primary_key=True)
    role_cd = db.Column(db.SmallInteger, primary_key=True)
    role_disp_name = db.Column(db.String(50), nullable=True)
    role_long_name = db.Column(db.String(50), nullable=True)
    role_parent_role = db.Column(db.SmallInteger, nullable=True)
    role_type = db.Column(db.String(50), nullable=True)
    role_disp_seq_no = db.Column(db.SmallInteger, nullable=True)
    sys_admin_flag = db.Column(db.String(1), nullable=True)
    role_id = db.Column(db.String(50), nullable=True)
    per_item_limit = db.Column(db.Numeric(21, 2), nullable=True)
    per_transaction_limit = db.Column(db.Numeric(21, 2), nullable=True)
    created_by = db.Column(db.String(10), nullable=False)
    created_dt = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.String(10), nullable=True)
    updated_dt = db.Column(db.DateTime, nullable=True)
    terminal_id = db.Column(db.String(100), nullable=True)
    active_yn = db.Column(db.String(1), nullable=True)
    creator_role_cd = db.Column(db.SmallInteger, nullable=True)
    updator_role_cd = db.Column(db.SmallInteger, nullable=True)
    role_exp_app_flag = db.Column(db.String(1), nullable=False)
    ref_role_id = db.Column(db.String(10), nullable=True)
    hr_admin_flag = db.Column(db.SmallInteger, nullable=True)
    default_yn = db.Column(db.SmallInteger, nullable=True)

    def __repr__(self):
        return f"<EppsRoleMst(comp_cd={self.comp_cd}, div_cd={self.div_cd}, role_cd={self.role_cd})>"


class EppsEmpLocLnkSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = EppsEmpLocLnk
        load_instance = True
app.db = db

epps_emp_loc_lnk_schema = EppsEmpLocLnkSchema()
epps_emp_loc_lnks_schema = EppsEmpLocLnkSchema(many=True)
class EcodeCatgLnkResource(Resource):
    def get(self):
        """Endpoint to get ecode_catg_lnk data.

        ---
        tags:
          - ecode_catg_lnk
        parameters:
          - name: page
            in: query
            type: integer
            description: Page number
          - name: per_page
            in: query
            type: integer
            description: Items per page (limited to 100)
          - name: companyCode
            in: query
            type: integer
            description: Company Code
          - name: divisionCode
            in: query
            type: integer
            description: Division Code
          - name: ecode
            in: query
            type: string
            description: E-Code
          - name: isActive
            in: query
            type: integer
            description: Active (1/0)
        responses:
          200:
            description: Successful response
            content:
              application/json:
                schema:
                #   $ref: '#/components/schemas/api.EppsEcodeCatgLnk'
        """
        page = int(request.args.get('page', 1))
        per_page = min(int(request.args.get('per_page', 100)), 100)  # Limit per_page to 100

        company_code = request.args.get('companyCode')
        division_code = request.args.get('divisionCode')
        e_code = request.args.get('ecode')
        is_active = request.args.get('isActive')

        total_records = EppsEcodeCatgLnk.query.count()

        offset = (page - 1) * per_page

        query = EppsEcodeCatgLnk.query
        if company_code:
            query = query.filter_by(comp_cd=company_code)
        if division_code:
            query = query.filter_by(div_cd=division_code)
        if e_code:
            query = query.filter_by(ecode=e_code)
        if is_active is not None:
            query = query.filter_by(active_yn=is_active)

        ecode_catg_lnk_pagination = query.offset(offset).limit(per_page).all()

        # Convert the result to JSON
        result = []
        for link in ecode_catg_lnk_pagination:
            result.append({
                'company_code': link.comp_cd,
                'division_code': link.div_cd,
                'employee_code': link.ecode,
                'item_category': link.item_category,
                'created_by': link.created_by,
                'updated_by': link.updated_by,
                'terminal_id': link.terminal_id,
                'isactive': link.active_yn,
                'creator_role_cd': link.creator_role_cd,
                'updator_role_cd': link.updator_role_cd
            })

        return jsonify({
            'ecode_catg_lnk': result,
            'page': page,
            'per_page': per_page,
            'total_items': total_records
        })


api = Api(app)
api.add_resource(EcodeCatgLnkResource, '/ecode/catg/lnk/v1', endpoint='E-Code Category Link Data')

if __name__ == '__main__':
    app.run(debug=True)

class EppsBusinessZoneMstResource(Resource):
    def get(self):
        """Endpoint to bus_zone_cd data.

        ---
        tags:
          - ecode_catg_lnk
        parameters:
          - name: page
            in: query
            type: integer
            description: Page number
          - name: per_page
            in: query
            type: integer
            description: Items per page (limited to 100)
          - name: companyCode
            in: query
            type: integer
            description: Company Code
          - name: divisionCode
            in: query
            type: integer
            description: Division Code
        responses:
          200:
            description: Successful response
            content:
              application/json:
                schema:
                #   $ref: '#/components/schemas/api.EppsEcodeCatgLnk'
        """
        page = int(request.args.get('page', 1))
        per_page = min(int(request.args.get('per_page', 100)), 100)  # Limit per_page to 100

        company_code = request.args.get('companyCode')
        division_code = request.args.get('divisionCode')

        total_records = EppsBusinessZoneMst.query.count()

        offset = (page - 1) * per_page

        query = EppsBusinessZoneMst.query
        if company_code:
            query = query.filter_by(comp_cd=company_code)
        if division_code:
            query = query.filter_by(div_cd=division_code)

        business_zone_mst_pagination = query.offset(offset).limit(per_page).all()

        # Convert the result to JSON
        result = []
        for link in business_zone_mst_pagination:
            result.append({
                'company_code': link.comp_cd,
                'division_code': link.div_cd,
                'bus_zone_cd' : link.bus_zone_cd,
                'bus_zone_disp_name' : link.bus_zone_disp_name,
                'bus_zone_long_name' : link.bus_zone_long_name,
                'parent_bus_zone_cd': link.parent_bus_zone_cd,
                'bus_level_flag': link.bus_level_flag
            })

        return jsonify({
            'ecode_catg_lnk': result,
            'page': page,
            'per_page': per_page,
            'total_items': total_records
        })


api = Api(app)
api.add_resource(EppsBusinessZoneMstResource, '/bussiness/zone/tree/v1', endpoint='Business Zone Mst')

if __name__ == '__main__':
    app.run(debug=True)

class EppsBusinessZoneMstResourceget(Resource):
    def get(self):
        """Endpoint to bus_zone_cd data.

        ---
        tags:
          - ecode_catg_lnk
        parameters:
          - name: page
            in: query
            type: integer
            description: Page number
          - name: per_page
            in: query
            type: integer
            description: Items per page (limited to 100)
          - name: companyCode
            in: query
            type: integer
            description: Company Code
          - name: divisionCode
            in: query
            type: integer
            description: Division Code
          - name: businessZoneCode
            in: query
            type: integer
            description: businessZoneCode
          - name: businessZoneType
            in: query
            type: integer
            description: businessZoneType
          - name: parentBusinessZoneCode
            in: query
            type: integer
            description : parentBusinessZoneCode
        responses:
          200:
            description: Successful response
            content:
              application/json:
                schema:
                #   $ref: '#/components/schemas/api.EppsEcodeCatgLnk'
        """
        page = int(request.args.get('page', 1))
        per_page = min(int(request.args.get('per_page', 100)), 100)  # Limit per_page to 100

        company_code = request.args.get('companyCode')
        division_code = request.args.get('divisionCode')
        bus_zone_cd = request.args.get('bus_zone_cd')
        bus_zone_disp_name = request.args.get('bus_zone_disp_name')
        parent_bus_zone_cd = request.args.get('parent_bus_zone_cd')

        total_records = EppsBusinessZoneMst.query.count()

        offset = (page - 1) * per_page

        query = EppsBusinessZoneMst.query
        if company_code:
            query = query.filter_by(comp_cd=company_code)
        if division_code:
            query = query.filter_by(div_cd=division_code)
        if bus_zone_cd:
            query = query.filter_by(div_cd=bus_zone_cd)
        if bus_zone_disp_name:
            query = query.filter_by(bus_zone_disp_name=bus_zone_disp_name)
        if parent_bus_zone_cd:
            query = query.filter_by(parent_bus_zone_cd=parent_bus_zone_cd)

        business_zone_mstget_pagination = query.offset(offset).limit(per_page).all()

        # Convert the result to JSON
        result = []
        for link in business_zone_mstget_pagination:
            result.append({
                'company_code': link.comp_cd,
                'division_code': link.div_cd,
                'bus_zone_cd' : link.bus_zone_cd,
                'bus_zone_disp_name' : link.bus_zone_disp_name,
                'bus_zone_long_name' : link.bus_zone_long_name,
                'parent_bus_zone_cd': link.parent_bus_zone_cd,
                'bus_level_flag': link.bus_level_flag
            })

        return jsonify({
            'ecode_catg_lnk': result,
            'page': page,
            'per_page': per_page,
            'total_items': total_records
        })


api = Api(app)
api.add_resource(EppsBusinessZoneMstResourceget, '/bussiness/zone/v1', endpoint='Business Zone Mst get')

if __name__ == '__main__':
    app.run(debug=True)

class EppsEmpLocLnkResource(Resource):
    def get(self):
        """Endpoint to get epps_emp_loc_lnk data.

        ---
        tags:
          - ecode_catg_lnk
        parameters:
          - name: page
            in: query
            type: integer
            description: Page number
          - name: per_page
            in: query
            type: integer
            description: Items per page (limited to 100)
          - name: companyCode
            in: query
            type: integer
            description: Company Code
          - name: divisionCode
            in: query
            type: integer
            description: Division Code
        responses:
          200:
            description: Successful response
            content:
              application/json:
                schema:
                  # $ref: '#/components/schemas/api.EppsEmpLocLnk'
        """
        page = int(request.args.get('page', 1))
        per_page = min(int(request.args.get('per_page', 100)), 100)  # Limit per_page to 100

        company_code = request.args.get('companyCode')
        division_code = request.args.get('divisionCode')
        # bus_zone_cd = request.args.get('bus_zone_cd')
        # bus_zone_disp_name = request.args.get('bus_zone_disp_name')
        # parent_bus_zone_cd = request.args.get('parent_bus_zone_cd')

        total_records = EppsEmpLocLnk.query.count()

        offset = (page - 1) * per_page

        query = EppsEmpLocLnk.query
        if company_code:
            query = query.filter_by(comp_cd=company_code)
        if division_code:
            query = query.filter_by(div_cd=division_code)
        # if bus_zone_cd:
        #     query = query.filter_by(div_cd=bus_zone_cd)
        # if bus_zone_disp_name:
        #     query = query.filter_by(bus_zone_disp_name=bus_zone_disp_name)
        # if parent_bus_zone_cd:
        #     query = query.filter_by(parent_bus_zone_cd=parent_bus_zone_cd)

        epps_emp_pagination = query.offset(offset).limit(per_page).all()

        # Convert the result to JSON
        result = []
        for link in epps_emp_pagination:
            result.append({
                'company_code': link.comp_cd,
                'division_code': link.div_cd,
                # 'bus_zone_cd' : link.bus_zone_cd,
                # 'bus_zone_disp_name' : link.bus_zone_disp_name,
                # 'bus_zone_long_name' : link.bus_zone_long_name,
                # 'parent_bus_zone_cd': link.parent_bus_zone_cd,
                # 'bus_level_flag': link.bus_level_flag
            })

        return jsonify({
            'ecode_catg_lnk': result,
            'page': page,
            'per_page': per_page,
            'total_items': total_records
        })
    
    from flask_restful import Resource, Api, reqparse, abort



    parser = reqparse.RequestParser()
    parser.add_argument('comp_cd', type=int, required=True, help='comp_cd is required')
    parser.add_argument('div_cd', type=int, required=True, help='div_cd is required')
    parser.add_argument('role_cd', type=int, required=True, help='role_cd is required')
    parser.add_argument('loc_cd', type=int, required=True, help='loc_cd is required')
    parser.add_argument('emp_cd', type=str, required=True, help='emp_cd is required')
    parser.add_argument('created_dt', type=str, required=True, help='created_dt is required')

    def post(self):
        args = EppsEmpLocLnkResource.parser.parse_args()
        session = Session()

        try:
            # Check if the referenced record exists in EppsRoleMst
            referenced_record = session.query(EppsRoleMst).get((
                args['comp_cd'],
                args['div_cd'],
                args['role_cd']
            ))
            if not referenced_record:
                session.close()
                return {"detail": "Referenced record in EppsRoleMst does not exist."}, 400
        except NoResultFound:
            session.close()
            return {"detail": "Referenced record in EppsRoleMst does not exist."}, 400

        # Check if the record with the same composite key already exists
        if session.query(EppsEmpLocLnk).filter_by(
            comp_cd=args['comp_cd'],
            div_cd=args['div_cd'],
            loc_cd=args['loc_cd'],
            role_cd=args['role_cd'],
            emp_cd=args['emp_cd'],
            created_dt=args['created_dt']
        ).first():
            session.close()
            return {"detail": "Record with the same composite key already exists."}, 400

        # Create the EppsEmpLocLnk instance
        new_entry = EppsEmpLocLnk(**args)
        session.add(new_entry)
        session.commit()
        session.close()

        return {"message": "Employee entry created successfully"}, 201

    def get(self):
        # Implement your GET logic here
        return {"message": "GET request is not supported for this endpoint"}, 405

api.add_resource(EppsEmpLocLnkResource, '/employee/v1/')

if __name__ == '__main__':
    app.run(debug=True)
