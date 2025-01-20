---
created: 2025-01-20T23:46:19 (UTC +08:00)
tags: []
source: https://www.wenxuecity.com/blog/201507/14140/15671.html?utm_source=pocket_shared
author: 
---

# CME SKEW指數和CME VIX指數及它們的關係和使用 | www.wenxuecity.com

> ## Excerpt
> 您的位置：
      文學城
      » 部落格
      »CME SKEW指數和CME VIX指數及它們的關係和使用

---
您的位置： [文學城](https://wenxuecity.com/) » [部落格](https://blog.wenxuecity.com/) »CME SKEW指數和CME VIX指數及它們的關係和使用

2015-07-18 02:49:18

[![nj_guy](https://passport.wenxuecity.com/members/script/blogAvatar.php?uid=478140 "nj_guy")](https://passport.wenxuecity.com/members/index.php?act=profile&cid=nj_guy)

**CME SKEW指數和CME VIX指數及它們的關係和使用**  
 

這裡我們不做過多的數學討論，只簡單的從trading的角度去觀察。首先為方便起見做個約定：在這個帖子裡，除非特別指出，凡是談到期權，都是指OTM或ATM期權，如果有必要討論ITM期權，會特別指出。  
 

首先談一下大家熟悉的VIX指數，VIX指數是對所有的SPX PUT期權和SPX CALL期權進行加權平均得出。VIX更數學化的定義在我以前的Blog([**blog.wenxuecity.com/myblog/14140/201407/17403.html**](http://blog.wenxuecity.com/myblog/14140/201407/17403.html))裡有過較為深入的介紹，有興趣的可以自己看一下。從這裡大家可以看出，VIX代表整個期權的價格水平，無論是PUT期權還是CALL期權價格的上漲，都會使VIX升高。VIX有個重要的特性:它和underlying指數SPX有負correlation。從理論上講，對於其他的underlyer，比如外匯，黃金，石油等期權，可以定義類似指數，但這些指數和underlyer之間，並不一定具有負correlation，這是SPX期權特有的。

另一個重要的CME指數是SKEW指數，它的數學定義可以在這篇CME檔案的APPENDIX裡查到([**www.cboe.com/micro/skew/documents/SKEWwhitepaperjan2011.pdf**](https://www.cboe.com/micro/skew/documents/SKEWwhitepaperjan2011.pdf))。簡單的說它反應的是PUT期權和CALL期權價格的相對差，當指數為100時PUT期權和CALL期權之間價格平均上講一致，當PUT價格高於CALL價格時，SKEW指數會高於100.  
由於VIX和SPX指數的負相關性，PUT的價格高於CALL的價格，SKEW指數一般總會高於100，平均在115左右。如果市場上大量買入PUT，那麼PUT的價格會上漲，SKEW指數也會上漲，相反如果大量買入CALL，那麼CALL價格會上漲，SKEW指數會降低。注意SKEW指數放映的是PUT價格相對於CALL的價格，並不放映絕對價格。有些人會認為這和PUT  
CALL RATIO差不多，Well, Put Call Ratio是從Volume上觀察，SKEW指數是從價格比上觀察。

最後我們討論一下SKEW和VIX的關係，SKEW和VIX之間並沒有簡單的correlation關係，上面CME  
document裡也提到了這點。大家可以把VIX和SKEW畫在同一張圖上。但是SKEW和VIX的升降可以反應股票波動的不同階段:  
 

1.  VIX降，SKEW降。這一般表示SPX在上升期。Market對於期權，特別是PUT期權不感興趣。
2.  VIX低，但SKEW緩緩升高。這表示SPX接近頂部，Smart money在悄悄囤積PUT。當這種不一致到達一定水平，SPX就開始下行。
3.  VIX走高，SKEW也走高。這時SPX下行，Market恐慌。
4.  VIX高，但SKEW緩緩下降。這表示SPX接近底部，Smart Money在悄悄Sell PUT/Buy CALL準備反彈。

以上只是大致的關係，具體啥叫高，啥叫低，啥是臨界點，這些都要在實戰中自己總結，自己做spreadsheet估算。如果你想用，那你必須做進一步的統計研究，另外別忘了統計只反應歷史，並不一定代表將來。記住YMYD!
