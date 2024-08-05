
from flask import Blueprint, request, render_template, jsonify
from app.models import Domain
from app.tasks import scan_domain
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    domains = Domain.query.all()
    return render_template('dashboard.html', domains=domains)

@bp.route('/scan', methods=['POST'])
def scan():
    domain_name = request.form['domain_name']
    domain = Domain.query.filter_by(domain_name=domain_name).first()
    if not domain:
        domain = Domain(domain_name=domain_name)
        db.session.add(domain)
        db.session.commit()

    scan_domain.delay(domain.id)
    return jsonify({'message': 'Scan started for domain: {}'.format(domain_name)})
