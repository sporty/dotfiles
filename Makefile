
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

#
# bash
#

install-bash:
	rm -f ~/.bashrc ~/.profile
	ln -s ~/dotfiles/_bashrc ~/.bashrc
	ln -s ~/dotfiles/_profile ~/.profile

#
# vim
#

install-vim:
	# git submoduleサブコマンドでvimプラグインのvundleを取得
	cd ~/dotfiles
	git submodule init
	git submodule update
	# ドットファイルのシンボリックリンクを作成
	rm -rf ~/vimfiles ~/.vimrc ~/.gvimrc
	ln -s ~/dotfiles/vimfiles ~/vimfiles
	ln -s ~/dotfiles/_vimrc ~/.vimrc
	ln -s ~/dotfiles/_gvimrc ~/.gvimrc

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

dump-plist:
ifeq ($(shell uname),Darwin)
	cp ~/Library/Preferences/com.apple.Terminal.plist mac/
	plutil -convert xml1 mac/com.apple.Terminal.plist
else
	@echo "dump-plist can use only on mac os."
endif


