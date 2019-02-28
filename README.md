<!-- # P
#### This is a web application where a user can add,comment on,upvote and downvote a pitch,Current version:25 february 2019

### By **TUYISENGE Anabella**
## Description
The pitch is a web app where a user can add a one minute pitch and other users can comment on it and upvote or downvote it.These pitches are divided in different categories such as pickup lines ,interview pitches and so on.A user has to create an account and they have to be logged in to post,vote on or comment on a pitch

## BDD

##Setup/Installations
### Prerequisites
* Python3.6
* Pip

### Cloning
* In your terminal<br>
   $ git clone https://github.com/Anabella1109/MeBlog.git
   $ cd MeBlog

### Install postgres
[Postgres]()
  
### Create virtual environment
sudo apt-get install python3.6-venv<br>
python3.6 -m venv virtual<br>
source virtual/bin/activate<br>

### Install dependencies
pip3 install -r requirements<br>

### Exporting environment variables
export DATABASE_URL='postgresql+psycopg2://username:password@localhost/meblog'<br>
export SECRET_KEY='Your secret key'

## Run database migrations
python manage.py db init<br>
python manage.py db migrate -m "initial migration"<br>
python manage.py db upgrade

### Running
 * In your terminal<br>

     $ chmod +x start.sh<br>
     $ ./start.sh

## Technologies used
* Python3.6
* HTML
* Bootstrap
* CSS
* Postgresql


## Support and contact details

Having any issues?
Email:bellaxbx1109@gmail.com
Slack:TUYISENGE Anabella

### License

[MIT](https://choosealicense.com/licenses/mit/)
Copyright (c) 2019 **TUYISENGE Anabella**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

 -->
