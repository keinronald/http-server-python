# HTTP Server python

### Task-description
*sorry for german*

**Schreiben Sie ein Programm, welches die Prozesse P0, . . . , P6 startet, welche folgende Eigenschaften aufweisen:**
* Jeder Prozess startet mit Hilfe von http.server.HTTPServer einen HTTP Server auf einem eigenen Port. Der Prozess Pi bindet z.B. den Port 17300 + i.
* Jeder Prozess Pi hat einen Zustand Si, welcher initial zufällig aus {0, . . . , 9} gewählt wird. Dieser Zustand wird bei einem HTTP GET zugänglich gemacht wird.2
* Die Prozesse P1, . . . , P6 prüfen alle 0.5 Sekunden den Zustand des Vorgängers: Wenn sich dieser unterscheidet übernehmen sie diesen. (Also Prozess Pi übernimmt den Zustand Si−1.) Der Prozess P0 verhält sich etwas anders: Er prüft alle 0.5 Sekunden den Zustand von P6 und wenn dieser gleich ist, dann inkrementiert er seinen eigenen Zustand modulo 10. (Also S0 wird zu (S0 + 1)%10, falls S0 = S6.) Verwenden Sie urllib.request.urlopen um den Zustand eines Prozesses zu erhalten. Jeder Prozess soll ausgeben, wenn er den Zustand wechselt, und wie dieser lautet.

### Technologie:
* Python
