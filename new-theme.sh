#!/bin/bash
# 使い方: ./new-theme.sh <テーマ名>
# 例: ./new-theme.sh context-lost

THEME=$1

if [ -z "$THEME" ]; then
  echo "エラー: テーマ名を指定してください"
  echo "使い方: ./new-theme.sh <テーマ名>"
  exit 1
fi

BASE="$(dirname "$0")/themes/$THEME"

if [ -d "$BASE" ]; then
  echo "エラー: '$THEME' は既に存在します"
  exit 1
fi

mkdir -p "$BASE/video/project"
mkdir -p "$BASE/video/素材"
mkdir -p "$BASE/video/書き出し"

cat > "$BASE/script.md" << 'EOF'
# タイトル

Claude CLIあるある

# テーマ



---

# 台本

## 0-3秒

## 3-7秒

## 7-12秒

## 12-16秒

## 16-20秒

## 20-25秒

## 25-30秒

---

# 今日の学び

EOF

echo "✅ 作成完了: themes/$THEME/"
echo ""
echo "次のステップ:"
echo "  1. themes/$THEME/script.md を編集"
echo "  2. ideas/theme-list.md に追加"
