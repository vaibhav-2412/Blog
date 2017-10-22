# Blog
Blog Application (phase:1) in which users can login with gmail or using in-app signin to add new blogs or edit their existing blogs. Non-Authenticated users can only view the blogs.

Fork this repository

git clone git@github.com:<your username>/Blog.git

mkvirtualenv Blog

cd Blog/

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
