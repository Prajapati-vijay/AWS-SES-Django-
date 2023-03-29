 AWS SES Project 

# Setting up the AWS :

1. First got to AWS 
2. Go to the verified identites
3. Now verify the new identity (You can verify both the email and the domain)
4. This is the email form which you are going to send the mail to anyone.
5. After go IAM user 
6. You will see a warning by AWS that your account is sandbox mode.
7. To move out from the sandbox mode we have to send the request to AWS team by filling their request form.
8. Give your complete details in the form.
9. AWS team will approve the account in 24hrs .
10. Now go to IAM user dashboard .
11. click on the users
12. Create new user and give the following permissons:-
a. AdministratorAccess
b. AmazonSESFullAccess
c.IAMUserChangePasword
13. Now get the credentials .
14. The credentials will be displayed only once so copy it .
15. Now we are done with the AWS

# Setting up the Django project:

1. Create a virtual environment 
```
py -m venv env
```
2. Install django in virtual environment after activating it 
3. Start new project
4. Add the following in settings.py file
```
EMAIL_BACKEND = 'django_ses.SESBackend'

AWS_ACCESS_KEY_ID='# Access key'
AWS_SECRET_ACCESS_KEY ='# Secret acess key'
AWS_SES_REGION_NAME='#Region'
AWS_SES_REGION_ENDPOINT='# Endpoint'
```

5. Install the library for working with AWS
```
pip install django-ses

```

6. Now configure the AWS before starting the project
```
aws configure

```
7. Enter all the credentials you have
8. Now you are all set to run the project 
9. ``` python manage.py runserver```