dotfiles セットアップ方法
================================================

必要なソフトウェア
------------------

* python 2.6 
* git

gitの設定
---------

```
git config --global core.autocrlf false
```

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

全システム共通

```
python install.py all
```

以上。
