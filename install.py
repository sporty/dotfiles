#!/usr/bin/env python
# coding=utf-8

import sys
import os
import shutil
import inspect
import subprocess


def git():
    symlink("~/dotfiles/git/_gitignore_global", "~/.gitignore_global")
    execute('git config --global user.name "Ryo Takahashi"')
    execute('git config --global user.email rt.sporty@gmail.com')
    execute('git config --global color.ui auto')
    execute('git config --global core.pager "less -R"')

    if sys.platform == "mac":
        #execute('git config --global core.editor "/Applications/MacVim.app/Contents/MacOS/Vim"')
        pass


def bash():
    symlink('~/dotfiles/bash/_bashrc', '~/.bashrc')
    symlink('~/dotfiles/bash/_profile', '~/.profile')
    symlink('~/dotfiles/bash/_inputrc', '~/.inputrc')


def vim():
    # submoduleを更新。主にvundle。
    execute('cd '+np('~/dotfiles'))
    execute('git submodule init')
    execute('git submodule update')

    # ドットファイルのシンボリックリンクを作成
    symlink('~/dotfiles/vimfiles', '~/vimfiles')
    if sys.platform == "win32":
        prefix = "_"
    else:
        prefix = "."
    symlink('~/dotfiles/vimfiles/_vimrc', '~/%svimrc' % (prefix, ))
    symlink('~/dotfiles/vimfiles/_gvimrc', '~/%sgvimrc' % (prefix, ))

    # vundleのアップデート
    # TODO: コマンド実行後終了するオプションがほしい
    if sys.platform == "win32":
        execute('gvim -c "BundleInstall"')
    else:
        execute('vim -c "BundleInstall"')
    # jediのアップデート
    execute('cd '+np('~/.vim/bundle/jedi-vim'))
    execute('git submodule update --init')


def powerline():
    symlink('~/dotfiles/powerline', '~/.config/powerline')


def mac():
    if sys.platform == "mac":
        # ターミナル.appの設定をコピー
        copy('~/Library/Preferences/com.apple.Terminal.plist',
             '~/dotfiles/mac/com.apple.Terminal.plist.back')
        print "backup plist to mac/ (with extension .back)..."
        copy('~/dotfiles/mac/com.apple.Terminal.plist',
             '~/Library/Preferences/')
        # ファインダーのタイトルバーにパスを表示
        execute('defaults write com.apple.finder _FXShowPosixPathInTitle -boolean true')
        execute('killall Finder')


def dump_preferences():
    if sys.platform == "mac":
        copy('~/Library/Preferences/com.apple.Terminal.plist', 'mac/')
        execute('plutil -convert xml1 mac/com.apple.Terminal.plist')
    else:
        print "dump_preference can use only on mac os."


def documents():
    '''
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

    '''
    pass


def all():
    git()
    bash()
    vim()


def test():
    symlink('./test', '~/test_link')
    symlink('./test_dir', '~/test_dir_link')


if __name__ == "__main__":

    def np(fpath):
        """
        pathの正規化
        """
        fpath = os.path.expanduser(fpath)
        fpath = os.path.expandvars(fpath)
        fpath = os.path.normpath(fpath)
        fpath = os.path.abspath(fpath)
        return fpath

    def execute(cmd):
        """
        コマンド実行
        """
        print cmd
        if sys.platform == "win32":
            pass
        else:
            pass

        if subprocess.call(cmd, shell=True):
            raise Exception("error")

    def copy(src, dest):
        """
        コピー作成
        """
        print "cp %s %s" % (src, dest)
        shutil.copyfile(src, dest)

    def symlink(src, dest):
        """
        シンボリックリンク作成
        """

        src = np(src)
        dest = np(dest)

        if sys.platform == "win32":
            # 一旦削除
            if os.path.isdir(dest):
                execute('RMDIR /Q %s' % (dest, ))
            elif os.path.isfile(dest):
                execute('DEL /F /Q %s' % (dest, ))

            # ジャンクションまたはハードリンク作成
            if os.path.isdir(src):
                execute("CMD.EXE /C mklink /J /D %s %s" % (dest, src))
            else:
                execute("CMD.EXE /C mklink /H %s %s" % (dest, src))
        else:
            # 一旦削除
            execute('rm -f %s' % (dest, ))
            # シンボリックリンク作成
            print "ln -s %s %s" % (src, dest)
            os.symlink(src, dest)

    # 使用可能関数の検索
    funcs = {}
    excepts = ["np", "execute", "copy", "symlink"]
    mod = inspect.getmodule(all)
    for (name, function) in inspect.getmembers(mod, inspect.isfunction):
        if inspect.isfunction(function) and not name in excepts:
            funcs[name] = function

    # 引数で指定された関数を実行
    if len(sys.argv) == 1:
        print "usage: install.py [TARGETS]"
        print ""
        print "TARGETS:"
        for key in funcs.keys():
            print " "+key
    else:
        for arg in sys.argv[1:]:
            if arg in funcs.keys():
                funcs[arg]()
            else:
                print "can't find function [%s]" % (arg, )

        print "finish."

# EOF
