/**
# Felhasználói fiók jelszó visszaállítása

Ez a funkció lehetővé teszi a felhasználók számára, hogy elfelejtett vagy elveszített jelszavukat biztonságosan visszaállítsák.

## Elfelejtett jelszó jelenség

Az "elfelejtett jelszó" gyakori probléma a felhasználói rendszerekben, amikor a felhasználó nem emlékszik a belépéshez szükséges jelszóra. Ez előfordulhat ritka bejelentkezés, több fiók használata vagy egyszerű figyelmetlenség miatt. A rendszernek ezért biztosítania kell egy biztonságos és egyszerű módot a jelszó visszaállítására, hogy a felhasználó hozzáférése helyreállítható legyen anélkül, hogy veszélyeztetné a fiók biztonságát.

## Teendők elfelejtett jelszó esetén

1. **Nyisd meg a bejelentkezési oldalt.**
2. Kattints az **"Elfelejtett jelszó"** linkre.
3. Add meg a regisztrált e-mail címedet vagy felhasználónevedet.
4. Ellenőrizd a postafiókodat, és keresd meg a jelszó-visszaállítási e-mailt.
5. Kattints az e-mailben kapott visszaállítási linkre, vagy használd a kapott kódot.
6. Állíts be egy új, biztonságos jelszót a fiókodhoz.

## Folyamat áttekintése

1. Felhasználó azonosítása (e-mail vagy felhasználónév alapján).
2. Jelszó-visszaállítási token generálása és elküldése.
3. Token érvényességének ellenőrzése.
4. Új jelszó beállítása a token felhasználásával.

## Biztonsági megfontolások

- A token csak egyszer használható és időkorlátos.
- A jelszó-visszaállítási folyamat naplózásra kerül.
- Az új jelszónak meg kell felelnie a rendszer jelszókövetelményeinek.
