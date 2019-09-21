# Django web project - Schoolmanager
My first web project for learning Django

# Project requirements
List of required modules:

django==2.2.3

psycopg2-binary==2.8.3

To install Requirements type in command line:

`pip install requirements.txt -r`

# PROJECT DESCRIPTION:

The application allows you to keep track of attendance and student performance.
This app shows:
- list of student;
- list of discipline;
- classes schedule;
- stedent presense and marks;
- student's details;
- discipline's details;
- class's details.

Data can be added in Django Admin panel.

# MODELS DESCRIPTION:
Students have following fields:
- full name;
- entrance date;
- exit date;
- knowledge level.

Disciplines have discipline names field only.

Classes schedule have following fields:
- discipline name;
- class date;
- class time.

Classes presence have following fields:
- schedule class ID;
- student ID;
- grade value.

# APP PAGES MAP STRUCTURE:

Get app pages map here: 
https://drive.google.com/file/d/1ckIJIi8Hp8Irkz3n53I6vkTFwKRSKF7C/view?usp=sharing

