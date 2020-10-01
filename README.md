# OnlineBooking
Online Booking System for Dog Grooming

Contributors: Hongxiang Yang, Callum Vidler, Tianyi Ou, Yu-Heng Hong (Group 16)



This project belongs to the subject SWEN90016 Software Processes and Management in University of Melbourne. It provides a simple platform for dog grooming clients to book this service and the dog groomers can easily plan the grooming schedule.



## Environment installation view

```Sh
# You have to install python3.6
pip install django
# cd into the project folder
# Database setting up
python manage.py migrate
python manage.py makemigrations signup
manage.py sqlmigrate signup 0001
# Run local server
python manage.py runserver
```



## Development environment

IDE: PyCharm CE 2018.1.2 (Community Edition)

Python: 3.6



## The MIT License

Copyright (c) 2018-2018 Hongxiang Yang, Callum Vidler, Tianyi Ou, Yu-Heng Hong

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
