# 第 9 章 單元測試| Clean Code - 手寫筆記 - Medium

[https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/unit-tests-ecc8ed18d583](https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/unit-tests-ecc8ed18d583)

![1*m7u0ruDgIXFU6Aj1mID4oQ.jpeg](9%20Clean%20Code%20Medium%20352bedb6e5b542629193faebe745e678/1m7u0ruDgIXFU6Aj1mID4oQ.jpeg)

```
🔖 文章索引1. TDD 的三大法則
2. 特定領域的測試語言
3. 一個測試一個概念 & 一個測試應該儘可能減少 Assert
4. F.I.R.S.T Principle
5. 小結
```

# **TDD 的三大法則**

**👉 步驟 1**：在撰寫一個單元測試 (測試失敗的單元測試) 前，不可以撰寫任何產品測試。

**👉 步驟 2**：只撰寫剛好無法通過的單元測試。

**👉 步驟 3**：只撰寫剛好能通過當前測試失敗的產品。

> 以上三個步驟可以將我們限制在一個約 30 秒的循環內。

另外，還有一項有些人誤解 TDD 是一個非常複雜的方法，其實 TDD 說白了只是「**測試程式和產品程式是一起被撰寫的，測試程式比產品程式早幾秒鐘寫而已。**」

如果想看實際範例的人可以看看 [🔗 第七章 — 錯誤處理](https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/error-handling-6132b22fe5c2) 的單元，文中有一個範例是*如何利用 TDD 撰寫一個測試錯誤處理的單元程式與主程式*。

我們使用 TDD 的方法開發軟體，長期下來我們將會累積數以千計的測試程式，數量足以跟開發軟體的程式碼匹敵。如果不擅加控管，將會徒增無法維護的程式碼。

# **測試跟產品一樣重要**

想像一個伐木工只專注於如何比昨天砍更多的樹木，而忽略保養斧頭，隨著一天又一天的過去，斧頭越來越鈍，儘管伐木工花費更多的時間與更多的精力伐木，但是砍的數量只會越來越少，效率越來越差。

單元測試就像是那把斧頭，如果不善加維護，測試的技術債越堆越高，相對的產品的品質也會漸漸地崩解。我們在撰寫單元測試時，必須確保測試與產品一樣是可以擴充、可讀的。

Uncle Bob:「什麼是一個整潔的測試？三件事，可讀性，可讀性，還是可讀性。」

> 延伸閱讀：🔗 AcceptanceTestPatterns Build Operate Check。

---

# **特定領域的測試語言**

我們平常在寫單元測試的時候，經常需要做很多的**前置作業**，如下方的例子中，我們想要測試一個爬蟲應用的函式，就得先寫不少的程式碼。但是，**前置作業太多的話，反而不容易專注在單元測試上**。

```python
class CrawlerTest(unittest.TestCase):
    def test_get_weather_forecast(self):
        weather_forecast_uri = "https://www.cwb.gov.tw/V7/forecast/taiwan/Taipei_City.htm"
        html = requests.get(weather_forecast_uri)
        html.encoding = 'utf8'
        weather_page = BeautifulSoup(html.text, "html.parser")
        weather_section = weather_page.find(id="ContainerInOne")
        todoy_and_tomorrow_forecast_table = weather_section.find(class_="FcstBoxTable01")

        expected_time = get_weather_forecast_time(forecast_table)
        time_pattern = r'[\u4e00-\u9fa5] \d+/\d+ \d+:\d+~\d+/\d+ \d+:\d+'
        for time in expected_time:
            self.assertRegex(time, time_pattern)
            
        expected_temperature = get_weather_forecast_temperature(forecast_table)
        temperature_pattern = r'\d+ ~ \d+'
        for temperature in expected_temperature:
            self.assertRegex(temperature, temperature_pattern)
```

因此，有時候我們可以不使用主程式提供的 API，而是撰寫單元測試才用得到的 API，作者稱它為「**特定領域的測試語言**」。

我們將前置作業包裝起來，比較上下兩個例子，下方的例子是不是更容易瞭解測試在描述什麼？

```python
class CrawlerTest(unittest.TestCase):
    def test_get_weather_forecast(self):
        forecast_table = get_taipei_forecast_weather_page()

        expected_time = get_weather_forecast_time(forecast_table)
        time_pattern = r'[\u4e00-\u9fa5] \d+/\d+ \d+:\d+~\d+/\d+ \d+:\d+'
        for time in expected_time:
            self.assertRegex(time, time_pattern)

        expected_temperature = get_weather_forecast_temperature(forecast_table)
        temperature_pattern = r'\d+ ~ \d+'
        for temperature in expected_temperature:
            self.assertRegex(temperature, temperature_pattern)
```

---

# **一個測試一個概念 & 一個測試應該儘可能減少 Assert**

在撰寫單元測試的函式後，想想還能夠如何改進，還記得 [🔗 第 3 章 — 函式](https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/functions-3663c2ca9c16)說得嗎？「**一個函式只能做一件事**」，單元測試同樣是一個函式。因此，盡可能的讓單元測試只包含一個概念，並且盡可能減少 Assert。

```python
class CrawlerTest(unittest.TestCase):
    def test_get_weather_forecast_time(self):
        forecast_table = get_taipei_forecast_weather_page()

        expected = get_weather_forecast_time(forecast_table)
        time_pattern = r'[\u4e00-\u9fa5] \d+/\d+ \d+:\d+~\d+/\d+ \d+:\d+'
        for time in expected:
            self.assertRegex(time, time_pattern)

    def test_get_weather_forecast_temperature(self):
        forecast_table = get_taipei_forecast_weather_page()

        expected = get_weather_forecast_temperature(forecast_table)
        temperature_pattern = r'\d+ ~ \d+'
        for temperature in expected:
            self.assertRegex(temperature, temperature_pattern)
```

但是，單元測試最重要的還是**可讀性**，如果你在寫單元測試的時候，覺得有些測試中包含數個 Assert 也能夠清楚表達測試的意義，這樣做也是可以的。

---

# **F.I.R.S.T Principle**

如果你在網路上搜尋「F.I.R.S.T」，應該可以搜尋到兩種不同的結果，主要差別在於最後的 T 有兩種解釋 (**T**horough / Timely)，在這邊兩種解釋都採用，因為它們的解釋都有它們的道理。

**F**ast**：測試執行的速度要越快越好**，沒有一個工程師會喜歡執行需要 20 秒的測試；而且，雖著系統越來越龐大，測試越來越多，如果測試執行速度夠快，工程師更能夠不厭其煩地跑測試。

**I**ndependent：**不要讓一個測試高度相依其他測試**，如果這麼做的話，一個測試一旦 failure，其他相依的測試也會 failure，將無法輕易地使用測試找出問題。

**R**epeatable：**測試應該要能夠在任何環境下都能夠成功執行**，不能夠因為網路、作業系統，甚至是不同的日期而導致測試失敗。

**S**elf-validating：**測試應該要輸出 Boolean，讓人能夠分辨哪些測試通過與沒通過**。作者在書中提到的這點，現今有許多 IDE 都已經能夠輔助做到這一點，例如 vscode 便能夠顯示通過與沒通過的單元測試。

![https://miro.medium.com/max/1016/0*Y43UaT2UiL7ZtoRy.png](https://miro.medium.com/max/1016/0*Y43UaT2UiL7ZtoRy.png)

取自 [Python unit testing in Visual Studio Code](https://code.visualstudio.com/docs/python/unit-testing)

**T**horough：**測試不應該只追求涵蓋率 100%，更應該追求測盡所有的使用情境**。包括 boundary value、數量龐大的資料集、資安、大數、例外處理與非預期的函數數量或輸入。

**T**imely：**測試應該要在產品程式之前撰寫**，也就是測試驅動開發 (TDD)，如果能夠維持在 TDD 的循環結束後，持續地通過單元測試，我們就能確保程式碼的行為一直是正確的。

> 延伸閱讀： 🔗 Test F.I.R.S.T、 🔗 第二種 F.I.R.S.T

# **小結**

在這個章節，作者主要希望我們能夠讓單元測試的可讀性愈高愈好，因為單元測試與產品一樣重要，兩者是互相牽制的存在。

再者，為了提高單元測試的可讀性，我們可以撰寫特定領域的程式語言、盡量讓單元測試只做一件事，以及盡量只使用一個 assert 等技巧。

最後，作者讓我們知道什麼是 F.I.R.S.T 原則，F.I.R.S.T 讓我們能夠井然有序的撰寫有品質的單元測試。

# **✋ 延伸閱讀**

**[第 10 章 類別 | Clean Code**根據 Uncle Bob 整理的 SOLID 原則撰寫程式，包括單一職責原則 (SRP)、開放封閉原則 (OCP)、里氏替換原則 (LSP)、接口遠離原則 (ISP) 與依賴反轉原則 (DIP)，我們容易開發出易維護與擴展的系統。medium.com](https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/%E7%AC%AC-10-%E7%AB%A0-%E9%A1%9E%E5%88%A5-clean-code-1c7898d11cd7)