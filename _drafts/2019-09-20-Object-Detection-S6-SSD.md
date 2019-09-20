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
作為one-stage模型，SSD以VGG-16為整個模型的主幹，在不同尺度的feature maps下進行辨識的工作。所以這次我會分做default box的部分和辨識兩部分來探討。

### Backbone

![Darknet-19網路架構圖](/assets/images/yolov2_darknet19.png)  
*Darknet-19*
{: .text-center}


### Anchor  

### Feature map   

## 結論  

這是我個人對這篇論文的消化，如果有錯誤之處，請各位朋友指教或幫我指出  
如果喜歡這篇文章，記得在下面幫我按個Recommend↓  
謝謝～















