#!/usr/bin/env python
# coding=utf-8

import sys
import os
import shutil
import inspect
import subprocess
import urlparse
import httplib
import pprint
pp = pprint.PrettyPrinter(indent=4)


def git():
    _symlink("~/dotfiles/git/_gitignore_global", "~/.gitignore_global")
    _do('git config --global user.name "Ryo Takahashi"')
    _do('git config --global user.email rt.sporty@gmail.com')
    _do('git config --global color.ui auto')
    _do('git config --global core.pager "less -R"')

    if sys.platform == "mac":
        #_do('git config --global core.editor
        #"/Applications/MacVim.app/Contents/MacOS/Vim"')
        pass


def python():
    fn = download('http://python-distribute.org/distribute_setup.py')
    _sudo('python ' + fn)
    _sudo('easy_install virtualenv')
    _sudo('easy_install flake8')


def bash():
    _symlink('~/dotfiles/bash/_bashrc', '~/.bashrc')
    _symlink('~/dotfiles/bash/_profile', '~/.profile')
    _symlink('~/dotfiles/bash/_inputrc', '~/.inputrc')


def vim():
    # submoduleを更新。主にvundle。
    _do('cd '+_np('~/dotfiles'))
    _do('git submodule init')
    _do('git submodule update')

    # ドットファイルのシンボリックリンクを作成
    _symlink('~/dotfiles/vimfiles', '~/vimfiles')
    if sys.platform == "win32":
        prefix = "_"
    else:
        prefix = "."
    _symlink('~/dotfiles/vimfiles/_vimrc', '~/%svimrc' % (prefix, ))
    _symlink('~/dotfiles/vimfiles/_gvimrc', '~/%sgvimrc' % (prefix, ))

    # vundleのアップデート
    # TODO: コマンド実行後終了するオプションがほしい
    if sys.platform == "win32":
        _do('gvim -c "BundleInstall"')
    else:
        _do('vim -c "BundleInstall"')
    # jediのアップデート
    _do('cd '+_np('~/.vim/bundle/jedi-vim'))
    _do('git submodule update --init')


def powerline():
    _symlink('~/dotfiles/powerline', '~/.config/powerline')


def mac():
    if sys.platform == "mac":
        # ターミナル.appの設定をコピー
        _copy('~/Library/Preferences/com.apple.Terminal.plist',
              '~/dotfiles/mac/com.apple.Terminal.plist.back')
        print "backup plist to mac/ (with extension .back)..."
        _copy('~/dotfiles/mac/com.apple.Terminal.plist',
              '~/Library/Preferences/')
        # ファインダーのタイトルバーにパスを表示
        _do('defaults write com.apple.finder \
                _FXShowPosixPathInTitle -boolean true')
        _do('killall Finder')


def dump_preferences():
    if sys.platform == "mac":
        _copy('~/Library/Preferences/com.apple.Terminal.plist', 'mac/')
        _do('plutil -convert xml1 mac/com.apple.Terminal.plist')
    else:
        print "dump_preference can use only on mac os."


def documents():
    '''
    #
    # documents
    #

    install-documents:
        http://jp2.php.net/get/php_manual_ja.tar.gz/from/jp.php.net/mirror
        http://python-doc-ja.googlecode.com/files/python-doc-2.7ja1-html.tar.gz
        mkdir -p ~/Documents/references
        tar zxvf php_manual_ja.tgz -C ~/Documents/references

    '''
    pass


def all():
    git()
    bash()
    vim()
    python()


def test():
    _symlink('./test', '~/test_link')
    _symlink('./test_dir', '~/test_dir_link')


if __name__ == "__main__":

    def _np(fpath):
        """
        pathの正規化
        """
        fpath = os.path.expanduser(fpath)
        fpath = os.path.expandvars(fpath)
        fpath = os.path.normpath(fpath)
        fpath = os.path.abspath(fpath)
        return fpath

    def _sudo(cmd):
        """
        _sudoでコマンド実行
        TODO: 未実装
        """
        _do(cmd)

    def _do(cmd):
        """
        コマンド実行
        """
        print cmd
        if sys.platform == "win32":
            pass
        else:
            pass

        if subprocess.call(cmd, shell=True):
            raise Exception("process error. stop installation.")

    def _copy(src, dest):
        """
        コピー作成
        """
        print "cp %s %s" % (src, dest)
        shutil.copyfile(src, dest)

    def _symlink(src, dest):
        """
        シンボリックリンク作成
        """

        src = _np(src)
        dest = _np(dest)

        if sys.platform == "win32":
            # 一旦削除
            if os.path.isdir(dest):
                _do('RMDIR /Q %s' % (dest, ))
            elif os.path.isfile(dest):
                _do('DEL /F /Q %s' % (dest, ))

            # ジャンクションまたはハードリンク作成
            if os.path.isdir(src):
                _do("CMD.EXE /C mklink /J /D %s %s" % (dest, src))
            else:
                _do("CMD.EXE /C mklink /H %s %s" % (dest, src))
        else:
            # 一旦削除
            _do('rm -f %s' % (dest, ))
            # シンボリックリンク作成
            print "ln -s %s %s" % (src, dest)
            os.symlink(src, dest)

    def download(url, filename=None):
        print "download %s" % (url, )
        o = urlparse.urlparse(url)
        if o.scheme == "http":
            conn = httplib.HTTPConnection(o.netloc)
            conn.request("GET", o.path)
            r1 = conn.getresponse()
            if r1.status == 200:
                data = r1.read()
            else:
                raise Exception("status error. %d (%s)" % (r1.status, url))
        else:
            raise Exception("unsupported scheme.")

        if filename:
            output_filename = _np(filename)
        else:
            # ヘッダで指定されていたらファイル名を取り出す
            disposition = r1.getheader("Content-Disposition")
            if disposition:
                output_filename = disposition
            else:
                # URLからファイル名を決定する
                utmp = url
                utmp = utmp.strip('/')
                utmp = utmp.split('/')
                output_filename = utmp[-1]

        with file(output_filename, "wb") as fp:
            fp.write(data)

        return output_filename

    # 使用可能関数の検索
    funcs = {}
    excepts = ["_np", "_sudo", "_do", "_copy", "_symlink"]
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
