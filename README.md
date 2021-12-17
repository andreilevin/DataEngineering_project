# MoneyB-ball 

### Predicting the market value of NBA players from in-season stats 

We can all go online to look up our favorite NBA player's current salary, but how do we tell if this salary matches up with his actual market value?  In other words, if this player suddenly became a free agent, how much would a team likely pay him compared to what he's making now?  To answer this question using machine learning, I scraped the last 5 years of NBA free agent data using `beautifulsoup` and trained a linear regression model in `scikit-learn` to predict the contract each free agent signed, based on their previous-season data.  Using this model, I was able to predict the market value of all current NBA players based on their season stats so far.  I then deployed these predictions to a [web app](https://share.streamlit.io/andreilevin/dataeng_project/main/streamlit-app.py) using streamlit.  My presentation slide deck can be viewed [here](https://github.com/andreilevin/DataEng_project/blob/main/AndreiPresentation.pdf).

The workflow consists of four main steps.  In order:

1. Scrape and clean the past 5 years of free agent stats (from basketball-reference.com) and salaries (from hoopshype.com) and store the the data locally in the [data/](https://github.com/andreilevin/DataEng_project/tree/main/data)  folder.   This only needs to be done once a year and is best done is a jupyter notebook:  [model-scrape.ipynb](https://github.com/andreilevin/DataEng_project/blob/main/notebooks/model-scrape.ipynb)

2. Use this data to train a regression model and save the resulting model parameters locally in a pkl file.  This also only needs to be done once a year:  [model-fit.ipynb](https://github.com/andreilevin/DataEng_project/blob/main/notebooks/model-fit.ipynb)

3. During the NBA season, games are played almost daily.  Thus, we need update our current player stats by running [current-scrape.py](https://github.com/andreilevin/DataEng_project/blob/main/current-scrape.py)

4. After updating the current-season stats, we update the corresponding market value predictions as well by running [current-predict.py](https://github.com/andreilevin/DataEng_project/blob/main/current-predict.py)

   

#### To run the web app:

* From within this directory, run `python current-scrape.py`  in terminal followed by `python current-predict.py`  This will update the dataframe `data/df_marketvalues.csv` with the current season stats and corresponding market value predictions. 

* Push the updated `df_marketvalues.csv` file to github.  The streamlit app should update automatically.

* __App Code__:  [streamlit-app.py](https://github.com/andreilevin/DataEng_project/blob/main/streamlit-app.py)

* __App Website__:  https://share.streamlit.io/andreilevin/dataeng_project/main/streamlit-app.py

  

