Implementation
==============

The StUF-BG specification does not map exactly to the Haal Centraal BRP API.
There are several implementation details that are documented below, starting
with a mapping of all API to StUF-BG attributes.

If an attribute mapping has no design decision remarks, the attribute value is
not changed.

StUF-BG attribute notation
--------------------------

* **`attribute`** - API value is derived directly from `attribute`.
* **FUNCTION(`attribute`)** - API value is derived from `attribute` via a
  specific FUNCTION. These FUNCTIONs should be self explanatory.
* **"value"** - API value is staticly set to this "value".
* ***(`attribute` == "value")*** - API value is derived from simple calculation.
* ***(calculated)*** - API value is derived from complex calculation. The
  remarks should indicate how exactly.


Ingeschreven persoon
--------------------

=====================================================================   =====================================================================   =====================================================================
API attribute                                                           StUF-BG attribute                                                       Design decision  remarks
=====================================================================   =====================================================================   =====================================================================
`burgerservicenummer`                                                   `inp.bsn`
`geheimhoudingPersoonsgegevens`                                         `inp.indicatieGeheim`
`naam.geslachtsnaam`                                                    `geslachtsnaam`
`naam.voorletters`                                                      `voorletters`
`naam.voornamen`                                                        `voornamen`
`naam.voorvoegsel`                                                      `voorvoegselGeslachtsnaam`
`naam.inOnderzoek.geslachtsnaam`                                        `inOnderzoek`                                                           No exact match in StUF-BG, used super property.
`naam.inOnderzoek.voornamen`                                            `inOnderzoek`                                                           No exact match in StUF-BG, used super property.
`naam.inOnderzoek.voorvoegsel`                                          `inOnderzoek`                                                           No exact match in StUF-BG, used super property.
`naam.inOnderzoek.datumIngangOnderzoek.dag`                             1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`naam.inOnderzoek.datumIngangOnderzoek.datum`                           "01-01-1900"                                                            Fixed value since not in StUF-BG and cannot be `null`.
`naam.inOnderzoek.datumIngangOnderzoek.jaar`                            1900                                                                    Fixed value since not in StUF-BG and cannot be `null`.
`naam.inOnderzoek.datumIngangOnderzoek.maand`                           1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`naam.aanhef`                                                           *(calculated)*                                                          See `features`_ (TODO)
`naam.aanschrijfwijze`                                                  *(calculated)*                                                          See `features`_ (TODO)
`naam.gebruikInLopendeTekst`                                            *(calculated)*                                                          See `features`_ (TODO)
`naam.aanduidingNaamgebruik`                                            `aanduidingNaamgebruik`
`geboorte.datum.dag`                                                    DAY(`geboortedatum`)
`geboorte.datum.datum`                                                  `geboortedatum`
`geboorte.datum.jaar`                                                   YEAR(`geboortedatum`)
`geboorte.datum.maand`                                                  MONTH(`geboortedatum`)
`geboorte.land.code`                                                    COUNTRY_CODE(`inp.geboorteLand`)                                        TODO
`geboorte.land.omschrijving`                                            `inp.geboorteLand`
`geboorte.plaats.code`                                                  CITY_CODE(`inp.geboorteplaats`)                                         TODO
`geboorte.plaats.omschrijving`                                          `inp.geboorteplaats`
`geboorte.inOnderzoek.datum`                                            `inOnderzoek`                                                           No exact match in StUF-BG, used super property.
`geboorte.inOnderzoek.land`                                             `inOnderzoek`                                                           No exact match in StUF-BG, used super property.
`geboorte.inOnderzoek.plaats`                                           `inOnderzoek`                                                           No exact match in StUF-BG, used super property.
`geboorte.inOnderzoek.datumIngangOnderzoek.dag`                         1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`geboorte.inOnderzoek.datumIngangOnderzoek.datum`                       "01-01-1900"                                                            Fixed value since not in StUF-BG and cannot be `null`.
`geboorte.inOnderzoek.datumIngangOnderzoek.jaar`                        1900                                                                    Fixed value since not in StUF-BG and cannot be `null`.
`geboorte.inOnderzoek.datumIngangOnderzoek.maand`                       1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`geslachtsaanduiding`                                                   `geslachtsaanduiding`
`leeftijd`                                                              *(calculated)*                                                          See `features`_
`datumEersteInschrijvingGBA.dag`                                        DAY(`inp.datumInschrijving`)
`datumEersteInschrijvingGBA.datum`                                      `inp.datumInschrijving`
`datumEersteInschrijvingGBA.jaar`                                       YEAR(`inp.datumInschrijving`)
`datumEersteInschrijvingGBA.maand`                                      MONTH(`inp.datumInschrijving`)
`kiesrecht.europeesKiesrecht`                                           *(`ing.aanduidingEuropeesKiesrecht` == `2`)*                            StUF-BG value "2" evaluates to "true".
`kiesrecht.uitgeslotenVanKiesrecht`                                     *(`ing.aanduidingUitgeslotenKiesrecht` == `A`)*                         StUF-BG value "A" evaluates to "true".

`kiesrecht.einddatumUitsluitingEuropeesKiesrecht.dag`                   `integer(ing.aanduidingEuropeesKiesrecht)`                              TODO
`kiesrecht.einddatumUitsluitingEuropeesKiesrecht.datum`                 `ing.aanduidingEuropeesKiesrecht`                                       TODO
`kiesrecht.einddatumUitsluitingEuropeesKiesrecht.jaar`                  `integer(ing.aanduidingEuropeesKiesrecht)`                              TODO
`kiesrecht.einddatumUitsluitingEuropeesKiesrecht.maand`                 `integer(ing.aanduidingEuropeesKiesrecht)`                              TODO
`kiesrecht.einddatumUitsluitingKiesrecht.dag`                           `integer(ing.aanduidingUitgeslotenKiesrecht)`                           TODO
`kiesrecht.einddatumUitsluitingKiesrecht.datum`                         `ing.aanduidingUitgeslotenKiesrecht`                                    TODO
`kiesrecht.einddatumUitsluitingKiesrecht.jaar`                          `integer(ing.aanduidingUitgeslotenKiesrecht)`                           TODO
`kiesrecht.einddatumUitsluitingKiesrecht.maand`                         `integer(ing.aanduidingUitgeslotenKiesrecht)`                           TODO
`inOnderzoek.burgerservicenummer`                                       `boolean(inp.bsn)`                                                      TODO
`inOnderzoek.geslachtsaanduiding`                                       `boolean(geslachtsaanduiding)`                                          TODO
`inOnderzoek.datumIngangOnderzoek.dag`                                  `0`                                                                     TODO
`inOnderzoek.datumIngangOnderzoek.datum`                                `string`                                                                TODO
`inOnderzoek.datumIngangOnderzoek.jaar`                                 `0`                                                                     TODO
`inOnderzoek.datumIngangOnderzoek.maand`                                `0`                                                                     TODO
`nationaliteit.aanduidingBijzonderNederlanderschap`                     `string`                                                                TODO
`nationaliteit.datumIngangGeldigheid.dag`                               `0`                                                                     TODO
`nationaliteit.datumIngangGeldigheid.datum`                             `string`                                                                TODO
`nationaliteit.datumIngangGeldigheid.jaar`                              `0`                                                                     TODO
`nationaliteit.datumIngangGeldigheid.maand`                             `0`                                                                     TODO
`nationaliteit.nationaliteit.code`                                      `string`                                                                TODO
`nationaliteit.nationaliteit.omschrijving`                              `string`                                                                TODO
`nationaliteit.redenOpname.code`                                        `string`                                                                TODO
`nationaliteit.redenOpname.omschrijving`                                `string`                                                                TODO
`nationaliteit.inOnderzoek.aanduidingBijzonderNederlanderschap`         `True`                                                                  TODO
`nationaliteit.inOnderzoek.nationaliteit`                               `True`                                                                  TODO
`nationaliteit.inOnderzoek.redenOpname`                                 `True`                                                                  TODO
`nationaliteit.inOnderzoek.datumIngangOnderzoek.dag`                    `0`                                                                     TODO
`nationaliteit.inOnderzoek.datumIngangOnderzoek.datum`                  `string`                                                                TODO
`nationaliteit.inOnderzoek.datumIngangOnderzoek.jaar`                   `0`                                                                     TODO
`nationaliteit.inOnderzoek.datumIngangOnderzoek.maand`                  `0`                                                                     TODO
`opschortingBijhouding.reden`                                           `inp.redenOpschortingBijhouding`
`opschortingBijhouding.datum.dag`                                       `DAY(inp.datumOpschortingBijhouding)`
`opschortingBijhouding.datum.datum`                                     `inp.datumOpschortingBijhouding`
`opschortingBijhouding.datum.jaar`                                      `YEAR(inp.datumOpschortingBijhouding)`
`opschortingBijhouding.datum.maand`                                     `MONTH(inp.datumOpschortingBijhouding)`
`overlijden.indicatieOverleden`                                         `True`                                                                  TODO
`overlijden.datum.dag`                                                  `DAY(overlijdensdatum)`
`overlijden.datum.datum`                                                `overlijdensdatum`
`overlijden.datum.jaar`                                                 `YEAR(overlijdensdatum)`
`overlijden.datum.maand`                                                `MONTH(overlijdensdatum)`
`overlijden.land.code`                                                  `inp.overlijdenLand`
`overlijden.land.omschrijving`                                          `string`                                                                TODO
`overlijden.plaats.code`                                                `inp.overlijdenplaats`
`overlijden.plaats.omschrijving`                                        `string`                                                                TODO
`overlijden.inOnderzoek.datum`                                          `True`                                                                  TODO
`overlijden.inOnderzoek.land`                                           `True`                                                                  TODO
`overlijden.inOnderzoek.plaats`                                         `True`                                                                  TODO
`overlijden.inOnderzoek.datumIngangOnderzoek.dag`                       `0`                                                                     TODO
`overlijden.inOnderzoek.datumIngangOnderzoek.datum`                     `string`                                                                TODO
`overlijden.inOnderzoek.datumIngangOnderzoek.jaar`                      `0`                                                                     TODO
`overlijden.inOnderzoek.datumIngangOnderzoek.maand`                     `0`                                                                     TODO
`verblijfplaats.functieAdres`                                           `string`                                                                TODO
`verblijfplaats.huisletter`                                             `verblijfsadres.aoa.huisletter`
`verblijfplaats.huisnummer`                                             `verblijfsadres.aoa.huisnummer`
`verblijfplaats.huisnummertoevoeging`                                   `verblijfsadres.aoa.huisnummertoevoeging`
`verblijfplaats.aanduidingBijHuisnummer`                                `string`                                                                TODO
`verblijfplaats.identificatiecodeNummeraanduiding`                      `verblijfsadres.aoa.identificatie`
`verblijfplaats.naamOpenbareRuimte`                                     `verblijfsadres.gor.openbareRuimteNaam`
`verblijfplaats.postcode`                                               `verblijfsadres.aoa.postcode`
`verblijfplaats.woonplaatsnaam`                                         `verblijfsadres.wpl.woonplaatsNaam`
`verblijfplaats.identificatiecodeAdresseerbaarObject`                   `verblijfsadres.wpl.identificatie`
`verblijfplaats.indicatieVestigingVanuitBuitenland`                     `True`                                                                  TODO
`verblijfplaats.locatiebeschrijving`                                    `verblijfsadres.inp.locatiebeschrijving`
`verblijfplaats.straatnaam`                                             `verblijfsadres.gor.straatnaam`
`verblijfplaats.vanuitVertrokkenOnbekendWaarheen`                       `True`                                                                  TODO
`verblijfplaats.datumAanvangAdreshouding.dag`                           `0`                                                                     TODO
`verblijfplaats.datumAanvangAdreshouding.datum`                         `string`                                                                TODO
`verblijfplaats.datumAanvangAdreshouding.jaar`                          `0`                                                                     TODO
`verblijfplaats.datumAanvangAdreshouding.maand`                         `0`                                                                     TODO
`verblijfplaats.datumIngangGeldigheid.dag`                              `0`                                                                     TODO
`verblijfplaats.datumIngangGeldigheid.datum`                            `string`                                                                TODO
`verblijfplaats.datumIngangGeldigheid.jaar`                             `0`                                                                     TODO
`verblijfplaats.datumIngangGeldigheid.maand`                            `0`                                                                     TODO
`verblijfplaats.datumInschrijvingInGemeente.dag`                        `0`                                                                     TODO
`verblijfplaats.datumInschrijvingInGemeente.datum`                      `string`                                                                TODO
`verblijfplaats.datumInschrijvingInGemeente.jaar`                       `0`                                                                     TODO
`verblijfplaats.datumInschrijvingInGemeente.maand`                      `0`                                                                     TODO
`verblijfplaats.datumVestigingInNederland.dag`                          `0`                                                                     TODO
`verblijfplaats.datumVestigingInNederland.datum`                        `string`                                                                TODO
`verblijfplaats.datumVestigingInNederland.jaar`                         `0`                                                                     TODO
`verblijfplaats.datumVestigingInNederland.maand`                        `0`                                                                     TODO
`verblijfplaats.gemeenteVanInschrijving.code`                           `string`                                                                TODO
`verblijfplaats.gemeenteVanInschrijving.omschrijving`                   `string`                                                                TODO
`verblijfplaats.landVanwaarIngeschreven.code`                           `string`                                                                TODO
`verblijfplaats.landVanwaarIngeschreven.omschrijving`                   `string`                                                                TODO
`verblijfplaats.verblijfBuitenland.adresRegel1`                         `string`                                                                TODO
`verblijfplaats.verblijfBuitenland.adresRegel2`                         `string`                                                                TODO
`verblijfplaats.verblijfBuitenland.adresRegel3`                         `string`                                                                TODO
`verblijfplaats.verblijfBuitenland.vertrokkenOnbekendWaarheen`          `True`                                                                  TODO
`verblijfplaats.verblijfBuitenland.land.code`                           `string`                                                                TODO
`verblijfplaats.verblijfBuitenland.land.omschrijving`                   `string`                                                                TODO
`verblijfplaats.aanduidingBijHuisnummer`                                `True`                                                                  TODO
`verblijfplaats.datumAanvangAdreshouding`                               `True`                                                                  TODO
`verblijfplaats.datumIngangGeldigheid`                                  `True`                                                                  TODO
`verblijfplaats.datumInschrijvingInGemeente`                            `True`                                                                  TODO
`verblijfplaats.datumVestigingInNederland`                              `True`                                                                  TODO
`verblijfplaats.functieAdres`                                           `True`                                                                  TODO
`verblijfplaats.gemeenteVanInschrijving`                                `True`                                                                  TODO
`verblijfplaats.inOnderzoek.huisletter`                                 `True`                                                                  TODO
`verblijfplaats.inOnderzoek.huisnummer`                                 `True`                                                                  TODO
`verblijfplaats.inOnderzoek.huisnummertoevoeging`                       `True`                                                                  TODO
`verblijfplaats.inOnderzoek.identificatiecodeNummeraanduiding`          `True`                                                                  TODO
`verblijfplaats.inOnderzoek.identificatiecodeAdresseerbaarObject`       `True`                                                                  TODO
`verblijfplaats.inOnderzoek.landVanwaarIngeschreven`                    `True`                                                                  TODO
`verblijfplaats.inOnderzoek.locatiebeschrijving`                        `True`                                                                  TODO
`verblijfplaats.inOnderzoek.naamOpenbareRuimte`                         `True`                                                                  TODO
`verblijfplaats.inOnderzoek.postcode`                                   `True`                                                                  TODO
`verblijfplaats.inOnderzoek.straatnaam`                                 `True`                                                                  TODO
`verblijfplaats.inOnderzoek.verblijfBuitenland`                         `True`                                                                  TODO
`verblijfplaats.inOnderzoek.woonplaatsnaam`                             `True`                                                                  TODO
`verblijfplaats.inOnderzoek.datumIngangOnderzoek.dag`                   `0`                                                                     TODO
`verblijfplaats.inOnderzoek.datumIngangOnderzoek.datum`                 `string`                                                                TODO
`verblijfplaats.inOnderzoek.datumIngangOnderzoek.jaar`                  `0`                                                                     TODO
`verblijfplaats.inOnderzoek.datumIngangOnderzoek.maand`                 `0`                                                                     TODO
`gezagsverhouding.indicatieCurateleRegister`                            `True`                                                                  TODO
`gezagsverhouding.indicatieGezagMinderjarige`                           `ouder1`                                                                TODO
`gezagsverhouding.inOnderzoek.indicatieCurateleRegister`                `True`                                                                  TODO
`gezagsverhouding.inOnderzoek.indicatieGezagMinderjarige`               `True`                                                                  TODO
`gezagsverhouding.inOnderzoek.datumIngangOnderzoek.dag`                 `0`                                                                     TODO
`gezagsverhouding.inOnderzoek.datumIngangOnderzoek.datum`               `string`                                                                TODO
`gezagsverhouding.inOnderzoek.datumIngangOnderzoek.jaar`                `0`                                                                     TODO
`gezagsverhouding.inOnderzoek.datumIngangOnderzoek.maand`               `0`                                                                     TODO
`verblijfstitel.aanduiding.code`                                        `vbt.aanduidingVerblijfstitel`
`verblijfstitel.aanduiding.omschrijving`                                `string`                                                                TODO
`verblijfstitel.datumEinde.dag`                                         `0`                                                                     TODO
`verblijfstitel.datumEinde.datum`                                       `string`                                                                TODO
`verblijfstitel.datumEinde.jaar`                                        `0`                                                                     TODO
`verblijfstitel.datumEinde.maand`                                       `0`                                                                     TODO
`verblijfstitel.datumIngang.dag`                                        `0`                                                                     TODO
`verblijfstitel.datumIngang.datum`                                      `string`                                                                TODO
`verblijfstitel.datumIngang.jaar`                                       `0`                                                                     TODO
`verblijfstitel.datumIngang.maand`                                      `0`                                                                     TODO
`verblijfstitel.inOnderzoek.aanduiding`                                 `True`                                                                  TODO
`verblijfstitel.inOnderzoek.datumEinde`                                 `True`                                                                  TODO
`verblijfstitel.inOnderzoek.datumIngang`                                `True`                                                                  TODO
`verblijfstitel.inOnderzoek.datumIngangOnderzoek.dag`                   `0`                                                                     TODO
`verblijfstitel.inOnderzoek.datumIngangOnderzoek.datum`                 `string`                                                                TODO
`verblijfstitel.inOnderzoek.datumIngangOnderzoek.jaar`                  `0`                                                                     TODO
`verblijfstitel.inOnderzoek.datumIngangOnderzoek.maand`                 `0`                                                                     TODO
=====================================================================   =====================================================================   =====================================================================


Kind
--------------------

=====================================================================   =====================================================================   =====================================================================
API attribute                                                           StUF-BG attribute                                                       Design decision  remarks
=====================================================================   =====================================================================   =====================================================================
burgerservicenummer                                                     inp.bsn
geheimhoudingPersoonsgegevens                                           True
naam.geslachtsnaam                                                      geslachtsnaam
naam.voorletters                                                        voorletters
naam.voornamen                                                          voornamen
naam.voorvoegsel                                                        voorvoegselGeslachtsnaam
naam.inOnderzoek.geslachtsnaam                                          boolean(geslachtsnaam)
naam.inOnderzoek.voornamen                                              boolean(voornamen)
naam.inOnderzoek.voorvoegsel                                            boolean(voorvoegselGeslachtsnaam)
naam.inOnderzoek.datumIngangOnderzoek.dag                               0
naam.inOnderzoek.datumIngangOnderzoek.datum                             string
naam.inOnderzoek.datumIngangOnderzoek.jaar                              0
naam.inOnderzoek.datumIngangOnderzoek.maand                             0
geboorte.datum.dag                                                      integer(geboortedatum)                                                  Day portion of date value
geboorte.datum.datum                                                    geboortedatum                                                           Full date value
geboorte.datum.jaar                                                     integer(geboortedatum)                                                  Year portion of date value
geboorte.datum.maand                                                    integer(geboortedatum)                                                  Month portion of date value
geboorte.land.code                                                      string
geboorte.land.omschrijving                                              inp.geboorteLand
geboorte.plaats.code                                                    string
geboorte.plaats.omschrijving                                            inp.geboorteplaats
geboorte.inOnderzoek.datum                                              True
geboorte.inOnderzoek.land                                               True
geboorte.inOnderzoek.plaats                                             True
geboorte.inOnderzoek.datumIngangOnderzoek.dag                           0
geboorte.inOnderzoek.datumIngangOnderzoek.datum                         string
geboorte.inOnderzoek.datumIngangOnderzoek.jaar                          0
geboorte.inOnderzoek.datumIngangOnderzoek.maand                         0
leeftijd                                                                calculate_age(geboortedatum)                                            Age calculated from geboortedatum
inOnderzoek.burgerservicenummer                                         boolean(inp.bsn)
inOnderzoek.datumIngangOnderzoek.dag                                    0
inOnderzoek.datumIngangOnderzoek.datum                                  string
inOnderzoek.datumIngangOnderzoek.jaar                                   0
inOnderzoek.datumIngangOnderzoek.maand                                  0
=====================================================================   =====================================================================   =====================================================================


Ouder
--------------------

=====================================================================   =====================================================================   =====================================================================
API attribute                                                           StUF-BG attribute                                                       Design decision  remarks
=====================================================================   =====================================================================   =====================================================================
burgerservicenummer                                                     inp.bsn
geslachtsaanduiding                                                     geslachtsaanduiding
ouderAanduiding                                                         ouderAanduiding
datumIngangFamilierechtelijkeBetrekking.dag                             integer(datumIngangFamilierechtelijkeBetrekking)                        Day portion of date value
datumIngangFamilierechtelijkeBetrekking.datum                           datumIngangFamilierechtelijkeBetrekking                                 Full date value
datumIngangFamilierechtelijkeBetrekking.jaar                            integer(datumIngangFamilierechtelijkeBetrekking)                        Year portion of date value
datumIngangFamilierechtelijkeBetrekking.maand                           integer(datumIngangFamilierechtelijkeBetrekking)                        Month portion of date value
naam.geslachtsnaam                                                      geslachtsnaam
naam.voorletters                                                        voorletters
naam.voornamen                                                          voornamen
naam.voorvoegsel                                                        voorvoegselGeslachtsnaam
naam.inOnderzoek.geslachtsnaam                                          boolean(geslachtsnaam)
naam.inOnderzoek.voornamen                                              boolean(voornamen)
naam.inOnderzoek.voorvoegsel                                            boolean(voorvoegselGeslachtsnaam)
naam.inOnderzoek.datumIngangOnderzoek.dag                               0
naam.inOnderzoek.datumIngangOnderzoek.datum                             string
naam.inOnderzoek.datumIngangOnderzoek.jaar                              0
naam.inOnderzoek.datumIngangOnderzoek.maand                             0
inOnderzoek.burgerservicenummer                                         boolean(inp.bsn)
inOnderzoek.datumIngangFamilierechtelijkeBetrekking                     boolean(datumIngangFamilierechtelijkeBetrekking)
inOnderzoek.geslachtsaanduiding                                         boolean(geslachtsaanduiding)
inOnderzoek.datumIngangOnderzoek.dag                                    0
inOnderzoek.datumIngangOnderzoek.datum                                  string
inOnderzoek.datumIngangOnderzoek.jaar                                   0
inOnderzoek.datumIngangOnderzoek.maand                                  0
geboorte.datum.dag                                                      integer(geboortedatum)                                                  Day portion of date value
geboorte.datum.datum                                                    geboortedatum                                                           Full date value
geboorte.datum.jaar                                                     integer(geboortedatum)                                                  Year portion of date value
geboorte.datum.maand                                                    integer(geboortedatum)                                                  Month portion of date value
geboorte.land.code                                                      0000
geboorte.land.omschrijving                                              inp.geboorteLand
geboorte.plaats.code                                                    0000
geboorte.plaats.omschrijving                                            inp.geboorteplaats
geboorte.inOnderzoek.datum                                              boolean(geboortedatum)
geboorte.inOnderzoek.land                                               boolean(inp.geboorteLand)
geboorte.inOnderzoek.plaats                                             boolean(inp.geboorteplaats)
geboorte.inOnderzoek.datumIngangOnderzoek.dag                           0
geboorte.inOnderzoek.datumIngangOnderzoek.datum                         string
geboorte.inOnderzoek.datumIngangOnderzoek.jaar                          0
geboorte.inOnderzoek.datumIngangOnderzoek.maand                         0
geheimhoudingPersoonsgegevens                                           True
=====================================================================   =====================================================================   =====================================================================


Partner
--------------------

=====================================================================   =====================================================================   =====================================================================
API attribute                                                           StUF-BG attribute                                                       Design decision  remarks
=====================================================================   =====================================================================   =====================================================================
burgerservicenummer                                                     inp.bsn
geslachtsaanduiding                                                     geslachtsaanduiding
soortVerbintenis                                                        soortVerbintenis
naam.geslachtsnaam                                                      geslachtsnaam
naam.voorletters                                                        voorletters
naam.voornamen                                                          voornamen
naam.voorvoegsel                                                        voorvoegselGeslachtsnaam
naam.inOnderzoek.geslachtsnaam                                          boolean(geslachtsnaam)
naam.inOnderzoek.voornamen                                              boolean(voornamen)
naam.inOnderzoek.voorvoegsel                                            boolean(voorvoegselGeslachtsnaam)
naam.inOnderzoek.datumIngangOnderzoek.dag                               0
naam.inOnderzoek.datumIngangOnderzoek.datum                             string
naam.inOnderzoek.datumIngangOnderzoek.jaar                              0
naam.inOnderzoek.datumIngangOnderzoek.maand                             0
geboorte.datum.dag                                                      integer(geboortedatum)                                                  Day portion of date value
geboorte.datum.datum                                                    geboortedatum                                                           Full date value
geboorte.datum.jaar                                                     integer(geboortedatum)                                                  Year portion of date value
geboorte.datum.maand                                                    integer(geboortedatum)                                                  Month portion of date value
geboorte.land.code                                                      0000
geboorte.land.omschrijving                                              inp.geboorteLand
geboorte.plaats.code                                                    0000
geboorte.plaats.omschrijving                                            inp.geboorteplaats
geboorte.inOnderzoek.datum                                              boolean(geboortedatum)
geboorte.inOnderzoek.land                                               boolean(inp.geboorteLand)
geboorte.inOnderzoek.plaats                                             boolean(inp.geboorteplaats)
geboorte.inOnderzoek.datumIngangOnderzoek.dag                           0
geboorte.inOnderzoek.datumIngangOnderzoek.datum                         string
geboorte.inOnderzoek.datumIngangOnderzoek.jaar                          0
geboorte.inOnderzoek.datumIngangOnderzoek.maand                         0
inOnderzoek.burgerservicenummer                                         boolean(inp.bsn)
inOnderzoek.geslachtsaanduiding                                         boolean(geslachtsaanduiding)
inOnderzoek.datumIngangOnderzoek.dag                                    0
inOnderzoek.datumIngangOnderzoek.datum                                  string
inOnderzoek.datumIngangOnderzoek.jaar                                   0
inOnderzoek.datumIngangOnderzoek.maand                                  0
aangaanHuwelijkPartnerschap.datum.dag                                   0
aangaanHuwelijkPartnerschap.datum.datum                                 string
aangaanHuwelijkPartnerschap.datum.jaar                                  0
aangaanHuwelijkPartnerschap.datum.maand                                 0
aangaanHuwelijkPartnerschap.land.code                                   0000
aangaanHuwelijkPartnerschap.land.omschrijving                           string
aangaanHuwelijkPartnerschap.plaats.code                                 0000
aangaanHuwelijkPartnerschap.plaats.omschrijving                         string
aangaanHuwelijkPartnerschap.inOnderzoek.datum                           True
aangaanHuwelijkPartnerschap.inOnderzoek.land                            True
aangaanHuwelijkPartnerschap.inOnderzoek.plaats                          True
aangaanHuwelijkPartnerschap.inOnderzoek.datumIngangOnderzoek.dag        0
aangaanHuwelijkPartnerschap.inOnderzoek.datumIngangOnderzoek.datum      string
aangaanHuwelijkPartnerschap.inOnderzoek.datumIngangOnderzoek.jaar       0
aangaanHuwelijkPartnerschap.inOnderzoek.datumIngangOnderzoek.maand      0
geheimhoudingPersoonsgegevens                                           True
=====================================================================   =====================================================================   =====================================================================


.. _features: https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/blob/v1.0.0/features/
