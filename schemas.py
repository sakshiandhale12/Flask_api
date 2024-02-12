
from marshmallow import Schema, fields

class VDivIdSchema(Schema):
    div_cd = fields.String(required=True)
    emp_cd = fields.String(required=True)
    emp_first_name = fields.String(required=True)
    emp_last_name = fields.String(required=True)
