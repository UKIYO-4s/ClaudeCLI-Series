# タイトル

Claude CLIあるある

# テーマ

２を連打していたらたまにYes NoでNoになってしまう

---

# 台本

## 0-3秒

ユーザー「Claudeがコマンドの許可を次々と聞いてくる」

## 3-8秒

[3択バージョンの確認画面]

```
Do you want to proceed?
  1. Yes
❯ 2. Yes, and don't ask again for: du:*
  3. No
```

ユーザー「2連打で一気に許可しよう」[2を連打]

## 8-14秒

[また3択バージョン]

```
Do you want to proceed?
  1. Yes
❯ 2. Yes, and don't ask again for: ls:*
  3. No
```

ユーザー「はいはい」[2を連打]

## 14-20秒

[突然2択バージョンに切り替わる]

```
Command contains newlines that could separate multiple commands

Do you want to proceed?
❯ 1. Yes
  2. No
```

## 20-26秒

ユーザー「はいはい」[勢いで2を押してしまう]

## 26-32秒

Claude「キャンセルしました」

## 32-38秒

ユーザー「あれ？なんで止まってる？」

## 38-45秒

[さっきの2択画面に気づく]

ユーザー「2択でNoを選んでた…」

---

# 今日の学び

3択の「2」と2択の「2」は意味が違う。画面が切り替わったら一度手を止めて選択肢を確認しよう
