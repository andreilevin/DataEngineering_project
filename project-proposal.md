# Andrei's Data Engineering Project Proposal

My goal is to deploy a web app that predicts an NBA player's market value based on his general player information (weight, height, age, position, draft pick, etc.) and current-season stats. 

First, I will train a regression model in sklearn based on the past 5 years of web scraped NBA contract and statistical data and extract the model parameters (this only needs to be done once a year) .

Next, I will create a pipeline that involves the following steps:

* Use beautifulsoup, pandas and sqlite to create a database with current-season stats and info for all active NBA players
* Scrape basketball-reference.com once a day to update this database
* Using the stored model parameters, predict the market value of each player (also updated daily)
* Create a simple web app with streamlit and deploy it with heroku

I would love some suggestions for which tools would be most appropriate for this task (instead of or in addition to some of the tools I proposed above).   Perhaps most importantly, should the pipeline live on my local machine or in the cloud?  If in the cloud, do you recommend I use Google Colab, GCP, or AWS?  If I use cron to automate the daily scraping and updates, does this change the answer to the previous question?  Are there any other features you would like to see?   
