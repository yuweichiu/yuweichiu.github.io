---
title: "[SQL]001-基本語法Create, Select, Insert, Drop, Update, Delete"
header:
  teaser: 
categories:
  - Programming
tags:
  - SQL
toc_label: "Outline"
toc_sticky: true
---

> 這系列文章，會建立在使用IBM cloud上的database，database操作介面的部分可能會因為database系統不同而有所不同。


# 1. 連線到Database

---

本篇文章所使用的是IBM系統，且後續的指令下達基本上都透過python直接下達，所以在jupyter notebook中要執行之前，需先安裝一些套件：**ibm_db**, **ibm_db_sa** and **ipython-sql**，直接在terminal中用`pip`安裝即可。

安裝完成後，依照[這篇文章的做法](https://www.notion.so/yuweichiu/jupyter-notebook-IBM-cloud-cb4ed8938c724bdd88391b200cefb7ed#3c17b5cc16c642f08f8742e41532a569)，利用magic方式進行連線。

```python
# 載入sql套件
%load_ext sql

# 建立連線
%sql ibm_db_sa://fsv20059:rjpg%5Et45fb7w4w80@dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net:50000/BLUDB

>>>'Connected: fsv20059@BLUDB'
```

如果你知道你在jupyter中的一個cell裡會完全使用sql的語法的話，可以在開頭處使用`%%sql`即可。但如此你在該cell中便完全不能下達python語句。

# 2. 在database中建立資料表

---

假定今天要新建一個資料表table名叫INSTRUCTOR，我們必須要確認database中是否已經存在同樣名稱的資料表。如果有的話，而且該表並不重要可以捨棄，我們便可以在進行SQL練習之前，先把舊的給丟棄drop。

```python
%sql drop table INSTRUCTOR
# If this cell raises error, it means that you do not have the table named INSTRUCTOR in your database
```

確認之後，便可以開始建立我們要的新資料表。

建立新資料表的時候，我們必須先賦予其中每一欄的資料型態，嚴謹的資料型態定義有助於資料庫的資源利用、運算速度，以及後續的處理。

```sql
create table TABLE_NAME (
    col1 int NOT NULL,
    col2 char(2),
    col3 varchar(60),
    PRIMARY KEY (ID)
    );
```

以下列舉常用的資料型態

- `INTERGER` for interger.
- `VARCHAR(n)` for strings with variable length below n.
- `CHAR(n)` for a character string of a fixed length n.
- `DATE` for a date-type data like YYYY-MM-DD.

`NOT NULL` 可以指定該欄資料不可以有缺值，否則無法新增。

`PRIMARY KEY ()` 是指資料表中通常會有一個或多個資料行包含可唯一識別資料表中每個資料列的值。 此資料行稱為資料表的主索引鍵，也就是index，強制資料表具有實體完整性。 主索引鍵條件約束保證唯一的資料，因此通常是定義在識別欄位上。  

>可參考：  
>[主要與外部索引鍵條件約束 - SQL Server](https://docs.microsoft.com/zh-tw/sql/relational-databases/tables/primary-and-foreign-key-constraints?view=sql-server-ver15)

以下我們就建立名叫INSTRUCTOR的資料表，並用select指令展示：

```sql
%%sql
CREATE TABLE INSTRUCTOR
  (ins_id INTEGER PRIMARY KEY NOT NULL, 
   lastname VARCHAR(15) NOT NULL, 
   firstname VARCHAR(15) NOT NULL, 
   city VARCHAR(15), 
   country CHAR(2)
  );

-- show the INSTRUCTOR
select * from INSTRUCTOR
```

Output:
```sql
ins_id	lastname	firstname	city	country
```

因為資料表僅被初始化定義，尚未有資料，所以只會秀出各個欄的名稱。

# 3. 插入資料到資料表中

使用 `INSERT`指令

插入資料到單一資料表中的指令如下
```sql
%%sql
--- Insert a row of data into table:
INSERT INTO INSTRUCTOR VALUES (1, 'Ahuja', 'Rav', 'Toronto', 'CA');

--- Insert few row of data into the table:
INSERT INTO INSTRUCTOR
    VALUES
    (2, 'Chong', 'Raul', 'Toronto', 'CA'),
    (3, 'Vasudevan', 'Hima', 'Chicago', 'US')
    ;

select * from INSTRUCTOR
```

Output:
```sql
		ins_id	    lastname	   firstname	      city	   country
0	        1	       Ahuja	         Rav	   Toronto	        CA
1	        2	       Chong	        Raul	   Toronto	        CA
2	        3	   Vasudevan	        Hima	   Chicago	        US
```

# 4. 選取資料表中的資料

使用 `SELECT`指令

- Select the specific columns

```sql
%sql select lastname, firstname from INSTRUCTOR
```

```sql
		lastname	   firstname
0	       Ahuja	         Rav
1	       Chong	        Raul
2	   Vasudevan	        Hima
```

- Assign the condition to selection by clause `WHERE`

```sql
%sql select lastname, firstname from INSTRUCTOR where country='CA'
```

```sql
		lastname	   firstname
0	       Ahuja	         Rav
1	       Chong	        Raul
```

# 5. Change data in the table

使用指令 `UPDATE`與 `SET`

```sql
%sql update INSTRUCTOR set city='Markham' where ins_id=1
%sql select * from INSTRUCTOR
```

```sql
		ins_id	    lastname	   firstname	      city	   country
0	        1	       Ahuja	         Rav	   Markham	        CA
1	        2	       Chong	        Raul	   Toronto	        CA
2	        3	   Vasudevan	        Hima	   Chicago	        US
```

# 6. Delete data in the table

使用`DELETE`指令

```sql
%sql DELETE FROM INSTRUCTOR where ins_id=2
%sql select * from INSTRUCTOR
```

```sql
		ins_id	    lastname	   firstname	      city	   country
0	        1	       Ahuja	         Rav	   Markham	        CA
1	        3	   Vasudevan	        Hima	   Chicago	        US
```

Source: https://www.coursera.org/learn/sql-data-science