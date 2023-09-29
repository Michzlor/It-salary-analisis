# Analiza zarobków
### 1.Opis
Porównanie zarobków na różnych stanowiskach branży it w różnych miastach w Indiach.

Aplikacja używa bazy danych z tabeli:
https://www.kaggle.com/iamsouravbanerjee/analytics-industry-salaries-2022-india

Użytkownik wybiera miasto - Bangalore, Pune, Hyderabad, New Delhi, Mumbai
Aplikacja zwraca:
- Średnie roczne zarobki na każdym z dostępnych stanowisk w wybranym mieście
- 3 Firmy które płacą najwięcej w danym mieście
- O ile procent powyżej średniej wynoszą zarobki w tych firmach w porównaniu do średnich zarobków na danym stanowisku
- Rekomendacja jakie stanowisko w której firmie jest najbardziej opłacalne 
## 2.Instalacja
#### Wymagania wstępne:
-Python w wersji 3.9.13 lub wyższej
#### Instalacja manualna:

1. Stworzyć katalog dla aplikacji
2. Skopiować wszystkie pliki z repozytorium do utworzonego katalogu
#### Instalacja z użyciem Git:
W terminalu(cmd) wykonać polecenie
>git clone https://github.com/Michzlor/It-salary-analisis

Stworzy ono katalog analiza-zarobkow zawirający pliki aplikacji w aktualnej lokacji(Domyślnie: C/Users/Nazwa użytkownika)

## 3.Uruchomienie

1. Towrzenie środowiska wirtualnego dla aplikacji
W terminalu(cmd) znajdując się w katalogu aplikacji wykonać polecenie
>  python -m venv env
2. Aktywowanie srodowiska
>  env/Scripts/activate
3. Instalacja pakietów używanych przez aplikację do stowrzonego środowiska
> pip install -r requirements.txt
4. Uruchomienie serwera aplikacji. Domyślnie serwer uruchamiany jest pod adresem hosta lokalnego:  http://127.0.0.1:5000

> flask run
