"""
Claude CLI あるある - ターミナル画像生成スクリプト

Usage:
  python3 generate_image.py --theme english-switch
  python3 generate_image.py --theme english-switch --size 22
"""

import argparse
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# パス設定
BASE_DIR = Path(__file__).parent.parent
BG_PATH = BASE_DIR / "assets/backgrounds/BG.png"
FONT_DIR = BASE_DIR / "assets/fonts/MoralerspaceHWJPDOC_v2.0.0"
FONT_REGULAR = FONT_DIR / "MoralerspaceArgonHWJPDOC-Regular.ttf"

# テキスト設定
USER_TEXT   = "ついでにコメントも追加して"
CLAUDE_TEXT = "Sure. Here's the updated version with detailed comments explaining the asynchronous processing and possible edge cases"

# グレーバー領域（y=162〜187）
GRAY_BAR_Y   = 162
GRAY_BAR_H   = 26  # 187 - 162 + 1 ≈ 26px
USER_TEXT_X  = 42  # ">" の右隣から

# Claudeテキスト領域
CLAUDE_TEXT_X = 40
CLAUDE_TEXT_Y = 210
WRAP_WIDTH    = 58  # 1行あたりの文字数（半角換算）


def generate(output_path: Path, font_size: int = 24):
    img = Image.open(BG_PATH).convert("RGBA")
    draw = ImageDraw.Draw(img)

    font_claude = ImageFont.truetype(str(FONT_REGULAR), font_size)
    font_user   = ImageFont.truetype(str(FONT_REGULAR), font_size - 4)

    # ユーザーテキストをグレーバー内に縦中央揃えで配置
    user_y = GRAY_BAR_Y + (GRAY_BAR_H - (font_size - 4)) // 2
    draw.text((USER_TEXT_X, user_y), USER_TEXT, font=font_user, fill=(255, 255, 255))

    # Claudeテキストを折り返して配置
    wrapped_lines = textwrap.wrap(CLAUDE_TEXT, width=WRAP_WIDTH)
    y = CLAUDE_TEXT_Y
    line_height = font_size + 8
    for line in wrapped_lines:
        draw.text((CLAUDE_TEXT_X, y), line, font=font_claude, fill=(255, 255, 255))
        y += line_height

    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(str(output_path))
    print(f"保存しました: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="ターミナル画像生成")
    parser.add_argument("--theme", default="english-switch", help="テーマ名")
    parser.add_argument("--output", default=None, help="出力ファイル名")
    parser.add_argument("--size", type=int, default=24, help="Claudeテキストのフォントサイズ（デフォルト24）")
    args = parser.parse_args()

    output_path = Path(args.output) if args.output else \
        BASE_DIR / f"themes/{args.theme}/video/素材/claude_response.png"

    generate(output_path, font_size=args.size)


if __name__ == "__main__":
    main()
