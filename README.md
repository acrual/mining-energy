# Motivation

In order to promote liquid, we need to bring interesting assets to it. We already have BMN but unfortunately the part of the market that has an interest in Bitcoin, is very small and the part of it that understands Bitcoin mining is way smaller. This project is an attempt at making BMN easier to approach and most importantly, to explain how interesting are its economics, in order to hopefully attract investors to it.

By building a strong foundation for this project, we can use it to eventually model some other financial products to be eventually launched on liquid

## The project

It consists of a series of python scripts that download some data, store it in excel sheets and then manipulate it to generate charts showing not only the past performance of BMN in BTC and USD terms, but also a forecast of what BMN can accomplish until maturity (July 2024) given two parameters (expected annual evolution of Bitcoin's price and expected annual evolution of Bitcoin's network hashrate)

Next is an explanation of what each file is doing:

### pruebas.py

The data it needs to feed into the model is:

- Extract the network's hashrate up to the last date. I do this in pruebas.py extracting it from blockchain.com's API
- Extract bitcoin's price in USD also up to the last date. I also do it in pruebas.py extracting it from the same site
- Extract miner's revenue, in the same file and the same site, which then will allow me to calculate how many bitcoin's were generated in the past days.

In this file, in one of the functions I return a dataframe that contains all this data

### datos.py

In this file, I import that dataframe from pruebas.py and I store it in an excel file named DatosExcelMineria"+now+".xlsx where now is today's date.

The script selects the last file (where the now variable is equal to today) and then starts defining some variables that will be important for future calculations.

### frikada3.py

In this file we import everything from datos.py and there are several functions in it.

#### addRows

This function adds a lot of record to the dataframe we imported and in it, each of the new columns of the dataframe is a "scenario" for bitcoin's price and bitcoin's network hashrate evolution. So for example, bitcoinP10 is how the price of Bitcoin would evolve daily, if the price were to increase 10% annually. But each record is per day, so I have to translate 10% to an annual rate. Same for all other bitcoinP numbers up to 100% which would mean a 100% increase in one year and also for columns like HR10, HR20, etc... which are an expected evolution of the hashrate of respectively 10%, 20% annually, since the last date's network hash rate.

#### addMoreRows

This function adds more columns that are needed for the chart, like the accumulated bitcoin's mined which are a function of BMN's hashrate divided by the network's hashrate of each day. And of course we have to do it for each scenario (HR10, HR20, etc...)

#### addRowsCustom and addMoreRowsCustom

These two functions do the same than the previous two, but instead of assuming 10 scenarios for the network hashrate (10%, 20%, 30%...100%) and bitcoin price evolution (10%, 20%, 30%...100%), it expects two parameters from the user (price and hashrate) and then plots a custom chart accordingly

#### chartIt and ChartIt2

These two functions make use of the matplotlib library to plot the charts using the dataframes returned by the addRow functions

#### additional comment about frikada3

At the end of this file, a loop populates a table showing all expected returns in USD of BMN from now until the end of the period, for the 100 different scenarios (i.e. 10 for hashrates, and 10 for bitcoin's price)

### twittea.py and responseBot.py

This is were the project starts becoming a bit interactive.

twittea.py allows me to run all previous files, and then post the several charts to a test twitter account I have created (@mulokotests)
responseBot.py uses the addRowsCustom and addMoreRowsCustom functions as well as a new chartIt3 function, to respond to any tweet that would request a chart using the hashrate and price parameters for the expected evolution of the network's hashrate and bitcoin's price

## What this project is missing

### Hosting

First, all of this is hosted in my PC, so it only tweets and responds when I run the script in my computer. Of course this is not ideal because an investor will not be expecting to wait for me to sit in front of my computer. The twitter side of things can tweet once per day the more general charts. The respond side of things should be able to respond frequently, but not immediately. The part that should be able to respond any time would be any request from stokr or anyone consuming the API (I mention this below)

### Optimization

All the permanent storage is done in excel sheets. This means if this would get some traction, I don't know but I believe this is probably not very scalable, or maybe it is, but it's probably not the foundation on which we could build something that could work for different financial products on liquid

Of course, given that I'm a very amateurish python developer, I'm 100% certain there is a lot that can be done to improve the code and for example the renderization of the charts which is currently painfully slow, and I haven't figured out why

### API

Our partner stokr, asked me if we could serve the data if a user in their website would request an interaction using as parameters hashrate and price. They will build the frontend but we need to provide the API with the return of the data (I'm guessing JSON format). There are other parameters that they are asking for but we can start with these two. Ideally, this API should work for Stokr, for ourselves too, but also for any other party that could eventually provide information about this or any other financial product.

I think that one of the most fun thing about liquid assets is this kind of real time information that can be provided. Think e.g. of a tokenized renewable solar plant generating depending on data we can parse, and we could show the information about the money token holders were earning, etc... All these assets are very interactive if we build this kind of foundation properly.

What I'd like to know is if our team can help with these things that are missing, if there is anything else I can help with and if there is any estimated ETA for this to happen (not particularly urgent, except any API data we can show to Stokr)

