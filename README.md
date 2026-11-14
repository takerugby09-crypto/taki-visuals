# TAKI VISUALS

映像・アート制作のための、ダークカラーの静的ポートフォリオ。HTML / CSS / JavaScriptのみで構成し、ビルドや外部サービスは不要です。

実作品・経歴・連絡先は未提供のため、作品は公開準備中、連絡先は準備中と明示しています。架空の作品、実績、人物紹介は掲載していません。トップの抽象的な光はCSSによる装飾です。

## 構成

- `index.html`：トップ、Works、About、Contact、作品カード用テンプレート
- `styles.css`：レスポンシブレイアウト、装飾、キーボードフォーカス、動きを抑える設定
- `script.js`：フッターの西暦更新（JavaScript無効時も閲覧・移動可能）
- `assets/media/`：後から追加する画像・動画の置き場

## 起動・動作確認

リポジトリのルートで以下を実行します（Python 3）。

```sh
python3 -m http.server 8000
```

ブラウザーで http://localhost:8000 を開きます。終了は Ctrl+C。`index.html` を直接開くこともできます。

確認項目：

- スマートフォン（幅375px前後）、iPad（768〜1024px）、PC（1440px前後）で横スクロールや文字の重なりがないこと
- Works / About / Contact とトップへのリンクが正しい場所に移動すること
- Tabキーでリンクを操作でき、フォーカスが見えること（最初のリンクは本文へのスキップ）
- JavaScript無効時も本文とナビゲーションが利用できること
- OSの「視差効果を減らす」設定時、スムーズスクロールを抑えること

## 作品・素材の追加

1. 実際の画像を `assets/media/` に置きます。
2. `index.html` の `#work-template` 内の `article` をコピーし、`#works-list` 内に配置します。`template` 自体は編集用の雛形で、画面には表示されません。
3. `img` の `src`、実際の画像を説明する `alt`、画像寸法、`h3` の作品名、`p` の説明を設定します。
4. 作品を公開したら `.empty-work` の準備中表示を削除します。

画像カードの例（実際の素材を用意してから追加）：

```html
<article class="work-card">
  <img src="assets/media/your-work.webp" alt="作品画像の内容を記載" width="1600" height="900" loading="lazy">
  <div class="work-caption"><h3>実際の作品名</h3><p>実際の制作内容</p></div>
</article>
```

動画の場合は `img` を次の要素に置き換えます。操作ボタンを表示し、自動再生しない構成です。

```html
<video controls playsinline preload="metadata" poster="assets/media/your-poster.webp">
  <source src="assets/media/your-video.mp4" type="video/mp4">
  お使いのブラウザーは動画の再生に対応していません。
  <a href="assets/media/your-video.mp4">動画をダウンロード</a>
</video>
```

トップの `.hero-art` はCSSの抽象装飾です。画像に差し替える場合は内部要素を削除し、装飾用画像なら `alt=""` の画像を配置して `object-fit: cover` 等を設定してください。

Aboutは事実確認できた紹介文に更新してください。Contactは連絡先が確定した段階で `.contact-status` を実際の `mailto:` リンク等に差し替えます。現時点で送信フォームやメール送信機能はありません。

## ブランチ

`feat/taki-visuals-portfolio` で作成。作成時点ではリポジトリにコミットがなく、mainは未作成です。mainへのコミットやマージ、公開設定は行いません。GitHubのブランチ画面からファイル・コミットを確認できます。mainに比較元のコミットが存在しない間は、通常のPull Requestを作成できません。

## 実施した確認

Chromium（ヘッドレス、Playwright）で以下を確認済みです。

- 320×740、375×812、768×1024、1024×768、1440×900：横方向のはみ出しなし、3つのナビゲーションリンクが動作
- キーボードの最初のTabで本文へのスキップリンクにフォーカス
- reduced-motion設定でスムーズスクロールを無効化
- JavaScript無効時のAboutへの移動
- ページのJavaScriptエラー・HTTPエラーなし
- `node --check script.js` による構文確認
- スマートフォン・PC幅のスクリーンショットを目視確認

実機のiPhone/iPad、Safariでの確認は未実施です。

### WebKitでの追加確認（2026-11-14）

Linux上のPlaywright WebKit 26.5（ビルド2336）で以下を追加確認しました。**Safari本体やApple実機での検証ではありません。** この環境にはiPhone・iPad実機、macOS、実機検証サービスへの接続がありません。

| 環境 | 確認内容 | 結果 |
| --- | --- | --- |
| WebKit：320×740 / 375×812 / 768×1024 / 1024×768 / 1440×900 | 横はみ出し、Works / About / Contactへの移動 | 通過 |
| iPhone 13設定のタッチエミュレーション：390×664 / 664×390 | 縦横の画面サイズ、タップでの各セクションへの移動先が画面内にあること、横はみ出し | 通過 |
| iPad（第7世代）設定のタッチエミュレーション：810×1080 / 1080×810 | 縦横の画面サイズ、タップでの各セクションへの移動先が画面内にあること、横はみ出し | 通過 |
| WebKit | 最初のTabでスキップリンクにフォーカス、reduced-motion、JavaScript無効時の移動 | 通過 |
| WebKit | JavaScriptエラー・HTTPエラー、スマートフォン・PC幅の画面目視確認 | エラーなし、横はみ出し・要素の重なりなし |

端末設定のエミュレーションは実機の代わりにはなりません。iOS/iPadOSのSafariでのアドレスバー伸縮、セーフエリア、実機フォント、macOS Safari固有の動作は未確認です。実機で確認する場合は、端末と同じLAN内のPCで `python3 -m http.server 8000 --bind 0.0.0.0` を起動し、Safariから `http://<PCのLAN内IP>:8000` を開いてください。信頼できるLAN内だけで使用し、確認後はCtrl+Cで停止します。
