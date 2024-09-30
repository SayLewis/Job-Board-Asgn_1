from App.database import db
from datetime import datetime


class Applicant(db.Model):
    applicantID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    resume = db.Column(db.String(200))  # Assume this is a link or path to the resume file
    appliedDate = db.Column(db.DateTime, default=datetime.utcnow)
    jobID = db.Column(db.Integer, db.ForeignKey('job.jobID'), nullable=False)  # Foreign key relationship

    def __init__(self, name, email, resume, jobID):
        self.name = name
        self.email = email
        self.resume = resume
        self.jobID = jobID

    def get_json(self):
        return {
            'ApplicantID': self.applicantID,
            'Name': self.name,
            'Email': self.email,
            'Resume': self.resume,
            'AppliedDate': self.appliedDate.strftime('%Y-%m-%d %H:%M:%S'),
            'JobID': self.jobID
        }
