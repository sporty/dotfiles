dotfiles セットアップ方法
================================================

前準備
---------

* sshの設定
  
* Windowsの場合はCurlを用意する(https://github.com/gmarik/vundle/wiki/Vundle-for-Windows)


git clone
---------

```
git clone https://sporty@github.com/sporty/dotfiles.git ~/dotfiles
cd ~/dotfiles
git submodule init
git submodule update
```

自動初期設定
---------

WidnowsXP

```
~/dotfiles/setup_xp.bat
```

WidnowsVista Windows7

```
未実装
```

Mac

```
~/dotfiles/setup_mac.sh
```

Linux

```
未実装
```

Vundle
---------

```
:BundleInstall
```

関連情報
=================

* http://d.hatena.ne.jp/holypp/20110515/1305443997
* http://d.hatena.ne.jp/holypp/20110516/1305552171

