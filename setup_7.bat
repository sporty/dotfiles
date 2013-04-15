@echo off

rem ======================================================================
rem gitの設定
rem ======================================================================

rem シンボリックリンクの作成
del "%HOME%\.gitignore_global"
mklink /H "%HOME%\.gitignore_global" "%HOME%\dotfiles\git\_gitignore_global"

rem ======================================================================
rem bashの設定
rem ======================================================================

rem シンボリックリンクの作成
del "%HOME%\.bashrc"
del "%HOME%\.profile"
del "%HOME%\.inputrc"
mklink /H "%HOME%\.bashrc" "%HOME%\dotfiles\bash\_bashrc"
mklink /H "%HOME%\.profile" "%HOME%\dotfiles\bash\_profile"
mklink /H "%HOME%\.inputrc" "%HOME%\dotfiles\bash\_inputrc"

rem ======================================================================
rem vimの設定
rem ======================================================================

rem git submoduleサブコマンドでvimプラグインのvundleを取得

cd %HOME%/dotfiles
git submodule init
git submodule update

rem シンボリックリンクの作成

del "%HOME%\_vimrc"
del "%HOME%\_gvimrc"
mklink /H "%HOME%\_vimrc" "%HOME%\dotfiles\vimfiles\_vimrc"
mklink /H "%HOME%\_gvimrc" "%HOME%\dotfiles\vimfiles\_gvimrc"

mklink /J /D "%HOME%\vimfiles" "%HOME%\dotfiles\vimfiles"

rem ======================================================================
rem powerlineの設定
rem ======================================================================

rem シンボリックリンクの作成

mklink /J /D "%HOME%\.config\powerline" "%HOME%\dotfiles\powerline"

rem EOF
