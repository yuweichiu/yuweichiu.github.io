# 第 4 章 註解 | Clean Code - 手寫筆記 - Medium

[https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/comments-6964cb2eef34](https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/comments-6964cb2eef34)

# 敏捷軟體開發技巧守則

[Airwaves](https://medium.com/@airwaves?source=post_page-----6964cb2eef34----------------------)

Follow

[Jun 8, 2019](https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/comments-6964cb2eef34?source=post_page-----6964cb2eef34----------------------) · 5 min read

Photo by [William Iven](https://unsplash.com/photos/gcsNOsPEXfs?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/technology?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

![https://miro.medium.com/max/5241/1*RlD_EebvaZt--pxPDmc0rQ.jpeg](https://miro.medium.com/max/5241/1*RlD_EebvaZt--pxPDmc0rQ.jpeg)

```
🔖 文章索引1. 註解無法彌補糟糕的程式碼
2. 有益的註解 - 法律型註解
3. 有益的註解 - 對意圖的解釋
4. 有益的註解 — docstring
5. 糟糕的註解 - 干擾型註解
6. 小結
```

# 不要替糟糕的程式碼寫註解 — 重寫它。

# **註解無法彌補糟糕的程式碼**

Uncle Bob：「**寫註解的其中一個動機，是因為程式碼寫的太糟糕**」。

如果我們有足夠的能力單純使用程式語言就能表達我們的意圖，那麼我們就不需要為程式碼加上註解。因為程式碼寫的函式、命名寫的太糟糕，無法輕易的了解程式撰寫者想表達的意圖，所以才需要花費額外的力氣撰寫註解。

# **你比較偏好哪一種 (書中範例)？**

> 作者其實是使用駝峰，不過我認為底線更容以閱讀，所以做了一點修改。

**👉 第 1 種：**

```
// Check to see if the employee is eligible for full benefits
if (employee.flags & HOURLY_FLAG) and (employee.age > 65)
```

**👉 第 2 種 ：**

```
if employee.is_eligible_for_full_benefits()
```

很明顯地，第 2 種方法透過**函式命名**更能夠清楚表達程式碼的意圖，不需再額外的為程式碼寫註解。

> 但是，我認為有時候在撰寫程式時，沒有必要為一件非常簡單的事情抽離原本的程式為一個新的函式，如果每一件事都必須這樣做，只會徒增閱讀上的痛苦 😥。

# **有益的註解 — 法律型註解**

你可以在大部份來自於公司或是組織的 **Open Source** 看過這樣子的資訊，在每個檔案的開頭都會寫入著作權聲名，這就是有益的註解。

例如，在 TensorFlow 的原始碼中我們可以看以下的著作權聲名：

![https://miro.medium.com/max/1280/1*hTw8YCMOxH6ZsCn_WEG-HA.png](https://miro.medium.com/max/1280/1*hTw8YCMOxH6ZsCn_WEG-HA.png)

[https://github.com/tensorflow/tensorflow/blob/master/configure.py](https://github.com/tensorflow/tensorflow/blob/master/configure.py)

# **有益的註解 — 對意圖的解釋**

如果沒辦法使用少量的單字為變數命名，或是用適當的動詞作為函式的命名，因此，就得用註解完整描述程式碼。換句話說，**如果可以透過命名解釋意圖，則不用註解解釋程式碼的意圖**。

**👉** **範例 1：**

![https://miro.medium.com/max/1571/1*hXVM8sI54Ks21sl3hSKsgA.png](https://miro.medium.com/max/1571/1*hXVM8sI54Ks21sl3hSKsgA.png)

[https://github.com/tensorflow/tensorflow/blob/master/configure.py#L57](https://github.com/tensorflow/tensorflow/blob/master/configure.py#L57)

**👉 範例 2：**

![https://miro.medium.com/max/1531/1*I9U5YU0mkoJ_pkrPceIBWQ.png](https://miro.medium.com/max/1531/1*I9U5YU0mkoJ_pkrPceIBWQ.png)

[https://github.com/tensorflow/tensorflow/blob/master/configure.py#L1006](https://github.com/tensorflow/tensorflow/blob/master/configure.py#L1006)

# **有益的註解 — docstring**

現今，有許多工具可以將 docstring 直接轉換成文件，當你在寫程式時，順帶把文件完成，不就是一件一舉兩得的事情嗎？

> 順帶一提，你可以使用 🛠sphinx 這個工具幫你自動轉換文件。

**Requests — Developer Interface**

![https://miro.medium.com/max/941/1*1RmSMo45AKRRxyF-HS6JXA.png](https://miro.medium.com/max/941/1*1RmSMo45AKRRxyF-HS6JXA.png)

[https://2.python-requests.org/en/master/api/](https://2.python-requests.org/en/master/api/)

**Requests — Source Code**

![https://miro.medium.com/max/1285/1*MYtdQ-_aoOMhJy85KeB-Iw.png](https://miro.medium.com/max/1285/1*MYtdQ-_aoOMhJy85KeB-Iw.png)

[https://github.com/kennethreitz/requests/blob/master/requests/api.py#L63](https://github.com/kennethreitz/requests/blob/master/requests/api.py#L63)

# **糟糕的註解 — 干擾型註解**

作者提到，有時候寫註解只是徒增干擾 ，尤其是 getter 與 setter 中容易出現這種情況。以下是 scrapy 中的一段程式碼，你認為哪一種比較好呢？

**👉 第 1 種 (resolver.py 的原始碼)：**

```python
def getHostByName(self, name, timeout=None):
    if name in dnscache:
        return defer.succeed(dnscache[name])
    # in Twisted<=16.6, getHostByName() is always called with
    # a default timeout of 60s (actually passed as (1, 3, 11, 45) tuple),
    # so the input argument above is simply overridden
    # to enforce Scrapy's DNS_TIMEOUT setting's value
    timeout = (self.timeout,)
    d = super(CachingThreadedResolver, self).getHostByName(name, timeout)
    if dnscache.limit:
        d.addCallback(self._cache_result, name)
    return d
```

[https://github.com/scrapy/scrapy/blob/master/scrapy/resolver.py#L16](https://github.com/scrapy/scrapy/blob/master/scrapy/resolver.py#L16)

**👉 第 2 種 (在 resolver.py 增加感擾型註解的程式碼)：**

```python
def getHostByName(self, name, timeout=None):
    """Get host by name
    
    Args:
      name: The name of the host.
      timeout: The timeout.
      
    Return:
      Return host by name.
      
    """
    if name in dnscache:
        return defer.succeed(dnscache[name])
    # in Twisted<=16.6, getHostByName() is always called with
    # a default timeout of 60s (actually passed as (1, 3, 11, 45) tuple),
    # so the input argument above is simply overridden
    # to enforce Scrapy's DNS_TIMEOUT setting's value
    timeout = (self.timeout,)
    d = super(CachingThreadedResolver, self).getHostByName(name, timeout)
    if dnscache.limit:
        d.addCallback(self._cache_result, name)
    return d
```

[https://github.com/scrapy/scrapy/blob/master/scrapy/resolver.py#L16](https://github.com/scrapy/scrapy/blob/master/scrapy/resolver.py#L16)

有沒有發現，在添加了沒必要的註解之後，第 2 種方法反而會讓程式碼看起來更複雜。因此，**如果一段註解對於理解程式碼沒有幫助，則沒必要為程式碼添加註解。**

# **小結**

大家都認為寫註解是很重要的一個環節，程式碼無法只用命名以及函式表達其目的時，就得撰寫註解幫助我們理解程式碼的邏輯。但是，如果程式碼本身就能清楚表達邏輯時，註解就不是必要的一環。

因此，我們可以用作者在本章節中提到的技巧檢查，是否註解都是有益的，或者只是干擾型的註解。

# **✋ 延伸閱讀**

**[第 5 章 — 編排 | Clean Code**程式編排就像是房子的內部裝潢，裝潢能夠直接影響人的心情，好的裝潢能夠讓人彷彿置身天堂，壞的裝潢讓人翻桌瘋狂。medium.com](https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/formatting-845cf3000416)