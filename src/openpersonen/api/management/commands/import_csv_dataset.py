import csv

from django.core.management import BaseCommand

from openpersonen.api.testing_models import *

"""
Row index   |    Field name

0   |   A-nummer persoon
1   |   Burgerservicenummer persoon
2   |   Voornamen persoon
3   |   Adellijke titel/predikaat persoon
4   |   Voorvoegsel geslachtsnaam persoon
5   |   Geslachtsnaam persoon
6   |   Geboortedatum persoon
7   |   Geboorteplaats persoon
8   |   Geboorteland persoon
9   |   Geslachtsaanduiding
10   |   Vorig A-nummer
11   |   Volgend A-nummer
12   |   Aanduiding naamgebruik
13   |   Registergemeente akte waaraan gegevens over persoon ontleend zijn
14   |   Aktenummer van de akte waaraan gegevens over persoon ontleend zijn
15   |   Gemeente waar de gegevens over persoon aan het document ontleend zijn
16   |   Datum van de ontlening van de gegevens over persoon
17   |   Beschrijving van het document waaraan de gegevens over persoon ontleend zijn
18   |   Aanduiding gegevens in onderzoek
19   |   Datum ingang onderzoek
20   |   Datum einde onderzoek
21   |   Indicatie onjuist dan wel strijdigheid met de openbare orde
22   |   Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Persoon
23   |   Datum van opneming met betrekking tot de elementen van de categorie Persoon
24   |   RNI-deelnemer
25   |   Omschrijving verdrag
26   |
27   |   A-nummer ouder1
28   |   Burgerservicenummer ouder1
29   |   Voornamen ouder1
30   |   Adellijke titel/predikaat ouder1
31   |   Voorvoegsel geslachtsnaam ouder1
32   |   Geslachtsnaam ouder1
33   |   Geboortedatum ouder1
34   |   Geboorteplaats ouder1
35   |   Geboorteland ouder1
36   |   Geslachtsaanduiding ouder1
37   |   Datum ingang familierechtelijke betrekking ouder1
38   |   Registergemeente akte waaraan gegevens over ouder1 ontleend zijn
39   |   Aktenummer van de akte waaraan gegevens over ouder1 ontleend zijn
40   |   Gemeente waar de gegevens over ouder1 aan het document ontleend zijn
41   |   Datum van de ontlening van de gegevens over ouder1
42   |   Beschrijving van het document waaraan de gegevens over ouder1 ontleend zijn
43   |   Aanduiding gegevens in onderzoek
44   |   Datum ingang onderzoek
45   |   Datum einde onderzoek
46   |   Indicatie onjuist dan wel strijdigheid met de openbare orde
47   |   Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Ouder1
48   |   Datum van opneming met betrekking tot de elementen van de categorie Ouder1
49   |
50   |   A-nummer ouder2
51   |   Burgerservicenummer ouder2
52   |   Voornamen ouder2
53   |   Adellijke titel/predikaat ouder2
54   |   Voorvoegsel geslachtsnaam ouder2
55   |   Geslachtsnaam ouder2
56   |   Geboortedatum ouder2
57   |   Geboorteplaats ouder2
58   |   Geboorteland ouder2
59   |   Geslachtsaanduiding ouder2
60   |   Datum ingang familierechtelijke betrekking ouder2
61   |   Registergemeente akte waaraan gegevens over ouder2 ontleend zijn
62   |   Aktenummer van de akte waaraan gegevens over ouder2 ontleend zijn
63   |   Gemeente waar de gegevens over ouder2 aan het document ontleend zijn
64   |   Datum van de ontlening van de gegevens over ouder2
65   |   Beschrijving van het document waaraan de gegevens over ouder2 ontleend zijn
66   |   Aanduiding gegevens in onderzoek
67   |   Datum ingang onderzoek
68   |   Datum einde onderzoek
69   |   Indicatie onjuist dan wel strijdigheid met de openbare orde
70   |   Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Ouder2
71   |   Datum van opneming met betrekking tot de elementen van de categorie Ouder2
72   |
73   |   Nationaliteit
74   |   Reden opname nationaliteit
75   |   Reden beëindigen nationaliteit
76   |   Aanduiding bijzonder Nederlanderschap
77   |   EU-persoonsummer
78   |   Gemeente waar de gegevens over nationaliteit aan het document ontleend dan wel afgeleid zijn
79   |   Datum van de ontlening dan wel afleiding van de gegevens over nationaliteit
80   |   Beschrijving van het document waaraan de gegevens over nationaliteit ontleend dan wel afgeleid zijn
81   |   Aanduiding gegevens in onderzoek
82   |   Datum ingang onderzoek
83   |   Datum einde onderzoek
84   |   Indicatie onjuist
85   |   Datum van ingang geldigheid met betrekking tot de elementen van de categorie Nationaliteit
86   |   Datum van opneming met betrekking tot de elementen van de categorie Nationaliteit
87   |   RNI-deelnemer
88   |   Omschrijving verdrag
89   |
90   |   A-nummer echtgenoot/geregistreerd partner
91   |   Burgerservicenummer echtgenoot/geregistreerd partner
92   |   Voornamen echtgenoot/geregistreerd partner
93   |   Adellijke titel/predikaat echtgenoot/geregistreerd partner
94   |   Voorvoegsel geslachtsnaam echtgenoot/geregistreerd partner
95   |   Geslachtsnaam echtgenoot/geregistreerd partner
96   |   Geboortedatum echtgenoot/geregistreerd partner
97   |   Geboorteplaats echtgenoot/geregistreerd partner
98   |   Geboorteland echtgenoot/geregistreerd partner
99   |   Geslachtsaanduiding echtgenoot/geregistreerd partner
100   |   Datum huwelijkssluiting/aangaan geregistreerd partnerschap
101   |   Plaats huwelijkssluiting/aangaan geregistreerd partnerschap
102   |   Land huwelijkssluiting/aangaan geregistreerd partnerschap
103   |   Datum ontbinding huwelijk/geregistreerd partnerschap
104   |   Plaats ontbinding huwelijk/geregistreerd partnerschap
105   |   Land ontbinding huwelijk/geregistreerd partnerschap
106   |   Reden ontbinding huwelijk/geregistreerd partnerschap
107   |   Soort verbintenis
108   |   Registergemeente akte waaraan gegevens over huwelijk/geregistreerd partnerschap ontleend zijn
109   |   Aktenummer van de akte waaraan gegevens over huwelijk/geregistreerd partnerschap ontleend zijn
110   |   Gemeente waar de gegevens over huwelijk/geregistreerd partnerschap aan het document ontleend zijn
111   |   Datum van de ontlening van de gegevens over huwelijk/geregistreerd partnerschap
112   |   Beschrijving van het document waaraan de gegevens over huwelijk/ geregistreerd partnerschap ontleend zijn
113   |   Aanduiding gegevens in onderzoek
114   |   Datum ingang onderzoek
115   |   Datum einde onderzoek
116   |   Indicatie onjuist dan wel strijdigheid met de openbare orde
117   |   Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Huwelijk/geregistreerd part
118   |   Datum van opneming met betrekking tot de elementen van de categorie Huwelijk/geregistreerd partnersc
119   |
120   |   Datum overlijden
121   |   Plaats overlijden
122   |   Land overlijden
123   |   Registergemeente akte waaraan gegevens over overlijden ontleend zijn
124   |   Aktenummer van de akte waaraan gegevens over overlijden ontleend zijn
125   |   Gemeente waar de gegevens over overlijden aan het document ontleend zijn
126   |   Datum van de ontlening van de gegevens over overlijden
127   |   Beschrijving van het document waaraan de gegevens over overlijden ontleend zijn
128   |   Aanduiding gegevens in onderzoek
129   |   Datum ingang onderzoek
130   |   Datum einde onderzoek
131   |   Indicatie onjuist dan wel strijdigheid met de openbare orde
132   |   Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Overlijden
133   |   Datum van opneming met betrekking tot de elementen van de categorie Overlijden
134   |   RNI-deelnemer
135   |   RNI-deelnemer
136   |
137   |   Datum ingang blokkering PL
138   |   Datum opschorting bijhouding
139   |   Omschrijving reden opschorting bijhouding
140   |   Datum eerste inschrijving GBA/RNI
141   |   Gemeente waar de PK zich bevindt
142   |   Indicatie geheim
143   |   Datum verfificatie
144   |   Omschrijving verificatie
145   |   Versienummer
146   |   Datumtijdstempel
147   |   PK-gegevens volledig meegeconverteerd
148   |   RNI-deelnemer
149   |   Omschrijving verdrag
150   |
151   |   Gemeente van inschrijving
152   |   Datum inschrijving in de gemeente
153   |   Functie adres
154   |   Gemeentedeel
155   |   Datum aanvang adreshouding
156   |   Straatnaam
157   |   Naam openbare ruimte
158   |   Huisnummer
159   |   Huisletter
160   |   Huisnummertoevoeging
161   |   Aanduiding bij huisnummer
162   |   Postcode
163   |   Woonplaatsnaam
164   |   Identificatiecode verblijfplaats
165   |   Identificatiecode nummeraanduiding
166   |   Locatiebeschrijving
167   |   Land adres buitenland
168   |   Datum aanvang adres buitenland
169   |   Regel 1 adres buitenland
170   |   Regel 2 adres buitenland
171   |   Regel 3 adres buitenland
172   |   Land vanwaar ingeschreven
173   |   Datum vestiging in Nederland
174   |   Omschrijving van de aangifte adreshouding
175   |   Indicatie document
176   |   Aanduiding gegevens in onderzoek
177   |   Datum ingang onderzoek
178   |   Datum einde onderzoek
179   |   Indicatie onjuist
180   |   Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Verblijfplaats
181   |   Datum van opneming met betrekking tot de elementen van de categorie Verblijfplaats
182   |   RNI-deelnemer
183   |   Omschrijving verdrag
184   |
185   |   A-nummer kind
186   |   Burgerservicenummer kind
187   |   Voornamen kind
188   |   Adellijke titel/predikaat kind
189   |   Voorvoegsel geslachtsnaam kind
190   |   Geslachtsnaam kind
191   |   Geboortedatum kind
192   |   Geboorteplaats kind
193   |   Geboorteland kind
194   |   Registergemeente akte waaraan gegevens over kind ontleend zijn
195   |   Aktenummer van de akte waaraan gegevens over kind ontleend zijn
196   |   Gemeente waar de gegevens over kind aan het document ontleend zijn
197   |   Datum van de ontlening van de gegevens over kind
198   |   Beschrijving van het document waaraan de gegevens over kind ontleend zijn
199   |   Aanduiding gegevens in onderzoek
200   |   Datum ingang onderzoek
201   |   Datum einde onderzoek
202   |   Indicatie onjuist dan wel strijdigheid met de openbare orde
203   |   Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Kind
204   |   Datum van opneming met betrekking tot de elementen van de categorie Kind
205   |   Registratie betrekking
206   |
207   |   Aanduiding verblijfstitel
208   |   Datum einde verblijfstitel
209   |   Ingangsdatum verblijfstitel
210   |   Aanduiding gegevens in onderzoek
211   |   Datum ingang onderzoek
212   |   Datum einde onderzoek
213   |   Indicatie onjuist
214   |   Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Verblijfstitel
215   |   Datum van opneming met betrekking tot de elementen van de categorie Verblijfstitel
216   |
217   |   Indicatie gezag minderjarige
218   |   Indicatie curateleregister
219   |   Gemeente waar de gegevens over gezagsverhouding aan het document ontleend zijn
220   |   Datum van de ontlening van de gegevens over gezagsverhouding
221   |   Beschrijving van het document waaraan de gegevens over gezagsverhouding ontleend zijn
222   |   Aanduiding gegevens in onderzoek
223   |   Datum ingang onderzoek
224   |   Datum einde onderzoek
225   |   Indicatie onjuist
226   |   Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Gezagsverhouding
227   |   Datum van opneming met betrekking tot de elementen van de categorie Gezagsverhouding
228   |
229   |   Soort Nederlands reisdocument
230   |   Nummer Nederlands reisdocument
231   |   Datum uitgifte Nederlands reisdocument
232   |   Autoriteit van afgifte Nederlands reisdocument
233   |   Datum einde geldigheid Nederlands reisdocument
234   |   Datum inhouding dan wel vermissing Nederlands reisdocument
235   |   Aanduiding inhouding dan wel vermissing Nederlands reisdocument
236   |   Signalering met betrekking tot verstrekken Nederlands reisdocument
237   |   Gemeente waar het paspoortdossier zich bevindt
238   |   Datum van opname in het paspoortdossier
239   |   Beschrijving dossier waarin de aanvullende paspoortgegevens zich bevinden
240   |   Aanduiding gegevens in onderzoek
241   |   Datum ingang onderzoek
242   |   Datum einde onderzoek
243   |   Datum van ingang geldigheid met betrekking tot de elementen van de categorie Reisdocument
244   |   Datum van opneming met betrekking tot de elementen van de categorie Reisdocument
245   |
246   |   Aanduiding Europees kiesrecht
247   |   Datum verzoek of mededeling Europees kiesrecht
248   |   Einddatum uitsluiting Europees kiesrecht
249   |   Aanduiding uitgesloten kiesrecht
250   |   Einddatum uitsluiting kiesrecht
251   |   Gemeente waar de gegevens over kiesrecht aan het document ontleend zijn
252   |   Datum van de ontlening van de gegevens over kiesrecht
253   |   Beschrijving van het document waaraan de gegevens over kiesrecht ontleend zijn
254   |
255   |
256   |
257   |
258   |
259   |
"""


class Command(BaseCommand):
    help = 'Read in an csv file and populate models to use for test data'

    def add_arguments(self, parser):
        parser.add_argument('infile', help='The csv file containing the data to import.')

    def handle(self, **options):
        with open(options['infile'], newline='') as csvfile:
            rows = csv.reader(csvfile, delimiter=';', quotechar='|')

            for row in list(rows)[3:]:
                if row[1]:
                    person = Persoon.objects.create(
                        a_nummer_persoon=row[0],
                        burgerservicenummer_persoon=row[1],
                        voornamen_persoon=row[2],
                        adellijke_titel_predikaat_persoon=row[3],
                        voorvoegsel_geslachtsnaam_persoon=row[4],
                        geslachtsnaam_persoon=row[5],
                        geboortedatum_persoon=row[6],
                        geboorteplaats_persoon=row[7],
                        geboorteland_persoon=row[8],
                        geslachtsaanduiding=row[9],
                        vorig_a_nummer=row[10],
                        volgend_a_nummer=row[11],
                        aanduiding_naamgebruik=row[12],
                        registergemeente_akte_waaraan_gegevens=row[13],
                        aktenummer_van_de_akte=row[14],
                        gemeente_waar_de_gegevens_over_persoon=row[15],
                        datum_van_de_ontlening_van_de_gegevens_over_persoon=row[16],
                        beschrijving_van_het_document=row[17],
                        aanduiding_gegevens_in_onderzoek=row[18],
                        datum_ingang_onderzoek=row[19],
                        datum_einde_onderzoek=row[20],
                        indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde=row[21],
                        ingangsdatum_geldigheid_met_betrekking=row[22],
                        datum_van_opneming_met_betrekking=row[23],
                        rni_deelnemer=row[24],
                    )
