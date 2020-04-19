---
title: "在Mac環境上搭建使用GitHub pages之環境"
header:
  teaser: /assets/images/.png
categories:
  - Tutorials
tags:
  - Mac
  - Github pages
  - Jekyll
toc_label: "Outline"
---

## 1. Install Git
到[git的官網](https://git-scm.com/download/mac)上進行安裝，安裝的方法選擇使用Homebrew來完成，基本上照著網站上的流程進行即可完成安裝。
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"  
brew install git
```

## 2. Install Jekyll
### 2.1. Prepare Ruby
Mac 中其實是自帶Ruby的，但是我們在github page中因為需要搭配Jekyll主題的關係，需要Ruby 2.4以上的版本，不是新的Mac可能會因為版本過舊而導致Jekyll無法安裝成功。所以在這邊我們要先進行Ruby的版本更新。
對Ruby更新，我們需要先安裝`rvm`（Ruby Version Manager）,是Ruby版本管理器，包括Ruby的版本管理和Gem庫管理(gemset)。安裝指令如下：
```
curl -L get.rvm.io | bash -s stable
```
待其完成後，以以下指令測試是否成功：
```
source ~/.bashrc  
source ~/.bash_profile
rvm -v
```
![](fig01)

接著，使用以下檢查Ruby版本：
```
ruby -v
# ruby 2.3
rvm list known
```
最後進行安裝：
```
rvm install 2.4
```

如果報出以下錯誤
```
Error running 'env GEM_HOME=/Users/stella/.rvm/gems/ruby-2.3.8@global GEM_PATH= /Users/stella/.rvm/rubies/ruby-2.3.8/bin/ruby -d /Users/stella/.rvm/src/rubygems-3.0.8/setup.rb --no-document',
please read /Users/stella/.rvm/log/1587178056_ruby-2.3.8/rubygems.install.log
```
則有可能是缺少openssl，這時可以透過以下指令獲取rvm中的必要套件，並安裝openssl：
```
rvm autolibs rvm_pkg
rvm pkg install openssl
rvm reinstall all --force
```
之後重新輸入安裝指令
```
rvm install 2.4
```

### 2.2. Prepare Bundle
Bundle為安裝Jekyll的重要套件，因為他可以管理Ruby gem的相依套件之外，也避免Jekyll在build時報錯或是運行環境上錯誤的機會。利用以下指令即可安裝：
```
gem install bundler
```

### 2.3. Install Jekyll
終於，在以上步驟成功後，就能夠來完成Jekyll了。
```
gem install jekyll bundler
```

## 3. GitHub pages
在GitHub上建立好要給自己的pages部落格運用的專案後，clone到本機上，就可以在相同的路徑上，於終端機中利用以下命令運行部落格的本機端預覽模式：
```

```


https://stackoverflow.com/questions/15129355/ruby-2-0-rails-gem-install-error-cannot-load-such-file-openssl
https://stackoverflow.com/questions/15236490/ruby-gem-install-not-working-gem-path
https://jekyllrb.com/docs/
https://blog.csdn.net/weixin_39718665/article/details/78142515
https://www.jianshu.com/p/d99b5662d8a0
https://hellogithub2014.github.io/2017/09/16/github-pages-jekyll-setup-step/