# JumpyPotatoes

Team roster: Runmin (William) Lu, Raymond Wu, Jerry Ye, Ivan Zhang

## Project Description
The goal of PoliTracker is to allow its users to follow and keep track of what actions their political representatives are taking. By taking advantage of the News API, The New York Times API, Twitter API, and Google’s Civic Information API, based on how many posts and articles are written about a politician, we can determine how active any given politician is. By combining the Twitter API and the TwinWord Sentiment Analysis API, we can determine public sentiment and support toward any given politician. On our user interface, the user can see all of this information, as well as recent articles about a politician for more details. We can make the data we aggregate even stronger by storing the data in a database, and analyzing it for our users (public sentiment/activity across states, political parties, etc.; additional feature).

We will be using Bootstrap because it has a grid system that is built into Flexbox. In addition, it provides simplified and easily usable forms. There are features of Foundation that are still in their Beta version whereas Bootstrap has long supported it. Bootstrap's forum is also populated by a massive community of other developers.


## Usage

**System requirements/Dependencies**:
Most of our dependencies can be installed through simple pip command listed below, however, you will need Python 3 and SQLite 3 on your system which must be installed. Python 3 is the programming language used to run the application while sqlite3 is used to maintain our databases. Both of these are essential. If, in your terminal, running `$ python3` invokes the Python 3 interpreter, and running `$ sqlite3` opens the SQLite 3 shell, you are good to go. If not, please follow the links below.
* [Install sqlite3](https://mislav.net/rails/install-sqlite3/ "Install sqlite3")
* [Install python3](https://realpython.com/installing-python/ "Install python3")

First, clone this repository:
```
$ git clone https://github.com/raywu6/JumpyPotatoes.git
```
Activate your virtual environment. If you do not have one set up, you may create one in the current working directory, and activate it like so:
```
$ python3 -m venv dc
$ . dc/bin/activate
```

Next, change your directory to go into your local copy of the repository:
```
(dc)$ cd JumpyPotatoes
```
Now, install all of the requirements needed to run this project. This command simply installs jinja and Flask. Flask is the python framework used to allow for simpler software development. Jinja is used to connect front end HTML/CSS code to back-end Python Flask code.

```
(dc)$ pip install -r requirements.txt
```

Now, run the python file to start the Flask server:
```
(dc)$ python3 app.py
```


Finally, open your web browser and open `localhost:5000`.

To terminate your server instance, type <kbd> CTRL </kbd> + <kbd> C </kbd>.

To exit your virtual environment, run the command `$ deactivate`.

### Procuring API Keys

We are using the Google Civic Information API, the News API, The New York Times API, the IP API, as well as the Wikipedia API.

#### [Google Civic Information API](https://developers.google.com/civic-information/docs/v2/)
0. Sign up for a Google Developers account [here](https://console.developers.google.com) with your Google account.
1. Create a new project by following the only prompt on the user interface. Enter a project name and description.
2. Click Library on the navigation pane on the left. In the search box, type "Civic Information."
3. Click Enable to enable this API, and click Create Credentials to set up your API credentials.
3. You will be then given an API key registered to your account for the registered application.
4. Put the API key in a text file named `googleCivic.txt` in the root directory of the cloned repo.
5. To send test API requests, consult the [API documentation](https://developers.google.com/civic-information/docs/v2/) for the appropriate API request URL and parameters you need for the desired information. You will need to include the key-value pair `key=YOUR_API_KEY_HERE`.

#### [News API](https://newsapi.org/)
0. Sign up for a News API account [here](https://newsapi.org/register).
1. You will be then given an API key registered to your account.
2. Put the API key in a text file named `newsApi.txt` in the root directory of the cloned repo.
3. To send test API requests, consult the appropriate [API documentation](https://newsapi.org/docs/get-started) for the appropriate API request URL and parameters for the information you want to obtain. Most commonly, you will need to include the key-value pair `apiKey=YOUR_API_KEY_HERE`.

#### [The New York Times API](https://developer.nytimes.com/)
0. Sign up for an account [here](https://developer.nytimes.com/signup). When prompted to select an API, choose "Article Search API."
1. Your API key will be sent to your e-mail.
2. Put the API key in a text file named `nytApi.txt` in the root directory of the cloned repo.
3. To send test API requests, consult the [API documentation](https://developer.nytimes.com/article_search_v2.json) for the appropriate API request URL and parameters you need for the desired information. You will need to include the key-value pair `api-key=YOUR_API_KEY_HERE`.

#### [IP API](https://ipapi.co/)
0. You do not need to obtain an API key to use this API service! You can get information based on the IP address by using the following link: `https://ipapi.co/json`

#### [Wikipedia API](https://en.wikipedia.org/api/rest_v1/)
0. You do not need to obtain an API key to use this API service! You can get information based on the IP address by using the following link: `https://en.wikipedia.org/api/rest_v1/page/summary/` followed by the name of the Wikipedia article you wish to look up, with underscores (`_`) in place of spaces. Example: `https://en.wikipedia.org/api/rest_v1/page/summary/Bill_de_Blasio`.