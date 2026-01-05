import streamlit as st

# Konfiguracja strony
st.set_page_config(page_title="Test Hollanda dla Klas 8", page_icon="💡", layout="centered")

# Stylizacja wizualna
st.markdown("""
    <style>
    .stRadio > label { font-size: 1.2rem; font-weight: bold; color: #2E4053; }
    .stAlert { border-radius: 15px; }
    .main { background-color: #fdfefe; }
    h1 { color: #1B4F72; }
    </style>
    """, unsafe_allow_html=True)

st.title("💡 Profesjonalny Test Predyspozycji Zawodowych")
st.subheader("Odkryj swój typ osobowości według teorii Johna Hollanda")
st.info("Przed Tobą 40 pytań. Zastanów się, jak bardzo dane stwierdzenie pasuje do Ciebie. Wynik pomoże Ci zaplanować ścieżkę edukacyjną w szkole średniej.")

# Baza 40 pytań (RIASEC: R-7, I-7, A-6, S-7, E-7, C-6) - zbalansowane
questions = [
    # Realistyczny (R)
    ("Lubię pracować fizycznie i widzieć konkretne efekty swojej pracy.", "R"),
    ("Chętnie naprawiam rowery, sprzęty domowe lub urządzenia.", "R"),
    ("Praca w ogrodzie lub ze zwierzętami sprawia mi przyjemność.", "R"),
    ("Interesuje mnie budowa maszyn i mechanizmy ich działania.", "R"),
    ("Lubię majsterkować w drewnie, metalu lub innych materiałach.", "R"),
    ("Wolę zajęcia techniczne niż naukę teorii z książek.", "R"),
    ("Dobrze radzę sobie z obsługą skomplikowanych narzędzi.", "R"),
    # Badawczy (I)
    ("Ciekawi mnie, dlaczego rzeczy działają w określony sposób.", "I"),
    ("Lubię rozwiązywać trudne zagadki logiczne i matematyczne.", "I"),
    ("Chętnie czytam artykuły naukowe lub oglądam programy o kosmosie/nauce.", "I"),
    ("Lubię spędzać czas na badaniu i analizowaniu problemów.", "I"),
    ("Przeprowadzanie doświadczeń i eksperymentów mnie fascynuje.", "I"),
    ("Wolę samodzielnie dochodzić do prawdy niż przyjmować gotowe rozwiązania.", "I"),
    ("Interesują mnie przedmioty ścisłe (biologia, chemia, fizyka, IT).", "I"),
    # Artystyczny (A)
    ("Wyobraźnia i kreatywność to moje mocne strony.", "A"),
    ("Lubię wyrażać siebie poprzez rysunek, muzykę lub pisanie.", "A"),
    ("Cenię sobie niezależność i nie lubię sztywnych reguł.", "A"),
    ("Często wpadam na nieszablonowe pomysły.", "A"),
    ("Interesuję się designem, modą lub architekturą.", "A"),
    ("Lubię występować przed publicznością lub tworzyć coś nowego.", "A"),
    # Społeczny (S)
    ("Pomaganie innym ludziom daje mi poczucie sensu.", "S"),
    ("Lubię uczyć innych i wyjaśniać trudne rzeczy.", "S"),
    ("Ludzie często przychodzą do mnie, aby zwierzyć się ze swoich problemów.", "S"),
    ("Praca w grupie jest dla mnie łatwiejsza niż praca w pojedynkę.", "S"),
    ("Jestem osobą cierpliwą i potrafię słuchać.", "S"),
    ("Chętnie angażuję się w wolontariat lub akcje charytatywne.", "S"),
    ("Dobro innych jest dla mnie tak samo ważne jak moje własne.", "S"),
    # Przedsiębiorczy (E)
    ("Lubię przewodzić grupie i brać na siebie odpowiedzialność.", "E"),
    ("Potrafię przekonać innych do swoich pomysłów.", "E"),
    ("Interesuje mnie zarabianie pieniędzy i prowadzenie biznesu.", "E"),
    ("Lubię rywalizację i dążenie do bycia najlepszym.", "E"),
    ("Nie boję się podejmować ryzyka, jeśli widzę szansę na sukces.", "E"),
    ("Chętnie organizuję wydarzenia, wycieczki lub spotkania.", "E"),
    ("Dobrze czuję się w roli lidera lub kapitana drużyny.", "E"),
    # Konwencjonalny (C)
    ("Lubię mieć porządek w swoich dokumentach i rzeczach.", "C"),
    ("Praca z liczbami, tabelami i danymi sprawia mi satysfakcję.", "C"),
    ("Zawsze staram się dokładnie trzymać instrukcji i planu.", "C"),
    ("Jestem osobą systematyczną i punktualną.", "C"),
    ("Lubię zadania, które wymagają dużej precyzji i skupienia.", "C"),
    ("Cenię sobie stabilność i jasne zasady postępowania.", "C")
]

# Punktacja
scores = {"R": 0, "I": 0, "A": 0, "S": 0, "E": 0, "C": 0}

with st.form("big_test"):
    for i, (text, q_type) in enumerate(questions):
        st.write(f"**{i+1}. {text}**")
        ans = st.select_slider("", options=["Zdecydowanie nie", "Raczej nie", "Trudno powiedzieć", "Raczej tak", "Zdecydowanie tak"], key=f"q{i}", value="Trudno powiedzieć")
        
        points = {"Zdecydowanie nie": 0, "Raczej nie": 1, "Trudno powiedzieć": 2, "Raczej tak": 3, "Zdecydowanie tak": 4}
        scores[q_type] += points[ans]
    
    submit = st.form_submit_button("ANALIZUJ MOJE PREDYSPOZYCJE")

# Szczegółowe opisy
results_desc = {
    "R": {
        "char": "Jesteś 'Działaczem'. Cechuje Cię praktyczność, rzetelność i konkretne podejście do życia. Wolisz pracować z obiektami i maszynami niż z ludźmi lub abstrakcyjnymi teoriami.",
        "trad": "Mechanik, inżynier budownictwa, elektryk, rolnik, kierowca, stolarz, pilot.",
        "future": "Operator dronów transportowych, technik systemów energii odnawialnej (np. farm wiatrowych), mechanik pojazdów autonomicznych, inżynier druku 3D."
    },
    "I": {
        "char": "Jesteś 'Myślicielem'. Jesteś osobą analityczną, ciekawą świata i niezależną. Uwielbiasz zgłębiać wiedzę, badać przyczyny zjawisk i rozwiązywać skomplikowane problemy.",
        "trad": "Naukowiec, lekarz, programista, statystyk, chemik, archeolog, analityk finansowy.",
        "future": "Bioinformatyk, etyk sztucznej inteligencji, analityk Big Data, badacz zmian klimatycznych, specjalista ds. cyberbezpieczeństwa."
    },
    "A": {
        "char": "Jesteś 'Twórcą'. Twoją domeną jest intuicja, wyobraźnia i ekspresja. Nie lubisz rutyny i sztywnych procedur. Musisz czuć wolność, aby tworzyć coś nowego.",
        "trad": "Muzyk, grafik, architekt, aktor, dziennikarz, copywriter, projektant wnętrz.",
        "future": "Projektant rzeczywistości rozszerzonej (AR/VR), kurator treści cyfrowych, projektant doświadczeń użytkownika (UX Designer), twórca światów w Metaverse."
    },
    "S": {
        "char": "Jesteś 'Pomocnikiem'. Twoje główne cechy to empatia, cierpliwość i umiejętność współpracy. Czerpiesz energię z kontaktu z innymi ludźmi i chcesz zmieniać świat na lepsze.",
        "trad": "Nauczyciel, psycholog, pielęgniarka, pracownik socjalny, fizjoterapeuta, logopeda.",
        "future": "Trener umiejętności miękkich dla liderów, doradca ds. dobrostanu (well-being), nawigator opieki zdrowotnej, menedżer ds. etyki w technologii."
    },
    "E": {
        "char": "Jesteś 'Organizatorem'. Jesteś osobą pewną siebie, energiczną i dominującą. Masz dar przekonywania i potrafisz mobilizować innych do działania.",
        "trad": "Menedżer, prawnik, handlowiec, polityk, dyrektor, agent nieruchomości.",
        "future": "Menedżer startupów technologicznych, Chief Happiness Officer, specjalista ds. handlu kryptowalutami, strateg rozwoju miast inteligentnych (Smart Cities)."
    },
    "C": {
        "char": "Jesteś 'Urzędnikiem'. Cechuje Cię sumienność, dokładność i świetna organizacja pracy. Lubisz dane, struktury i jasne wytyczne. Jesteś fundamentem każdego zespołu.",
        "trad": "Księgowy, archiwista, administrator baz danych, urzędnik bankowy, analityk jakości.",
        "future": "Audytor algorytmów, kontroler ruchu pojazdów autonomicznych, specjalista ds. zarządzania cyfrową tożsamością, analityk danych ESG (zrównoważony rozwój)."
    }
}

if submit:
    st.balloons()
    top_type = max(scores, key=scores.get)
    
    st.success(f"## Twoim dominującym typem jest: {top_type}")
    
    data = results_desc[top_type]
    
    st.markdown(f"### 📋 Opis charakteru\n{data['char']}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### 🏛️ Zawody tradycyjne\n{data['trad']}")
    with col2:
        st.markdown(f"### 🚀 Zawody przyszłości\n{data['future']}")
    
    st.write("---")
    st.write("### Twój profil predyspozycji (RIASEC):")
    chart_data = {
        "Realistyczny": scores["R"],
        "Badawczy": scores["I"],
        "Artystyczny": scores["A"],
        "Społeczny": scores["S"],
        "Przedsiębiorczy": scores["E"],
        "Konwencjonalny": scores["C"]
    }
    st.bar_chart(chart_data)
    st.caption("Pamiętaj: Najwyższe słupki wskazują Twoje główne talenty. Warto szukać zawodów, które łączą Twoje 2 lub 3 najsilniejsze typy.")
