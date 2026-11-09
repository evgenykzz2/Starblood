# Звездная Кровь — Вики

Неофициальная фанатская энциклопедия вселенной Романа Прокофьева «Звездная Кровь» и «Тысяча Братьев».

**Сайт:** https://evgenykzz2.github.io/Starblood/

Сайт собирается [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) и публикуется на GitHub Pages автоматически при каждом пуше в `main` (`.github/workflows/pages.yml`).

## Локальный просмотр

```bash
pip install -r requirements.txt
mkdocs serve
```

## Структура

| Путь | Что там |
|---|---|
| `docs/mir/` | Механика, космология и история, Народы и фракции, география, Руны |
| `docs/personazhi/` | Досье персонажей и указатели |
| `docs/karta/` | Интерактивная карта мира |
| `docs/slovar.md` | Словарь терминов |
| `docs/knigi/` | Фанатские книги: чтение в браузере и FB2 (генерируются `tools/build_book.py` в star-blood) |
| `docs/assets/personazhi/` | Иллюстрации персонажей (подставляются на страницы автоматически, см. «О вики») |
| `hooks/character_images.py` | Вставка иллюстраций на страницы персонажей |

Тексты статей генерируются из базы знаний в репозитории `evgenykzz2/star-blood` скриптом `tools/build_wiki.py`. Ручные страницы (`index.md`, `o-vike.md`, `oboznacheniya.md`, `karta/index.md`) и `docs/assets/` при пересборке не перезаписываются.

Все права на произведения принадлежат автору. Тексты книг в репозиторий не входят.
