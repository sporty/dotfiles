#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import, division, print_function

import inspect
import os
import shutil
import subprocess
import sys
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse
try:
    import httplib
except ImportError:
    import http.client as httplib


def thisdir(filename=""):
    if hasattr(sys, "frozen") and sys.frozen in ("windows_exe", "console_exe"):
        path = os.path.dirname(unicode(sys.executable, sys.getfilesystemencoding()))
    else:
        path = os.path.dirname(unicode(__file__, sys.getfilesystemencoding()))

    return os.path.normpath(os.path.abspath(os.path.join(path, filename)))


def git():
    _ln(thisdir("git/_gitignore_global"), "~/.gitignore_global")
    _do('git config --global user.name "Ryo Takahashi"')
    _do('git config --global user.email rt.sporty@gmail.com')
    _do('git config --global color.ui auto')
    _do('git config --global core.pager "less -R"')

    if sys.platform == "mac":
        # _do('git config --global core.editor
        # "/Applications/MacVim.app/Contents/MacOS/Vim"')
        pass


def python():
    _sudo('python {0}'.format(_np(thisdir('python/get-pip.py'))))
    _sudo('python -m pip install -U pip')
    _sudo('pip install -r {0}'.format(_np(thisdir('python/requirements.txt'))))


def bash():
    _ln(thisdir('bash/_bashrc'), '~/.bashrc')
    _ln(thisdir('bash/_profile'), '~/.profile')
    _ln(thisdir('bash/_inputrc'), '~/.inputrc')


def zsh():
    _ln(thisdir('zsh/_zshrc'), '~/.zshrc')


def tmux():
    _ln(thisdir('tmux/_tmux.conf'), '~/.tmux.conf')


def vim():
    # submoduleを更新。主にvundle。
    _do('cd ' + _np(thisdir()))
    _do('git submodule init')
    _do('git submodule update')

    # ドットファイルのシンボリックリンクを作成
    _ln(thisdir('vimfiles'), '~/vimfiles')
    if sys.platform == "win32":
        prefix = "_"
    else:
        prefix = "."
    _ln(thisdir('vimfiles/_vimrc'), '~/{0}vimrc'.format(prefix))
    _ln(thisdir('vimfiles/_gvimrc'), '~/{0}gvimrc'.format(prefix))

    # プラグインの更新
    '''
    if sys.platform == "win32":
        _do('gvim +NeoBundleInstall +qall')
    else:
        _do('vim +NeoBundleInstall +qall')
    '''


def powerline():
    _ln(thisdir('powerline'), '~/.config/powerline')


def mac():
    if sys.platform == "mac":
        # ターミナル.appの設定をコピー
        _cp('~/Library/Preferences/com.apple.Terminal.plist',
            thisdir('mac/com.apple.Terminal.plist.back'))
        print("backup plist to mac/ (with extension .back)...")
        _cp(thisdir('mac/com.apple.Terminal.plist'),
            '~/Library/Preferences/')
        # ファインダーのタイトルバーにパスを表示
        _do('defaults write com.apple.finder \
            _FXShowPosixPathInTitle -boolean true')
        _do('killall Finder')


def dump_preferences():
    if sys.platform == "mac":
        _cp('~/Library/Preferences/com.apple.Terminal.plist', 'mac/')
        _do('plutil -convert xml1 mac/com.apple.Terminal.plist')
    else:
        print("dump_preference can use only on mac os.")


def windows():
    reg_files = [
        "excel_multi_windows.reg",  # エクセルで同名ファイルを開く
        "foldertype.reg",  # ファイル名ソート
        "keyboard_us.reg",  # 英語キーボード
        # "keyboard_jp.reg",  # 日本語キーボード
        "max_cached_icons.reg",  # アイコンキャッシュサイズ最大
        "no_window_minimizing_shortcuts.reg",  # 最小化ジェスチャーの無効化
    ]

    if sys.platform == "win32":
        for reg_filename in reg_files:
            _do(r"regedit windows\{0}".format(reg_filename))


def chocolatey():
    if sys.platform == "win32":
        _do(r"cinst chocolatey/packages.config")


def documents():
    u'''documents

    http://jp2.php.net/get/php_manual_ja.tar.gz/from/jp.php.net/mirror
    http://python-doc-ja.googlecode.com/files/python-doc-2.7ja1-html.tar.gz
    mkdir -p ~/Documents/references
    tar zxvf php_manual_ja.tgz -C ~/Documents/references
    '''
    pass


def all():
    git()
    bash()
    zsh()
    tmux()
    vim()
    python()


def test():
    _ln('./test', '~/test_link')
    _ln('./test_dir', '~/test_dir_link')


if __name__ == "__main__":

    def _np(fpath):
        u"""pathの正規化"""

        fpath = os.path.expanduser(fpath)
        fpath = os.path.expandvars(fpath)
        fpath = os.path.normpath(fpath)
        fpath = os.path.abspath(fpath)
        return fpath

    def _sudo(cmd):
        u"""_sudoでコマンド実行

        TODO: 未実装
        """
        _do(cmd)

    def _do(cmd):
        u"""コマンド実行"""

        print(cmd)
        if sys.platform == "win32":
            pass
        else:
            pass

        if subprocess.call(cmd, shell=True):
            raise Exception("process error. stop installation.")

    def _cp(src, dest):
        u"""コピー作成"""

        print("cp {0} {1}".format(src, dest))
        shutil.copyfile(src, dest)

    def _ln(src, dest):
        u"""シンボリックリンク作成"""

        src = _np(src)
        dest = _np(dest)

        if sys.platform == "win32":
            # 一旦削除
            if os.path.isdir(dest):
                _do('RMDIR /Q {0}'.format(dest))
            elif os.path.isfile(dest):
                _do('DEL /F /Q {0}'.format(dest))

            # ジャンクションまたはハードリンク作成
            if os.path.isdir(src):
                _do("CMD.EXE /C mklink /J /D {0} {1}".format(dest, src))
            else:
                _do("CMD.EXE /C mklink /H {0} {1}".format(dest, src))
        else:
            # 一旦削除
            _do('rm -f {0}'.format(dest))
            # シンボリックリンク作成
            print("ln -s {0} {1}".format(src, dest))
            os.symlink(src, dest)

    def _dl(url, filename=None):
        u"""ファイルをダウンロード"""

        print("download {0}".format(url))
        o = urlparse.urlparse(url)
        if o.scheme == "http":
            conn = httplib.HTTPConnection(o.netloc)
            conn.request("GET", o.path)
            r1 = conn.getresponse()
            if r1.status == 200:
                data = r1.read()
            else:
                raise Exception(
                    "status error. {0} ({1})".format(r1.status, url)
                )
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

        with open(output_filename, "wb") as fp:
            fp.write(data)

        return output_filename

    # 使用可能関数の検索
    funcs = {}
    excepts = ["_np", "_sudo", "_do", "_cp", "_ln", "_dl"]
    mod = inspect.getmodule(all)
    for (name, function) in inspect.getmembers(mod, inspect.isfunction):
        if inspect.isfunction(function) and name not in excepts:
            funcs[name] = function

    # 引数で指定された関数を実行
    if len(sys.argv) == 1:
        print("usage: install.py [TARGETS]")
        print("")
        print("TARGETS:")
        for key in funcs.keys():
            print(" " + key)
    else:
        for arg in sys.argv[1:]:
            if arg in funcs.keys():
                funcs[arg]()
            else:
                print("can't find function [{0}]".format(arg))

        print("finish.")

# EOF
