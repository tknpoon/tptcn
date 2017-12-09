#!/usr/bin/python

import pandas_datareader.data as web

ticker='^HSI'
source='yahoo'
start='01/01/1990'
end='01/01/2018'

qthsbc = web.DataReader(ticker, source, start, end)
print qthsbc.head()
print qthsbc.tail()
