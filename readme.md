dotfiles セットアップ方法
================================================

必要なソフトウェア
------------------

* python 2.6 
* git 1.8
* gvim 7.3
 * python 2.7 x64


git clone
---------

```
git clone git@github.com:sporty/dotfiles.git ~/dotfiles
```

gitの設定
---------

git://は通りにくいのでhttps://に自動変換されるようにしておく。

```
git config --global url."https://".insteadOf git://
```

会社ではローカル設定でメールアドレスを設定しておく。

```
cd ~/dotfiles
git config --local user.email "********@gmail.com"
```

自動初期設定
---------

全システム共通

```
python install.py all
```

以上。
