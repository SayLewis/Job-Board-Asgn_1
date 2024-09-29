from App.database import db
from datetime import datetime

class Job(db.Model):
    jobID =db.Column(db.Integer, primary_key=True)
    jobName= db.Column(db.String(50), nullable=False)
    jobDetails=db.Column(db.String(1000), nullable=False)
    postedDate=db.Column(db.DateTime, default=datetime.utcnow)


def __init__(self,jobName,jobDetails,postedDate):
    self.jobName=jobName
    self.jobDeatils=jobDetails
    self.postedDate=postedDate

def get_json(self):
    return{
        'JobID': self.jobID,
        'JobName': self.jobName,
        'Job Details':self.jobDetails,
        'posted Date':self.postedDate
    }  