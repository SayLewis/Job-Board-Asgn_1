from App.models import Applicant
from App.database import db
from datetime import datetime

def add_applicant(name, email, resume, jobID):
    try:
        applicant = Applicant(name=name, email=email, resume=resume, jobID=jobID)
        db.session.add(applicant)
        db.session.commit()
        return True, "Applicant added successfully"
    except Exception as e:
        db.session.rollback()
        return False, str(e)

def get_applicants_by_job(jobID):
    applicants = Applicant.query.filter_by(jobID=jobID).all()
    return [applicant.get_json() for applicant in applicants]

def get_all_applicants():
    applicants = Applicant.query.all()
    return [applicant.get_json() for applicant in applicants]

