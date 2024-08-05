
from app import celery, db
from app.models import Domain
from app.utils import check_vulnerability
from datetime import datetime

@celery.task
def scan_domain(domain_id):
    domain = Domain.query.get(domain_id)
    if domain:
        is_vulnerable = check_vulnerability(domain.domain_name)
        domain.is_vulnerable = is_vulnerable
        domain.last_checked = datetime.utcnow()
        db.session.commit()
