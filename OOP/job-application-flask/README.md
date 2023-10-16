# Job Application App👨🏻‍💻

The Flask Form Submission and Email Notification App is a Python-based web application built using Flask. This application allows users to submit a form with their information, which is then stored in a SQLite database. Additionally, an email notification is sent to the user confirming the submission of the form.

## Installation 🏗️

### Prerequisites
* Python 3.7+
* Flask
* Flask-SQLAlchemy
* Flask-Mail

### Installation and Setup
1. Environment Variables:

* Create an environment variable named PASSWORD to store your email account's password, which is used for sending email notifications.

2. Database Setup:

* The application is configured to use an SQLite database. The database file will be created as data.db in the same directory as your application script.

3. Application Configuration:

* In the script, you can customize the following configurations in the app.config dictionary:
* SECRET_KEY: Modify the secret key to enhance security.
* SQLALCHEMY_DATABASE_URI: Change the database URI if needed.
* MAIL_SERVER, MAIL_PORT, MAIL_USE_SSL, MAIL_USERNAME, and 
* MAIL_PASSWORD: Set the email server and credentials for sending notifications.

#### Running the Chatbot Application
Run the application by executing the provided Python script. This script initializes the Flask app, creates the database, and starts the development server.

python
Copy code
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)


