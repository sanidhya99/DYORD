# DYORD

Project Configuration
Install required dependencies by running the following commands:


    pip install django-restframework
    pip install djangorestframework_simplejwt
    pip install django-cors-headers

Set up the Django project and apps by running the necessary migrations. Navigate to the project directory containing the manage.py file and execute the following command:

    python manage.py makemigrations
    python manage.py migrate
Once the migrations have been applied successfully, start the Django development server:

shell
Copy code
python manage.py runserver
The server should now be running at http://localhost:8000.
intern task
This Django project consists of three apps: "register," "info," and "dealing." Each app has its own set of functionalities and permissions. Below is an overview of each app and its components.

Register App
The "register" app handles user registration, login, and user profile management. It includes a custom user model and uses JWT authentication for the register and login views.

Components
manage.py: This file is used to manage the custom user model and perform administrative tasks.

register/views.py: Contains the views for user registration, login, and user profile management.

Register view: Allows users to register with the system.
Login view: Authenticates users and provides a JWT token upon successful login.
User profile view: Displays the profile information for authenticated users.
Info App
The "info" app manages a blog model and includes views for creating, listing, updating, and deleting blog posts. The blog posts can be created by superusers only and can be read by any authenticated user. Update and delete operations are restricted to superusers.

Components
info/models.py: Defines the blog model.

info/views.py: Contains the views for managing blog posts.

Create view: Allows superusers to create new blog posts.
List view: Displays a list of all blog posts visible to authenticated users.
Update and Destroy views: Restricted to superusers for modifying and deleting blog posts.
Dealing App
The "dealing" app handles the product model and order delivery tracking. Only superusers can create, modify, or delete products. Product information can be viewed by anyone, but modifications are restricted to superusers. Delivery objects can be created by any user. Superusers can view all deliveries, while normal users can only see their own deliveries. Normal users can delete their own deliveries by providing the delivery ID, while superusers have the ability to delete any delivery.

Components
dealing/models.py: Defines the product and delivery models.

dealing/views.py: Contains the views for product and delivery management.

Product Create and List views: Allows superusers to create new products and displays a list of all products.
Product Update and Destroy views: Restricted to superusers for modifying and deleting products.
Delivery Create, List, and Delete views: Users can create delivery objects, view their own deliveries, and delete their own deliveries by providing the delivery ID. Superusers have access to all deliveries.
