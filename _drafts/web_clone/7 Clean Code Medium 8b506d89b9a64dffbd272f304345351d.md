# 第 7 章 錯誤處理 | Clean Code - 手寫筆記 - Medium

[https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/error-handling-6132b22fe5c2](https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/error-handling-6132b22fe5c2)

![1*RijhIwu_gn98_W_QnYcGAA.jpeg](7%20Clean%20Code%20Medium%208b506d89b9a64dffbd272f304345351d/1RijhIwu_gn98_W_QnYcGAA.jpeg)

```
🔖 文章索引1. 使用例外事件而非回傳錯誤碼
2. 在開頭時就寫下 try-except-finally 的敘述
3. 包裝第三方函示庫可能拋出的例外事件
4. 定義正常的程式流程
5. 不要傳遞 null (空值)
```

我們需要撰寫錯誤處理的原因是，如果程式發生異常時，仍需要讓程式碼做它該做的事情。但是，散亂的錯誤處理程式碼，反而會導致我們不意理解程式碼真正的意圖，會模糊了程式碼原本的邏輯。

# **使用例外事件而非回傳錯誤碼**

寫程式一定會碰到需要例外處理的情況，有時候我們會選擇定義不同的訊息 FLAG 處理例外，但是一旦 FLAG 越來越多，而且不斷得使用巢狀 if-else 的方式抓取錯誤，程式碼看起來就越來越雜亂。

```python
class ExperimentController:
    ...
    def start_experiment(self):
        status = self.get_status()
        if status  ExperimentHandler.STOP:
            experiment = self.experiment_worker.run()
            if experiment.get_status() != EXPERIMENT_ERROR:
                experiment.close()
            else:
                logging.error("Experiment error. Unable to run.")
        else:
            logging.error("Experiment didn't run.")
    ...
```

因此，作者不建議使用 FLAG 來處理例外的情況，而是**使用例外事件的方式，讓程式偵測到錯誤時，可以主動拋出例外**。

```python
class ExperimentController:
    ...
    def start_experiment(self):
        try:
            self._run_experiment()
        except ExperimentError as e:
            logging.error(e)

    def _run_experiment(self):
        self.experiment_worker.run()
        self.experiment_worker.close()

class ExperimentWorker:
    ...
    def run(self):
        ...
        raise ExperimentError("Experiment didn't run.")
```

使用例外事件寫程式碼是不是看起來乾淨許多呢？這也是在 [🔗 **第 3 章 函式**](https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/functions-3663c2ca9c16)所說的「**只做一件事情**」，這樣拆分後，每個函式可以更加專注於做自己的事情，在閱讀與維護上更容易。

# **在開頭時就寫下 try-except-finally 的敘述**

**👉STEP 1.** 寫下一個單元測試程式碼，當讀取不到檔案時，程式會丟出一個 SomeCoolError 的例外事件：

```python
class ReaderTest(unittest.TestCase):
    def setUp(self):
        self.reader = Reader()

    def test_read_file(self):
        with self.assertRaises(SomeCoolError):
            self.reader.read_file()

if __name__ == "__main__":
    unittest.main()
```

👉 **STEP 2.** 先寫下一個可以提供測試的 stub：

```python
class Reader:
    def read_file(self):
        data = []
        return data
```

我們的測試失敗了，因為程式並沒有如預期般丟出 SomeCoolError。

👉 **STEP 3.** 接著改寫程式碼，讓程式碼可以如預期般丟出例外事件：

```python
class Reader:
    def read_file(self):
        try:
            data = []
            with open("./somefile.txt", "r") as inputfile:
                data = inputfile.read()
        except Exception as e:
            print("Some cool error {}.".format(e))
            raise SomeCoolError("Some cool error {}.".format(e))
            
        return data
```

👉 **STEP 4.** 這次成功讓程式碼丟出例外事件，通過了測試。現在，我們可以精煉程式碼，讓程式家取實際上被 `read()` 丟出的 FileNotFoundError。

```python
class Reader:
    def read_file(self):
        try:
            data = []
            with open("./somefile.txt", "r") as inputfile:
                data = inputfile.read()
        except FileNotFoundError as e:
            raise SomeCoolError("Some cool error {}.".format(e))

        return data
```

> 以上 4 個步驟是作者在書中提出「如何利用測試驅動開發 (TDD) 建構我們需要的例外處理邏輯」，只要按照以上的 TDD 流程，其餘的邏輯也可以用相似的方式進行開發。

# **包裝第三方函示庫可能拋出的例外事件**

你一定曾經使用過第三方的函式庫，而且有可能曾經遇到必須處理第三方函式庫會丟出的例外事件。除了基本的程式邏輯之外，我們還必須建構處理例外的邏輯，讓程式碼變得更加複雜。

```python
URL = "..."
try:
    page = requests.get(URL).text
except HTTPError as e:
    report_error(e)
    logging.error(e)
except ConnectionError as e:
    report_error(e)
    logging.error(e)
except Timeout as e:
    report_error(e)
    logging.error(e)
finally:
    ...
```

作者在 [🔗 **第 3 章 函式](https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/functions-3663c2ca9c16)** 就有提到**一個函式必須專注做一件事情**，如果要遇到需要處理多種例外時，解決辦法是「**抓取例外事件共同繼承的類別**」。

你可以從 [🔗 requests 的文件](https://2.python-requests.org/en/master/_modules/requests/exceptions/) 中看到 HTTPError、ConnectionError、Timeout 都是繼承 RequestException，所以我們便能夠使用 RequestException 這個例外事件。

```python
uri = "..."
request = RequestPage(uri)

try:
    request.get()
except RequestException as e;
    report_error(e)
    logging.error(e)
finally:
    ...
```

至於第三方函式庫的例外事件，在抓到特定的例外事件後，便可以直接丟出，讓上一層的程式抓到共同的例外事件。

```python
class RequestPage:
    def __init__(self, uri):
        self.uri = uri

    def get(self):
        try:
            page = requests.get(self.uri).text
        except HTTPError as e:
            raise RequestException(e)
        except ConnectionError as e:
            raise RequestException(e)
        except Timeout as e:
            raise RequestException(e)
```

# **定義正常的程式流程**

> 不要把例外事件當作 if-else 使用。

假設有一個市長被質詢，一般來說，市長會自行思考並經過思考後憑藉自身的專業能力回答問題 (HanResponse)；但是，當他無法回答該問題時，總不能不處理的這情況，所以他也許會拋出例外事件，讓專家幫他回答問題。

# **實作一般的例外處理**

我們可以看到程式碼中如果 `HanResponse.search()` 經過搜尋後，無法找到問題的解答，`get_response()` 拋出了一個例外事件 AnswerNotFoundError，轉而使用另一個函式 `get_response_from_experts()` 讓其他專家回答問題。

```python
try:
    han_response = HanResponse.search(question)
    response = han_response.get_response()
except AnswerNotFoundError:
    response = get_response_from_experts()
```

但是這樣的實作方法會需要額外維護 `get_response_from_experts()` ，而且讓程式碼看起來更複雜，用例外事件當作 if-else 不是一個好的方法。

> Uncle Bob：「如果我們不需要處理例外的情況，那不是更好嗎？」

有一個非常實用的 Design Pattern 可以解決這問題，接下來我們用舉例讓大家了解 **Special Case Pattern (特殊情況模式)**。

# **Special Case Pattern (特殊情況模式)**

![https://miro.medium.com/max/649/1*mfo5VCKJVpoKnYW9UtiKFQ.png](https://miro.medium.com/max/649/1*mfo5VCKJVpoKnYW9UtiKFQ.png)

Special Case Pattern 也就是除了一般情況的物件之外，建立一個 Special Case 的物件專門處理例外的情況。

當我們用到 Special Case Pattern 時，經常會使用**工廠模式 (Factory Pattern)** ，讓工廠中的物件繼承同一個抽象類別，並且可以額外傳遞 **Special Case** 的物件。

我們先來看看經過重構後的程式碼，是不是看起來更簡短扼要呢？

```python
response_factory = ResponseFactory.search(question)
response = response_factory.get_response()
```

> 範例取自 🔗 Design Patterns — Null Object Pattern

![https://miro.medium.com/max/9694/1*Lydcd8ofLXS7duKQil-AeA.jpeg](https://miro.medium.com/max/9694/1*Lydcd8ofLXS7duKQil-AeA.jpeg)

如果你是使用 Python 實作的話，也許會用到 ABC 這個內建的函式庫，因為 Python 沒有提供抽象的修飾子，所以我們只能用繼承跟 decorator 宣告抽象類別跟抽象方法。

> 如果想知道工廠內部實作可以參考「[不要傳遞 null (空值)](https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/error-handling-6132b22fe5c2#4891)」的內容。

以下是實作 HanResponse 與 ExpertResponse 的範例程式：

```python
from abc import ABC, abstractmethod

class AbstractResponse(ABC):
    @abstractmethod
    def get_response(self):
        pass

class HanResponse(AbstractResponse):
    def __init__(self, question):
        self.response = question

    def get_response(self):
        return "Han Response."

class ExpertResponse(AbstractResponse):
    def __init__(self, question):
        self.response = self.search(question)

    def get_response(self):
        return self.response
    
    def search(self):
        ...
```

# **不要傳遞 null (空值)**

這一點與前面所提到的「定義正常的程式流程」有些類似，作者提醒「不斷地檢查 null 是在增加自己的工作量，也是讓需要用到這段程式碼的人找麻煩」。況且，如果一時忘記檢查，後果將會不堪設想。

```python
def get_customer(name):
    if name is not None:
        customer_storage = get_customer_storage()
        if customer_storage is not None:
            customer = customer_storage.get_customer(name)
            print("Customer ", customer)
```

為了解決這種情況便是使用上述的 **Special Case Pattern (特殊情況模式)** ，可以選擇回傳一個 Null Object，又稱作是 **Null Object Pattern**。

# **Null Object Pattern**

> 範例取自 🔗 Design Patterns — Null Object Pattern

![https://miro.medium.com/max/9694/1*W-JhOhHrDpq-0tgf5BMIHA.jpeg](https://miro.medium.com/max/9694/1*W-JhOhHrDpq-0tgf5BMIHA.jpeg)

**👉 STEP 1**：建立抽象類別 AbstractCustomer，並且讓物件共同繼承這個類別，限定所有類別都必須實作在抽象類別中的抽象方法。因此，如同前一章節，所有類別都有同樣的方法。

```python
from abc import ABC, abstractmethod

class AbstractCustomer(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def is_none(self):
        pass

class RealCustomer(AbstractCustomer):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_none(self):
        return False

class NullCustomer(AbstractCustomer):
    def get_name(self):
        return "Not Available in Customer Database"

    def is_none(self):
        return True
```

**👉 STEP 2**：我們建立一座工廠，讓工廠找不到名字時回傳 **Null Object**。

```python
from Customer import RealCustomer, NullCustomer

class CustomerFactory:
    def __init__(self):
        self.names = ["Rob", "Joe", "Julie"]
    
    def get_customer(self, customer_name):
        for name in self.names:
            if name == customer_name:
                return RealCustomer(name)
        return NullCustomer()
```

**👉 STEP 3**：使用 Special Case Pattern 的好處就是，儘管我們查詢的名字不存在，但是回傳的物件同樣繼承 AbstractCustomer，所以最後能夠呼叫同樣名稱的函式。

```python
from CustomerFactory import CustomerFactory

customer_factory = CustomerFactory()
customer_1 = customer_factory.get_customer("Rob")
customer_2 = customer_factory.get_customer("Henry")
customer_3 = customer_factory.get_customer("Julie")
customer_4 = customer_factory.get_customer("Peter")

print("Customer 1: ", customer_1.get_name())
print("Customer 2: ", customer_2.get_name())
print("Customer 3: ", customer_3.get_name())
print("Customer 4: ", customer_4.get_name())
```

我們看到儘管查詢的 Henry 與 Peter 都不在 Customer 的資料庫中，但是仍然可以使用 `get_name()` ，因此我們就不用寫額外的程式碼判斷 Null 的情況。

```
Customer 1:  Rob
Customer 2:  Not Available in Customer Database
Customer 3:  Julie
Customer 4:  Not Available in Customer Database
```

# **小結**

我們在錯誤處理這個章節學到不少知識，知道了在處理例外事件時盡量不要回傳錯誤碼，因為一旦錯誤碼越來越多，我們得花費更多的成本維護它。

此外，我們經由一個 TDD 的範例學習如何從零開始定義個例外處理的程式，藉由 3 個步驟就能夠完成單元測試與主程式。

> 在 🔗 [第 9 章 — 單元測試](https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/unit-tests-ecc8ed18d583) 的章節，會針對測試有更多的說明。

當你使用第三方的函式庫時，經常會遇到需要處理第三方函式庫所拋出的例外事件，但是我們不想讓程式碼過度髒亂，可以藉由封裝「例外事件共同繼承的類別」讓程式碼簡明扼要。

最後，我們學到了 Special Case Pattern 以及 Null Object Pattern，兩者都能夠讓我們不用處理例外的情況，讓程式碼的可讀性更高，而且更容易維護。

# **✋ 延伸閱讀**

**[第 8 章 邊界| Clean Code**邊界是一個交戰非常猛烈的區域。不論是依賴第三方的軟體，或是面對未知的邊界，一不小心，就有可能讓戰火一發不可收拾。 我們必須控管這些邊界，所以我們需要使用最少量的程式碼將它們封裝起來，把邊界隔離出來，把主導權放在我們能夠控制的程式上。medium.com](https://medium.com/%E6%89%8B%E5%AF%AB%E7%AD%86%E8%A8%98/boundaries-774cae00dfbd)