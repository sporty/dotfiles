#!/bin/sh 

# Linux用ドットファイルのシンボリックリンクを作成
if [ ! -d ~/vimfiles ]; then
	ln -s ~/dotfiles/vimfiles ~/vimfiles
fi

if [ ! -f ~/.vimrc ]; then
	ln -s ~/dotfiles/_vimrc ~/.vimrc
fi
if [ ! -f ~/.gvimrc ]; then
	ln -s ~/dotfiles/_gvimrc ~/.gvimrc
fi
if [ ! -f ~/.bashrc ]; then
	ln -s ~/dotfiles/_bashrc ~/.bashrc
fi
if [ ! -f ~/.profile ]; then
	ln -s ~/dotfiles/_profile ~/.profile
fi

# EOF