@echo off

rem git submoduleサブコマンドでvimプラグインのvundleを取得

cd %HOME%/dotfiles
git submodule init
git submodule update

rem シンボリックリンクの作成

mklink /H "%HOME%\_vimrc" "%HOME%\dotfiles\vimfiles\_vimrc"
mklink /H "%HOME%\_gvimrc" "%HOME%\dotfiles\vimfiles\_gvimrc"

mklink /J /D "%HOME%\vimfiles" "%HOME%\dotfiles\vimfiles"

rem EOF
