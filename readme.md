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

シンボリックリンクの作成
---------

WidnowsXP

```
fsutil hardlink create "%HOME%\_vimrc" "%HOME%\dotfiles\_vimrc"
fsutil hardlink create "%HOME%\_gvimrc" "%HOME%\dotfiles\_gvimrc"

linkd "%HOME%vimfiles" "%HOME%\dotfiles\vimfiles"
```

WidnowsVista Windows7

```
使ってない・・・
```

Mac,Linux

```
ln -s ~/dotfiles/vimfiles ~/vimfiles
ln -s ~/dotfiles/_vimrc ~/.vimrc
ln -s ~/dotfiles/_gvimrc ~/.gvimrc
ln -s ~/dotfiles/_bashrc ~/.bashrc
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

