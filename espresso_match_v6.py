import streamlit as st
st.title(" ☕ EspressoMatch ☕ ")
koffies = {
    "Mellow Fellow - Sprout": {
        "smaken": {"chocolade": 3, "karamel": 1},
        "info": "Deze koffie, onze vertrouwde klassieker voor dagelijks gebruik, heeft een robuuster karakter. Een romige body met tonen van chocolade en noten, en een volle, lang aanhoudende zoetheid van marsepein. Deze geruststellende dagelijkse favoriet zorgt met zijn klassieke profiel voor een rustgevende start van de dag.",
        "Recept": {
            "Dosering": "19.6 gram koffie",
            "Output": "43 gram espresso",
            "Tijd": "28-30 seconden",
        }
    },

    "Brazil Dulce - Schot": {
        "smaken": {"chocolade": 3, "noten": 2},
        "info": "Deze bonen bieden alles wat we van een goede Braziliaanse koffie verwachten: een volle body en zoetheid, een milde zuurgraad en uitgesproken chocolade- en notenaroma’s zonder fruitige tonen. Een echte publiekslieveling.",
        "Recept": {
            "Dosering": "18.5 gram koffie",
            "Output": "36 gram espresso",
            "Tijd": "26-30 seconden",
        }
    },

    "Friedhats Blend - Friedhats": {
        "smaken": {"chocolade": 3},
        "info": "50% Brazilië, 50% Ethiopië – nu en altijd. Een melange. Geen goedkope vulstoffen, geen koffie van vorige oogsten, alleen koffiesoorten die samen heerlijk smaken.",
        "Recept": {
            "Dosering": "19 gram koffie",
            "Output": "42 gram espresso",
            "Tijd": "26-28 seconden",
        }
    },

    "Ethiopia ALO Natural - Ripsnorter": {
        "smaken": {"fruitig": 3, "funky": 1},
        "info": "Deze koffie is rijk, fruitig en vol aroma en is speciaal gemaakt voor mensen die meer willen dan alleen cafeïne: zij willen er even van genieten.",
        "Recept": {
            "Dosering": "19.5 gram koffie",
            "Output": "44 gram espresso",
            "Tijd": "27-31 seconden",
        }
    },

    "Colombia Alexander Vargas - Friedhats": {
        "smaken": {"fruitig": 3, "funky": 2},
        "info": "Alexander Vargas is een technisch meester in zijn vak. Met meer dan twintig jaar ervaring in het experimenteren met en verfijnen van de koffieproductie en -verwerking, zijn zijn passie en vakmanschap duidelijk merkbaar wanneer je een kopje zet. Voor deze partij Pink Bourbon laat Alexander de koffie eerst 72 uur in de open lucht fermenteren, voordat hij de koffie overbrengt naar tanks met ontgassingskleppen voor een langdurige anaërobe fermentatie van 98 uur. Het resultaat is een verbluffend profiel van rijke, rijpe rode vruchten en een ongelooflijk kenmerkende, jamachtige zoetheid.",
        "Recept": {
            "Dosering": "19 gram koffie",
            "Output": "42 gram espresso",
            "Tijd": "27-29 seconden",
        }
    },

    "Pitcher Perfect - Sprout": {
        "smaken": {"fruitig": 2, "karamel": 2},
        "info": "Deze krachtige basismelange van een gewassen Colombiaanse koffie en een natuurlijke Ethiopische koffie geeft je melkdrankjes een boost met de body van donkere chocolade, de zachte zoetheid van marsepein en een langdurige nasmaak van bessen.",
        "Recept": {
            "Dosering": "19.5 gram koffie",
            "Output": "43 gram espresso",
            "Tijd": "27-29 seconden",
        }
    },

    "Delirious - Ripsnorter": {
        "smaken": {"noten": 4, "chocolade": 3},
        "info": "Delirious is a versatile and approachable coffee, crafted for both the purist and those who enjoy pairing their coffee with dairy or plant-based beverages. A rich, sweet cup with a balanced body and subtle complexity, making it ideal for any occasion.",
        "Recept": {
            "Dosering": "19 gram koffie",
            "Output": "42 gram espresso",
            "Tijd": "26-28 seconden",
        }
    },

    "Colombia Casa - Schot": {
        "smaken": {"noten": 3, "karamel": 2, "fruitig": 1},
        "info": "De belichaming van een comfortabele kop koffie. Uitermate evenwichtig, met een hoge zoetheid en een lage, maar toch citrusachtige zuurgraad. ",
        "Recept": {
            "Dosering": "19 gram koffie",
            "Output": "42 gram espresso",
            "Tijd": "26-28 seconden",
        }
    },

    "You're Nuts - Dak": {
        "smaken": {"noten": 3, "karamel": 2, "chocolade": 1},
        "info": "Een leuke variant op een klassieke Braziliaanse koffie van Adriano Muñiz! Deze anaërobe arara uit Kaapverdië is rond en zoet, met een vleugje wijnachtige toets. Proefnotities van siroop van donkere bessen, karamel en cacaonibs.",
        "Recept": {
            "Dosering": "19.5 gram koffie",
            "Output": "44 gram espresso",
            "Tijd": "27-30 seconden",
        }
    },

    "Mount Suket - Ripsnorter": {
        "smaken": {"karamel": 3, "fruitig": 2},
        "info": "een verrassend zuivere en levendige smaak voor een koffie met zo’n lange fermentatietijd, met sappige papaja, frisse grapefruit en een diepe melassezoetheid die de koffie structuur en warmte geeft.",
        "Recept": {
            "Dosering": "19 gram koffie",
            "Output": "42 gram espresso",
            "Tijd": "24-26 seconden",
        }
    },

    "Peru Carnaval - Schot": {
        "smaken": {"karamel": 4, "fruitig": 2, "noten": 2},
        "info": "Peruaanse espresso met tonen van amandel, rode appel en karamel, afkomstig uit Callayuc, Cajamarca, geteeld op ongeveer 1.900 meter hoogte en langer gefermenteerd dan de meeste gewassen Peruaanse koffiesoorten, voor een extra fruitige diepte.",
        "Recept": {
            "Dosering": "19 gram koffie",
            "Output": "42 gram espresso",
            "Tijd": "26-28 seconden",
        }
    },

    "Espresso No 2 - Blommers": {
        "smaken": {"karamel": 3, "chocolade": 2},
        "info": "Romig en krachtig: deze combinatie van twee koffiesoorten biedt diepe chocoladetonen, een rijke nootachtige smaak en een volle body.",
        "Recept": {
            "Dosering": "18.5 gram koffie",
            "Output": "38 gram espresso",
            "Tijd": "27-30 seconden",
        }
    },

    "Cream Donut - Dak": {
        "smaken": {"funky": 5, "karamel": 3},
        "info": "Cream Donut uit Colombia neemt je mee op een zoete reis vol chocolademelk (Nesquik), vanille en met kersen gevulde donuts. Een kop koffie die jeugherinneringen oproept in een volwassen omgeving. Deze koffie is zeker niet alledaags. Het is een genot voor iedereen die op zoek is naar een uitgesproken zoetheid, fruitige sappigheid en een verfijnd smaakprofiel.",
        "Recept": {
            "Dosering": "19,5 gram koffie",
            "Output": "44 gram espresso",
            "Tijd": "28-32 seconden",
        }
    },

    "Banana Bubble Butt - Sprout": {
        "smaken": {"funky": 4, "fruitig": 3},
        "info": "Deze experimentele gele papaja van Finca El Diviso in Pitalito, Huila, Colombia, geproduceerd door Nestor Lasso, is een waanzinnige mix van snoepjes en allerlei zoete lekkernijen. Veel lekkerder dan deze bananenbeignet wordt het niet.",
        "Recept": {
            "Dosering": "19 gram koffie",
            "Output": "42 gram espresso",
            "Tijd": "26-28 seconden",
        }
    },

    "Milky Cake - Dak": {
        "smaken": {"funky": 3, "chocolade": 3},
        "info": "De koffie, die de bijzondere naam Milky Cake draagt, doet bij de eerste slok echt denken aan een vanillecake. Bij de tweede slok proef je ook tonen van pistache, kardemom en honing.",
        "Recept": {
            "Dosering": "19.5 gram koffie",
            "Output": "42 gram espresso",
            "Tijd": "24-26 seconden",
        }
    },
}
# Session state toevoegen
if "pagina" not in st.session_state:
    st.session_state["pagina"] = "home"  ## Ik wil beginnen bij home, zonder het geheugen vergeet ie bij elke klik waar ik ben

if "gekozen_koffie" not in st.session_state: #opslaan welke koffie iemand klikt
    st.session_state["gekozen_koffie"] = None # het begint bij niks

if "scores" not in st.session_state:    #hierbij begint me session bij niks, lege lijst. lijst wordt gevuld met wat je klikt
    st.session_state["scores"] = []


# Detail functie om info te krjgen van koffie
def toon_koffie_detail(Koffie_naam):
    koffie = koffies[Koffie_naam] #juiste koffie naam

    st.header(Koffie_naam)

    st.subheader("Smaakprofiel")
    for smaak, punten in koffie["smaken"].items():
        st.write(f"- {smaak.capitalize()}: {punten} punten") #hoofdletter en punten? kan weg halen

    st.subheader("Info")
    if koffie["info"]:
        st.write(koffie["info"])
    else:
        st.write("Nog geen extra informatie toegevoegd.") #hiermee kan ik koffies toevoegen en later info

    st.subheader("Espresso recept")
    st.write(f"**Dosering:** {koffie['Recept']['Dosering']}")  #sterretjes voor vetgedrukt
    st.write(f"**Output:** {koffie['Recept']['Output']}")
    st.write(f"**Tijd:** {koffie['Recept']['Tijd']}")

    if st.button("⬅ Terug naar matches"):
        st.session_state["pagina"] = "home"
        st.rerun() #hier gaat het terug naar homepage en laadt met nieuwe pagina


# Detailpagina tonen
if st.session_state["pagina"] == "detail":
    toon_koffie_detail(st.session_state["gekozen_koffie"])


# Homepage tonen
else:
    st.write("Kies je favoriete smaaknoten")

    gekozen = []

    if st.checkbox("Chocolade"):
        gekozen.append("chocolade")

    if st.checkbox("Karamel"):
        gekozen.append("karamel")

    if st.checkbox("Noten"):
        gekozen.append("noten")

    if st.checkbox("Fruitig"):
        gekozen.append("fruitig")

    if st.checkbox("Funky"):
        gekozen.append("funky")

    if st.button("Zoek mijn espresso"):
        if not gekozen:
            st.warning("Kies eerst minimaal één smaaknoot.")
        else:
            scores = [] #dit is zodat python de scores berekent

            for koffie_naam, koffie_data in koffies.items(): #hier loopt ie basically door me database
                score = 0
                smaken = koffie_data["smaken"]

                for smaak in gekozen:
                    score += smaken.get(smaak, 0)

                if score > 0:
                    scores.append((koffie_naam, score))

            scores.sort(key=lambda x: x[1], reverse=True) # lastige formule ? meer opzoeken
            st.session_state["scores"] = scores

    if st.session_state["scores"]:
        st.subheader("🏆 Jouw top 3 matches")

        medailles = ["🥇", "🥈", "🥉"]

        for i, (koffie_naam, score) in enumerate(st.session_state["scores"][:3]):  #python pakt hier de beste 3
            st.write(f"{medailles[i]} {koffie_naam}")

            if st.button(f"Bekijk {koffie_naam}", key=koffie_naam):
                st.session_state["gekozen_koffie"] = koffie_naam
                st.session_state["pagina"] = "detail"
                st.rerun()
if st.button("Mijn koffie-extractie gaat te snel of te langzaam"):
    st.subheader("Pas de maalgraad van je grinder aan")

    st.write("**Gaat de extractie te snel?**")
    st.write(
        "Zet de grinder **fijner**. Hierdoor stroomt het water langzamer "
        "door de koffie en duurt de extractie langer."
    )

    st.write("**Gaat de extractie te langzaam?**")
    st.write(
        "Zet de grinder **grover**. Hierdoor stroomt het water sneller "
        "door de koffie en duurt de extractie korter."
    )
st.link_button(
        "Bekijk latte art tutorial",
        "https://www.youtube.com/watch?v=SiefJJv-Qho"
    )

st.markdown("""
<style>
div[data-testid="stLinkButton"] a[href^="tel:"] {
    color: red !important;
}
</style>
""", unsafe_allow_html=True)

st.link_button(
    "Koffie noodnummer",
    "tel:+31648513116"
)