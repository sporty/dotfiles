dotfiles セットアップ方法
================================================

前準備
---------

* git 設定

会社なら会社のメールアドレスを設定する。

```
git config --global user.name "Ryo Takahashi"
git config --global user.email "ryo_takahashi@********.co.jp"
```

家ならグローバルでプライベートメールアドレスを設定してしまう。

```
git config --global user.name "Ryo Takahashi"
git config --global user.email "********@gmail.com"
```

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

会社ではローカル設定でメールアドレスを設定しておく。

```
git config --local user.name "Ryo Takahashi"
git config --local user.email "********@gmail.com"
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
~/dotfiles/setup_linux.sh
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

