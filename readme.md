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

Windows7・Windows8

* github for windows(http://windows.github.com/)
* githubのGit Shell(PowerShell)で以下のコマンドにてセットアップスクリプトを実行

```
cmd /C ~/dotfiles/setup_7.bat
```

WidnowsXP

* msysGit(http://code.google.com/p/msysgit/downloads/list)

* Resource Kit Tools(http://www.microsoft.com/downloads/details.aspx?FamilyID=9d467a69-57ff-4ae7-96ee-b18c4790cffd&DisplayLang=en&displaylang=en)

```
~/dotfiles/setup_xp.bat
```

Vundle
---------
Windowsの場合はCurlを用意する (https://github.com/gmarik/vundle/wiki/Vundle-for-Windows)

vimを起動し、以下のコマンドを実行

```
:BundleInstall
```

jediのみサブモジュールアップデートが必要。

```
cd .vim/bundle/jedi-vim
git submodule update --init
```

関連情報
=================

* http://d.hatena.ne.jp/holypp/20110515/1305443997
* http://d.hatena.ne.jp/holypp/20110516/1305552171

