# Codex instructions — TAKI VISUALS

このリポジトリには既存の静的ポートフォリオと、制作知識ベース `creative-brain/` が共存する。

## 作業方針
- **勝手に既存サイトを変更しない。** Webの変更が明示された場合のみ `index.html`, `styles.css`, `script.js` を編集する。
- 動画・画像の**生成を無断で実行しない**。課金が発生しうる処理はモデル、費用、出力数を確認してから提案する。
- 企画時は特定のジャンル（ストリート、プリンセス、SFなど）を前提にしない。異なる方向性を比較可能に提案する。
- 制作提案は「企画→参考素材→ショット→画像→動画→編集→評価」の流れで考える。
- アドバイスで終わらず、試せる最小の実践課題を1つ提示する。
- プロンプトは **原文、意味、狙い、変数、失敗時の修正案** に分ける。
- モデル名やHiggsfieldのUIは変更されるため、学習動画内の操作と現行仕様を混同しない。
- ユーザーの好みとSNSの定量的な成果を分けて評価する。実測がなければ推測と明記する。
- **秘密情報、個人情報、クライアント素材、未公開案をPublicリポジトリに保存しない。**
- 本文で見られるまで、素材や外部動画を「確認済み」と言わない。過去の説明は逐語訳ではない。

## 読む順番
1. `creative-brain/README.md`
2. `creative-brain/creative-principles.md`
3. `creative-brain/guides/higgsfield-workflow.md`
4. `creative-brain/lessons/README.md`
5. `creative-brain/sources/README.md`（過去の参考動画・文字起こし台帳）
6. `creative-brain/sources/commercial-nanobanana-kling.md`（詳細なCM制作事例）
7. `creative-brain/integrations/higgsfield-codex.md`

## 参考資料の確度
- `creative-brain/sources/README.md` の A/B/C/D を確認してから主張する。
- A=ユーザーからの全文文字起こし、B=過去会話で要点のみ、C=リンクのみ、D=画面中心の要約。B/C/Dを全文確認済みとして扱わない。
- 参考動画から得た技法と、新たに提案する応用アイデアを区別する。

## Higgsfieldとの受け渡し
- CodexからHiggsfieldへ**直接API連携済みだと主張しない**。
- まず `creative-brain/integrations/higgsfield-codex.md` を読んで、ショット仕様書とプロンプトを作成する。
- Higgsfield側での生成は、認証済みのHiggsfield機能を持つChatGPT環境か、ユーザー本人の操作で実施する。
- 生成結果（ジョブID、モデル、設定、採用理由、失敗、修正）をユーザーが確認できる範囲で記録する。
- 将来API連携を実装する場合は、Higgsfieldの**公式に利用可能な認証・API仕様**を先に検証する。鍵をリポジトリに保存しない。

## 依頼例
「creative-brainの知識を参照し、世界観を固定せず15秒の映像企画を3案提案して。各案で学べる技術を変え、選んだ案の3ショットのHiggsfield用プロンプトと修正手順を作成して」
