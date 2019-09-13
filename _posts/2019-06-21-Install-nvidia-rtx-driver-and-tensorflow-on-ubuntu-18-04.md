---
title: "在Ubuntu 18.04 中安裝NVIDIA RTX系列顯示卡驅動程式與Tensorflow"
header:
  teaser: /assets/images/2019-06-21 18-28-31 的螢幕擷圖.png
categories:
  - installation
  - ubuntu
tags:
  - NVIDIA 
  - driver
  - Tensorflow
  - CUDA
toc_label: "Outline"
---

> 爬了一堆文，每一篇都有收穫！但是我實際用全新的Ubuntu 18.04，照著reference的文章來試試看時，卻還是不斷踩坑QQ。還好不斷努力之下終於試出一整套完整流程可以把這些事完成，在這邊做個紀錄！

## 軟硬體
### 硬體
* 裝置：MSI GE75 9SE
* GPU：Nvidia RTX 2060  

### 軟體需求：
* gcc
* make
* NVIDIA Driver
* CUDA 10.0
* cuDNN 7.6.0  


## Step 0. 基本軟體準備
去BIOS中把安全開機的選項關閉！  
而如果你的ubuntu是全新的  
記得先安裝gcc, make套件  
```
sudo apt install gcc
sudo apt install make
```  


## Step 1. 安裝NVIDIA Driver
就在我一直嘗試用.run檔來安裝nvidia驅動不斷失敗然後重裝系統好幾次到懷疑人生之後，在nvidia的討論區找到了一篇留言，它說：  
> 乖乖用ppa去抓ubuntu線上套件庫上有發行的NVIDIA驅動。  

我照著試。。。就成功啦！整個黑人問號我之前到底在幹麻Orz  
所以如果對Linux還不是很熟的朋友，就不要去用官網上的.run檔安裝了，會搞死身為新手的自己。乖乖照著以下這個方法安裝吧！  
直接在terminal中輸入以下指令：  
```
sudo apt-get purge nvidia* 
sudo add-apt-repository ppa:graphics-drivers/ppa 
sudo apt-get update
```  
完成之後，接著去**軟體與更新>額外驅動程式**  
![](/assets/images/2019-06-21 18-25-13 的螢幕擷圖.png)  

查看現有發行的NVIDIA驅動版本號（本文檔之當前版本為nvidia-driver-418)  
> 如果你沒有調整過這邊的設定  
照理來說你會看到選項試選在X.org那一項的！  
這邊就先不要更動選項  

然後就回到當前terminal輸入以下指令  
```
sudo apt-get install nvidia-driver-418
```
乖乖等它完成後用reboot重新啟動之後，在terminal中輸入  
```
nvidia-smi
# or
nvidia-settings
```  

觀察是否有正確選到NVIDIA顯示卡，你應該會看到下面兩張圖的樣子：  
![](/assets/images/2019-06-21 18-28-31 的螢幕擷圖.png)  

![](/assets/images/2019-06-21 18-29-21 的螢幕擷圖.png)  

如果都成功的話，恭喜你完成我遇到最艱難的一步！！！  


## Step 2. 安裝CUDA
到NVIDIA官網上下載對應版本的CUDA，CUDA的版本會根據tensorflow-gpu所對應的支援版本有所差異，而tensorflow-gpu 1.13.1的版本只支援到CUDA-10.0，所以本文使用10.0板，[官網連結](https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=deblocal)在此。  

![](/assets/images/2019-06-21 10-50-10 的螢幕擷圖.png)  

下載完成後，在目的地的資料夾中依照以下指令完成安裝:
```
sudo dpkg -i cuda-repo-ubuntu1804–10–0-local-10.0.130–410.48_1.0–1_amd64.deb
sudo apt-key add /var/cuda-repo-10–0-local-10.0.130–410.48/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda-toolkit-10–0
```  

記得如果有補釘包，也要接著把他們都裝完喔！接著設定系統變數，如果沒有文本編輯器，可以先安裝vim:
```
sudo apt install vim
```   
然後用vim來編輯 ~/.bashrc:
```
vim ~/.bashrc
```
然後到文件最下面按i鍵開始輸入:
```
export PATH=/usr/local/cuda-10.0/bin${PATH:+:$PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64:$LD_LIBRARY_PATH
```
完成以後，按esc退出編輯模式，然後輸入``:wq``儲存並離開vim。然後重新載入terminal的設定檔：
```
source ~/.bashrc
sudo ldconfig
```
最後輸入指令：
```
nvcc -V
```
如果出現以下字樣就是成功安裝CUDA:
```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005–2018 NVIDIA Corporation
Built on Sat_Aug_25_21:08:01_CDT_2018
Cuda compilation tools, release 10.0, V10.0.130
```
到此，CUDA的安裝就完成了！  


## Step 3. 安裝cuDNN 相應版本
到[這個網址](https://developer.nvidia.com/rdp/cudnn-download)登入後才可找尋對應版本進行下載。注意到，一定要下載CUDA對應版本得cuDNN，我們這邊既然使用CUDA 10.0，就下載有標記CUDA 10.0的cuDNN。選擇for Linux的下載包下載tar檔案：  

![](/assets/images/2019-06-21 10-55-13 的螢幕擷圖.png)  

開啟terminal並導引到下載的資料夾中，接著用以下指令解壓縮：
```
tar -xzvf cudnn-10.0-linux-x64-v7.6.0.64.tgz
```
接著在使用以下指令，來將cuDNN的檔案複製到CUDA中：
```
sudo cp cuda/include/cudnn.h /usr/local/cuda/include
sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*
```
至此，使用tensorflow-gpu的前製作業已全部完成，接著就來安裝它吧！   


## Step 4. 安裝tensorflow-gpu==1.13.1
※如果有虛擬環境的人，記得先激活虛擬環境再開始安裝！  
我們利用pip來安裝即可：
```
pip3 install tensorflow-gpu==1.13.1 
```
如果是用Anaconda的朋友，只好在這邊轉去其他厲害的前輩他們更好的教學文，只要版本對了，應該照著操作都不會有問題！  


## Step 5. 測試
最後，實際來run看看tensorflow，測時一下是不是安裝完成了！
```
python
import tensorflow as tf
hello = tf.constant(‘hello tensorflow’)
with tf.Session() as sess:
     sess.run(hello)
```
如果成功運行，輸出的結果會長這樣：
```
 ‘hello tensorflow’
```
到這裡，這篇紀錄文章就告一個段落了！   
下面的附錄有再紀錄我途中遇到的問題，如果有遇到一樣的朋友，希望能對你有幫助！  


## 附錄
※執行你的DNN程式時，若發生明明顯卡記憶體足夠，而cudnn啟動失敗，錯誤訊息如下：
```
Could not create cudnn handle: CUDNN_STATUS_INTERNAL_ERROR
```
試試看手動設定允許增加使用GPU記憶體，在你的程式碼中加入下面的設定：
```
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config, …)
```
※如果裝錯CUDA版本如何移除：
```
sudo apt-get  --purge remove cuda-X.Y
sudo apt autoremove
sudo apt update
```


## Reference
[How to install Nvidia drivers and cuda-10.0 for RTX 2080 Ti GPU on ubuntu-16.04/18.04](https://medium.com/@avinchintha/how-to-install-nvidia-drivers-and-cuda-10-0-for-rtx-2080-ti-gpu-on-ubuntu-16-04-18-04-ce32e4edf1c0?source=post_page-----6eb58a5da818----------------------)  

[Ubuntu 搭建深度學習開發環境 RTX 2080 + CUDA 10.0+cuDNN 7.4 + TensorFlow GPU r1.12 + nVIDIA docker](https://hackmd.io/@kcchien/BJzHPQdSN?type=view&source=post_page-----6eb58a5da818----------------------)  

[Using GPUs,TensorFlow Core,TensorFlow](https://www.tensorflow.org/guide/using_gpu?hl=zh_cn&source=post_page-----6eb58a5da818----------------------)  

