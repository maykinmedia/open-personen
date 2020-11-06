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

`kiesrecht.einddatumUitsluitingEuropeesKiesrecht.dag`                   `integer(ing.aanduidingEuropeesKiesrecht)`                              Day portion of date value
`kiesrecht.einddatumUitsluitingEuropeesKiesrecht.datum`                 `ing.aanduidingEuropeesKiesrecht`                                       Full date value
`kiesrecht.einddatumUitsluitingEuropeesKiesrecht.jaar`                  `integer(ing.aanduidingEuropeesKiesrecht)`                               Year portion of date value
`kiesrecht.einddatumUitsluitingEuropeesKiesrecht.maand`                 `integer(ing.aanduidingEuropeesKiesrecht)`                               Month portion of date value
`kiesrecht.einddatumUitsluitingKiesrecht.dag`                           `integer(ing.aanduidingUitgeslotenKiesrecht)`                            Day portion of date value
`kiesrecht.einddatumUitsluitingKiesrecht.datum`                         `ing.aanduidingUitgeslotenKiesrecht`                                    Full date value
`kiesrecht.einddatumUitsluitingKiesrecht.jaar`                          `integer(ing.aanduidingUitgeslotenKiesrecht)`                            Year portion of date value
`kiesrecht.einddatumUitsluitingKiesrecht.maand`                         `integer(ing.aanduidingUitgeslotenKiesrecht)`                            Month portion of date value
`inOnderzoek.burgerservicenummer`                                       `boolean(inp.bsn)`
`inOnderzoek.geslachtsaanduiding`                                       `boolean(geslachtsaanduiding)`
`inOnderzoek.datumIngangOnderzoek.dag`                                  `0`
`inOnderzoek.datumIngangOnderzoek.datum`                                `string`
`inOnderzoek.datumIngangOnderzoek.jaar`                                 `0`
`inOnderzoek.datumIngangOnderzoek.maand`                                `0`
`nationaliteit.aanduidingBijzonderNederlanderschap`                     `inp.aanduidingBijzonderNederlanderschap`
`nationaliteit.datumIngangGeldigheid.dag`                               `0`
`nationaliteit.datumIngangGeldigheid.datum`                             `string`
`nationaliteit.datumIngangGeldigheid.jaar`                              `0`
`nationaliteit.datumIngangGeldigheid.maand`                             `0`
`nationaliteit.nationaliteit.code`                                      `string`
`nationaliteit.nationaliteit.omschrijving`                              `string`
`nationaliteit.redenOpname.code`                                        `string`
`nationaliteit.redenOpname.omschrijving`                                `string`
`nationaliteit.inOnderzoek.aanduidingBijzonderNederlanderschap`         `boolean(inp.aanduidingBijzonderNederlanderschap)`
`nationaliteit.inOnderzoek.nationaliteit`                               `True`
`nationaliteit.inOnderzoek.redenOpname`                                 `True`
`nationaliteit.inOnderzoek.datumIngangOnderzoek.dag`                    `0`
`nationaliteit.inOnderzoek.datumIngangOnderzoek.datum`                  `string`
`nationaliteit.inOnderzoek.datumIngangOnderzoek.jaar`                   `0`
`nationaliteit.inOnderzoek.datumIngangOnderzoek.maand`                  `0`
`opschortingBijhouding.reden`                                           `overlijden`
`opschortingBijhouding.datum.dag`                                       `0`
`opschortingBijhouding.datum.datum`                                     `string`
`opschortingBijhouding.datum.jaar`                                      `0`
`opschortingBijhouding.datum.maand`                                     `0`
`overlijden.indicatieOverleden`                                         `True`
`overlijden.datum.dag`                                                  `0`
`overlijden.datum.datum`                                                `string`
`overlijden.datum.jaar`                                                 `0`
`overlijden.datum.maand`                                                `0`
`overlijden.land.code`                                                  `string`
`overlijden.land.omschrijving`                                          `inp.overlijdenLand`
`overlijden.plaats.code`                                                `string`
`overlijden.plaats.omschrijving`                                        `inp.overlijdenplaats`
`overlijden.inOnderzoek.datum`                                          `boolean(overlijdensdatum)`
`overlijden.inOnderzoek.land`                                           `boolean(inp.overlijdenLand)`
`overlijden.inOnderzoek.plaats`                                         `boolean(inp.overlijdenplaats)`
`overlijden.inOnderzoek.datumIngangOnderzoek.dag`                       `0`
`overlijden.inOnderzoek.datumIngangOnderzoek.datum`                     `string`
`overlijden.inOnderzoek.datumIngangOnderzoek.jaar`                      `0`
`overlijden.inOnderzoek.datumIngangOnderzoek.maand`                     `0`
`verblijfplaats.functieAdres`                                           `woonadres`
`verblijfplaats.huisletter`                                             `verblijfsadres.aoa.huisletter`
`verblijfplaats.huisnummer`                                             `verblijfsadres.aoa.huisnummer`
`verblijfplaats.huisnummertoevoeging`                                   `verblijfsadres.aoa.huisnummertoevoeging`
`verblijfplaats.aanduidingBijHuisnummer`                                `tegenover`
`verblijfplaats.identificatiecodeNummeraanduiding`                      `string`
`verblijfplaats.naamOpenbareRuimte`                                     `string`
`verblijfplaats.postcode`                                               `verblijfsadres.aoa.postcode`
`verblijfplaats.woonplaatsnaam`                                         `verblijfsadres.wpl.woonplaatsNaam`
`verblijfplaats.identificatiecodeAdresseerbaarObject`                   `string`
`verblijfplaats.indicatieVestigingVanuitBuitenland`                     `True`
`verblijfplaats.locatiebeschrijving`                                    `string`
`verblijfplaats.straatnaam`                                             `verblijfsadres.gor.straatnaam`
`verblijfplaats.vanuitVertrokkenOnbekendWaarheen`                       `True`
`verblijfplaats.datumAanvangAdreshouding.dag`                           `0`
`verblijfplaats.datumAanvangAdreshouding.datum`                         `string`
`verblijfplaats.datumAanvangAdreshouding.jaar`                          `0`
`verblijfplaats.datumAanvangAdreshouding.maand`                         `0`
`verblijfplaats.datumIngangGeldigheid.dag`                              `0`
`verblijfplaats.datumIngangGeldigheid.datum`                            `string`
`verblijfplaats.datumIngangGeldigheid.jaar`                             `0`
`verblijfplaats.datumIngangGeldigheid.maand`                            `0`
`verblijfplaats.datumInschrijvingInGemeente.dag`                        `0`
`verblijfplaats.datumInschrijvingInGemeente.datum`                      `string`
`verblijfplaats.datumInschrijvingInGemeente.jaar`                       `0`
`verblijfplaats.datumInschrijvingInGemeente.maand`                      `0`
`verblijfplaats.datumVestigingInNederland.dag`                          `0`
`verblijfplaats.datumVestigingInNederland.datum`                        `string`
`verblijfplaats.datumVestigingInNederland.jaar`                         `0`
`verblijfplaats.datumVestigingInNederland.maand`                        `0`
`verblijfplaats.gemeenteVanInschrijving.code`                           `string`
`verblijfplaats.gemeenteVanInschrijving.omschrijving`                   `string`
`verblijfplaats.landVanwaarIngeschreven.code`                           `string`
`verblijfplaats.landVanwaarIngeschreven.omschrijving`                   `string`
`verblijfplaats.verblijfBuitenland.adresRegel1`                         `string`
`verblijfplaats.verblijfBuitenland.adresRegel2`                         `string`
`verblijfplaats.verblijfBuitenland.adresRegel3`                         `string`
`verblijfplaats.verblijfBuitenland.vertrokkenOnbekendWaarheen`          `True`
`verblijfplaats.verblijfBuitenland.land.code`                           `string`
`verblijfplaats.verblijfBuitenland.land.omschrijving`                   `string`
`verblijfplaats.aanduidingBijHuisnummer`                                `True`
`verblijfplaats.datumAanvangAdreshouding`                               `True`
`verblijfplaats.datumIngangGeldigheid`                                  `True`
`verblijfplaats.datumInschrijvingInGemeente`                            `True`
`verblijfplaats.datumVestigingInNederland`                              `True`
`verblijfplaats.functieAdres`                                           `True`
`verblijfplaats.gemeenteVanInschrijving`                                `True`
`verblijfplaats.huisletter`                                             `boolean(verblijfsadres.aoa.huisletter)`
`verblijfplaats.huisnummer`                                             `boolean(verblijfsadres.aoa.huisnummer)`
`verblijfplaats.huisnummertoevoeging`                                   `boolean(verblijfsadres.aoa.huisnummertoevoeging)`
`verblijfplaats.identificatiecodeNummeraanduiding`                      `True`
`verblijfplaats.identificatiecodeAdresseerbaarObject`                   `True`
`verblijfplaats.landVanwaarIngeschreven`                                `True`
`verblijfplaats.locatiebeschrijving`                                    `True`
`verblijfplaats.naamOpenbareRuimte`                                     `True`
`verblijfplaats.postcode`                                               `boolean(verblijfsadres.aoa.postcode)`
`verblijfplaats.straatnaam`                                             `boolean(verblijfsadres.gor.straatnaam)`
`verblijfplaats.verblijfBuitenland`                                     `True`
`verblijfplaats.woonplaatsnaam`                                         `boolean(verblijfsadres.wpl.woonplaatsNaam)`
`verblijfplaats.datumIngangOnderzoek.dag`                               `0`
`verblijfplaats.datumIngangOnderzoek.datum`                             `string`
`verblijfplaats.datumIngangOnderzoek.jaar`                              `0`
`verblijfplaats.datumIngangOnderzoek.maand`                             `0`
`gezagsverhouding.indicatieCurateleRegister`                            `True`
`gezagsverhouding.indicatieGezagMinderjarige`                           `ouder1`
`gezagsverhouding.inOnderzoek.indicatieCurateleRegister`                `True`
`gezagsverhouding.inOnderzoek.indicatieGezagMinderjarige`               `True`
`gezagsverhouding.inOnderzoek.datumIngangOnderzoek.dag`                 `0`
`gezagsverhouding.inOnderzoek.datumIngangOnderzoek.datum`               `string`
`gezagsverhouding.inOnderzoek.datumIngangOnderzoek.jaar`                `0`
`gezagsverhouding.inOnderzoek.datumIngangOnderzoek.maand`               `0`
`verblijfstitel.aanduiding.code`                                        `string`
`verblijfstitel.aanduiding.omschrijving`                                `string`
`verblijfstitel.datumEinde.dag`                                         `0`
`verblijfstitel.datumEinde.datum`                                       `string`
`verblijfstitel.datumEinde.jaar`                                        `0`
`verblijfstitel.datumEinde.maand`                                       `0`
`verblijfstitel.datumIngang.dag`                                        `0`
`verblijfstitel.datumIngang.datum`                                      `string`
`verblijfstitel.datumIngang.jaar`                                       `0`
`verblijfstitel.datumIngang.maand`                                      `0`
`verblijfstitel.inOnderzoek.aanduiding`                                 `True`
`verblijfstitel.inOnderzoek.datumEinde`                                 `True`
`verblijfstitel.inOnderzoek.datumIngang`                                `True`
`verblijfstitel.inOnderzoek.datumIngangOnderzoek.dag`                   `0`
`verblijfstitel.inOnderzoek.datumIngangOnderzoek.datum`                 `string`
`verblijfstitel.inOnderzoek.datumIngangOnderzoek.jaar`                  `0`
`verblijfstitel.inOnderzoek.datumIngangOnderzoek.maand`                 `0`
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