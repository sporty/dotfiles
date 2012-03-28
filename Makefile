
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
	# ターミナル.appの設定をコピー
	cp ~/dotfiles/mac/com.apple.Terminal.plist ~/Library/Preferences/
	# ファインダーのタイトルバーにパスを表示
	defaults write com.apple.finder _FXShowPosixPathInTitle -boolean true
	killall Finder




