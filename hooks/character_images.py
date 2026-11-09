"""Автоматически вставляет иллюстрации на страницы персонажей.

Положите картинку в docs/assets/personazhi/ с именем страницы персонажа:
    docs/assets/personazhi/sigurd.png        -> главная иллюстрация на странице «Сигурд»
    docs/assets/personazhi/sigurd/*.png      -> галерея обликов (по алфавиту имён файлов)
Подойдут .png, .jpg, .jpeg, .webp. Подпись к картинке галереи — имя файла без номера и расширения
(например «03_v-dospehe-nebesnogo-yastreba.png» -> «v dospehe nebesnogo yastreba»), поэтому лучше
называть файлы по-русски: «03_В доспехе Небесного Ястреба.png».
"""
import re
from pathlib import Path

EXT = (".png", ".jpg", ".jpeg", ".webp")


def on_page_markdown(markdown, page, config, files):
    src = page.file.src_uri
    if not src.startswith("personazhi/"):
        return markdown
    stem = Path(src).stem
    root = Path(config["docs_dir"]) / "assets" / "personazhi"
    main = next((root / f"{stem}{e}" for e in EXT if (root / f"{stem}{e}").exists()), None)
    gallery_dir = root / stem
    gallery = sorted(p for p in gallery_dir.glob("*") if p.suffix.lower() in EXT) if gallery_dir.is_dir() else []
    if not main and not gallery:
        return markdown
    title = page.title or stem
    block = []
    if main:
        block.append(f'![{title}](../assets/personazhi/{main.name}){{ .char-portrait loading=lazy }}\n')
    if gallery:
        block.append('<div class="char-gallery" markdown>\n')
        for p in gallery:
            cap = re.sub(r"^\d+[_\-. ]*", "", p.stem).replace("_", " ").replace("-", " ")
            block.append(f'<figure markdown>\n![{cap}](../assets/personazhi/{stem}/{p.name}){{ loading=lazy }}\n<figcaption>{cap}</figcaption>\n</figure>\n')
        block.append("</div>\n")
    lines = markdown.split("\n")
    for i, l in enumerate(lines):
        if l.startswith("# "):
            return "\n".join(lines[: i + 1] + [""] + block + lines[i + 1:])
    return "\n".join(block) + "\n" + markdown
