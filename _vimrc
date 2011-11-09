" vi:set sts=2 sw=2 tw=0:
"
" vim向けの設定(gvim向けは_gvimrcに記述すること)
"
"


"===============================================================================
" プラグインの設定
"===============================================================================

"---------------------------------------------------------------------------
" vundle
"---------------------------------------------------------------------------
set nocompatible
filetype off

set rtp+=~/vimfiles/vundle.git/
call vundle#rc()
Bundle 'http://github.com/Shougo/unite.vim.git'
Bundle 'http://github.com/Shougo/neocomplcache.git'
Bundle 'http://github.com/thinca/vim-ref.git'
Bundle 'http://github.com/groenewege/vim-less.git'
Bundle 'http://github.com/tpope/vim-markdown.git'
filetype plugin indent on 


"---------------------------------------------------------------------------
" neocomplcache
"---------------------------------------------------------------------------
" 有効化
let g:neocomplcache_enable_at_startup = 1
" 自動補完を無効化
let g:neocomplcache_disable_auto_complete = 1
" 補完項目の自動選択を有効化
let g:neocomplcache_enable_auto_select = 1

" Enable omni completion.
autocmd FileType css setlocal omnifunc=csscomplete#CompleteCSS
autocmd FileType html,markdown setlocal omnifunc=htmlcomplete#CompleteTags
autocmd FileType javascript setlocal omnifunc=javascriptcomplete#CompleteJS
autocmd FileType python setlocal omnifunc=pythoncomplete#Complete
autocmd FileType xml setlocal omnifunc=xmlcomplete#CompleteTags


"===============================================================================
" 一般的な設定
"===============================================================================

"---------------------------------------------------------------------------
"タブの幅
"---------------------------------------------------------------------------
"タブストップ（タブの文字数）
set ts=4
"シフトワイズ（オートインデントの文字数）
set sw=4
set softtabstop=4 

"--------------------------------------------------------------------------- 
" ビープ音を消す 
set vb t_vb= 

"--------------------------------------------------------------------------- 
" クリップボードを*レジスタに自動割り当て
set clipboard=unnamed,autoselect

"--------------------------------------------------------------------------- 
" 印刷設定（行番号を表示）
set printoptions=number:y

"---------------------------------------------------------------------------
"フォールドメソッド
"---------------------------------------------------------------------------
set fdm=marker

"---------------------------------------------------------------------------
" モードライン
"---------------------------------------------------------------------------
set modeline


"---------------------------------------------------------------------------
" タグファイルの自動指定
"---------------------------------------------------------------------------
"ＭａｙａＳＤＫ。インクルードファイルから作成
"autocmd FileType cpp,h :set tags+=~/.vim/tags/maya.tags


"---------------------------------------------------------------------------
" 辞書ファイルの自動指定
"---------------------------------------------------------------------------
"ＰＨＰ
"autocmd FileType php :setlocal dictionary=~/.vim/dict/php.dict

"===============================================================================
" Pythonの設定
"===============================================================================

"タブをスペースに自動変換
autocmd FileType python :setlocal expandtab
"djangoのtagsを追加
"autocmd FileType python :setlocal tags+=C:/Python25/Lib/site-packages/django/tags

"数字のハイライト:
let python_highlight_numbers = 1
"組み込み関数のハイライト:
let python_highlight_builtins = 1
"標準例外のハイライト:
let python_highlight_exceptions = 1
"行末の空白と、スペースとタブの混在をハイライト:
let python_highlight_space_errors = 1
"以上全部
"let python_highlight_all = 1


"--------------------------------------------------------------------------- 
" タグファイル
" 再帰的に上位ディレクトリのtagsを検索
"set tags+=tags;


"-------------------------------------------------------------------------------
" EOF
"-------------------------------------------------------------------------------
