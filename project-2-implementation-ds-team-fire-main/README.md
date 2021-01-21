# Data Science Project

#### Abhimanshu Mishra, Aditya Bhagwat, Vinit Bhosale, Sharvari Joshi

## Setup

Create a conda environment using ```conda create --name nepu python=3.6```.

Activate it using ```conda activate nepu```.

Install the required packages using ```pip install -r requirements.txt```.

## Data

Obtain the data as shared by the team members and place it in the data directory such that it has the structure explained below.
The data is freely available [here](https://drive.google.com/drive/folders/1XNLey7DcHbMLP0v4ooZZaVs0BbMh07iI?usp=sharing).

## Structure

```data/``` - This folder contains the unified imdb reviews file and a subfolder twitter_data/ which has tweets for each TV show, all in json format.

```src/``` - This folder contains the code for analysis of all the data. Everything is done in a single jupyter notebook.

## Running

Once the conda environment has been created and activated successfully, run ```jupyter notebook``` which will automatically open up a browser window. In this window, navigate to the .ipynb analysis file and open it. You will now be able to run all the cells and see their outputs.