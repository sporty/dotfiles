dotfiles セットアップ方法
================================================

gitの設定
---------

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

sshの設定
---------

http://rt-sporty.blogspot.jp/2012/03/ssh.html


git clone
---------

```
git clone git@github.com:sporty/dotfiles.git ~/dotfiles
```

会社ではローカル設定でメールアドレスを設定しておく。

```
cd ~/dotfiles
git config --local user.email "********@gmail.com"
```

自動初期設定
---------

Mac・Linux

```
cd ~/dotfiles
make install
```

WidnowsXP

```
~/dotfiles/setup_xp.bat
```

WidnowsVista・Windows7

```
未実装
```

Vundle
---------
Windowsの場合はCurlを用意する (https://github.com/gmarik/vundle/wiki/Vundle-for-Windows)

vimを起動し、以下のコマンドを実行

```
:BundleInstall
```

関連情報
=================

* http://d.hatena.ne.jp/holypp/20110515/1305443997
* http://d.hatena.ne.jp/holypp/20110516/1305552171

