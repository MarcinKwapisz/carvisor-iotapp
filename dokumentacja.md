# CarVisor Moduł IoT
## Autor: Marcin Kwapisz

### Aplikacja jest podzielona na dwie aplikacje które są uruchamiane przy starcie systemu
### APIMiddleware i savingModule są uruchamiane razem i działają jako pośrednik między główną aplikacją i serwerem, obsługują także zapis danych w przypadku niepowodzenia w przesyle na serwer

### main jest główną aplikacją która obsługuje wszystkie pozostałe funkcjonalności i pracuje bezpośrednio z pojazdem oraz dołączonymi fizycznymi modułami

## Moduły:

#### - Main
    Jest to moduł początkowy programu, wywołuje on pozostałe moduły
#### - API
    Moduł ten zarządza komunikacją z serwerem oraz odbiera i przesyła dane
    na/z serwera. 
#### - APIMiddleware
    Moduł współpracujący z głównym programem, działa jako pośrednik pomiędzy nim a serwerem
#### - BT
    Moduł do inicjalizacji połączenia z aplikacją mobilną po BT w celu odebrania pierwszej konfiguracji
#### - Config
    Moduł do odbierania, zmiany i propagowania opcji konfiguracyjnych dla
    urządzenia
#### - NFC
    Moduł ten obsługuje urządzenie NFC do odczytu tagów użytkowników
#### - OBD
    Moduł ten zarządza połączeniem urządzenia IoT z interfejsem OBD
#### - Send
    Moduł służący do przygotowania danych do przesłania na serwer
#### - Saver
    Moduł służący do przechowywania danych do późniejszego przesłania na serwer
#### - Gps
    Moduł służący do obsługi modułu GPS lub jego emulacji
#### - APIMiddleware
    Moduł służący jako pośrednik między głównym programem a serwerem 
    w celu sprawnego przesyłania nawet przy słabym połączeniu

## Funkcje modułów

### API
    
    POST
    Funkcja do wysyłania żądania POST do serwera
    Wartości:
        url - adres na który ma zostać przesłane zapytanie
        data_to_send - JSON z danymi do przesłania
####
    GET
    Funkcja do wysyłania żądania GET do serwera
    Wartości:
        url - adres na który ma zostać przesłane zapytanie
####
    send_path
    Funkcja przesyłająca adres serwera do modułu saver
    Wartości:
        address - adres serwera
####
    start_session_car
    Funkcja służaca do rozpoczęcia sesji z serwerem
####
    check_authorization
    Funkcja wysyłająca zapytanie do serwera o podanie statusu autoryzacji
####
    get_config_from_server
    Funkcja wysyłająca zapytanie do serwera o podanie aktualnej 
    konfiguracji dla urządzenia
####
    send_obd_data
    Funkcja wysyłająca dane(obd, gps, time) na serwer
    Wartości:
        obd_data - dane do przesłania na serwer
####
    start_track
    Funkcja wysyłająca na serwer informacje o rozpoczęciu trasy
    Wartości:
        tag - tag NFC użytkownika
####
    create_own_response
    Funkcja służąca do tworzenia własnej odpowiedzi od serwera
### APIMiddleware

    send
    Funkcja do przesyłania danych z trasy na serwer w sposób współbieżny
    Wartości:
        path - adres na który ma zostać przesłane zapytanie
####
    send_path 
    Funkcja przesyłająca adres serwera do modułu saver
    Wartości:
        path - adres serwera
####
    index
    Funkcja obsługująca wszystkie pozostałe żądania
    Wartości:
        path - adres na który ma zostać przesłane zapytanie
####
    send_obd
    Funkcja współpracująca z funkcją send, wysyła dane z trasy na serwer
    Wartości:
        path - adres na który ma zostać przesłane zapytanie
        data - JSON z danymi do przesłania
####
    send_obd_saved
    Funkcja do przesyłu danych z trasy które nie mogły zostać przesłane
    Wartości:
        path - adres na który ma zostać przesłane zapytanie
        data - JSON z danymi do przesłania
####
    create_own_response
    Funkcja służąca do tworzenia własnej odpowiedzi od serwera
### BT
    connect
    Funkcja do inicjalizacji połączenia BT i odebrania danych logowania
### Config
    create_new_config
    Funkcja tworząca nowy plik konfiguracyjny w przypadku braku takiego pliku 
    oraz uruchamiająca oczekiwanie na konfigurację z aplikacji mobilnej
####
    check_server_credentials
    Funkcja sprawdzająca czy plik konfiguracyjny posiada konfiguracje
####
    section_returner
    Funkcja zwracająca zadaną sekcje z pliku konfiguracyjnego
    Wartości:
        section - żądana sekcja pliku konfiguracyjnego
####
    get_config_from_server
    Funkcja wysyłająca żądanie pobrania konfiguracji
    dla urządzeniada modułu API 
    Warości: 
        config - zainicjalizowany plik konfiguracyjny
####
    return_send_interval
    Funkcja zwracająca częstotliwość wysyłania danych na serwer
### GPS

####
    gps
    Funkcja odczytująca i zapisująca odczyty z modułu GPS
####
    get_only_position_values
    Funkcja zwracająca pozycję GPS w formacie listy
####
    get_position
    Funkcja zwracająca pozycję GPS w formacie gotowym do przesłania jako JSON
### Main

    __init__
    Funkcja odpowiedzialna za inicjalizację modułów oraz kolejne wywołania funkcji
####
    start_logging
    Funkcja rozpoczynająca logowanie działania aplikacji
####
    init_obd
    Funkcja rozpoczynająca połączenie z pojazdem
####
    start_obd_reading
    Funkcja rozpoczynająca odczyt z interfejsu OBD
### NFC
    get_tag
    Funkcja odpowiedzialna za odczyt tagu NFC do logowania
### OBD
    logging
    Funkcja określająca wyświetlanie logów OBD o danej ważności
####
    start_read
    Funkcja dodająca parametry do odczytu przez interfejs OBD
####
    check_supported_commands
    Funkcja zwracająca liste wspieranych parametrów przez interfejs OBD
### Send
    pack
    Funkcja pakująca dane dostarczone przez moduł OBD
    Wartości:
        value - wartość informacji z pojazdu
        name - identyfikator wartości
####
    get_new_timestamp
    Funkcja pobierająca nowy timestamp na potrzeby kolejnej iteracji
####
    new_iteration
    Funkcja czyszcząca zmienne dla następnej iteracji danych
####
    prepare_to_send
    Funkcja przygotowująca dane do przesłania na serwer przy pomocy modułu API
### Saver

    insert
    Funkcja obsługująca problematykę zapisu współbierznego
    Wartości:
        base - baza do której mają być zapisane dane
        data - dane do zapisania w bazie
        counter - wewnętrzny licznik
####
    get_all_data
    Funkcja pobierająca wszystkie dane z bazy
####
    get_amount_of_data
    Funkcja pobierająca ilość wpisów w bazie
####
    get_path
    Funkcja do zapisania adresu serwera
    Wartości:
        path - adres serwera
####
    remove_entry
    Funkcja usuwająca wpis z bazy
    Wartości:
        doc_id - id wiersza w bazie
####
    send_obd_data
    Funkcja Zapisująca dane w przypadku braku możliwości ich wysłania
    Wartości:
        obd_data - dane do zapisu do bazy
####
    send_payload
    Funkcja wysyłająca dane na serwer w przypadku przywrócenia połączenia

---
# Testy

- Sprawdzanie czy dane z modułu send są poprawnie przesyłane do modułu API
- Sprawdzanie połączenia z serwerem
- Sprawdzanie czy dane są poprawnie zapisywane w lokalnej bazie
- Sprawdzanie czy odczyty z GPS są prawidłowe