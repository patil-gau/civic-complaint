### STEPS TO FOLLOW FOR INSTALLATION ###
1. Following softwares but be installed before before.
    1. Xammp
    2. Git
2. open cmd and type git clone https://github.com/letzzBuild/civic-complaint-backend.git
3. after downloading the project type cd civic-complaint-backend  
4. type pip install -r requirements.txt
5. Start mysql from xampp control panel (seach on windows search bar)
5. type python manage.py makemigrations 
6. type python manage.py migrate
7. python manage.py runserver  => this starts your application of `http://127.0.0.1:8000`