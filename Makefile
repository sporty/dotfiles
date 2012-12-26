# セットアップ

all:
	@echo "初期設定を行いたい場合は make install と実行してください"

#
# 全部
#

install: install-git install-bash install-vim install-mac

#
# git
#

install-git:
	rm -f ~/.gitignore_global
	ln -s ~/dotfiles/git/_gitignore_global ~/.gitignore_global
	# gitconfigは環境依存が大きいので未使用
	#rm -f ~/.gitconfig
	#ln -s ~/dotfiles/git/_gitconfig ~/.gitconfig
	# config
	git config --global user.name "Ryo Takahashi"
ifeq ($(shell uname),Darwin)
	git config --global core.editor "/Applications/MacVim.app/Contents/MacOS/Vim"
endif

#
# bash
#

install-bash:
	rm -f ~/.bashrc ~/.profile
	ln -s ~/dotfiles/bash/_bashrc ~/.bashrc
	ln -s ~/dotfiles/bash/_profile ~/.profile
	ln -s ~/dotfiles/bash/_inputrc ~/.inputrc

#
# vim
#

install-vim: install-git
	# git submoduleサブコマンドでvimプラグインのvundleを取得
	cd ~/dotfiles
	git submodule init
	git submodule update
	# ドットファイルのシンボリックリンクを作成
	rm -rf ~/vimfiles ~/.vimrc ~/.gvimrc
	ln -s ~/dotfiles/vimfiles ~/vimfiles
	ln -s ~/dotfiles/vimfiles/_vimrc ~/.vimrc
	ln -s ~/dotfiles/vimfiles/_gvimrc ~/.gvimrc

#
# Mac OS
#

install-mac:
ifeq ($(shell uname),Darwin)
	# ターミナル.appの設定をコピー
	cp ~/Library/Preferences/com.apple.Terminal.plist ~/dotfiles/mac/com.apple.Terminal.plist.back
	@echo "backup plist to mac/ ( with extension .back)..."
	cp ~/dotfiles/mac/com.apple.Terminal.plist ~/Library/Preferences/
	# ファインダーのタイトルバーにパスを表示
	defaults write com.apple.finder _FXShowPosixPathInTitle -boolean true
	killall Finder
endif

dump-preferences:
ifeq ($(shell uname),Darwin)
	cp ~/Library/Preferences/com.apple.Terminal.plist mac/
	plutil -convert xml1 mac/com.apple.Terminal.plist
else
	@echo "dump-plist can use only on mac os."
endif

#
# documents
#

install-documents:
	mkdir -p ~/Documents/references
	# php
	wget -O php_manual_ja.tgz "http://jp2.php.net/get/php_manual_ja.tar.gz/from/jp.php.net/mirror"
	tar zxvf php_manual_ja.tgz -C ~/Documents/references
	# python 2.7
	wget -O python-doc-2.7ja1-html.tgz http://python-doc-ja.googlecode.com/files/python-doc-2.7ja1-html.tar.gz
	tar zxvf python-doc-2.7ja1-html.tgz -C ~/Documents/references/

#
# 不要なファイルを削除
#

clean:
	rm -f *.tgz *~ .*~

# EOF
