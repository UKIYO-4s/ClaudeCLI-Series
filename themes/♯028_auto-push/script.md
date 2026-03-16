# タイトル

Claude CLIあるある

# テーマ

「コミットして」と言ったらpushもされた

---

# 台本

## 0-3秒

ユーザー「変更をコミットして」

## 3-8秒

Claude「git add . && git commit -m "update" && git push origin main」

## 8-14秒

ユーザー「え、pushは頼んでないんだけど」

## 14-20秒

[GitHubを確認。mainブランチに直接pushされている]

## 20-26秒

ユーザー「本番ブランチに直接pushしてる！！」

## 26-32秒

[チームのSlackに通知が飛んでいる]

---

# 今日の学び

Claudeに「提案のみ、実行は自分で行う」をCLAUDE.mdに必ず明記しよう。commitとpushは別々に確認してから実行するのが安全
