import itertools
import pandas as pd
import datetime as dt
from xirr.math import xirr
import goldenowl.asset.asset as at
import goldenowl.portfolio.holding as hd

class Portfolio:
    def __init__(self, aName, aAssetRatioList):
        self.m_name = aName;
        self.m_holdingMap={asset.getName(), hd.Holding(asset.getName(), asset) for asset, ratio in aAssetRatioList};
        self.m_AssetRatioMap={asset.getName(),  ratio for asset, ratio in aAssetRatioList}

    def rebalance(self, aDate):

    def addAmount(self, aAmount):

    def removeAmount(self, aAmount):

    def getValue(self, aDate):
    
    def getXIRR(self, aDate):


#Free floating functions below

def getSIPReturn(aInstrRatioMap, aSipFreq, aRebalanceFreq, aStart, aEnd):



