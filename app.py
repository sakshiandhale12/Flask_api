from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI') + "?options=-c%20search_path%3Depps_admin"
db = SQLAlchemy(app)

class EppsEcodeCatgLnk(db.Model):
    __tablename__ = 'epps_ecode_catg_lnk'
    __table_args__ = {'schema': 'epps_admin'}

    comp_cd = db.Column(db.String(10), primary_key=True)
    div_cd = db.Column(db.SmallInteger)
    ecode = db.Column(db.String(10))
    item_category = db.Column(db.String(50))
    created_dt = db.Column(db.DateTime)
    created_by = db.Column(db.String(10), nullable=True)
    updated_dt = db.Column(db.DateTime, nullable=True)
    updated_by = db.Column(db.String(10), nullable=True)
    terminal_id = db.Column(db.String(100), nullable=True)
    active_yn = db.Column(db.String(1), nullable=True)
    creator_role_cd = db.Column(db.SmallInteger, nullable=True)
    updator_role_cd = db.Column(db.SmallInteger, nullable=True)

# Routes
# Routes
@app.route('/ecode_catg_lnk/', methods=['GET'])
def get_ecode_catg_lnk():
    ecode_catg_lnk_list = EppsEcodeCatgLnk.query.all()
    result = []
    for link in ecode_catg_lnk_list:
        try:
            created_dt_str = link.created_dt.strftime('%Y-%m-%d %H:%M:%S') if 1900 <= link.created_dt.year <= 2100 else None
        except (AttributeError, ValueError):
            created_dt_str = None

        try:
            updated_dt_str = link.updated_dt.strftime('%Y-%m-%d %H:%M:%S') if link.updated_dt and 1900 <= link.updated_dt.year <= 2100 else None
        except (AttributeError, ValueError):
            updated_dt_str = None

        result.append({
            'comp_cd': link.comp_cd,
            'div_cd': link.div_cd,
            'ecode': link.ecode,
            'item_category': link.item_category,
            'created_dt': created_dt_str,
            'created_by': link.created_by,
            'updated_dt': updated_dt_str,
            'updated_by': link.updated_by,
            'terminal_id': link.terminal_id,
            'active_yn': link.active_yn,
            'creator_role_cd': link.creator_role_cd,
            'updator_role_cd': link.updator_role_cd
        })
    return jsonify({'ecode_catg_lnk': result})

# Define the initdb command
@app.cli.command("initdb")
def initdb_command():
    """Initialize the database."""
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
