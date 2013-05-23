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
git config --global color.ui true
```

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

Vundle
---------

vimを起動（windowsの場合はmsys bashとかから）し、以下のコマンドを実行

```
:BundleInstall
```

jediのみサブモジュールアップデートが必要。

```
cd .vim/bundle/jedi-vim
git submodule update --init
```

以上。
