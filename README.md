# [make_a_poll](https://www.twitter.com/make_a_poll)

Welcome to make_a_poll! The purpose of this Python script is to automatically reply to tweets which contain popular phrases such as: "like for no", "retweet for yes", and "just trying to prove a point" and automatically reply to them with a poll. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing the repository and running the script

1.) First you will need to clone the repository

```
git clone https://github.com/RyChrome/make_a_poll
```

2.) Then, you will need to go to https://developer.twitter.com/ and generate a Consumer Key, Consumer Secret, Access Key, and Access Secret. 

3.) Once you have done this, create a config.ini file.

```
touch config.ini
```

4.) In your config.ini file place these strings on lines 1 through 4 in respective order. Make sure you don't share these with others, or they will be able to send tweets to your twitter account.

Once you're done, fire up your favorite text editor or IDE and run the program

```
python3 bot.py
```

## Additional notes

As of today, tweepy works with all Python versions except 3.7.0. Because of this, you will need to create a virtual environment using [Python 3.6.6 or lower] (https://www.python.org/downloads/release/python-366/)

## Built With

* [Python 3.6](https://docs.python.org/3.6/) - Python version used
* [Tweepy](http://tweepy.readthedocs.io/en/v3.6.0/) - External twitter library for Python
* certifi==2018.4.16
* chardet==3.0.4
* idna==2.7
* oauthlib==2.1.0
* PySocks==1.6.8
* requests==2.19.1
* requests-oauthlib==1.0.0
* six==1.11.0
* tweepy==3.6.0
* urllib3==1.23

## Authors

* **Ryan Dils** - *Initial work* - [RyChrome](https://github.com/rychrome)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

## Acknowledgments

The inspiration for this project came from my own annoyance with people fishing for engagements on twitter instead of just creating a poll that gives them actual data. Visit (http://twitter.com/make_a_poll)
