# Codex × Higgsfield：制作連携 v0.1

## 現在できること（2026-11-15 時点の構想・実装）
- **Codex**：GitHubのこの知識ベースを読んで、企画・ショットリスト・プロンプト・評価のひな型を作れる。
- **Higgsfield**：ChatGPTに接続済みのHiggsfield機能、またはユーザーのブラウザから画像・動画を制作できる。
- **受け渡し**：企画と生成条件をMarkdownで記録し、生成後の結果を追記する。人が確認する「半自動」方式。
- **未実装**：CodexからのHiggsfield自動ジョブ送信、結果の自動同期、課金の自動実行、Instagramデータの自動取得。単にGitHubリポジトリを接続しただけではこれらは起きない。

## ワークフロー
1. 制作者が「作りたい体験 / 試したい技術」を決める。
2. Codexが `projects/project-template.md` を使って企画・ショットリスト・プロンプトを準備する。
3. 必要ならChatGPT経由のHiggsfield連携で**使用可能モデルと料金・入力条件を確認**。モデルの存在やパラメータを決め打ちしない。
4. ユーザーが生成の実行を明示した時点で、対応するHiggsfield機能またはHiggsfield画面を使う。
5. 出力を見て「採用 / 修正 / 再生成」を判断する。カメラ動作、人物・小道具の崩れ、構図を記録。
6. 完成した映像を編集し、音楽と合わせる。素材の利用権と公開許可を確認する。
7. 公開後の反応と技術的な学びを分析し、次の実験に活かす。

## ショット受け渡しテンプレート
~~~yaml
project: "仮の作品名"
objective: "今回試す技術"
format:
  aspect_ratio: "9:16"
  duration_target_seconds: 15
references:
  - "権利を確認した素材の保管場所・説明"
shots:
  - id: "S01"
    role: "導入"
    subject: "誰・何"
    action: "画面内で何が変化するか"
    scene: "場所・光・色"
    shot_size: "wide / medium / close-up"
    camera: "固定 / dolly-in / orbit / pan など"
    image_prompt: ""
    video_prompt: ""
    model: "実行前に対応モデルを確認"
    status: "planned"
review:
  good: []
  issues: []
  next_change: ""
~~~

## プロンプトの基本構成
**被写体 + 行動 + 場所 + 撮影 + 雰囲気 + 制約**。画像修正では「変える部分」と「維持する部分」を分けて伝える。

例（教材原文ではなく学習用）：
- IMAGE: `A ceramic cup on a wooden table at dawn, warm side light, cinematic close-up, shallow depth of field.`
- VIDEO: `The cup remains still while sunlight slowly moves across the table. Slow dolly-in, stable framing, no new objects.`

## 注意
- 特定モデル（Soul / Kling / Nano Bananaなど）は利用可否と仕様が変わる。毎回Higgsfieldで確認する。
- 著作権で保護された音楽や肖像・ブランドの商用利用を当然とみなさない。
- **現在のリポジトリはPublic**。実際の顧客素材や公開前の秘密は保存しない。Private化を確認してから機密情報を扱う。
- 公開動画そのものを大量にリポジトリへ保存すると容量・権利の問題がある。学習メモと許諾を得た参照情報を優先する。

## 次の技術段階（未着手）
- Higgsfieldに公式の外部API・認証経路があるかを確認する。
- 利用規約と料金管理を満たした上で、環境変数による認証、送信、状態取得、結果保存を実装する。
- GitHub Actions等から勝手に有料ジョブが動かないよう、明示承認と予算上限を組み込む。
