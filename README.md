# RAKUDA
## RAKUDAについて
RAKUDAは物品の購入申請時に必要な申請書を自動生成してくれるツールです。
Excelに入力された商品ページurlと注文数から、商品情報(名前、値段)などのデータを自動取得し、Excelファイルに自動入力します。
<br>思わず、「あー、らくだー」と口に出してしまいます。

## 対応サイト
- 秋月電子通商
- Switchscience
- Marutu
<br>となっています。
<br>非対応サイトのURLが入力されている場合は、その行の処理は行われません。(URLが混合していても問題はありません)

## RAKUDA v0.1の使い方
![スクリーンショット 2021-08-23 124938_edit_1943099982225 - コピー](https://user-images.githubusercontent.com/45566778/130388648-57de9df4-5cbc-466a-bc40-72e75f509a3d.png)
生成ボタンを押したのちに"completed successfully!!"と表示されれば、問題なく生成されました。
エラーがある場合には、ボタン下のテキストボックスにエラーメッセージが表示されます。

※対応サイト以外のURLが記載されていた場合にはwarningとしてテキストボックスに表示されます。
