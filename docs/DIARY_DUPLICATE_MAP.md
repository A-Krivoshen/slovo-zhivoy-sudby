# Diary chapter duplicate map

**Date:** 2026-08-01  
**Rule:** one original_page → one primary full transcription; secondary chapters may link or quote briefly.

| original_page | Chapters with marker | Primary (full text) | Secondary action |
|--------------:|----------------------|---------------------|------------------|
| 012–013 | 02, 03 | **02** `otec-brak-deti` | 03: keep only if different narrative context; else link to 02 |
| 021 | 04, 05, 06 | **04** `voyna-1941` | 05/06: remove full re-post of 021 if present; link |
| 028–030 | 05, 06 | **05** `otec-vchk-i-stikhi` | 06: newspaper/docs ownership starts 041; drop 028–030 full dump if identical |
| 039–040 | 03, 06 | **03** `detstvo-moskva` | 06: link if only narrative overlap |
| 058 | 08 | **08** | — |
| 060 | 08 | **08** (note: partial of 058) | Mark as alternate scan, not new story |
| 067–068 | 08 | **08** (067 primary; 068 = 180° duplicate) | Keep archival markers; do not invent second story |
| 005–006 | 00 | **00** (005 primary; 006 alternate leaf scan) | physical_leaf_id: genealogy-krivoshein-01 |
| 101–102 | 12 | **12** (`str-101` primary figure; `str-102` alternate_scan only) | Same civil-defense exam photograph (two page-scan orientations). Chapter shows only 101 figure + short archive note for 102. Keep both files on disk. Gallery must not list both. |

## Large “FACTS EXTRACTED” blocks

These are **editor working reports**, not diplomatic transcription.

| Location | Action |
|----------|--------|
| RU/EN 03, 05, 06, 08, 09 facts sections | Remove from public content; move summary to `docs/transcription/` if needed |
| Orientation tables `pages/*.jpg` vs `work/p-*.jpg` | Remove from public |

## Newspaper / long document re-posts

Full newspaper text (e.g. *Pravda* / prison lists) must appear once:

- Prefer **chapter 06** or **chapter 09** / dedicated `dokumenty/` page for document-type sources.  
- Chapter 05 should keep narrative + short quote + link.

## Status after cleanup

Secondary chapters keep:

- page markers for navigation only where a short bridge is needed;  
- or an `archive_note` with link to the primary chapter URL.
