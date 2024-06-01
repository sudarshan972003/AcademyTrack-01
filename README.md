# Student Management System ( SMS )

A web-based application built using Django that allows users to manage student records. The application supports user authentication, and functionalities to add, view, update, and delete student records. It also displays location and weather information for logged-in users.

## Features

- **User Authentication**: Users can sign up, log in, and log out.
- **Student Management**:
  - Add new student records.
  - View a list of all students.
  - Update existing student records.
  - Delete student records.
- **Location and Weather Information**: Displays the current location and temperature for the logged-in user.

### Installation for this project :
```
pip install django
pip install requests
```

**Set Up the Database**:
    ```
    python manage.py migrate
    ```

**Create a Superuser**:
    ```
    python manage.py createsuperuser
    ```

**Collect Static Files**:
    ```
    python manage.py collectstatic
    ```

## How to Run

1. **Start the Development Server**:
    ```
    python manage.py runserver
    ```

2. **Access the Application**:
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Project Structure

- **templates**: Contains all HTML templates for the project.
- **static**: Contains static files like CSS.
- **smsapp**: The main Django app for the project.
- **views.py**: Contains the views for handling the HTTP requests.
- **models.py**: Defines the database models.
- **urls.py**: Contains the URL configurations for the app.

## Views

- **ulogin**: Handles user login.
- **usignup**: Handles user registration.
- **ulogout**: Handles user logout.
- **home**: Displays the home page with location and weather information.
- **addstudent**: Form to add a new student.
- **showstudent**: Displays a list of all students.
- **updatestudent**: Form to update student information.
- **deletestudent**: Form to delete a student record.

## Important Files

- **settings.py**: Django settings file.
- **urls.py**: URL routing file.
- **models.py**: Defines the Student model.
- **views.py**: Contains the logic for the views.

## Dependencies

- Django
- Requests (for fetching IP and weather data)

## CSS Styling

- **styles.css**: Contains the styles for the project.
- 

## Acknowledgements

- **IPify**: For providing the IP address.
- **ipapi**: For location data.
- **OpenWeatherMap**: For weather data.
