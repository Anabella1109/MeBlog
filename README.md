 # MeBlog
#### This is personal blog that talks about my interests and day to day experiences ,Current version:1st march 2019

### By **TUYISENGE Anabella**
## Description
MeBlog is  my personal blog that talks about my interests and day to day experiences.Only me as the admin can add posts but you can enjoy as user a by commentting on posts and subscribing to receive notifications when there are new posts
## BDD

<!-- ## User
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| View blogs | Click on an article on the homepage to view the whole blog post| Displays the entire |
| Comment on blogs | Type comment details on the comment text area box in the blog page. The name and email are also required | The comment is displayed on the blog page below the blog content |
| Subscribe | Type your email and name in the subscribe form in the homepage. | Redirects to ```successfully subscribed page```. The user will receive a subscription confirmation email |

## Writer
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Login | Enter login credentials in the login page | Redirects the writer to the homepage |
| Add Blog | The `create blog` button in the sidebar redirects to the blog form. Fill this form with blog details | Redirects the writer to the new blog post |
| Delete Blog | Press `delete` button just below the blog title  | The blog is deleted and redirects to the homepage |
| Delete Comment | Press `delete` buttom below the user's comment to delete the comment | Deletes the comment and refreshes the page | -->

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

<!-- ## Technologies used
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

 --> -->
