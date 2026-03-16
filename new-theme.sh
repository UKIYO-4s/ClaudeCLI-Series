#!/bin/bash
# 使い方: ./new-theme.sh <テーマ名> [--codex]
# 例（Claude CLIあるある）: ./new-theme.sh context-lost
# 例（Codexあるある）:      ./new-theme.sh copilot-hallucination --codex

THEME=""
SERIES="claude"

for arg in "$@"; do
  if [ "$arg" = "--codex" ]; then
    SERIES="codex"
  else
    THEME="$arg"
  fi
done

if [ -z "$THEME" ]; then
  echo "エラー: テーマ名を指定してください"
  echo "使い方: ./new-theme.sh <テーマ名> [--codex]"
  exit 1
fi

if [ "$SERIES" = "codex" ]; then
  FOLDER="themes-codex"
  TITLE="Codexあるある"
else
  FOLDER="themes"
  TITLE="Claude CLIあるある"
fi

BASE="$(dirname "$0")/$FOLDER/$THEME"

if [ -d "$BASE" ]; then
  echo "エラー: '$THEME' は既に存在します"
  exit 1
fi

mkdir -p "$BASE/video/project"
mkdir -p "$BASE/video/素材"
mkdir -p "$BASE/video/書き出し"

cat > "$BASE/script.md" << EOF
# タイトル

$TITLE

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

echo "✅ 作成完了: $FOLDER/$THEME/"
echo ""
echo "次のステップ:"
echo "  1. $FOLDER/$THEME/script.md を編集"
echo "  2. ideas/theme-list.md に追加"
