import itertools
import math
import pandas as pd
import datetime as dt

class Asset:
    def __init__(self, aName, aOHLC):
        self.m_name = aName;
        self.m_priceMap = aOHLC;
        self.m_priceMap['PrevClose'] = self.m_priceMap['Close'].shift(1)
        self.m_priceMap.fillna(-1, inplace=True);
        self.m_priceMap.loc[self.m_priceMap['PrevClose'] == -1, ['PrevClose']] = self.m_priceMap[self.m_priceMap['PrevClose'] == -1].Close
        self.m_priceMap.loc[self.m_priceMap['Open'] == 0, ['Open']] = self.m_priceMap[self.m_priceMap['Open'] == 0].PrevClose
        self.m_priceMap.loc[self.m_priceMap['Low'] == 0, ['Low']] = self.m_priceMap[self.m_priceMap['Low'] == 0].Close
        self.m_priceMap['High'] =self.m_priceMap[['Open','High','Low','Close']].max(axis=1)
        self.m_priceMap['Low'] =self.m_priceMap[['Open','High','Low','Close']].min(axis=1)

    def getName(self):
        return self.m_name;

    def getValue(self, aDate):
        norm_date = pd.to_datetime(aDate);
        date_set = set(self.m_priceMap.Date);
        min_date = min(date_set);
        if (norm_date < min_date):
            return 0;
        while not(norm_date in date_set) and norm_date > min_date: 
            norm_date-= dt.timedelta(days=1);
        return list(self.m_priceMap[self.m_priceMap.Date == norm_date].Close)[0]

    def _get_diffTimeFrame(self, timeframe):
        ohlc_dict = {'Open':'first', 'High':'max', 'Low':'min', 'Close': 'last'}
        if (timeframe =='1D'):
            result = self.m_priceMap[['Date','Open','High','Low','Close']];
            result =result.set_index('Date');
        else:
            result = self.m_priceMap.resample(timeframe, on='Date').apply(ohlc_dict)
        return result;

    def getReturnsTimeFrame(self, aTf):
        diff_tf = self._get_diffTimeFrame(aTf);
        diff_tf['Returns%'] = (diff_tf['Close'] -diff_tf['Open'])/diff_tf['Open'];
        return diff_tf['Returns%'];

    def getRangeTimeFrame(self, aTf):
        diff_tf = self._get_diffTimeFrame(aTf);
        diff_tf['Range'] = (diff_tf['High'] - diff_tf['Low']);
        return diff_tf['Range'];

