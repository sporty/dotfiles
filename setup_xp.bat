
rem git submoduleサブコマンドでvimプラグインのvundleを取得

cd ~/dotfiles
git submodule init
git submodule update

rem シンボリックリンクの作成

fsutil hardlink create "%HOME%\_vimrc" "%HOME%\dotfiles\_vimrc"
fsutil hardlink create "%HOME%\_gvimrc" "%HOME%\dotfiles\_gvimrc"

linkd "%HOME%vimfiles" "%HOME%\dotfiles\vimfiles"

