from flask_restful import Resource
from flask import jsonify, request
from models import EppsEcodeCatgLnk, EppsBusinessZoneMst
from flask import request
from flask_restful import Resource, reqparse
from models import EppsEmpLocLnk
from flask_restful import Resource, reqparse
from models import EppsEmpLocLnk, db
from models import EppsEmpLocLnk
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
class EcodeCatgLnkResource(Resource):
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

        total_records = EppsEcodeCatgLnk.query.count()

        offset = (page - 1) * per_page

        query = EppsEcodeCatgLnk.query
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
    
class EmployeeMstResource(Resource):
    def get(self):
        """Endpoint to Employee data.

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

        total_records = EppsEmpLocLnk.query.count()

        offset = (page - 1) * per_page

        query = EppsEmpLocLnk.query
        if company_code:
            query = query.filter_by(comp_cd=company_code)
        if division_code:
            query = query.filter_by(div_cd=division_code)

        Epps_Emp_Loc_Lnk_pagination = query.offset(offset).limit(per_page).all()

        # Convert the result to JSON
        result = []
        for link in Epps_Emp_Loc_Lnk_pagination:
            result.append({
                'company_code': link.comp_cd,
                'division_code': link.div_cd,
                'loc_cd' : link.loc_cd,
                'role_cd' :link.role_cd,
                'emp_cd': link.emp_cd,
                'sal_loc_flag':link.sal_loc_flag,
                'created_by':link.created_by,
                'created_dt':link.created_dt,
                'updated_by':link.updated_by,
                'updated_dt' : link.updated_dt,
                'terminal_id': link.terminal_id,
                'active_yn': link.active_yn
            })

        return jsonify({
            'ecode_catg_lnk': result,
            'page': page,
            'per_page': per_page,
            'total_items': total_records
        })
    


class EmployeeMstResource2(Resource):
    def post(self):
        """
        Endpoint to create a new employee.

        ---
        tags:
          - employee
        requestBody:
          required: true
          content:
            application/json:
              schema:
                type: object
                properties:
                  comp_cd:
                    type: integer
                  div_cd:
                    type: integer
                  loc_cd:
                    type: integer
                  role_cd:
                    type: integer
                  emp_cd:
                    type: string
                  active_yn:
                    type: string
                required:
                  - emp_cd
        responses:
          201:
            description: Employee created successfully
          400:
            description: Bad request
        """
        parser = reqparse.RequestParser()
        parser.add_argument('comp_cd', type=int, required=True)
        parser.add_argument('div_cd', type=int, required=True)
        parser.add_argument('loc_cd', type=int, required=True)
        parser.add_argument('role_cd', type=int, required=True)
        parser.add_argument('emp_cd', type=str, required=True)
        parser.add_argument('created_by', type=str, required=True)
        parser.add_argument('active_yn', type=str)

        args = parser.parse_args()

        from datetime import datetime

        created_dt = datetime.now()

        # Create a new employee instance
        new_employee = EppsEmpLocLnk(
            comp_cd=args['comp_cd'],
            div_cd=args['div_cd'],
            loc_cd=args['loc_cd'],
            role_cd=args['role_cd'],
            emp_cd=args['emp_cd'],
            active_yn=args['active_yn'],
            created_by=args['created_by'],
            created_dt=created_dt
        )

        # Add the new employee to the session and commit to the database
        db.session.add(new_employee)
        db.session.commit()

        return {'message': 'Employee created successfully'}, 201
    
from flask_restful import Resource, reqparse
from models import EppsEmpLocLnk, db
from datetime import datetime

class EmployeeMstResource3(Resource):
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('emp_cd', type=str, required=True)
        parser.add_argument('active_yn', type=str)
        parser.add_argument('comp_cd', type=int)
        parser.add_argument('div_cd', type=int)
        parser.add_argument('loc_cd', type=int)
        parser.add_argument('role_cd', type=int)
        parser.add_argument('created_by', type=str)
        parser.add_argument('created_dt', type=str)

        args = parser.parse_args()

        # Find the employee by emp_cd
        employee = db.session.query(EppsEmpLocLnk).filter_by(emp_cd=args['emp_cd']).first()

        if not employee:
            return {'message': 'Employee not found'}, 404

        # Check if the new combination of values already exists
        conflict_employee = db.session.query(EppsEmpLocLnk).filter_by(
            comp_cd=args.get('comp_cd', employee.comp_cd),
            div_cd=args.get('div_cd', employee.div_cd),
            loc_cd=args.get('loc_cd', employee.loc_cd),
            role_cd=args.get('role_cd', employee.role_cd),
            emp_cd=args.get('emp_cd')
        ).first()

        if conflict_employee:
            return {'message': 'Update failed. Conflict with existing record.'}, 400

        # Update employee attributes based on request data
        if 'active_yn' in args:
            employee.active_yn = args['active_yn']
        if 'comp_cd' in args:
            employee.comp_cd = args['comp_cd']
        if 'div_cd' in args:
            employee.div_cd = args['div_cd']
        if 'loc_cd' in args:
            employee.loc_cd = args['loc_cd']
        if 'role_cd' in args:
            employee.role_cd = args['role_cd']
        if 'created_by' in args:
            employee.created_by = args['created_by']
        if 'created_dt' in args:
            # Convert string to datetime
            try:
                created_dt = datetime.strptime(args['created_dt'], '%Y-%m-%dT%H:%M:%S')
                employee.created_dt = created_dt
            except ValueError:
                return {'message': 'Invalid format for created_dt. It should be in the format YYYY-MM-DDTHH:MM:SS'}, 400

        try:
            # Commit the changes to the database
            db.session.commit()
            return {'message': 'Employee updated successfully'}, 200
        except Exception as e:
            # Rollback changes if an exception occurs
            db.session.rollback()
            return {'message': 'Error updating employee: ' + str(e)}, 400
