" vi:set sts=2 sw=2 tw=0:
"
" vim向けの設定(gvim向けは_gvimrcに記述すること)
"
"


" プラグインの設定
"===============================================================================

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
Bundle 'http://github.com/h1mesuke/unite-outline.git'
Bundle 'http://github.com/Shougo/vimfiler.git'
filetype plugin indent on 


" unite
"---------------------------------------------------------------------------

" バッファとファイル履歴とファイル一覧
noremap <silent> ;u :Unite buffer file_mru file<CR>
" アウトライン
noremap <silent> ;l :Unite outline<CR>
" neocomplcacheのスニペット
noremap <silent> ;s :Unite snippet<CR>
" VimFiler起動
noremap <silent> ;f :VimFiler<CR>

" ESCキー２回で終了
au FileType unite nnoremap <silent> <buffer> <ESC><ESC> :q<CR>
au FileType unite inoremap <silent> <buffer> <ESC><ESC> <ESC>:q<CR>
au FileType vimfiler nnoremap <silent> <buffer> <ESC><ESC> :e#<CR>
au FileType vimfiler inoremap <silent> <buffer> <ESC><ESC> <ESC>:e#<CR>


" neocomplcache
"---------------------------------------------------------------------------

" 有効化
let g:neocomplcache_enable_at_startup = 1
" 自動補完を無効化
"let g:neocomplcache_disable_auto_complete = 1

" snippet
let g:neocomplcache_snippets_dir = '~/vimfiles/snippets'
imap <C-k> <Plug>(neocomplcache_snippets_expand)
smap <C-k> <Plug>(neocomplcache_snippets_expand)

" Enable omni completion.
autocmd FileType css setlocal omnifunc=csscomplete#CompleteCSS
autocmd FileType html,markdown setlocal omnifunc=htmlcomplete#CompleteTags
autocmd FileType javascript setlocal omnifunc=javascriptcomplete#CompleteJS
autocmd FileType python setlocal omnifunc=pythoncomplete#Complete
autocmd FileType xml setlocal omnifunc=xmlcomplete#CompleteTags

" 一般的な設定
"===============================================================================

" タブの幅
"---------------------------------------------------------------------------

" タブストップ（タブの文字数）
set ts=4
" シフトワイズ（オートインデントの文字数）
set sw=4
set softtabstop=4 

" ビープ音を消す 
" vbはビジュアルベルを使用するというオプション。t_vbはキー
"--------------------------------------------------------------------------- 

set vb t_vb= 

" クリップボードを*レジスタに自動割り当て
"--------------------------------------------------------------------------- 

set clipboard=unnamed,autoselect

" 印刷設定（行番号を表示）
"--------------------------------------------------------------------------- 

set printoptions=number:y

" フォールドメソッド
"---------------------------------------------------------------------------

set fdm=marker

" モードライン
"---------------------------------------------------------------------------

set modeline

" QuickFix
"---------------------------------------------------------------------------

" ;nでQuickFixを開く
noremap <silent> ;n :copen<CR>
" ESC２回で閉じる
au FileType qf :nnoremap <silent> <buffer> <ESC><ESC> :cclose<CR>
" make後に自動でQuickFixを開く
au QuickfixCmdPost * copen

" キーバインド
"---------------------------------------------------------------------------

" ESCキー２回でヘルプを閉じる
au FileType help nnoremap <silent> <buffer> <ESC><ESC> :q<CR>
au FileType help inoremap <silent> <buffer> <ESC><ESC> <ESC>:q<CR>


" Pythonの設定
"===============================================================================

" タブをスペースに自動変換
"---------------------------------------------------------------------------

autocmd FileType python :setlocal expandtab

" QuickFix関連
"---------------------------------------------------------------------------

" makeをpythonコマンドにしてエラーフォーマットを定義しておく
autocmd FileType python :setlocal makeprg=python\ %
autocmd FileType python :setlocal errorformat=%C\ %.%#,%A\ \ File\ \"%f\"\\,\ line\ %l%.%#,%Z%[%^\ ]%\\@=%m

" ハイライトオプション
"---------------------------------------------------------------------------

" 数字のハイライト:
let python_highlight_numbers = 1
" 組み込み関数のハイライト:
let python_highlight_builtins = 1
" 標準例外のハイライト:
let python_highlight_exceptions = 1
" 行末の空白と、スペースとタブの混在をハイライト:
let python_highlight_space_errors = 1
" 以上全部
"let python_highlight_all = 1

" djangoのtagsを追加
"autocmd FileType python :setlocal tags+=C:/Python25/Lib/site-packages/django/tags


" タグファイル
"===============================================================================

" タグファイルの自動指定
"---------------------------------------------------------------------------

" ＭａｙａＳＤＫ。インクルードファイルから作成
"autocmd FileType cpp,h :set tags+=~/.vim/tags/maya.tags

" 再帰的に上位ディレクトリのtagsを検索
"set tags+=tags;


" 辞書ファイル
"===============================================================================

" ＰＨＰ
"autocmd FileType php :setlocal dictionary=~/.vim/dict/php.dict


" EOF