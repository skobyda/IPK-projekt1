# IPK Projekt 1 - Varianta 2: Klient pro OpenWeatherMap API

[![N|Solid](https://www.fit.vutbr.cz/images/fitnewz.png)](https://www.fit.vutbr.cz/)
Autor: Simon Kobyda, FIT VUTBR

## Špecifikácia

Skript na získanie informácii o počasí pomocou OpenWeatherMap API.

## Technické informácie

* __Programovací jazyk__: Python 3
* __Použité moduly__: 
    * [socket](https://docs.python.org/3/library/socket.html): Práca s BSD socket interface
    * [json](https://docs.python.org/3/library/json.html): Spracovanie výstupu formátu JSON poskytnutého od [OpenWeather API](https://openweathermap.org/current#current_JSON)

## Stručný popis skriptu

HTTP dotazovanie je uskutočnené pomocou socketov. V prvom rade je je vytvorený socket typu SOCK_STREAM, adresovej rodiny  AF_INET. Socket je pripojený na host api.openweathermap.org a port 80. GET HTTP dotaz je zaslaný a odpoveď prijatá.
Po skontrolovaní hlavičky a správneho návratového kódu je z odpovedi naparsovaná JSON formulácia informácii o počasí.
Jednotlivé informácie sú vypisované. Try-catch je použitý na odignorovanie jednotlivých chýbajúcich informácii o počasí.

