import itertools
import pandas as pd
import datetime as dt
from xirr.math import xirr
import goldenowl.asset.asset as at
import goldenowl.portfolio.holding as hd

class Portfolio:
    def __init__(self, aName, aAssetRatioList):
        self.m_name = aName;
        self.m_holdingMap={asset.getName(): hd.Holding(asset.getName(), asset) for asset, ratio in aAssetRatioList};
        self.m_assetRatioMap={asset.getName(): ratio for asset, ratio in aAssetRatioList}
        self.m_cashFlow = {};

    def rebalance(self, aDate):
        print('TODO');

    def addAmount(self, aAmount, aDate):
        norm_date = pd.to_datetime(aDate);
        for asset, ratio in self.m_assetRatioMap.items():
            self.m_holdingMap[asset].buyAmount(aAmount * ratio, aDate);
        self.m_cashFlow[norm_date] = aAmount;

    def removeAmount(self, aAmount, aDate):
        norm_date = pd.to_datetime(aDate);
        for asset, ratio in self.m_assetRatioMap.items():
            self.m_holdingMap[asset].sellAmount(aAmount * ratio, aDate);
        self.m_cashFlow[norm_date] = -aAmount;

    def getValue(self, aDate):
        value = 0;
        for asset, holding in self.m_holdingMap.items():
            value += holding.getValue(aDate);
        return value;
    
    def getXIRR(self, aDate):
        norm_date = pd.to_datetime(aDate);
        cash_flow =self.m_cashFlow;
        filtered = dict(itertools.filterfalse(lambda i:i[0] > norm_date, cash_flow.items()))
        final_val = self.getValue(aDate);
        if (norm_date in filtered.keys()):
            filtered[norm_date]-= final_val;
        else:
            filtered[norm_date]= -final_val;
        return xirr(filtered)


#Free floating functions below

def getSIPReturn(aInstrRatioList, aSipFreq, aRebalanceFreq, aStart, aEnd):
    print('TODO');



