# Galleria
## Author  
  
>[Tony](https://github.com/Tony-34)  
  
# Description  
This is a Django application for personal gallery that allows a user to upload images for other to see and be able to to share by coping the image link.
  

## User Story  
  
* View different photos that interest them  
* Click a single image to expand it and view the details of that photo  
* Search for different categories   
* Copy a link to the photo to share with my friends.  
* View photos based on the location they were taken.  


## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/Tony-34/Gallery
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Gallery pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3.8 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python3.8 manage.py makemigrations mygallery
 ``` 
 Now Migrate  
 ```bash 
 python3.8 manage.py migrate 
```
##### Run the application  
 ```bash 
 python3.8 manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python3.8 manage.py server 
```
##### Testing the application  
 ```bash 
 python3.8 manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 3.1.2](https://docs.djangoproject.com/en/3.1/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [tr33947@gmail.com]  
  



* Copyright (c) 2021 **Tony**