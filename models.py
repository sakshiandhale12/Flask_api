# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EppsEcodeCatgLnk(db.Model):
    __tablename__ = 'epps_ecode_catg_lnk'
    __table_args__ = {'schema': 'epps_admin'}

    comp_cd = db.Column(db.Integer, primary_key=True)
    div_cd = db.Column(db.SmallInteger, primary_key=True)
    ecode = db.Column(db.String(10), primary_key=True)
    item_category = db.Column(db.String(50), primary_key=True)
    created_dt = db.Column(db.DateTime)
    created_by = db.Column(db.String(10), nullable=True)
    updated_dt = db.Column(db.DateTime, nullable=True)
    updated_by = db.Column(db.String(10), nullable=True)
    terminal_id = db.Column(db.String(100), nullable=True)
    active_yn = db.Column(db.String(1), nullable=True)
    creator_role_cd = db.Column(db.SmallInteger, nullable=True)
    updator_role_cd = db.Column(db.SmallInteger, nullable=True)

    # Define relationships if needed
    # Example:
    # epps_ecode_mst = db.relationship('EppsEcodeMst', backref='epps_ecode_catg_lnk')

    def __repr__(self):
        return f"<EppsEcodeCatgLnk(comp_cd={self.comp_cd}, div_cd={self.div_cd}, ecode={self.ecode}, item_category={self.item_category})>"

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

from sqlalchemy import Column, Integer, String, SmallInteger, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EppsEmpLocLnk(db.Model):
    __tablename__ = 'epps_emp_loc_lnk'
    __table_args__ = {'schema': 'epps_admin'}

    comp_cd = db.Column(db.Integer, primary_key=True)
    div_cd = db.Column(db.SmallInteger, primary_key=True)
    loc_cd = db.Column(db.SmallInteger)
    role_cd = db.Column(db.SmallInteger)
    emp_cd = db.Column(db.String(50))
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

    def __repr__(self):
        return f"<EppsEmpLocLnk(comp_cd={self.comp_cd}, emp_cd={self.emp_cd})>"



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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    def __repr__(self):
        return f"<EppsRoleMst(comp_cd={self.comp_cd}, div_cd={self.div_cd}, role_cd={self.role_cd})>"
