# MoneyB-ball

**Note**:  *This is another early version of what later became the more sophisticated [Hoops Hero](https://github.com/andreilevin/HoopsHero) project.* 

### Project Presentation [Slides](https://github.com/andreilevin/DataEng_project/blob/main/AndreiPresentation.pdf): 

[![AndreiPresentation.pdf:](https://raw.githubusercontent.com/andreilevin/DataEng_project/main/cover_slide.jpg)](https://github.com/andreilevin/DataEng_project/blob/main/AndreiPresentation.pdf)

## Summary

In an [earlier project](https://github.com/andreilevin/Regression_project/) I used a linear regression model to predict the salary of NBA free agents based on their previous year's stats.  Here I optimized the scraping and cleaning workflow and deployed the model to a basic web app that could be updated daily over the course of an NBA season.

## Workflow

1. Scrape and clean the past 5 years of free agent stats (from basketball-reference.com) and salaries (from hoopshype.com) and store the the data locally in the [data/](https://github.com/andreilevin/DataEng_project/tree/main/data)  folder.   This only needs to be done once a year and is best done in a jupyter notebook:  [model-scrape.ipynb](https://github.com/andreilevin/DataEng_project/blob/main/notebooks/model-scrape.ipynb)

2. Use this data to train a regression model and save the resulting model parameters locally in a ```.pkl``` file.  This also only needs to be done once a year:  [model-fit.ipynb](https://github.com/andreilevin/DataEng_project/blob/main/notebooks/model-fit.ipynb)

3. During the NBA season, games are played almost daily.  Thus, we need update our current-season player stats by running [current-scrape.py](https://github.com/andreilevin/DataEng_project/blob/main/current-scrape.py)

4. After updating the current-season stats, we update the corresponding market value predictions as well by running [current-predict.py](https://github.com/andreilevin/DataEng_project/blob/main/current-predict.py)


## Running the Web App:

* From within this directory, run `python current-scrape.py`  in terminal followed by `python current-predict.py`  This will update the dataframe `data/df_marketvalues.csv` with the current season stats and corresponding market value predictions. 

* Push the updated `df_marketvalues.csv` file to github.  The Streamlit app should update automatically.

* **Web App:**  [Code](https://github.com/andreilevin/DataEng_project/blob/main/streamlit-app.py)  |  [Website](https://share.streamlit.io/andreilevin/dataeng_project/main/streamlit-app.py)   

