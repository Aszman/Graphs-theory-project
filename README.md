# Projekt zaliczeniowy - Teoria Grafów 

## Instrukcja uruchomienia algorytmu

Algorytm Bellmana-Forda został zaimplementowany w języku *Python* i znajduje się w podfolderze **Algorithm** w pliku _BellmanFord.py_.
Dane do algorytmu są pobierane z pliku _data.json_, a wynik wyświetlany w konsoli i zapisywany do pliku _results.txt_


> ### Wszystkie powyższe pliki muszą znajdować się w tym samym katalogu

## Format danych w pliku data.json

```python
[
  ["begin_node", "end_node"],
  ["node_from", "node_to", "edge_weight"],
  ["node_from", "node_to", "edge_weight"],
  ⋮
  ["node_from", "node_to", "edge_weight"]
]
```
Pierwszy element listy składa się z wierzchołka początkowego i wierzchołka końcowego ścieżki. 
>Jeśli węzeł końcowy nie należy do grafu, to program wyświetli wagę i poprzedni węzeł dla każdego wierzchołka. 

Każdy kolejny element to krawędź grafu opisana poniższą kolejnością:
* _początek krawędzi_
* _koniec krawędzi_
* _waga krawędzi_
