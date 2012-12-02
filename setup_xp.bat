@echo off

rem git submoduleサブコマンドでvimプラグインのvundleを取得

cd %HOME%/dotfiles
git submodule init
git submodule update

rem シンボリックリンクの作成

fsutil hardlink create "%HOME%\_vimrc" "%HOME%\dotfiles\vimfiles\_vimrc"
fsutil hardlink create "%HOME%\_gvimrc" "%HOME%\dotfiles\vimfiles\_gvimrc"

linkd "%HOME%\vimfiles" "%HOME%\dotfiles\vimfiles"

rem EOF
