---
title: "[物件偵測] S8: Feature Pyramid Networks 簡介"
header:
  teaser: /assets/images/FPN_02and03.png
categories:
  - object detection
  - deep learning
tags:
  - Image Pyramid
toc_label: "Outline"
---
## 前言
不同的物體或他們的特徵在不同的影像上或是在影像中的大小(或尺度)都有所不同，所以當我們在進行影像的工作時，只在單一個尺度下進行影像處裡或是特徵提取，往往會是不夠的。因此，影像金字塔一直都是解決不同尺度的問題時常用的手段。而在深度學習基底上的物件偵測模型，要實際運用或參加競賽時，往往也都倚賴將整個模型與影像金字塔的概念結合，來創造更好、更全面的表現。今天我們就來介紹這些物件偵測模型是如何結合影像金字塔的概念，以及他們的優缺點在哪裡，最後提到目前泛用的好方法—Feature Pyramid Networks。  

論文：  
[Feature pyramid networks for object detection](https://medium.com/r/?url=http%3A%2F%2Fopenaccess.thecvf.com%2Fcontent_cvpr_2017%2Fhtml%2FLin_Feature_Pyramid_Networks_CVPR_2017_paper.html)  

## 演進
在這篇論文中，首先就列出四種運用影像金字塔概念的方式，而(d)就是這篇論文所要提出的方法。而Fig-01中，藍色的框框代表的就是feature map，不過框線的粗細代表著feature map特徵的級別，越粗者代表其特徵含意的層級越高。下面我們就一一來簡介這四種方式。  

![](/assets/images/FPN_01.png)  
*Fig-01*{: style="color: gray; font-size: 80%"}  
{: .text-center}

### (a) Feature Image Pyramid  
在影像辨識和物件偵測的應用上，最初都是使用Fig-01中的(a)方式進行。當不同尺寸的影像被抽取出特徵圖譜後，這些不同尺度下的特徵圖譜所構成的金字塔，在本篇中被稱作Featurized Image Pyramid。於是這樣就可以在不同尺度上的特徵進行分類、辨識、追蹤等的工作。這種方式多用在早期影像的特徵仍以人工標記的時代。然而，這樣子的做法等同於重複做了幾次辨識的工作，多了好幾倍作業量，因此要對不同尺度的特徵有充分掌握的話，所需的時間非常久。  

### (b) Single Feature Map  
圖1b的邏輯，是指模型只在最後一個feature map上才進行預測或是其他工作。在這篇論文提出來以前，大部分在ImageNet或是COCO等影像辨識競賽中出色的那些知名CNN或是物件偵測模型，都是依照這樣的邏輯設計的。但是這樣就缺乏了考量其他尺度下的feature map，所以他們在大賽上依然使用了影像金字塔的概念，仿照(a)圖的方式來將網路於不同尺度的輸入影像進行訓練。這些網路都證明，套用了Featurized Image Pyramid的話會獲得較好的表現，但是因為這樣計算量太大耗時太久，所以一般的應用下不太可能進行這麼浩大的工程。  

### (c) Pyramidal Feature Hierarchy  
將CNN進行卷積和降維過程中所產出的不同尺度的feature map用來做預測，神似原本的影像金字塔產生Featurized Image Pyramid的機制，被稱作Pyramidal Feature Hierarchy。而SSD網路是首先實現這種架構的網路。但是SSD只在的backbone VGG16的conv4_3層之後才開始利用在這之後的feature maps，而沒有使用到更前面較高解析度的feature maps。然而這些高解析度的feature maps 雖然特徵含意程度不高，卻對於小物體的檢測至關重要。因此雖然SSD這樣的設計並不會使得工作量大量增加且考慮到的feature maps較多元，但是還是有這樣不利辨識的一些缺點存在。  

### (d) Feature Pyramid Network (FPN)  
要充分利用CNN一路產生出知各階段的feature maps，又要讓金字塔中的每一個feature maps都有很強的特徵含意存在。因此，作者結合了top-down和skip-connection兩種概念，得到可以兼顧兩者的Feature Pyramid Network(FPN)。  

## 結構設計  
Top-dowm和skip-connection所組合起來得到的FPN網路架構是像下圖(Fig-02)，較高層級的feature map會回頭，upsampling後和低一個層級的feature map做相加，獲得新的 feature map。這樣的設計讓不同尺度上的特徵有了整合的效果。不過，FPN並不僅僅是在最後的feature map上進行預測(Fig-02(a))，而是在不同尺度的feature maps下都進行預測(Fig-02(b))。  

![](/assets/images/FPN_02and03.png)
*Fig-02*{: style="color: gray; font-size: 80%"}  
{: .text-center}  

而具體上在upsampling的過程是如何運算的，就由下圖(Fig-03)來說明。尺寸較小的feature map (P2)會先簡單的upsampling放大尺寸兩倍，就會與上一層feature map(C1)一樣size。這樣的架構其實很像FCN的segmentation在upsampling的過程，不過這裡的upsampling是單純的插值法，而非透過反卷積才進行。而C1會先經過1x1的conv.將深度調整成和P2一樣，再和P2做element-wise的相加。且在相加之後，會再通過3x3卷積，消除掉upsampling的副作用後，才作為最終要使用的feature map。  

![](/assets/images/FPN_04.png)
*Fig-03*{: style="color: gray; font-size: 80%"}  
{: .text-center}  

作者同時也分析了FPN加入的這些設計，在coco資料集上對於網路表現的影響，如下表。  

*Table-01. AR: Average Recall; s, m, l: 小中大物件。*{: style="color: gray; font-size: 80%"}  
![](/assets/images/FPN_tb01.png)  

- top-down設計：
這個比較案例是Table-01(d)，結構是參考Fig-01(b)。如果只有單向的bottom-up pyramid，因為各層的特徵含意層級落差太大。因此，你可以看到Fig-05中的(d)列只有在大物件上的偵測最好，就是因為這樣的設計只有在最高的幾層map上有足夠高級的特徵含意。
- Lateral connection：
這個比較案例是Table-01(e)，結構是參考Fig-01(c)。沒有側向連接的話，雖然因為top-down結構而可以使得feature maps都有很高程度的特徵含意和較細緻解析度，但會因為位置資訊隨著降採樣和上採樣的過程流失，導致位置精度變差。
- Pyramid representations：
這個比較案例是Table-01(f)，結構是參考Fig-02(a)。這點就是在測試只在最後一個featrue map上做anchor box detection還是在特徵金字塔的每一層都做，誰會比較好。結果顯示雖然這裡同時用了lateral connection和top-down結構，只在最後一個map上做detection雖然有比平均好的表現，但是在每一層map上都做的表現會更好。  

## 與物件偵測模型結合

![](/assets/images/FPN_05.png)
*Fig-04*{: style="color: gray; font-size: 80%"}  
{: .text-center}  

FPN這樣的設計，使得他可以很簡單地就與一般的影像辨識或是物件偵測中的CNN結合。而論文當中，FPN則是與Faster R-CNN結合，所以下面我們就針對這兩者的結合，來說明其中的關鍵就好。  
1. 首先，在Backbone網路的部分，作者使用ResNet50/101，所以有5個階段的residual block的Feature maps (C1～C5)輸出。然而，因為第一階段的C1尺寸太大，會占用太多運算資源，所以並沒有用來做FPN。  
2. 第二是RPN的部分。在[Faster R-CNN](https://yuweichiu.github.io/object%20detection/deep%20learning/Object-Detection-S3-Faster-R-CNN/)的簡介文章中，我們有提到RPN的架構，其初始的3×3卷積到一開始分成兩路的兩個1×1卷積，在論文中被稱作RPN的head。FPN中所有的feature map都會接上獨立的RPN head，去執行各自的RPN工作。而FPN的最後一個階段P5，還會再池化一次產生更粗糙的map P6，目的是為了可以提出更大的proposals使網路可以辨識影像中更大的物體。論文中有提到，其實各個層的RPN head是可以共用權重的，而且共用與不共用權重可以獲得相似的表現，代表各尺度feature maps之特徵層級都在相同的程度，再次映證FPN透過top-down和skip-connection來產生feature maps確實有效。  
3. 第三是anchor的部分。因為FPN本身已經代表著不同尺度下的feature maps，所以在設定anchor上，只需給定anchor的比例即可。  
不過，提出proposals的是P2～P6這些maps，但是他們提出的proposals，並不一定會在他們自身這層上獲得ROI。FPN的策略是利用下式來計算由\\(Pk_{0}\\)上提出的proposal若映射到輸入影像尺寸下的寬、高為w, h之ROI，則應該取自於feature map \\(P_k\\)：  

\\[k=\lfloor k_0+\log_{2}{(\sqrt{wh}/224)} \rfloor \\]
*Eq-01*{: style="color: gray; font-size: 80%"}  
{: .text-center}  

上式中，分母224就是ImageNet預訓練時的輸入影像大小。舉例來說，若今天是由P4提出proposal，則k＝4。若proposals映射到原圖上的尺寸w×h是112×112，則帶入Eq-01中簡單計算一下，就可以得到k=3。代表此proposals要在P3上取出ROI。  

下表是展示一下論文中所列出的一些FPN應用在Fast R-CNN中的差別。可以看到不管是在Table-01還是下表。FPN都可以比傳統的設計有很突出的進步。就是源自於各層級、各尺度的特徵良好地融合。  

*Table-02*{: style="color: gray; font-size: 80%"}  
![](/assets/images/FPN_tb02.png)
*Table-03*{: style="color: gray; font-size: 80%"}  
![](/assets/images/FPN_tb03.png)  

## 總結
FPN整個設計和論證，算是已經為長久以來物件偵測模型在不同尺度和層級的特徵圖譜無法良好連接或混合，而導致在面對不同尺度的物體辨識上或多或少有缺陷的情況，提出了全面的方法來改良。所以至此，物件偵測的整個模型架構基本上算是挺成熟的，應該不會太快有很大的變動了。不過FPN的設計，雖然是妥善利用backbone網路一路產生的特徵圖譜來產生特徵金字塔，但是，經過上面的介紹，可想而知，整個模型的計算量依舊是很沉重的。因此，後續也開始提出了一些改善效率的方式，然而他們的概念都還是圍繞著FPN的核心打轉，FPN的重要性可見一斑。  
這是我個人對這篇論文的消化，如果有錯誤之處，請各位朋友指教或幫我指出。  
如果喜歡這篇文章，記得在下面幫我按Recommand ↓  
謝謝～