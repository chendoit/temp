---
created: 2025-01-19T23:38:06 (UTC +08:00)
tags: [options skew,implied volatility skew.]
source: https://marketchameleon.com/Learn/Skew
author: 
---

# 波動率偏度 |學習期權交易 --- Volatility Skew | Learn Options Trading

> ## Excerpt
> Volatility skew refers to the fact that implied volatility is higher for OTM options strike prices than ATM prices for a given expiration date.  This is often referred to as a volatility "smile" due to the convex shape it creates when plotted on a chart.

---
## Option Volatility Skew

Skew is the implied volatility disparity between different strike prices within the same expiration. In some cases, implied volatility is relatively equal along all strikes in an expiration, which is referred to as a "straight skew" or a "flat skew". However, this is not common. Market forces dictate that some strikes get bid up to higher volatilities, while others sold lower.  
偏斜是同一到期日內不同執行價格之間的隱含波動率差異。 在某些情況下， 到期日所有行使價的隱含波動率相對相等，這被稱為“直線偏斜”或 一個 「flat skew」。。但是，這並不常見。市場力量決定了一些行權價的出價會提高到更高的波動性， 而其他的售價較低。

On a typical volatility skew, downside strikes have higher implied volatility, because historically stocks tend to fall with much greater speed and magnitude. Drops in stock prices go along with increased uncertainty in the market. Conversely, on upside strikes, the implied volatility is typically lower, as markets tend to go up in a more steady, constrained way.  
在典型的波動率偏度中，下行權價具有更高的隱含波動率，因為從歷史上看，股票往往會下跌很多 更快的速度和幅度。股價下跌伴隨著市場不確定性的增加。相反，在上行權價上， 隱含波動率通常較低，因為市場往往以更穩定、更受限制的方式上漲。

## Measuring Skew  測量偏移

Skew can be measured in many ways. In many places throughout our site, we refer to skew as it relates to the at-the-money strike volatility (ATM Volatility). We compare the volatility for a downside put strike, usually the 25-Delta put (or the closest strike to the 25-Delta) to the ATM Volatiltiy, as well as an upside call strike (the 25-Delta or closest).  
偏移可以通過多種方式進行測量。在我們網站的許多地方，我們提到 skew 是因為它與 平價行使價波動率 （ATM Volatility）。我們比較下行看跌期權行權價的波動性，通常是 25-Delta 看跌期權（或最接近 25-Delta 的行權價）到 ATM 波動率，以及上行看漲期權行權價（25-Delta 或最接近的行權價）。

If a 25-Delta put skew is indicated as being +25.0%, that means the volatility on that strike is 25% higher than the volatility on the ATM strike. Likewise for the call. A 25-Delta call skew of -20.0% is 20% lower than the ATM volatility.  
如果 25-Delta 看跌期權偏度顯示為 +25.0%，則意味著該行權價的波動率比 ATM 罷工的波動性。電話也是如此。-20.0% 的 25-Delta 看漲期權偏度比 ATM 波動率低 20%。

## Example  例

The example below is pulled from a recent expiration in SPY \[[SPY Option Chain](https://marketchameleon.com/Overview/SPY/OptionChain/)\]. We've highlighted the out-of-the-money 25-Delta put and the out-of-the-money 25-Delta call, as well as the at-the-money strike. You can see the difference in Implied Volatility (IV) from the downside, which is 20.5 Vol, to the at-the-money, which is 17.3 Vol, to the upside at 14.1 Vol.  
下面的示例是從 SPY \[[SPY 期權鏈](https://marketchameleon.com/Overview/SPY/OptionChain/)\] 中最近的到期中提取的。我們突出顯示了 價外 25-Delta 看跌期權和價外 25-Delta 看漲期權，以及平價行權價。您可以在隱含波動率 （IV） 中看到差異 從下行的 20.5 Vol 到平價的 17.3 Vol，再到上行的 14.1 Vol。

![An example of Volatility Skew for SPY](https://marketchameleon.com/Images/Learn/Skew%20Example%20Table.png "An example of Volatility Skew for SPY")

## Skew Over Time  隨時間傾斜

To benchmark the skew for a stock over time, we record these values for all expirations and calculate a corresponding 30-Day Constant Maturity Skew. These values are calculated to always be looking 30 days ahead, at the 25-Delta put strike and 25-Delta call strike, so that changes in stock price, ATM volatility, or time left until expiration are normalized.  
為了對股票隨時間變化的偏度進行基準測試，我們記錄所有到期日的這些值並計算相應的 30 天恆定到期日偏度。這些值的計算始終展望未來 30 天，在 25-Delta 看跌期權行使價和 25-Delta 看漲期權行權價，以便股票價格、ATM 波動性或距離到期的剩餘時間的變化正常化。

By comparing the current 30-Day Constant Maturity Skew to historical values, we can know whether the market is shifting in a bearish or bullish trend. When 25-Delta put skew moves from being +10.0% historically to being +15.0% currently, that would indicate that the markets are more bearish than usual, as traders are paying a higher relative premium for the expectation of a downside move.  
通過將當前的 30 天恆定到期偏斜與歷史值進行比較，我們可以了解市場是否正在發生變化 處於看跌或看漲趨勢中。當 25-Delta 看跌偏斜從歷史上的 +10.0% 變為目前的 +15.0% 時， 這表明市場比平時更加看跌，因為交易員為 預期下行走勢。

## How to Use Skew  如何使用 Skew

These are but a few of the many ways to use skew when analyzing the markets:  
這些只是在分析市場時使用 skew 的眾多方法中的一小部分：

-   Some investors may just want to know if markets are feeling more bearish or bullish. What are markets forecasting vs. average historical levels?  
    一些投資者可能只想知道市場是感覺更加看跌還是看漲。市場預測與歷史平均水平的對比如何？
-   Some investors may take the other side of the bet, hoping that the skew reverts to historical averages.  
    一些投資者可能會押注的另一方，希望偏度恢復到歷史平均水準。
-   Others may compare the skew of all stocks within some peer group and trade one security's skew versus another.  
    其他人可能會比較某個同行組內所有股票的偏度，並交易一種證券的偏度與另一種證券的偏度。
