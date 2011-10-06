================================================
dotfiles
================================================

セットアップ方法
==================

前準備
---------

- sshの設定
  
- Windowsの場合はCurlを用意する
 - https://github.com/gmarik/vundle/wiki/Vundle-for-Windows


git clone
---------

 git clone https://sporty@github.com/sporty/dotfiles.git ~/dotfiles

 cd ~/dotfiles

 git submodule init

 git submodule update


シンボリックリンクの作成
---------

- WidnowsXP

- Widnows7

- Mac,Linux
 ln -s ~/dotfiles/vimfiles ~/vimfiles

 ln -s ~/dotfiles/_gvimrc ~/.gvimrc

 ln -s ~/dotfiles/_bashrc ~/.bashrc

Vundle
---------

:BundleInstall


関連情報
=================

+----------+-------------+
|    OS    |             |
+==========+=============+
| mac      |             |
+----------+-------------+
| windows  |             |
+----------+-------------+

- http://d.hatena.ne.jp/holypp/20110515/1305443997
- http://d.hatena.ne.jp/holypp/20110516/1305552171

