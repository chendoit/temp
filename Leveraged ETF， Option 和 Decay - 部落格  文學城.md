---
created: 2025-01-20T23:57:25 (UTC +08:00)
tags: []
source: https://blog.wenxuecity.com/myblog/14140/201411/2910.html
author: 
---

# Leveraged ETF， Option 和 Decay - 部落格 | 文學城

> ## Excerpt
> 如果我们承认BlackScholes的假设，那么所有衍生合同（derviative)的价格，包括LeveragedETF和Option，必须遵守下面的BlackScholes微分方程。在上面这方程里，V是衍生和同的价格，S是原来underlyingasset的价格，sigma...

---
如果我們承認Black Scholes的假設，那麼所有衍生合同（derviative)的價格，包括Leveraged ETF和Option，必須遵守下面的 Black Scholes 微分方程。

![](http://upload.wikimedia.org/math/5/e/f/5ef2fa747d3a5d684ae67bdc7236e6d4.png)

在上面這方程裡，V 是衍生和同的價格， S 是原來underlying asset的價格，sigma 是 價格的volatility，r 是利率， t 是時間。為了簡單起見，我們假設利率為0，那麼這方程就簡化為：

dV/dt = -(1/2) \* sigma^2 \* S^2 \* d^2V/dS^2.

注意 dV/dt 就是 theta --- decay，而價格二階導 d^2V/dS^2 就是 gamma, 於是我們得出：

decay = -0.5 \* volatility平方 \* 價格平方 \* gamma.

這個公式給出了衍生合同decay的標準計算，它是對所有衍生和同，包括leveraged etf和期權，都成立。

在這裡特別看一下JNUG, 假設GDXJ的價格是x, JNUG的價格是y, 做為三倍leveraged的etf, 我們有：

dy/y = 3 \* dx/x.

解上述簡單常微分方程， 我們有 y = C \* x^3， 這裡 C>0 是一常數。在此我們可以看到 JNUG 的價格和 GDXJ 的價格不是線性關係，而是3次方關係，這就說明 y 對 x 的二階導是大於 0 的，用 trader 的語言就是 long gamma. 從上面 Black Scholes 公式可以看出 decay 的存在。

一般講 long gamma 必然要付 decay， 這在理論上是公平的， 但一般散戶由於種種原因不能充分利用 gamma 使得 gamma 白白浪費同時要付 decay，這樣長期持有leveraged etf變成一個頭疼的事。關於如何從期權， leveraged etf種提取 gamma value， 以後有時間再吹吧。
