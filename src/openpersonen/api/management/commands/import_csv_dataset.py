import csv
import os

from django.core.management import BaseCommand

from openpersonen.api.testing_models import *

"""
Row index   |    Field name

0     |   A-nummer persoon
1     |   Burgerservicenummer persoon
2     |   Voornamen persoon
3     |   Adellijke titel/predikaat persoon
4     |   Voorvoegsel geslachtsnaam persoon
5     |   Geslachtsnaam persoon
6     |   Geboortedatum persoon
7     |   Geboorteplaats persoon
8     |   Geboorteland persoon
9     |   Geslachtsaanduiding
10    |   Vorig A-nummer
11    |   Volgend A-nummer
12    |   Aanduiding naamgebruik
13    |   Registergemeente akte waaraan gegevens over persoon ontleend zijn
14    |   Aktenummer van de akte waaraan gegevens over persoon ontleend zijn
15    |   Gemeente waar de gegevens over persoon aan het document ontleend zijn
16    |   Datum van de ontlening van de gegevens over persoon
17    |   Beschrijving van het document waaraan de gegevens over persoon ontleend zijn
18    |   Aanduiding gegevens in onderzoek
19    |   Datum ingang onderzoek
20    |   Datum einde onderzoek
21    |   Indicatie onjuist dan wel strijdigheid met de openbare orde
22    |   Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Persoon
23    |   Datum van opneming met betrekking tot de elementen van de categorie Persoon
24    |   RNI-deelnemer
25    |   Omschrijving verdrag
26    |
27    |   A-nummer ouder1
28    |   Burgerservicenummer ouder1
29    |   Voornamen ouder1
30    |   Adellijke titel/predikaat ouder1
31    |   Voorvoegsel geslachtsnaam ouder1
32    |   Geslachtsnaam ouder1
33    |   Geboortedatum ouder1
34    |   Geboorteplaats ouder1
35    |   Geboorteland ouder1
36    |   Geslachtsaanduiding ouder1
37    |   Datum ingang familierechtelijke betrekking ouder1
38    |   Registergemeente akte waaraan gegevens over ouder1 ontleend zijn
39    |   Aktenummer van de akte waaraan gegevens over ouder1 ontleend zijn
40    |   Gemeente waar de gegevens over ouder1 aan het document ontleend zijn
41    |   Datum van de ontlening van de gegevens over ouder1
42    |   Beschrijving van het document waaraan de gegevens over ouder1 ontleend zijn
43    |   Aanduiding gegevens in onderzoek
44    |   Datum ingang onderzoek
45    |   Datum einde onderzoek
46    |   Indicatie onjuist dan wel strijdigheid met de openbare orde
47    |   Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Ouder1
48    |   Datum van opneming met betrekking tot de elementen van de categorie Ouder1
49    |
50    |   A-nummer ouder2
51    |   Burgerservicenummer ouder2
52    |   Voornamen ouder2
53    |   Adellijke titel/predikaat ouder2
54    |   Voorvoegsel geslachtsnaam ouder2
55    |   Geslachtsnaam ouder2
56    |   Geboortedatum ouder2
57    |   Geboorteplaats ouder2
58    |   Geboorteland ouder2
59    |   Geslachtsaanduiding ouder2
60    |   Datum ingang familierechtelijke betrekking ouder2
61    |   Registergemeente akte waaraan gegevens over ouder2 ontleend zijn
62    |   Aktenummer van de akte waaraan gegevens over ouder2 ontleend zijn
63    |   Gemeente waar de gegevens over ouder2 aan het document ontleend zijn
64    |   Datum van de ontlening van de gegevens over ouder2
65    |   Beschrijving van het document waaraan de gegevens over ouder2 ontleend zijn
66    |   Aanduiding gegevens in onderzoek
67    |   Datum ingang onderzoek
68    |   Datum einde onderzoek
69    |   Indicatie onjuist dan wel strijdigheid met de openbare orde
70    |   Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Ouder2
71    |   Datum van opneming met betrekking tot de elementen van de categorie Ouder2
72    |
73    |   Nationaliteit
74    |   Reden opname nationaliteit
75    |   Reden beëindigen nationaliteit
76    |   Aanduiding bijzonder Nederlanderschap
77    |   EU-persoonsummer
78    |   Gemeente waar de gegevens over nationaliteit aan het document ontleend dan wel afgeleid zijn
79    |   Datum van de ontlening dan wel afleiding van de gegevens over nationaliteit
80    |   Beschrijving van het document waaraan de gegevens over nationaliteit ontleend dan wel afgeleid zijn
81    |   Aanduiding gegevens in onderzoek
82    |   Datum ingang onderzoek
83    |   Datum einde onderzoek
84    |   Indicatie onjuist
85    |   Datum van ingang geldigheid met betrekking tot de elementen van de categorie Nationaliteit
86    |   Datum van opneming met betrekking tot de elementen van de categorie Nationaliteit
87    |   RNI-deelnemer
88    |   Omschrijving verdrag
89    |
90    |   A-nummer echtgenoot/geregistreerd partner
91    |   Burgerservicenummer echtgenoot/geregistreerd partner
92    |   Voornamen echtgenoot/geregistreerd partner
93    |   Adellijke titel/predikaat echtgenoot/geregistreerd partner
94    |   Voorvoegsel geslachtsnaam echtgenoot/geregistreerd partner
95    |   Geslachtsnaam echtgenoot/geregistreerd partner
96    |   Geboortedatum echtgenoot/geregistreerd partner
97    |   Geboorteplaats echtgenoot/geregistreerd partner
98    |   Geboorteland echtgenoot/geregistreerd partner
99    |   Geslachtsaanduiding echtgenoot/geregistreerd partner
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
        # with open(options['infile'], newline='') as csvfile:
        with open('test.csv', newline='') as csvfile:
            rows = csv.reader(csvfile, delimiter=';', quotechar='|')

            for row in list(rows)[3:]:
                if any(row[1:24]):
                    persoon = Persoon.objects.create(
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

                if any(row[27:48]):
                    Ouder.objects.create(
                        persoon=persoon,
                        a_nummer_ouder=row[27],
                        burgerservicenummer_ouder=row[28],
                        voornamen_ouder=row[29],
                        adellijke_titel_predikaat_ouder=row[30],
                        voorvoegsel_geslachtsnaam_ouder=row[31],
                        geslachtsnaam_ouder=row[32],
                        geboortedatum_ouder=row[33],
                        geboorteplaats_ouder=row[34],
                        geboorteland_ouder=row[35],
                        geslachtsaanduiding_ouder=row[36],
                        datum_ingang_familierechtelijke_betrekking_ouder=row[37],
                        registergemeente_akte_waaraan_gegevens_over_ouder_ontleend_zijn=row[38],
                        aktenummer_van_de_akte_waaraan_gegevens=row[39],
                        gemeente_waar_de_gegevens_over_ouder=row[40],
                        datum_van_de_ontlening_van_de_gegevens_over_ouder=row[41],
                        beschrijving_van_het_document_waaraan_de_gegevens=row[42],
                        aanduiding_gegevens_in_onderzoek=row[43],
                        datum_ingang_onderzoek=row[44],
                        datum_einde_onderzoek=row[45],
                        indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde=row[46],
                        ingangsdatum_geldigheid_met_betrekking=row[47],
                        datum_van_opneming_met_betrekking=row[48],
                    )

                if any(row[50:71]):
                    Ouder.objects.create(
                        persoon=persoon,
                        a_nummer_ouder=row[50],
                        burgerservicenummer_ouder=row[51],
                        voornamen_ouder=row[52],
                        adellijke_titel_predikaat_ouder=row[53],
                        voorvoegsel_geslachtsnaam_ouder=row[54],
                        geslachtsnaam_ouder=row[55],
                        geboortedatum_ouder=row[56],
                        geboorteplaats_ouder=row[57],
                        geboorteland_ouder=row[58],
                        geslachtsaanduiding_ouder=row[59],
                        datum_ingang_familierechtelijke_betrekking_ouder=row[60],
                        registergemeente_akte_waaraan_gegevens_over_ouder_ontleend_zijn=row[61],
                        aktenummer_van_de_akte_waaraan_gegevens=row[62],
                        gemeente_waar_de_gegevens_over_ouder=row[63],
                        datum_van_de_ontlening_van_de_gegevens_over_ouder=row[64],
                        beschrijving_van_het_document_waaraan_de_gegevens=row[65],
                        aanduiding_gegevens_in_onderzoek=row[66],
                        datum_ingang_onderzoek=row[67],
                        datum_einde_onderzoek=row[68],
                        indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde=row[69],
                        ingangsdatum_geldigheid_met_betrekking=row[70],
                        datum_van_opneming_met_betrekking=row[71],
                    )

                if any(row[50:71]):
                    Nationaliteit.objects.create(
                        persoon=persoon,
                        nationaliteit=row[73],
                        reden_opname_nationaliteit=row[74],
                        reden_beeindigen_nationaliteit=row[75],
                        aanduiding_bijzonder_nederlanderschap=row[76],
                        eu_persoonsummer=row[77],
                        gemeente_waar_de_gegevens_over_nationaliteit=row[78],
                        datum_van_de_ontlening=row[79],
                        beschrijving_van_het_document=row[80],
                        aanduiding_gegevens_in_onderzoek=row[81],
                        datum_ingang_onderzoek=row[82],
                        datum_einde_onderzoek=row[83],
                        indicatie_onjuist=row[84],
                        datum_van_ingang_geldigheid_met_betrekking=row[85],
                        datum_van_opneming_met_betrekking=row[86],
                        rni_deelnemer=row[87],
                        omschrijving_verdrag=row[88],
                    )

                if any(row[90:118]):
                    Partnerschap.objects.create(
                        persoon=persoon,
                        a_nummer_echtgenoot_geregistreerd_partner=row[90],
                        burgerservicenummer_echtgenoot_geregistreerd_partner=row[91],
                        voornamen_echtgenoot_geregistreerd_partner=row[92],
                        adellijke_titel_predikaat_echtgenoot_geregistreerd_partner=row[93],
                        voorvoegsel_geslachtsnaam_echtgenoot_geregistreerd_partner=row[94],
                        geslachtsnaam_echtgenoot_geregistreerd_partner=row[95],
                        geboortedatum_echtgenoot_geregistreerd_partner=row[96],
                        geboorteplaats_echtgenoot_geregistreerd_partner=row[97],
                        geboorteland_echtgenoot_geregistreerd_partner=row[98],
                        geslachtsaanduiding_echtgenoot_geregistreerd_partner=row[99],
                        datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap=row[100],
                        plaats_huwelijkssluiting_aangaan_geregistreerd_partnerschap=row[101],
                        land_huwelijkssluiting_aangaan_geregistreerd_partnerschap=row[102],
                        datum_ontbinding_huwelijk_geregistreerd_partnerschap=row[103],
                        plaats_ontbinding_huwelijk_geregistreerd_partnerschap=row[104],
                        land_ontbinding_huwelijk_geregistreerd_partnerschap=row[105],
                        reden_ontbinding_huwelijk_geregistreerd_partnerschap=row[106],
                        soort_verbintenis=row[107],
                        registergemeente_akte_waaraan_gegevens=row[108],
                        aktenummer_van_de_akte_waaraan_gegevens=row[109],
                        gemeente_waar_de_gegevens_over_huwelijk=row[110],
                        datum_van_de_ontlening_van_de_gegevens=row[111],
                        beschrijving_van_het_document_waaraan_de_gegevens=row[112],
                        aanduiding_gegevens_in_onderzoek=row[113],
                        datum_ingang_onderzoek=row[114],
                        datum_einde_onderzoek=row[115],
                        indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde=row[116],
                        ingangsdatum_geldigheid_met_betrekking=row[117],
                        datum_van_opneming_met_betrekking=row[118],
                    )

                if any(row[120:134]):
                    Overlijden.objects.create(
                        persoon=persoon,
                        datum_overlijden=row[120],
                        plaats_overlijden=row[121],
                        land_overlijden=row[122],
                        registergemeente_akte_waaraan_gegevens=row[123],
                        aktenummer_van_de_akte_waaraan_gegevens=row[124],
                        gemeente_waar_de_gegevens_over_overlijden=row[125],
                        datum_van_de_ontlening_van_de_gegevens_over_overlijden=row[126],
                        beschrijving_van_het_document_waaraan_de_gegevens=row[127],
                        aanduiding_gegevens_in_onderzoek=row[128],
                        datum_ingang_onderzoek=row[129],
                        datum_einde_onderzoek=row[130],
                        indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde=row[131],
                        ingangsdatum_geldigheid_met_betrekking=row[132],
                        datum_van_opneming_met_betrekking=row[133],
                        rni_deelnemer=row[134],
                    )

                if any(row[137:149]):
                    Inschrijving.objects.create(
                        persoon=persoon,
                        datum_ingang_blokkering_pl=row[137],
                        datum_opschorting_bijhouding=row[138],
                        omschrijving_reden_opschorting_bijhouding=row[139],
                        datum_eerste_inschrijving_gba_rni=row[140],
                        gemeente_waar_de_pk_zich_bevindt=row[141],
                        indicatie_geheim=row[142],
                        datum_verfificatie=row[143],
                        omschrijving_verificatie=row[144],
                        versienummer=row[145],
                        datumtijdstempel=row[146],
                        pk_gegevens_volledig_meegeconverteerd=row[147],
                        rni_deelnemer=row[148],
                        omschrijving_verdrag=row[149],
                    )

                if any(row[151:183]):
                    Verblijfplaats.objects.create(
                        persoon=persoon,
                        gemeente_van_inschrijving=row[151],
                        datum_inschrijving_in_de_gemeente=row[152],
                        functie_adres=row[153],
                        gemeentedeel=row[154],
                        datum_aanvang_adreshouding=row[155],
                        straatnaam=row[156],
                        naam_openbare_ruimte=row[157],
                        huisnummer=row[158],
                        huisletter=row[159],
                        huisnummertoevoeging=row[160],
                        aanduiding_bij_huisnummer=row[161],
                        postcode=row[162],
                        woonplaatsnaam=row[163],
                        identificatiecode_verblijfplaats=row[164],
                        identificatiecode_nummeraanduiding=row[165],
                        locatiebeschrijving=row[166],
                        land_adres_buitenland=row[167],
                        datum_aanvang_adres_buitenland=row[168],
                        regel_1_adres_buitenland=row[169],
                        regel_2_adres_buitenland=row[170],
                        regel_3_adres_buitenland=row[171],
                        land_vanwaar_ingeschreven=row[172],
                        datum_vestiging_in_nederland=row[173],
                        omschrijving_van_de_aangifte_adreshouding=row[174],
                        indicatie_document=row[175],
                        aanduiding_gegevens_in_onderzoek=row[176],
                        datum_ingang_onderzoek=row[177],
                        datum_einde_onderzoek=row[178],
                        indicatie_onjuist=row[179],
                        ingangsdatum_geldigheid_met_betrekking=row[180],
                        datum_van_opneming_met_betrekking=row[181],
                        rni_deelnemer=row[182],
                        omschrijving_verdrag=row[183],
                    )

                if any(row[185:205]):
                    Kind.objects.create(
                        persoon=persoon,
                        a_nummer_kind=row[185],
                        burgerservicenummer_kind=row[186],
                        voornamen_kind=row[187],
                        adellijke_titel_predikaat_kind=row[188],
                        voorvoegsel_geslachtsnaam_kind=row[189],
                        geslachtsnaam_kind=row[190],
                        geboortedatum_kind=row[191],
                        geboorteplaats_kind=row[192],
                        geboorteland_kind=row[193],
                        registergemeente_akte_waaraan_gegevens_over_kind_ontleend_zijn=row[194],
                        aktenummer_van_de_akte_waaraan_gegevens_over_kind_ontleend_zijn=row[195],
                        gemeente_waar_de_gegevens_over_kind=row[196],
                        datum_van_de_ontlening_van_de_gegevens_over_kind=row[197],
                        beschrijving_van_het_document=row[198],
                        aanduiding_gegevens_in_onderzoek=row[199],
                        datum_ingang_onderzoek=row[200],
                        datum_einde_onderzoek=row[201],
                        indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde=row[202],
                        ingangsdatum_geldigheid_met_betrekking=row[203],
                        datum_van_opneming_met_betrekking=row[204],
                        registratie_betrekking=row[205],
                    )

                if any(row[207:215]):
                    Verblijfstitel.objects.create(
                        persoon=persoon,
                        aanduiding_verblijfstitel=row[207],
                        datum_einde_verblijfstitel=row[208],
                        ingangsdatum_verblijfstitel=row[209],
                        aanduiding_gegevens_in_onderzoek=row[210],
                        datum_ingang_onderzoek=row[211],
                        datum_einde_onderzoek=row[212],
                        indicatie_onjuist=row[213],
                        ingangsdatum_geldigheid_met_betrekking=row[214],
                        datum_van_opneming_met_betrekking=row[215],
                    )

                if any(row[217:227]):
                    Gezagsverhouding.objects.create(
                        persoon=persoon,
                        indicatie_gezag_minderjarige=row[217],
                        indicatie_curateleregister=row[218],
                        gemeente_waar_de_gegevens_over_gezagsverhouding=row[219],
                        datum_van_de_ontlening_van_de_gegevens_over_gezagsverhouding=row[220],
                        beschrijving_van_het_document=row[221],
                        aanduiding_gegevens_in_onderzoek=row[222],
                        datum_ingang_onderzoek=row[223],
                        datum_einde_onderzoek=row[224],
                        indicatie_onjuist=row[225],
                        ingangsdatum_geldigheid_met_betrekking=row[226],
                        datum_van_opneming_met_betrekking=row[227],
                    )

                if any(row[229:244]):
                    Reisdocument.objects.create(
                        persoon=persoon,
                        soort_nederlands_reisdocument=row[229],
                        nummer_nederlands_reisdocument=row[230],
                        datum_uitgifte_nederlands_reisdocument=row[231],
                        autoriteit_van_afgifte_nederlands_reisdocument=row[232],
                        datum_einde_geldigheid_nederlands_reisdocument=row[233],
                        datum_inhouding_dan_wel_vermissing_nederlands_reisdocument=row[234],
                        aanduiding_inhouding_dan_wel_vermissing_nederlands_reisdocument=row[235],
                        signalering_met_betrekking=row[236],
                        gemeente_waar_het_paspoortdossier_zich_bevindt=row[237],
                        datum_van_opname_in_het_paspoortdossier=row[238],
                        beschrijving_dossier=row[239],
                        aanduiding_gegevens_in_onderzoek=row[240],
                        datum_ingang_onderzoek=row[241],
                        datum_einde_onderzoek=row[242],
                        datum_van_ingang_geldigheid_met_betrekking=row[243],
                        datum_van_opneming_met_betrekking=row[244],
                    )

                if any(row[246:253]):
                    Kiesrecht.objects.create(
                        persoon=persoon,
                        aanduiding_europees_kiesrecht=row[246],
                        datum_verzoek_of_mededeling_europees_kiesrecht=row[247],
                        einddatum_uitsluiting_europees_kiesrecht=row[248],
                        aanduiding_uitgesloten_kiesrecht=row[249],
                        einddatum_uitsluiting_kiesrecht=row[250],
                        gemeente_waar_de_gegevens_over_kiesrecht=row[251],
                        datum_van_de_ontlening_van_de_gegevens_over_kiesrecht=row[252],
                        beschrijving_van_het_document=row[253],
                    )
