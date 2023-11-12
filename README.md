# PEC-1
Hand made 8bitCPU

## Picuture
動いている様子．下記のSample Codeを動かしています．

![F-tropnacAAZ7CA](https://github.com/Basyo-Engineer/PEC-1/assets/142486631/ae064df1-a218-46eb-bad8-a73986ee0c59)

## Command List
PEC-1で使用可能なコマンド一覧です．

GRx,GRyは汎用レジスタです．ImはImmidiate Data，すなわち即値データです．

![スクリーンショット 2023-11-12 145332](https://github.com/Basyo-Engineer/PEC-1/assets/142486631/2abc60c7-57a8-49b4-b377-28f193abf2b8)

## Machine Code
コマンドのマシン語対応表です．

xxやyyは，コマンドで指定したいレジスタ番号の二進数表示です．00(0)～11(3)番まで行けます．

[imdt]は即値データです．データ長は6bitです．

基本的に，オペコード部で各部の制御を行っています．なので，
ジャンプ命令などは仕様上レジスタの指定は冗長と扱うためオペランドはどう書いても問題ありません．
また，即値が「000000」となっているコマンドも，即値の入力は冗長です，

![スクリーンショット 2023-11-12 145337](https://github.com/Basyo-Engineer/PEC-1/assets/142486631/b3fcf25a-9e4e-44c4-87cf-dded7901f843)

## Sample Code
サンプルコードです．掛け算と引き算を行うプログラムです．

![スクリーンショット 2023-11-12 145524](https://github.com/Basyo-Engineer/PEC-1/assets/142486631/334ea3b5-9ea0-43ea-bcb0-abe394734c2e)


