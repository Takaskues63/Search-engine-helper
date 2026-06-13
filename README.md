# Fuzzy Name Search

A lightweight Python script that finds matching names from a list even when the search query contains typos or misspellings. Originally built for searching anime, movies, or any other titles by name.

## How It Works

The algorithm uses a **dual-condition matching** system — a name is added to results if either condition is satisfied:

1. **Per-word match** — at least **70%** of a single word's letters are found in the query.
2. **Whole-name match** — at least **54%** of the full name's letters (spaces excluded) are found across the entire query.

This two-pronged approach handles both partial matches (you remember one word clearly) and fuzzy full-title matches (you roughly remember the whole thing but with typos).

**Example:**
```
Enter name: jujucu kasen
['Jujutsu Kaisen']

Enter name: won pece
['One Piece']

Enter name: apotecary
['Apothecary Diaries']

Enter name: modao
['Mo Dao Zu Shi']
```

## Getting Started

No external libraries needed — runs on pure Python 3.

```bash
python search.py
```

You'll be prompted to enter a name. Type `x` to exit.

## Customizing the Name List

Edit the `names` list at the top of the script to add your own titles:

```python
names = ['Jujutsu Kaisen', 'MoDao ZuShi', 'One Piece', 'Apothecary Diaries']
```

> Words within a title are split by spaces.

## Adjusting Sensitivity

Two thresholds control matching behavior:

```python
# Per-word threshold
if len(same_letters) / len(word) >= 0.70 ...

# Whole-name threshold
... or len(same_letters_in_name) / len(name) >= 0.54
```

| Threshold | Default | Lower → more matches | Higher → fewer false positives |
|-----------|---------|----------------------|-------------------------------|
| Per-word  | `0.70`  | `0.55`               | `0.85`                        |
| Full-name | `0.54`  | `0.40`               | `0.65`                        |

## Limitations

- The search is **order-independent**: letters are matched regardless of their position, so very short words (1–2 letters) may match too broadly.
- **Case-insensitive** — all comparisons are done in lowercase, and results are printed in lowercase.
