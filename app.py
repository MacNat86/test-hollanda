import streamlit as st

# Konfiguracja strony
st.set_page_config(page_title="Test Hollanda dla Klas 8", page_icon="🚀")

# Stylizacja
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stRadio > label { font-size: 1.1rem; color: #1f77b4; font-weight: 600; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #1f77b4; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Test Predyspozycji Zawodowych")
st.subheader("Dowiedz się, który typ osobowości zawodowej opisuje Ciebie najlepiej!")
st.write("Przeczytaj poniższe stwierdzenia i zaznacz, w jakim stopniu do Ciebie pasują. Nie ma złych odpowiedzi!")

# Baza 25 pytań przypisanych do typów: R, I, A, S, E, C
questions = [
    ("Lubię naprawiać zepsute przedmioty i urządzenia.", "R"),
    ("Chętnie rozwiązuję zadania matematyczne lub logiczne.", "I"),
    ("Szybko wymyślam nowe, oryginalne pomysły.", "A"),
    ("Lubię tłumaczyć innym trudne zagadnienia.", "S"),
    ("Lubię brać odpowiedzialność za pracę grupy.", "E"),
    ("Zwracam dużą uwagę na szczegóły i porządek w notatkach.", "C"),
    ("Praca na świeżym powietrzu jest dla mnie atrakcyjna.", "R"),
    ("Interesuje mnie, jak działają nowe technologie i nauka.", "I"),
    ("Lubię zajęcia artystyczne (muzyka, plastyka, teatr).", "A"),
    ("Pomaganie innym sprawia mi dużą satysfakcję.", "S"),
    ("Potrafię przekonać innych do swojego zdania.", "E"),
    ("Lubię pracować według jasno określonych zasad.", "C"),
    ("Obsługa maszyn i narzędzi sprawia mi przyjemność.", "R"),
    ("Lubię analizować dane i szukać przyczyn zjawisk.", "I"),
    ("Wolę pracować w sposób nieszablonowy i swobodny.", "A"),
    ("Dobrze czuję się, opiekując się innymi ludźmi.", "S"),
    ("Chciałbym w przyszłości zarządzać własnym projektem lub firmą.", "E"),
    ("Lubię planować i organizować harmonogramy.", "C"),
    ("Mam zdolności manualne i techniczne.", "R"),
    ("Ciekawi mnie przeprowadzanie eksperymentów.", "I"),
    ("Pisanie wierszy, opowiadań lub prowadzenie bloga mnie bawi.", "A"),
    ("Łatwo nawiązuję kontakty z nowymi osobami.", "S"),
    ("Lubię rywalizację i dążenie do sukcesu.", "E"),
    ("Dokładność w wypełnianiu dokumentów jest dla mnie ważna.", "C"),
    ("Interesuje mnie budownictwo, rolnictwo lub mechanika.", "R")
]

# Przechowywanie punktacji
scores = {"R": 0, "I": 0, "A": 0, "S": 0, "E": 0, "C": 0}

with st.form("test_form"):
    for i, (q_text, q_type) in enumerate(questions):
        st.write(f"**Pytanie {i+1}/25**")
        choice = st.radio(q_text, ["Nie pasuje", "Trochę pasuje", "Bardzo pasuje"], horizontal=True, key=f"q_{i}")
        
        if choice == "Bardzo pasuje":
            scores[q_type] += 2
        elif choice == "Trochę pasuje":
            scores[q_type] += 1
            
    submitted = st.form_submit_button("ZOBACZ MOJE WYNIKI")

# Opisy typów
descriptions = {
    "R": "**TYP REALISTYCZNY (Działacz):** Jesteś osobą praktyczną. Lubisz konkretne zadania, pracę z narzędziami, maszynami lub zwierzętami. Twoje mocne strony to umiejętności techniczne i fizyczne.",
    "I": "**TYP BADAWCZY (Myśliciel):** Uwielbiasz analizować, obserwować i uczyć się. Jesteś dociekliwy i lubisz rozwiązywać skomplikowane problemy naukowe lub logiczne.",
    "A": "**TYP ARTYSTYCZNY (Twórca):** Cenisz kreatywność i intuicję. Nie lubisz sztywnych reguł. Wyrażasz siebie poprzez sztukę, pisanie lub unikalne pomysły.",
    "S": "**TYP SPOŁECZNY (Pomocnik):** Twoją domeną jest praca z ludźmi. Lubisz uczyć, leczyć, wyjaśniać i wspierać innych w ich rozwoju.",
    "E": "**TYP PRZEDSIĘBIORCZY (Organizator):** Jesteś urodzonym liderem. Lubisz wpływać na ludzi, przewodzić, sprzedawać pomysły i podejmować ryzyko dla osiągnięcia celu.",
    "C": "**TYP KONWENCJONALNY (Urzędnik):** Cenisz porządek, strukturę i jasne instrukcje. Świetnie radzisz sobie z danymi, liczbami i organizacją biurową."
}

if submitted:
    st.balloons()
    top_type = max(scores, key=scores.get)
    
    st.success("### Twój wynik gotowy!")
    st.markdown(descriptions[top_type])
    
    st.write("### Twój wykres predyspozycji:")
    # Prosty wykres
    chart_data = {
        "Realistyczny": scores["R"],
        "Badawczy": scores["I"],
        "Artystyczny": scores["A"],
        "Społeczny": scores["S"],
        "Przedsiębiorczy": scores["E"],
        "Konwencjonalny": scores["C"]
    }
    st.bar_chart(chart_data)
    
    st.info("Pamiętaj, że każdy z nas jest mieszanką tych typów! Zazwyczaj dwa lub trzy najwyższe wyniki najlepiej opisują Twoją ścieżkę zawodową.")