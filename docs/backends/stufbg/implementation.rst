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
`naam.inOnderzoek.geslachtsnaam`                                        *(`inOnderzoek.groepsnaam` == `Persoonsgegevens`)*                      One of the multiple inOnderzoek occurrances matches
`naam.inOnderzoek.voornamen`                                            *(`inOnderzoek.groepsnaam` == `Persoonsgegevens`)*                      One of the multiple inOnderzoek occurrances matches
`naam.inOnderzoek.voorvoegsel`                                          *(`inOnderzoek.groepsnaam` == `Persoonsgegevens`)*                      One of the multiple inOnderzoek occurrances matches
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
`geboorte.inOnderzoek.datum`                                            *(`inOnderzoek.groepsnaam` == `Persoonsgegevens`)*                      One of the multiple inOnderzoek occurrances matches
`geboorte.inOnderzoek.land`                                             *(`inOnderzoek.groepsnaam` == `Persoonsgegevens`)*                      One of the multiple inOnderzoek occurrances matches
`geboorte.inOnderzoek.plaats`                                           *(`inOnderzoek.groepsnaam` == `Persoonsgegevens`)*                      One of the multiple inOnderzoek occurrances matches
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
`kiesrecht.einddatumUitsluitingEuropeesKiesrecht.dag`                   1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`kiesrecht.einddatumUitsluitingEuropeesKiesrecht.datum`                 "01-01-1900"                                                            Fixed value since not in StUF-BG and cannot be `null`.
`kiesrecht.einddatumUitsluitingEuropeesKiesrecht.jaar`                  1900                                                                    Fixed value since not in StUF-BG and cannot be `null`.
`kiesrecht.einddatumUitsluitingEuropeesKiesrecht.maand`                 1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`kiesrecht.einddatumUitsluitingKiesrecht.dag`                           1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`kiesrecht.einddatumUitsluitingKiesrecht.datum`                         "01-01-1900"                                                            Fixed value since not in StUF-BG and cannot be `null`.
`kiesrecht.einddatumUitsluitingKiesrecht.jaar`                          1900                                                                    Fixed value since not in StUF-BG and cannot be `null`.
`kiesrecht.einddatumUitsluitingKiesrecht.maand`                         1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`inOnderzoek.burgerservicenummer`                                       *(`inOnderzoek.groepsnaam` == `Persoonsgegevens`)*                      One of the multiple inOnderzoek occurrances matches
`inOnderzoek.geslachtsaanduiding`                                       *(`inOnderzoek.groepsnaam` == `Persoonsgegevens`)*                      One of the multiple inOnderzoek occurrances matches
`inOnderzoek.datumIngangOnderzoek.dag`                                  1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`inOnderzoek.datumIngangOnderzoek.datum`                                "01-01-1900"                                                            Fixed value since not in StUF-BG and cannot be `null`.
`inOnderzoek.datumIngangOnderzoek.jaar`                                 1900                                                                    Fixed value since not in StUF-BG and cannot be `null`.
`inOnderzoek.datumIngangOnderzoek.maand`                                1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`nationaliteit.aanduidingBijzonderNederlanderschap`                     "string"                                                                TODO
`nationaliteit.datumIngangGeldigheid.dag`                               DAY(`inp.heeftAlsNationaliteit.inp.datumVerkrijging`)
`nationaliteit.datumIngangGeldigheid.datum`                             `inp.heeftAlsNationaliteit.inp.datumVerkrijging`
`nationaliteit.datumIngangGeldigheid.jaar`                              YEAR(`inp.heeftAlsNationaliteit.inp.datumVerkrijging`)
`nationaliteit.datumIngangGeldigheid.maand`                             MONTH(`inp.heeftAlsNationaliteit.inp.datumVerkrijging`)
`nationaliteit.nationaliteit.code`                                      `string`                                                                TODO
`nationaliteit.nationaliteit.omschrijving`                              `string`                                                                TODO
`nationaliteit.redenOpname.code`                                        inp.heeftAlsNationaliteit.inp.redenVerkrijging
`nationaliteit.redenOpname.omschrijving`                                `string`                                                                TODO
`nationaliteit.inOnderzoek.aanduidingBijzonderNederlanderschap`         *(`inOnderzoek.elementnaam` == `aanduidingBijzonderNederlanderschap`)*   One of the multiple inOnderzoek occurrances matches
`nationaliteit.inOnderzoek.nationaliteit`                               *(`inOnderzoek.groepsnaam` == `Nationaliteit`)*   One of the multiple inOnderzoek occurrances matches
`nationaliteit.inOnderzoek.redenOpname`                                 `True`                                                                  TODO
`nationaliteit.inOnderzoek.datumIngangOnderzoek.dag`                    1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`nationaliteit.inOnderzoek.datumIngangOnderzoek.datum`                  "01-01-1900"                                                            Fixed value since not in StUF-BG and cannot be `null`.
`nationaliteit.inOnderzoek.datumIngangOnderzoek.jaar`                   1900                                                                    Fixed value since not in StUF-BG and cannot be `null`.
`nationaliteit.inOnderzoek.datumIngangOnderzoek.maand`                  1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
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
`overlijden.land.code`                                                  COUNTRY_CODE(`inp.overlijdenLand`)
`overlijden.land.omschrijving`                                          `inp.overlijdenLand`
`overlijden.plaats.code`                                                CITY_CODE(`inp.overlijdenplaats`)
`overlijden.plaats.omschrijving`                                        `inp.overlijdenplaats`
`overlijden.inOnderzoek.datum`                                          *(`inOnderzoek.groepsnaam` == `Overlijden`)*                      One of the multiple inOnderzoek occurrances matches
`overlijden.inOnderzoek.land`                                           *(`inOnderzoek.groepsnaam` == `Overlijden`)*                      One of the multiple inOnderzoek occurrances matches
`overlijden.inOnderzoek.plaats`                                         *(`inOnderzoek.groepsnaam` == `Overlijden`)*                      One of the multiple inOnderzoek occurrances matches
`overlijden.inOnderzoek.datumIngangOnderzoek.dag`                       1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`overlijden.inOnderzoek.datumIngangOnderzoek.datum`                     "01-01-1900"                                                            Fixed value since not in StUF-BG and cannot be `null`.
`overlijden.inOnderzoek.datumIngangOnderzoek.jaar`                      1900                                                                    Fixed value since not in StUF-BG and cannot be `null`.
`overlijden.inOnderzoek.datumIngangOnderzoek.maand`                     1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
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
`verblijfplaats.datumAanvangAdreshouding.dag`                           1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.datumAanvangAdreshouding.datum`                         "01-01-1900"                                                            Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.datumAanvangAdreshouding.jaar`                          1900                                                                    Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.datumAanvangAdreshouding.maand`                         1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.datumIngangGeldigheid.dag`                              DAY(`inp.verblijftIn.gerelateerde.ingangsdatumObject`)
`verblijfplaats.datumIngangGeldigheid.datum`                            `inp.verblijftIn.gerelateerde.ingangsdatumObject`
`verblijfplaats.datumIngangGeldigheid.jaar`                             YEAR(`inp.verblijftIn.gerelateerde.ingangsdatumObject`)
`verblijfplaats.datumIngangGeldigheid.maand`                            MONTH(`inp.verblijftIn.gerelateerde.ingangsdatumObject`)
`verblijfplaats.datumInschrijvingInGemeente.dag`                        1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.datumInschrijvingInGemeente.datum`                      "01-01-1900"                                                            Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.datumInschrijvingInGemeente.jaar`                       1900                                                                    Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.datumInschrijvingInGemeente.maand`                      1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.datumVestigingInNederland.dag`                          1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.datumVestigingInNederland.datum`                        "01-01-1900"                                                            Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.datumVestigingInNederland.jaar`                         1900                                                                    Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.datumVestigingInNederland.maand`                        1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.gemeenteVanInschrijving.code`                           `inp.verblijftIn.gerelateerde.gemeenteCode`
`verblijfplaats.gemeenteVanInschrijving.omschrijving`                   `inp.verblijftIn.gerelateerde.gemeenteNaam`
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
`verblijfplaats.inOnderzoek.huisletter`                                 *(`inOnderzoek.groepsnaam` == `Verblijfsplaats`)*
`verblijfplaats.inOnderzoek.huisnummer`                                 *(`inOnderzoek.groepsnaam` == `Verblijfsplaats`)*
`verblijfplaats.inOnderzoek.huisnummertoevoeging`                       *(`inOnderzoek.groepsnaam` == `Verblijfsplaats`)*
`verblijfplaats.inOnderzoek.identificatiecodeNummeraanduiding`          *(`inOnderzoek.groepsnaam` == `Verblijfsplaats`)*
`verblijfplaats.inOnderzoek.identificatiecodeAdresseerbaarObject`       *(`inOnderzoek.groepsnaam` == `Verblijfsplaats`)*
`verblijfplaats.inOnderzoek.landVanwaarIngeschreven`                    *(`inOnderzoek.groepsnaam` == `Verblijfsplaats`)*
`verblijfplaats.inOnderzoek.locatiebeschrijving`                        *(`inOnderzoek.groepsnaam` == `Verblijfsplaats`)*
`verblijfplaats.inOnderzoek.naamOpenbareRuimte`                         *(`inOnderzoek.groepsnaam` == `Verblijfsplaats`)*
`verblijfplaats.inOnderzoek.postcode`                                   *(`inOnderzoek.groepsnaam` == `Verblijfsplaats`)*
`verblijfplaats.inOnderzoek.straatnaam`                                 *(`inOnderzoek.groepsnaam` == `Verblijfsplaats`)*
`verblijfplaats.inOnderzoek.verblijfBuitenland`                         *(`inOnderzoek.groepsnaam` == `Verblijfsplaats`)*
`verblijfplaats.inOnderzoek.woonplaatsnaam`                             *(`inOnderzoek.groepsnaam` == `Verblijfsplaats`)*
`verblijfplaats.inOnderzoek.datumIngangOnderzoek.dag`                   1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.inOnderzoek.datumIngangOnderzoek.datum`                 "01-01-1900"                                                            Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.inOnderzoek.datumIngangOnderzoek.jaar`                  1900                                                                    Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.inOnderzoek.datumIngangOnderzoek.maand`                 1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`gezagsverhouding.indicatieCurateleRegister`                            `ing.indicatieCurateleRegister`
`gezagsverhouding.indicatieGezagMinderjarige`                           `string`                                                                TODO
`gezagsverhouding.inOnderzoek.indicatieCurateleRegister`                *(`inOnderzoek.groepsnaam` == `Gezagsverhouding`)*
`gezagsverhouding.inOnderzoek.indicatieGezagMinderjarige`               *(`inOnderzoek.groepsnaam` == `Gezagsverhouding`)*
`gezagsverhouding.inOnderzoek.datumIngangOnderzoek.dag`                 *(`inOnderzoek.groepsnaam` == `Gezagsverhouding`)*
`gezagsverhouding.inOnderzoek.datumIngangOnderzoek.datum`               *(`inOnderzoek.groepsnaam` == `Gezagsverhouding`)*
`gezagsverhouding.inOnderzoek.datumIngangOnderzoek.jaar`                *(`inOnderzoek.groepsnaam` == `Gezagsverhouding`)*
`gezagsverhouding.inOnderzoek.datumIngangOnderzoek.maand`               *(`inOnderzoek.groepsnaam` == `Gezagsverhouding`)*
`verblijfstitel.aanduiding.code`                                        `vbt.aanduidingVerblijfstitel`
`verblijfstitel.aanduiding.omschrijving`                                *(calculated)*                                                          Obtained from mapping https://publicaties.rvig.nl/dsresource?objectid=4801&type=org
`verblijfstitel.datumEinde.dag`                                         DAY(`ing.datumVerliesVerblijfstitel`)
`verblijfstitel.datumEinde.datum`                                       `ing.datumVerliesVerblijfstitel`
`verblijfstitel.datumEinde.jaar`                                        YEAR(`ing.datumVerliesVerblijfstitel`)
`verblijfstitel.datumEinde.maand`                                       MONTH(`ing.datumVerliesVerblijfstitel`)
`verblijfstitel.datumIngang.dag`                                        DAY(`ing.datumVerkrijgingVerblijfstitel`)
`verblijfstitel.datumIngang.datum`                                      `ing.datumVerkrijgingVerblijfstitel`
`verblijfstitel.datumIngang.jaar`                                       YEAR(`ing.datumVerkrijgingVerblijfstitel`)
`verblijfstitel.datumIngang.maand`                                      MONTH(`ing.datumVerkrijgingVerblijfstitel`)
`verblijfstitel.inOnderzoek.aanduiding`                                 *(`inOnderzoek.elementnaam` == `aanduidingVerblijfstitel`)*             One of the multiple inOnderzoek occurrances matches
`verblijfstitel.inOnderzoek.datumEinde`                                 "01-01-1900"                                                            Fixed value since not in StUF-BG and cannot be `null`.
`verblijfstitel.inOnderzoek.datumIngang`                                "01-01-1900"                                                            Fixed value since not in StUF-BG and cannot be `null`.
`verblijfstitel.inOnderzoek.datumIngangOnderzoek.dag`                   1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`verblijfstitel.inOnderzoek.datumIngangOnderzoek.datum`                 "01-01-1900"                                                            Fixed value since not in StUF-BG and cannot be `null`.
`verblijfstitel.inOnderzoek.datumIngangOnderzoek.jaar`                  1900                                                                    Fixed value since not in StUF-BG and cannot be `null`.
`verblijfstitel.inOnderzoek.datumIngangOnderzoek.maand`                 1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
=====================================================================   =====================================================================   =====================================================================


Kind
--------------------

=====================================================================   =====================================================================   =====================================================================
API attribute                                                           StUF-BG attribute                                                       Design decision  remarks
=====================================================================   =====================================================================   =====================================================================
burgerservicenummer                                                     `inp.heeftAlsKinderen.inp.bsn`
geheimhoudingPersoonsgegevens                                           `inp.heeftAlsKinderen.inp.indicatieGeheim`
naam.geslachtsnaam                                                      `inp.heeftAlsKinderen.geslachtsnaam`
naam.voorletters                                                        `inp.heeftAlsKinderen.voorletters`
naam.voornamen                                                          `inp.heeftAlsKinderen.voornamen`
naam.voorvoegsel                                                        `inp.heeftAlsKinderen.voorvoegselGeslachtsnaam`
naam.inOnderzoek.geslachtsnaam                                          *(`inp.heeftAlsKinderen.inOnderzoek.groepsnaam` == `Persoonsgegevens`)* One of the multiple inOnderzoek occurrances matches
naam.inOnderzoek.voornamen                                              *(`inp.heeftAlsKinderen.inOnderzoek.groepsnaam` == `Persoonsgegevens`)* One of the multiple inOnderzoek occurrances matches
naam.inOnderzoek.voorvoegsel                                            *(`inp.heeftAlsKinderen.inOnderzoek.groepsnaam` == `Persoonsgegevens`)* One of the multiple inOnderzoek occurrances matches
naam.inOnderzoek.datumIngangOnderzoek.dag                               1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
naam.inOnderzoek.datumIngangOnderzoek.datum                             "01-01-1900"                                                            Fixed value since not in StUF-BG and cannot be `null`.
naam.inOnderzoek.datumIngangOnderzoek.jaar                              1900                                                                    Fixed value since not in StUF-BG and cannot be `null`.
naam.inOnderzoek.datumIngangOnderzoek.maand                             1
geboorte.datum.dag                                                      DAY(`inp.heeftAlsKinderen.geboortedatum`)
geboorte.datum.datum                                                    `inp.heeftAlsKinderen.geboortedatum`
geboorte.datum.jaar                                                     YEAR(`inp.heeftAlsKinderen.geboortedatum`)
geboorte.datum.maand                                                    MONTH(`inp.heeftAlsKinderen.geboortedatum`)
geboorte.land.code                                                      COUNTRY_CODE(`inp.heeftAlsKinderen.inp.geboorteLand`)
geboorte.land.omschrijving                                              `inp.heeftAlsKinderen.inp.geboorteLand`
geboorte.plaats.code                                                    CITY_CODE(`inp.heeftAlsKinderen.inp.geboorteplaats`)
geboorte.plaats.omschrijving                                            `inp.heeftAlsKinderen.inp.geboorteplaats`
geboorte.inOnderzoek.datum                                              *(`inp.heeftAlsKinderen.inOnderzoek.groepsnaam` == `Persoonsgegevens`)* One of the multiple inOnderzoek occurrances matches
geboorte.inOnderzoek.land                                               *(`inp.heeftAlsKinderen.inOnderzoek.groepsnaam` == `Persoonsgegevens`)* One of the multiple inOnderzoek occurrances matches
geboorte.inOnderzoek.plaats                                             *(`inp.heeftAlsKinderen.inOnderzoek.groepsnaam` == `Persoonsgegevens`)* One of the multiple inOnderzoek occurrances matches
geboorte.inOnderzoek.datumIngangOnderzoek.dag                           1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
geboorte.inOnderzoek.datumIngangOnderzoek.datum                         "01-01-1900"                                                            Fixed value since not in StUF-BG and cannot be `null`.
geboorte.inOnderzoek.datumIngangOnderzoek.jaar                          1900                                                                    Fixed value since not in StUF-BG and cannot be `null`.
geboorte.inOnderzoek.datumIngangOnderzoek.maand                         1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
leeftijd                                                                *(calculated)*                                                          See `features`_
inOnderzoek.burgerservicenummer                                         *(`inp.heeftAlsKinderen.inOnderzoek.groepsnaam` == `Persoonsgegevens`)* One of the multiple inOnderzoek occurrances matches
inOnderzoek.datumIngangOnderzoek.dag                                    1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
inOnderzoek.datumIngangOnderzoek.datum                                  "01-01-1900"                                                            Fixed value since not in StUF-BG and cannot be `null`.
inOnderzoek.datumIngangOnderzoek.jaar                                   1900                                                                    Fixed value since not in StUF-BG and cannot be `null`.
inOnderzoek.datumIngangOnderzoek.maand                                  1                                                                       Fixed value since not in StUF-BG and cannot be `null`.
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
