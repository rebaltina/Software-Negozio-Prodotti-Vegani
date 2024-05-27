# Software-Negozio-Prodotti-Vegani
This repository is the final project for course 1 "porgramming with python" from ProfessionalAI

BioMarket s.a.s ti assume per sviluppare un piccolo software gestionale per la loro nuova bottega in Via Tan 6. Il software deve avere le seguenti funzionalità:
Registrare nuovi prodotti, con nome, quantità, prezzo di vendita e prezzo di acquisto.
Elencare tutti i prodotti presenti.
Registrare le vendite effettuate.
Mostrare i profitti lordi e netti.
Mostrare un menu di aiuto con tutti i comandi disponibili.


Il software è testuale, quindi utilizzabile da riga di comando.

# NOTE
Cerca di scrivere del buon codice organizzando le varie funzionalità in apposite funzioni.
Prima di scrivere il codice, pensa a quali sono le migliori strutture dati da utilizzare: liste, tuple, dizionari, o combinazioni di esse come liste di dizionari.
Il programma deve essere persistente, cioè le informazioni inserite dall'utente devono essere mantenute tra diverse esecuzioni del programma, per fare questo puoi utilizzare un file di testo scegliendo tu che tipo di codifica utilizzare per le informazioni.
Assicurati che gli input inseriti dall'utente siano validi, ad esempio che i numeri siano effettivamente numeri, gestisci i casi non validi con eccezioni e messagi di errore.
Durante un acquisto, verifica che i prodotti acquistati siano effettivamente presenti nel magazzino, nel caso negativo mostra all'utente un messaggio di errore.
Durante l'aggiunta in magazzino, verifica se il prodotto da aggiungere è già presente magazzino, nel caso positivo aggiungi la quantità a quella già presente in magazzino, in questo caso non serve specificare di nuovo il prezzo di acquisto e di vendita, altrimenti registralo come un nuovo prodotto.
Il profitto lordo è il totale delle vendite, cioè tutto ciò che i clienti hanno pagato, il profitto netto invece è pari al profitto lordo meno il costo di acquisto per i prodotti.

# ESEMPIO DI INTERAZIONE CON IL PROGRAMMA (in grassetto l'input dell'utente)


Inserisci un comando: aiuto
I comandi disponibili sono i seguenti:
aggiungi: aggiungi un prodotto al magazzino
elenca: elenca i prodotto in magazzino
vendita: registra una vendita effettuata
profitti: mostra i profitti totali
aiuto: mostra i possibili comandi
chiudi: esci dal programma


Inserisci un comando: aggiungi
Nome del prodotto: latte di soia
Quantità: 20
Prezzo di acquisto: 0.80
Prezzo di vendita: 1.40
AGGIUNTO: 20 X latte di soia


Inserisci un comando: aggiungi
Nome del prodotto: tofu
Quantità: 10
Prezzo di acquisto: 2.20
Prezzo di vendita: 4.19
AGGIUNTO: 10 X tofu


Inserisci un comando: aggiungi
Nome del prodotto: seitan
Quantità: 5
Prezzo di acquisto: 3
Prezzo di vendita: 5.49
AGGIUNTO: 5 X seitan


Inserisci un comando: elenca
PRODOTTO QUANTITA' PREZZO
latte di soia    20                     €1.4
tofu                    10                     €4.19
seitan                5                        €5.49


Inserisci un comando: vendita
Nome del prodotto: latte di soia
Quantità: 5
Aggiungere un altro prodotto ? (si/no): si
Nome del prodotto: tofu
Quantità: 2
Aggiungere un altro prodotto ? (si/no): no
VENDITA REGISTRATA
- 5 X latte di soia: €1.40
- 2 X tofu: €4.19
Totale: €15.38


Inserisci un comando: elenca
PRODOTTO QUANTITA' PREZZO
latte di soia    15                     €1.4
tofu                     8                        €4.19
seitan                 5                        €5.49


Inserisci un comando: vendita
Nome del prodotto: seitan
Quantità: 5
Aggiungere un altro prodotto ? (si/no): no
VENDITA REGISTRATA
5 X seitan: €5.49
Totale: €27.45


Inserisci un comando: elenca
PRODOTTO QUANTITA' PREZZO
latte di soia    15                      €1.4
tofu                     8                        €4.19


Inserisci un comando: profitti
Profitto: lordo=€42.83 netto=€19.43


Inserisci un comando: storna
Comando non valido
I comandi disponibili sono i seguenti:
aggiungi: aggiungi un prodotto al magazzino
elenca: elenca i prodotto in magazzino
vendita: registra una vendita effettuata
profitti: mostra i profitti totali
aiuto: mostra i possibili comandi
chiudi: esci dal programma


Inserisci un comando: chiudi
Bye bye

Punti importanti
Un progetto che non rispetta i seguenti punti verrà respinto


Nel lavoro è fondamentale seguire sempre le specifiche che ci vengono date alla lettera, quindi il programma deve contenere esattamente le funzioni specificate e deve produrre esattamente l'output dell'esempio se riceve lo stesso input.
Una funzione deve fare una e una cosa sola, cerca di scrivere funzioni brevi e concise, se una funzione è troppo lunga è molto probabile che vada spezzata in più funzioni. Approfondimento 1 Approfondimento 2
Sentirai spesso dire che è sempre necessario commentare il codice, falso! Un codice ben scritto si commenta da solo, non usare i commenti per descrivere quello che stai facendo, deve essere chiaro dal codice. Approfondimento 1 Approdondimento 2
Utilizza le docstrings per documentare funzioni, classi e metodi.
I nomi di variabili, funzioni e metodi vanno sempre scritti in inglese, utilizzando lo snake case, il CamelCase va usato solo per i nomi di classi. Non mischiare italiano e inglese, sempre e solo inglese. Approfondimento 1



