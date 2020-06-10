# 第 10 章 類別 | Clean Code - 手寫筆記 - Medium

[https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/%E7%AC%AC-10-%E7%AB%A0-%E9%A1%9E%E5%88%A5-clean-code-1c7898d11cd7](https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/%E7%AC%AC-10-%E7%AB%A0-%E9%A1%9E%E5%88%A5-clean-code-1c7898d11cd7)

![1*QSyHwBs_GKKTEqKkL8l6kA.jpeg](10%20Clean%20Code%20Medium%20d5d0074e54f747229ad4ad923b9a776d/1QSyHwBs_GKKTEqKkL8l6kA.jpeg)

Photo by [Annie Spratt](https://unsplash.com/@anniespratt?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/office?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

```
🔖 文章索引1. 內聚力 (Cohesion)
2. 單一職責原則 (Single Responsibility Principle, SRP)
3. 開放封閉原則 (Open-Close principle, OCP)
4. 里氏替換原則 (Liskov substitution principle, LSP)
5. 接口遠離原則 (Interface segregation principle, ISP)
6. 依賴反轉原則 (Dependency inversion principle, DIP)
```

# **內聚力 (Cohesion)**

> Cohesion 在書中翻譯為凝聚性，因此你在看書時也許會疑惑，而內聚力比較常見，因此在這邊使用內聚力一詞。

一個類別中應該只有少量的實體變數，類別的方法都應該要操縱一個或多個屬於該類別中的變數。

如果一個函式操縱越多該類別的實體變數，則該函式的內聚力就越高。更進一步來說，所有函式操縱該類別的實體變數越多，這個類別的內聚力就越高。

![https://miro.medium.com/max/829/1*r0seM_lb7pN_wN-l_vvUmg.png](https://miro.medium.com/max/829/1*r0seM_lb7pN_wN-l_vvUmg.png)

# **單一職責原則 (Single Responsibility Principle, SRP)**

> A class should only have a single responsibility, that is, only changes to one part of the software’s specification should be able to affect the specification of the class.

# **類別要夠簡短**

與 [🔗 第 3 章 — 函式](https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/functions-3663c2ca9c16) 所說的一樣，儘量讓類別夠簡短。也許你曾經聽過或是已經知道物件導向的 SOLID 原則，其中就說到「讓一個類別只有一個職責」，稱作**單一職責原則 (Single Responsibility Principle, SRP)。**

# **如何確定一個類別符合單一職責？**

你可以檢查類別的名稱與類別內部做的事情是否一致，同樣可以使用第 3 章說的「是否在同個層級」來做判定。

此外，在不使用「if」、「and」、「or」、「but」等字眼的情況下，應該要能夠用 25 個字詞內描述一個類別做的事情。

---

# **開放封閉原則 (Open-Close principle, OCP)**

> Software entities … should be open for extension, but closed for modification.

大家應該都有過類似的經驗，在開發軟體時非常容易，但是遇到需要**修改**程式碼就讓人捏一把冷汗。儘管像是在 [🔗 第 9 章 — 單元測試](https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/unit-tests-ecc8ed18d583) 說的「有了測試就不怕修改程式」，但是就怕 Test Case 在設計時想得不夠周全，總是在上線後才發現忘記撰寫某些使用情境的單元測試。

# **修改具有封閉性**

如果程式碼之間有高度相依，這種情況稱作「高耦合性」，修改 A 的程式碼，B 也要跟著一起修改，改完以後，結果 C 又發生錯誤，這是我們最不願意遇到的事情。

因此，開放封閉原則 (OCP) 提倡**修改程式碼應該要具有封閉性**，不會牽一髮動全身，讓我們能夠更專注於單一個組件內的程式碼。

# **擴充具有開放性**

與上述同樣的情況，假設程式碼之間高度相依，我們很難專注於擴充新的程式碼，會因為「高耦合性」不斷思考會不會發生「改了 A，B 也要跟著一起改」的情況。

所以，我們應該在儘可能不改動原始的程式碼的條件下，擴充新的功能。

以下的連結有提供很好的實作，如果想知道詳細違反 OCP 的程式碼，以及如何改善，不妨可以看看文章中的範例。

**[開放封閉原則 Open-Closed Principle (OCP)**軟體實體(類別,模組,函式等等) 應該是可以擴展的，但不能被修改medium.com](https://medium.com/@f40507777/%E9%96%8B%E6%94%BE%E5%B0%81%E9%96%89%E5%8E%9F%E5%89%87-open-closed-principle-31d61f9d37a5)

---

# **里氏替換原則 (Liskov substitution principle, LSP)**

> Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program

里氏替換原則 (LSP) 是專注在「**行為**」而不是「**繼承**」上的原則，行為也就是函式內部的程式碼做的事情，我們要確保在繼承時，盡管 override 部分的程式碼，也能夠讓子類別與副類別的行為兼容。

![https://miro.medium.com/max/303/1*WHF0tNTAfeTwXZeuuh5t2A.png](https://miro.medium.com/max/303/1*WHF0tNTAfeTwXZeuuh5t2A.png)

舉一個違反 LSP 例子，我們現在有兩個類別 Rectangle 與 Square，繼承的關係如上圖所示，Square 會繼承 Rectangle。

```python
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

class Square(Rectangle):
    def set_width(self, new_width):
        self.width = self.height = new_width

    def set_height(self, new_height):
        self.height = self.width = new_height
```

我們會說 Square 是 Rectangle 的一種，但是我們可以發現 Square 的不同之處在於「Square 的長跟寬一定相等」。因此，我們對它們撰寫了一個單元測試，希望它們能夠在 Override 的情況下，不會影響到其他行為。

```python
class TestShape(unittest.TestCase):
    def test_get_rectangle_area(self):
        width = 4
        height = 5
        rectangle = Rectangle()
        rectangle.set_width(width)
        rectangle.set_height(height)

        self.assertEqual(20, rectangle.get_area())

    def test_get_square_area(self):
        width = 4
        height = 5
        square = Square()
        square.set_width(width)
        square.set_height(height)

        self.assertEqual(20, square.get_area())
```

我們在撰寫這段單元測試時，就知道它們不會通過，因為 Rectangle 和 Square 設定 width 跟 height 是不一樣的行為，所以計算面積自然會得出不同的結果。

這兩個 class 的繼承關係違反了里氏替換原則 (LSP)，因為 LSP 就是在說**如果 Override 部份的行為，應該要以不牽動其他行為為目標進行開發。**

我們在使用「繼承」時，重要的是重複使用 (reuse) 已經寫好的行為，而不是將所有繼承的行為全部覆蓋。

# 

# **接口遠離原則 (Interface segregation principle, ISP)**

> Many client-specific interfaces are better than one general-purpose interface.

一個介面不應該提供過多的方法，因為，不是所有的客戶都想要實作所有的方法。

我們來看一個例子，一般來說，大眾認為政治家 (Politician) 會做 4 件事，分別為 **1️⃣ 提出政見 2️⃣ 拜票 3️⃣ 辯論 4️⃣ 工作勤勞**。但是，並非所有政治家都會做以上 4 件事情，例如：在實作政治家介面時，有些政治家不會實作 `working_hard()`，因此就會發生**空實作**的可能性。

![https://miro.medium.com/max/1094/1*4wTR-7UaT3tIcAeW4dpxNg.png](https://miro.medium.com/max/1094/1*4wTR-7UaT3tIcAeW4dpxNg.png)

所以，如果要符合**接口遠離原則**，可以建立多種的介面，讓需要實作的類別再進行實作即可。

![https://miro.medium.com/max/1094/1*MNzrRPakXHuIL7ZLzPFmDA.png](https://miro.medium.com/max/1094/1*MNzrRPakXHuIL7ZLzPFmDA.png)

# **依賴反轉原則 (Dependency inversion principle, DIP)**

> One should “depend upon abstractions, [not] concretions.”

依賴反轉簡單來說就是「」。

# **隔離修改**

![https://miro.medium.com/max/753/1*kqvNDmCd_4jDFH56p11Cqw.png](https://miro.medium.com/max/753/1*kqvNDmCd_4jDFH56p11Cqw.png)

這是一種常見的情況，我們經常會依賴於第三方的套件，但是依賴的套件不應該直接寫死在程式碼中，而是儘量解開與主程式之間的耦合性，例如我們可以將第三方套件用參數的方式傳入建構子，如此以來就可以動態地修改所使用的第三方套件。

而且，我們甚至可以更進一步使用 Adapter Pattern 將第三方套件與主程式隔離。當第三方套件被修改時，我們可以隔離修改封裝第三方套件的程式碼，因此不會動到其他的程式碼，也就將原本的依賴反轉成非依賴的情況。

```python
class WeatherBot:
    def __init__(self, weather_api):
        self.weather_api = weather_api

    def get_weather(self, city):
        return self.weather_api.get_weather(city)
```

# **單元測試**

如果現在想要對 Weather Bot 進行測試，要注意的是第三方 API 的部份，我們不能讓 API 隨時都有可能改變回傳的數值，例如 weather API 回傳的結果通常會隨時間而改變，這樣我們會非常難以撰寫單元測試。

因此，我們可以在實作時，傳入一個會回傳固定數值的 `weather_api_stub`，讓 Weather 不要高度相依於固定的 API，如此一來就能降低 API 和 WeatherBot 的耦合性。

> 延伸閱讀：🔗 [從被動變主動 — 依賴反轉](https://ithelp.ithome.com.tw/articles/10191603)

---

# **小結**

如果根據 Uncle Bob 整理的 SOLID 原則撰寫程式，包括 **1️⃣ 單一職責原則 (SRP)、 2️⃣ 開放封閉原則 (OCP)、 3️⃣ 里氏替換原則 (LSP)、 4️⃣ 接口遠離原則 (ISP) 與 5️⃣ 依賴反轉原則 (DIP)**，我們容易開發出易維護與擴展的系統。

但是在這個章節中，作者有只有稍微提到 SRP 以及 OCP 原則，其他 3 個原則都沒有詳細介紹，我想藉此了解其他 3 個作者提到的原則。因此，除了書中的內容之外，另外在網路上蒐集資料補充其他的 SOLID 原則，並且將書中的內容結合至其他 3 個沒提到原則中。

然而，因為在這篇文章中，大部份著重於 SOLID 原則，忽略了不少作者提及的優化方法。書中的內容更為豐富，作者提出更多如何優化程式碼的原則，並且帶有範例程式，更建議直接看書學習此章節。

# **參考資料**

- Clean Code 第 10 章 類別
- [http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod](http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod)
- [SOLID：五則皆變](http://teddy-chen-tw.blogspot.com/2014/04/solid.html)
- [設計模式五大基本原則 SOLID](http://www.andrewchen.tw/2017/04/09/20170409_NOTE_%E8%A8%AD%E8%A8%88%E6%A8%A1%E5%BC%8F%E4%BA%94%E5%A4%A7%E5%9F%BA%E6%9C%AC%E5%8E%9F%E5%89%87SOLID/)
- [我該學會SOLID嗎?](https://medium.com/@f40507777/%E6%88%91%E8%A9%B2%E5%AD%B8%E6%9C%83solid%E5%97%8E-4e73887c9156)
- [A simple example of the Open/Closed Principle](http://joelabrahamsson.com/a-simple-example-of-the-openclosed-principle/)
- [從合約判斷類別行為是否相容](http://teddy-chen-tw.blogspot.com/2017/02/blog-post.html)