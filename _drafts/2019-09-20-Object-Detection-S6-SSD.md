---
title: "[Object Detection] S6: SSD 簡介"
header:
  teaser: /assets/images/.png
categories:
  - object detection
  - deep learning
tags:
  - SSD
toc_label: "Outline"
---

## 前言
在two-stage模型中，雖然發展到了Faster R-CNN利用兩個網路來進行物件偵測已經相當成熟，但是網路的架構龐大、構造複雜，運算時間也是難以達到真正的real-time運用。而SSD作為一個在2016年發表的相當經典的one-stage模型，一樣透過一個一條龍的完成物件的分類和定位。他用的方法也是吸收了類似Faster R-CNN中anchor的概念，名叫default box來處理邊界框的問題，也使用了影像金字塔的概念來運用不同尺度的feature maps，讓網路對於不同尺度的特徵都能夠有所考量。

論文：  
[SSD: Single Shot MultiBox Detector](https://link.springer.com/chapter/10.1007/978-3-319-46448-0_2)  


## 演算法架構  
作為one-stage模型，SSD以VGG-16為整個模型的主幹，在不同尺度的feature maps下進行辨識的工作，這樣的機制被稱為pyramidal feature hierarchy。整個網路架構如下圖所示
![SSD stucture](/assets/images/SSD_structure.png)
*SSD overview*  
{: .text-center}  

從VGG-16的conv4_3之後，以38x38x512開始，每次降維之後的feature maps都會用來做detection用，就像圖中的分支所示。每一個支線，都會有各自的detection和classifier. 在SSD中，共有6條支線來處理不同尺度。隨著維度的降低，所處理的物體在影像中所佔有的比例是由小到大。  
接著，就是如何將這些支線用來處理邊界框的問題了

### Default box  
SSD中的default box就如論文中的圖中所示：

![SSD default box](/assets/images/SSD_default_box.png)  
*default box*
{: .text-center}

看起來就和anchor非常像。SSD設定了不同的default box的比例。以圖中為例，比例就有三種。而如果你看到*SSD overview*這張圖，就可以發現每個階段的比例有4, 6, 6, 6, 4, 4種。你可以針對想辨識的物體類型給予不同數量的比例。SDD在中間幾個feature map都給了6種比例來辨識，就是因為對於一般的物體在影像中的占比會是以中間這三層的尺度最為多數。

### Detector  
取出了feature map之後，SSD會讓它先通過一次3x3的convolution來得到真正用來作為detector的神經層。而convolution的深度就是和剛剛default box有關。若假定default box數量是D，而目標類別有C個類別，邊界框有4個值，所以深度的計算就是等於Dx(4+C)。  

![](/assets/images/SSD_paper02.png)

我們可以將這個map在深度上Dx(4+C)，拆成邊界框的定位(localization)和分類(Classification)，如下圖所示。SSD透過localization來調整

![](/assets/images/SSD_detector.png)
{: .full}  









### Training   

## 結論  

這是我個人對這篇論文的消化，如果有錯誤之處，請各位朋友指教或幫我指出  
如果喜歡這篇文章，記得在下面幫我按個Recommend↓  
謝謝～















