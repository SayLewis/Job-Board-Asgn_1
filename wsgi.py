import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User

from App.main import create_app
from App.controllers import * #(create_user, get_all_users_json, get_all_users, initialize)




# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Job Commands
'''

job_cli = AppGroup('job', help='Job object CLI commands')

# This command will be: flask job add Developer "Develops software" 2024-09-28
@job_cli.command("add", help="Adds a job object to the application")
@click.argument("jobName", default="Developer")
@click.argument("jobDetails", default="Develops software")
@click.argument("postedDate", default=None, required=False)
def add_job_command(jobname, jobdetails, posteddate):
    success, message = add_job(jobname, jobdetails, posteddate)
    if success:
        print("Job added:", message)
    else:
        print("Error:", message)

# This command will be: flask job update 1 Manager "Manages the team"
@job_cli.command("update", help="Updates a job object in the application")
@click.argument("jobID", default=1)
@click.argument("jobName", default="Manager")
@click.argument("jobDetails", default="Manages the team")
def update_job_command(jobid, jobname, jobdetails):
    success, message = update_job(jobid, jobname, jobdetails)
    if success:
        print("Job updated:", message)
    else:
        print("Error:", message)

# This command will be: flask job delete 1
@job_cli.command("delete", help="Deletes a job object from the application")
@click.argument("jobID", default=1)
def delete_job_command(jobid):
    success, message = delete_job(jobid)
    if success:
        print("Job deleted:", message)
    else:
        print("Error:", message)

# This command will be: flask job list
@job_cli.command("list", help="Lists all jobs that were added to the application")
def list_jobs_command():
    jobs = get_all_jobs()
    for job in jobs:
        print(job.get_json())

# This command will be: flask job list_by_id 1
@job_cli.command("list_by_id", help="Lists a job by its ID")
@click.argument("jobID", default=1)
def list_job_by_id_command(jobid):
    job = get_job_by_id(jobid)
    if job:
        print(job.get_json())
    else:
        print("Job not found")

# This command will be: flask job list_by_name Developer
@job_cli.command("list_by_name", help="Lists all jobs by name")
@click.argument("jobName", default="Developer")
def list_jobs_by_name_command(jobname):
    jobs = get_jobs_by_name(jobname)
    if jobs:
        for job in jobs:
            print(job.get_json())
    else:
        print("No jobs found with that name")

app.cli.add_command(job_cli)  # Add the job group to the CLI








'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)