# PILOT-001 — 画像・動画プロンプト

本書は**制作者向けの草案**。教材からの引用ではない。Higgsfield側の現行モデル・生成条件の確認後に実行する。

## 初回画像：Keyframe 01
**EN**:
```
A single clear water droplet resting on a sheet of glass in a dark studio, a narrow beam of warm light passing through the droplet, subtle rainbow refraction on the surface, extraordinary realistic macro photography, crisp natural reflections, restrained cinematic composition, clean background, no text, no logos, vertical 9:16.
```

**日本語の意味**：暗いスタジオのガラス上に透明な水滴が一つ。細い光が水滴を通過して虹色に屈折する。リアルなマクロ撮影、自然な反射、余計な文字や物がない縦型の構図。

**狙い**：一枚で「主役・照明・背景」が明確。次の動画化で変化を検証できる。

**初回の確認ポイント**：水滴が一つか／ガラスの反射が自然か／虹色の屈折が見えるか／背景が複雑すぎないか。

## 動画：S01（採用キー画像を開始画像に指定）
**EN**:
```
The water droplet stays in place as the warm beam of light slowly brightens and reveals subtle colors inside it. Very slow dolly-in camera movement, steady macro focus, realistic light refraction, no new objects, no sudden camera movement.
```
**日本語の意味**：水滴の位置は変えず、光が少しずつ強まり内側の色が現れる。非常にゆっくり近づくカメラ、マクロのピントを維持。新しい物体や急な移動はなし。

**狙い**：物体の形を保ちながら照明とカメラに変化をつける。
**失敗時**：水滴が変形したら `The droplet remains exactly the same shape` を加え、カメラの動きを弱める。

## 動画：S02（開始画像はS01と一貫したマクロ）
**EN**:
```
A narrow beam of light passes through a perfectly clear water droplet, creating a gently shifting rainbow spectrum. Extreme macro close-up, smooth slow camera push-in, stable glass surface and droplet shape, natural optical refraction.
```
**狙い**：光学的な変化を近距離から見せる。虹色が不自然な液体に変わったら速度を落とす。

## 動画：S03
**EN**:
```
The single droplet slowly rolls to the right across the glass, leaving a fleeting band of reflected light. Low-angle macro tracking shot following the droplet, consistent droplet shape and scale, smooth controlled motion.
```
**狙い**：動く主役をカメラが追いかける。水滴が分裂したら移動距離を短くする。

## 画像プロンプトの最小変更法
- カメラだけ変える：`same scene, extreme close-up of the water droplet`
- 光だけ変える：`same scene, slightly warmer sidelight`
- 構図だけ変える：`same scene, move the droplet toward the lower third of the frame`
何を維持するか、何を変更するかを分離し、一度の修正で変える変数を減らす。

## 生成後に保存すること
使用モデルID／画角／尺／プロンプト改訂番号／採用したテイク／問題点／次の修正1つ。
