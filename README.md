#teste-b2w

# project structure

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
```

# CAREFUL:

revenue = unit price * units sold

----------------

# todos

> are all data collected at regular intervals????

## presentation

- maybe two presentations, one for executives, one for technical audiences

- need to present **both** past behavious as well as current trends and predictions for the future.

## process

The first I felt I needed to do was to look at current frameworks and articles about time-series forecasting to avoid making silly mistakes.


#### first approach

The first approach was very naïve, it was just linear regression because sometimes really simple models give good results and are easy and cheap to build (also, you can give some kind of early information to decision-makers while you are still working on a more sophisticated model).

Using **just sales data**, transform the dataset into a new dataset where each pair (X_i, y_i) is the following:

X_i = 3 (or 4, or 5) prices for 3 (or 4, or 5) sequential days (for a single product)
y_i = price for the next day

So we learn a very simple model that estimates the next price (for a single product)

**Assumptions**

- the model is stationary, i.e. the target function does not change over time


#### second approach

the second model is the same, but using competitor information such as competitor price as features (for all competitors) for the same product and also a bit for the payment type?

#### targets

- given a product and a price, how much will be sold
 
  - per unit time?

#### differentiating factors (show off?)

 - git (I'm using git)

 - sql

   - maybe load the data into a database and perform a couple of queries to extract aggregation information, etc?

 - clustering

   - products with similar price behaviour?


#### promising packages

- pyflux

- cesium

- rpy2

 - ....

#### overfitting

I shouldn't try too many algorithms

#### seasonality

Acknowledge and explain how it's affected my analysis, what I did to handle that

#### time series

Acknowledge it's a time series (double check)

- ARIMA?

- SARIMA

#### evaluation metrics

 - MAE (relative)

 - RMSE (relative)

- if data is skewed, probably better to use AUC?


#### things I would do if I had more time

- recurrent neural networks (RNNs), which are neural-networks that take sequence into account

  - e.g. LSTM?


------

### references

- [Time Series Analysis with Python Intermediate | SciPy 2016 Tutorial | Aileen Nielsen](https://www.youtube.com/watch?v=JNfxr4BQrLk)

### stuff to look at

- [https://research.fb.com/prophet-forecasting-at-scale/](https://research.fb.com/prophet-forecasting-at-scale/)

- [unplugg API for time series forecasting](http://unplu.gg/test_api.html)