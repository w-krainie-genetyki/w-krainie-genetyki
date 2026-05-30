# 🧬 w_krainie_genetyki

> Jedno miejsce na polską genetykę — aktualności, grupy badawcze, konferencje i kursy.

Strona społecznościowa dla polskiej społeczności genetycznej. Hostowana na GitHub Pages.

**→ [w_krainie_genetyki.github.io](https://w-krainie-genetyki.github.io)**

---

## Sekcje

| Sekcja | Opis |
|---|---|
| **Aktualności** | Publikacje, nagrody, granty, ważne ogłoszenia |
| **Grupy badawcze** | Laboratoria i ośrodki genetyki w Polsce |
| **Konferencje** | Sympozja, meetupy, kongresy z datami i linkami |
| **Kursy** | Szkolenia, webinary, kursy online i stacjonarne |

---

## Jak zgłosić wpis?

Użyj formularza na stronie: **[Zgłoś wpis →](submit.html)**

Możesz zgłaszać:
- konferencje i sympozja
- meetupy i spotkania tematyczne
- kursy, szkolenia, webinary
- nowe projekty lub grupy badawcze
- ważne publikacje i granty

Wpisy są weryfikowane i publikowane bezpłatnie.

---

## Struktura repozytorium

```
/
├── index.html          # Strona główna
├── submit.html         # Formularz zgłoszenia wpisu
├── privacy.html        # Polityka prywatności
├── aktualnosci.html    # Archiwum aktualności (do rozbudowy)
├── grupy.html          # Pełna lista grup badawczych (do rozbudowy)
├── konferencje.html    # Pełna lista konferencji (do rozbudowy)
├── kursy.html          # Pełna lista kursów (do rozbudowy)
└── README.md
```

---

## Lokalny podgląd

Nie potrzebujesz żadnego frameworka — to statyczny HTML/CSS.

```bash
git clone https://github.com/TWOJ_USERNAME/w-krainie-genetyki.git
cd w-krainie-genetyki
# Otwórz index.html w przeglądarce lub użyj prostego serwera:
python3 -m http.server 8080
```

---

## Wdrożenie na GitHub Pages

1. Utwórz repozytorium o nazwie `w-krainie-genetyki` (lub `TWOJ_USERNAME.github.io`)
2. Wgraj pliki do brancha `main`
3. W ustawieniach repozytorium: **Settings → Pages → Source: Deploy from branch → main / (root)**
4. Strona będzie dostępna pod adresem `https://TWOJ_USERNAME.github.io/w-krainie-genetyki`

> Uwaga: w tym repo działa automatyczne wdrożenie GitHub Pages z workflow `.github/workflows/pages.yml`. Każdy push do `main` odświeży stronę.

### Formularz zgłoszeniowy

Strona korzysta z [Formspree](https://formspree.io) do obsługi formularza. Aby go aktywować:
1. Załóż konto na formspree.io
2. Utwórz nowy formularz i skopiuj ID
3. W pliku `submit.html` zamień `YOUR_FORM_ID` na swoje ID Formspree

---

## Chcesz pomóc?

Pull requesty mile widziane! Możesz:
- dodawać wpisy przez edycję HTML (lub zgłaszać przez formularz)
- zgłaszać błędy w zakładce **Issues**
- proponować nowe sekcje lub funkcjonalności

---

## Licencja

MIT — używaj swobodnie, pamiętaj o podaniu źródła.

---

*Prowadzone przez społeczność. Dla społeczności.*
