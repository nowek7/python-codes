# Znajdź wszystkie pliki .c zmodyfikowane później niż plik Makefile
find . -name '*.c' -newer Makefile -print

# Skonstruuj archiwum zip/tar z plików z kodów źródłowych
zip archive.zip *.h *.c

# Lub
tar cvf archive.tar *.h *.c

# Które pliki zostały zmienione w ostatnim tygodniu?
find . -name '*.cpp' -mtime +7 -print

# Który z plików korzysta z include iostream?
find . -name '*.cpp' -mtime +7 -print | xargs grep 'iostream'

# lista unikatowych pakietów bezpośrednio importowane przez kod, zapisane do pliku
grep '^import ' *.java |
  sed -e 's/.*import *//' -e 's/;.*$//' |
    sort -u >list