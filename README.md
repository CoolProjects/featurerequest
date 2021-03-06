# FEATURE REQUEST - Web Application in DJANGO

This application is developed to create a prototype of creating a Feature Request Application for support team taking feedback from the client about new Feature Request they want. The application is developed in [**DJANGO**] (https://www.djangoproject.com/) and default **SQLite**. For the frontend **Twitter Bootstrap** is used and lot of other **Java Script Plugins**.


## Requirements

1. Python3
2. Django 1.9.3
3. PIP
4. Virtualenv


## Application ScreenShot

![Feature Request Application](https://raw.githubusercontent.com/himadriganguly/featurerequest/master/screenshots/screenshot.jpg "Feature Request Application Browser Preview")


## Running The Application

1. Download it from github and unzip it to a folder
2. Create a virtual environment using Virtualenv and activate it
3. Now intall Django 1.9.3
4. Now move to the folder of the unzipped application 
5. Run `python manage.py migrate`
6. Now create the super user for the application by running `python manage.py createsuperuser`
7. Run `python manage.py runserver`
8. Open browser and go to `127.0.0.1:8000/admin` and log in
9. Now create some `Clients`, `Products`, you can also create some user without staff member previledges and then logout
10. Move to the `127.0.0.1` and log in with username and password that you created or admin username and password.
11. Enjoy!


## Additional Requirements

You can use these lines seperately for local development or can use `pip install -r requirements/local.txt`

1. pip install factory_boy

2. pip install --upgrade pyflakes

3. pip install django-debug-toolbar

4. pip install pyflakes

5. pip install pep8

6. pip install autopep8

7. pip install coverage

8. pip install django-jenkins

9. pip install python-dateutil

10. pip install selenium


## Other Tools Used

1. Jenkins (For CI) [**http://jenkins-ci.org/**](http://jenkins-ci.org/)

2. Git (For source code management) [**https://git-scm.com/**](https://git-scm.com/)

3. Selenium (Automated Browser Testing) [**http://www.seleniumhq.org/**](http://www.seleniumhq.org/) [Selenium is used along with Jenkins in a Grid Setup]


## Features

1. Admin Interface to create, edit, update, delete `Clients`, `Feature requests` and `Products`
2. Required user credentials to Login to the Application
3. Create Feature Request from the Application without the Admin Interface with much better interface and error checking. The Priority of the Feature Request will automatically be assigned with the latest number based on the Client.
4. View all the Feature Request for specific client in a table and also click the Feature Title to get more details.
6. Drag and Drop the Feature List to sort in the table to sort the Priority number which will automatically be sorted when drag and drop and then update to update to the backend.
7. View **Charts** based on the number of Feature Request of **Clients**, **Number of Feature Request on Product Area** and the **Target Date** of Feature Request.


## Limitations

1. Testing in progress.
2. The Application can be more dry by tweaking the code. Sorry developed in a hurry so make some mistakes.
3. Code can be more optimized by making better coding than me.
3. More Features can be added.


## Credits

1. [**Twitter Bootstrap**](http://getbootstrap.com/) - This is a great and quite popular Frontend Framework and I am using it for many years.

2. [**Animate.css**](https://daneden.github.io/animate.css/) - This is a great CSS for CSS3 animation. I love it.

3. [**gentelella**](https://github.com/puikinsh/gentelella) - This is an excellent Admin theme using Twitter Bootstrap which I have used for the application. 

2. [**jQuery Sortable**](https://johnny.github.io/jquery-sortable/) - This is quite useful drag and drop sorting plugin for jQuery.

3. Great and helpful community in the DJANGO IRC Channel at **#django**
 
4. OTHERS


## CONTRIBUTE

If you have any idea you want to implement in this project please do so or if you want to make the code better please go ahead and make a pull request, I will try my best to merge appropriately.


If you have any idea you want to develop in the open source community and like me to join you please feel free to contact. Thank you.


Hope you will like the application.

