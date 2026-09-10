#!/usr/bin/env python3
"""Render title cards referenced by front matter; requires Pillow and a Korean font."""

import argparse
import html
import json
from pathlib import Path
import re
import subprocess

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FONT_CANDIDATES = [
    Path('/System/Library/Fonts/AppleSDGothicNeo.ttc'),
    Path('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'),
]


def lines_for(draw, text, font, width):
    lines, line = [], ''
    for word in text.split():
        candidate = (line + ' ' + word).strip()
        if draw.textlength(candidate, font=font) <= width:
            line = candidate
            continue
        if line:
            lines.append(line)
        line = ''
        for char in word:
            if line and draw.textlength(line + char, font=font) > width:
                lines.append(line)
                line = ''
            line += char
    if line:
        lines.append(line)
    return lines


def render(title, destination, font_path):
    canvas = Image.new('RGB', (1200, 630), '#f5f2ed')
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, 0, 18, 630), fill='#26706c')
    small = ImageFont.truetype(str(font_path), 26)
    draw.text((76, 57), 'ROKROKSS  /  ENGINEERING NOTES', font=small, fill='#26706c')
    for size in range(68, 31, -2):
        font = ImageFont.truetype(str(font_path), size)
        lines = lines_for(draw, title, font, 1048)
        if len(lines) * (size + 16) <= 320:
            break
    else:
        raise ValueError(f'Title does not fit: {title}')
    y = 163 + (320 - len(lines) * (size + 16)) // 2
    for line in lines:
        draw.text((76, y), line, font=font, fill='#172d3c')
        y += size + 16
    draw.line((76, 524, 1124, 524), fill='#c8d5d2', width=2)
    draw.text((76, 553), '김형록 · 개발과 실험의 기록', font=small, fill='#465962')
    draw.text((865, 553), 'kimhyungrok.com', font=small, fill='#465962')
    destination.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(destination, optimize=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--font', type=Path, help='Path to a Korean-capable TTF or TTC font')
    args = parser.parse_args()
    font = args.font or next((p for p in FONT_CANDIDATES if p.is_file()), None)
    if font is None:
        parser.error('Pass --font with a Korean-capable font file.')
    # Read actual YAML with Ruby, which is already needed by Jekyll.
    script = '''
      records = [YAML.safe_load(File.read('_config.yml'), aliases: true)]
      Dir['_posts/*.md'].sort.each do |file|
        front_matter = File.read(file).split(/^---\\s*$\\n?/)[1]
        records << YAML.safe_load(front_matter, permitted_classes: [Date, Time], aliases: true)
      end
      puts JSON.generate(records)
    '''
    records = json.loads(subprocess.check_output(
        ['ruby', '-rdate', '-ryaml', '-rjson', '-e', script], cwd=ROOT, text=True))
    count = 0
    for record in records:
        image = record.get('image', '')
        if not image.startswith('/assets/images/social/'):
            continue
        title = html.unescape(re.sub('<[^>]+>', '', record['title']))
        if image.endswith('/site.png'):
            title = '김형록의 개발 블로그'
        render(title, ROOT / image.lstrip('/'), font)
        count += 1
    print(f'Generated {count} social cards (1200x630 PNG).')


if __name__ == '__main__':
    main()
