# タイトル

Claude CLIあるある

# テーマ

.envファイルをgitにコミット提案された

---

# 台本

## 0-3秒

ユーザー「変更をコミットして」

## 3-8秒

Claude「git add . && git commit -m "add config"」

## 8-14秒

ユーザー「あ、.gitignoreに.env書いてあるのに…」

## 14-20秒

[.envがステージングに含まれている]

## 20-26秒

[pushされた後、数分後にメール]

「⚠️ GitGuardian: Secret detected in your repository」

## 26-32秒

ユーザー「終わった…」

---

# 今日の学び

git addは必ず自分で確認してから実行。「git add .」を丸投げすると.gitignore漏れが起きることがある。Claudeにはコマンドの提案のみさせて、実行は自分で行おう
