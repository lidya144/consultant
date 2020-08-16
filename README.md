# Consultant app
# Instruction with docekr
1. docker-compose build
2. docker-compose run app sh -c "python manage.py makemigrations"
3. docker-compose run app sh -c "python manage.py migrate"
4. docker-compose up

# Instruction without docker
1. python -m pip  install -r requirements.txt
2. virtualenv venv
3. source venv/bin/activate
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py createsuperuser -- eneter the requested fields--
