import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv  

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
db = SQLAlchemy(app)

class EppsEcodeCatgLnk(db.Model):
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
@app.route('/ecode_catg_lnk/', methods=['GET'])
def get_ecode_catg_lnk():
    ecode_catg_lnk_list = EppsEcodeCatgLnk.query.all()
    result = []
    for link in ecode_catg_lnk_list:
        result.append({
            'comp_cd': link.comp_cd,
            'div_cd': link.div_cd,
            'ecode': link.ecode,
            'item_category': link.item_category,
            'created_dt': link.created_dt.strftime('%Y-%m-%d %H:%M:%S'),
            'created_by': link.created_by,
            'updated_dt': link.updated_dt.strftime('%Y-%m-%d %H:%M:%S') if link.updated_dt else None,
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
