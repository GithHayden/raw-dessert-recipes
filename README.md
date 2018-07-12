### Raw Chocolate Recipies
A data-driven web application that allows users to easily access and add new recipes.

### Functionalities
1. User selects...
2. User selects...
3. User selects...

### Technologies
1. **Cloud 9**: IDE `Integrated Development Environment` used to build project end to end.
2. **Materialize**:
3. **mLab**:
4. **MongoDB**: NoSQL Database.
5. **Flask**: A python microframework used to build and run the application. Flask offers beneficial functionality such as template logic, which allows the `base.html` file to be inherited on other html files via `{% extends 'base.html' %} {% block content %} {% endblock %}` code.
6. **Python code**: Written within `run.py`. Used to write the logic of the game.
7. **HTML files**: Used to build the structure of each application page.
8. **Chrome Dev Tools**: Used to execute inspection of application in browser and to perform UAT, including responsive testing.
9. **Git and GitHub**: Used for version control and to deploy a backup of the project.
10. **Heroku**: Used to deploy and host final project.

### Other Resources
1. Recipies - For purpose of populating this project used this [Recipe Website](http://rawfoodrecipes.com/).

### Development Process
1. **Workspace**: Blank `Cloud 9` workspace created.
2. **README.md**: Created with outline of the project and developed as project progressed.
3. **Files & Folders**: Created in line with wireframe and developed as project progressed.
4. **mLab**: Created the MongoDB database. Share details of how you created.
Flask - sudo pip3 install flask
App.py - set up for Flask
Heroku - create app to host project
5. **Materialize**: Add links to import library
6. **HTML files**: Build code
7. **App.py**:
8. **Commentary**: Developed throughout files to provide code guidance.
9. **Cloud 9 Linux Terminal**: Used to backup project via incremental `git status, git add <file/s> (staging area), git commit -m "<commentary>"` commands.

### Testing
**Manual testing**, ongoing via `Cloud 9`, `Run`. Once each functionality coded, checked application operating as expected in web browser by walking through each functionality. Testing included the following:

 recipies.html - jinja error rendering {{ endfor }}, should be  {% endfor %}
 app.py - application not rendering in browser. @app.route('add_recipe') should be @app.route('/add_recipe') '/' missing.
 jinja error - (edit_recipe spelled incorrectly)

Responsive

### Deploy via Heroku
1. Via Linux Terminal, login to Heroku, using 'heroku login' command. Input Heroku login details.
2. Create new Heroku app, using 'heroku apps:create appname' command.
3. Push project to Heroku, using 'push -u heroku master' command.
4. Create scale, using 'heroku ps:scale web=1' command.
5. Login to Heroku and select newly created app.
6. Select settings. Select ‘Reveal Config'. Add IP 0.0.0.0 and PORT 5000.
7. From 'More' menu on the top right, select 'Restart all dynos'.
8. View app: In settings, select Domain URL, NOT Git URL to view your hosted application.
9. Deployed via Heroku: [Raw Chocolate Recipes]().
10. 


Notes:
Ingredients - bullet point
Instructions - numbered
Alpha sort recipies
Add search, pagination, number of views, upvotes/likes, etc & statistics
Spellcheck
E2E commentary