# TestFramework
Framework testowy do automatyzacji testów.
Przygotowanie frameworka opartego na Selenium Web Driver.
Funkcjonalność:
- Pobieranie danych testowych. 
	Dane utrzymane w pliku w formacie csv docelowo może baza danych. 
	TCName|Enviroment|App_ver|Start_date|data
	Gdzie:
	Data będzie słownikiem lub dane będą w formacie json.
Dane będą pobierane dla uruchamianego TestCase i dostarczane do TestCase.
Dane będzie można pobrać wszystkie lub pojedynczo.
- Test Case – budowanie zestawów testowych przy pomocy Test Step
	Pobranie danych
	Wywołanie zdefiniowanych Test Step i weryfikacja wyników
	Zapis wyniku testu
- Test Step – zaimplementowana strona, która ma być testowana. Przyjmuje dane testowe, oraz tryb w jakim ma być uruchomiona.
	Przygotowanie danych testowych
	Definicja obiektów z testowanej strony, które będą wykorzystywane w Test Step
Kroki wykonywane na stronie (uzupełnianie danych, klikanie w przyciski, zaczytywanie oczekiwanych rezultatów, wybór elementów z listy, obsługa różnych typów elementów)
- Zapis rezultatów uruchomionych testów. 
	Zapis rezultatów do pliku csv. Plik przyrostowy
	TCName|Enviroment|App_ver|Start_date|End_date|Result|Error
Dodatkowo:
W przypadku gdy TestCase zakończy się niepowodzeniem podczas wykonywania, uruchomiony będzie kolejny test.
Wyłapywanie pojawiających się błędów i zapis w raporcie
Weryfikacja zapisu danych w bazie danych
