from App.models import Job
from App.database import db
from datetime import datetime

# Add Job
def add_job(jobName, jobDetails, postedDate=None):
    try:
        job = Job(jobName=jobName, jobDetails=jobDetails,postedDate=postedDate)
        db.session.add(job)
        db.session.commit()
        return True, "Job added successfully"
    except Exception as e:
        return False, str(e)

# Get Job by ID
def get_job_by_id(jobID):
    job = Job.query.filter_by(jobID=jobID).first()
    return job

# Get Jobs by Name
def get_jobs_by_name(jobName):
    jobs = Job.query.filter(Job.jobName == jobName).all()
    return jobs

def get_all_jobs_json():
    jobs = Job.query.all()
    if not jobs:
        return []
    jobs_json = [job.get_json() for job in jobs]
    return jobs_json

# Get All Jobs
def get_all_jobs():
    jobs = Job.query.all()
    return jobs

# Update Job
def update_job(jobID, jobName=None, jobDetails=None):
    try:
        job = Job.query.filter_by(jobID=jobID).first()
        if job:
            if jobName:
                job.jobName = jobName
            if jobDetails:
                job.jobDetails = jobDetails
            db.session.commit()
            return True, "Job updated successfully"
        else:
            db.session.rollback()
            return False, "Job does not exist"
    except Exception as e:
        db.session.rollback()
        return False, str(e)

# Delete Job
def delete_job(jobID):
    try:
        job = Job.query.filter_by(jobID=jobID).first()
        if job:
            db.session.delete(job)
            db.session.commit()
            return True, "Job deleted successfully"
        else:
            return False, "Job does not exist"
    except Exception as e:
        db.session.rollback()
        return False, str(e)
