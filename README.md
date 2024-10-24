# Twitter Clone 🐦

A simple Django-based Twitter clone that allows users to register, log in, post tweets, and view or delete them. Superusers have admin controls to delete any tweet. 

## Features

- **User Authentication**: 
  - Login, Logout, and Registration functionality.
  - User passwords are securely hashed.
  
- **Tweet Functionality**:
  - View all tweets on the home page.
  - Create new tweets (requires login).
  - Edit and update tweets.
  - Admin can delete any tweet.

- **Profile Management**:
  - Users have their own profiles with role-based redirection (admin vs regular user).

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS (with Django templates)
- **Database**: SQLite (default with Django)

## Installation and Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/sarfaraaz97/twitter-clone.git
   cd twitter-clone

2. **Create a virtual environment**:

   ```bash
      python -m venv env
      source env/bin/activate
   
3. **Install the dependencies**:

   ```bash
    pip install -r requirements.txt
   
4. **Migrate the database**:

   ```bash
    python manage.py migrate

5. **Run the development server**:

   ```bash
    python manage.py runserver
   
### Access the project:

Open your browser and navigate to http://127.0.0.1:8000.

Project Structure
php
Copy code
app1/                # Main app folder
  ├── migrations/    # Database migration files
  ├── models.py      # Tweet model definition
  ├── views.py       # Handles the logic for various pages
  ├── urls.py        # URL routes for the application
  ├── templates/     # HTML templates
  └── static/        # Static files (CSS, JavaScript)
  
twitter_clone/       # Project settings and configuration files
  ├── settings.py    # Django project settings
  └── urls.py        # Main URL configurations
Routes and Views
Home (/): Displays all tweets.
Login (/login): Log in with your credentials.
Logout (/logout): Log out of your account.
Register (/register): Create a new account.
Profile (/profile): View your profile.
Create Tweet (/create): Create a new tweet.
Edit Tweet (/show/<int:rid>): Edit an existing tweet.
Delete Tweet (/delete/<int:rid>): Superuser can delete any tweet.
Admin Controls
Superusers (admins) can access the Django admin panel to manage users and tweets.
Superusers can delete any tweet via the frontend using the delete button.
Screenshots
Home Page	Login Page
Future Improvements
Add likes and retweets functionality.
Implement tweet commenting.
Enhance the UI with CSS frameworks like Bootstrap or Tailwind CSS.
Contributing
Feel free to fork this repository, make updates, and submit pull requests!

License
This project is open-source and available under the MIT License.

