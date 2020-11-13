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

=====================================================================   ================================================================================   =====================================================================
API attribute                                                           StUF-BG attribute                                                                  Design decision  remarks
=====================================================================   ================================================================================   =====================================================================
`burgerservicenummer`                                                   `inp.bsn`
`geheimhoudingPersoonsgegevens`                                         `inp.indicatieGeheim`
`naam.geslachtsnaam`                                                    `geslachtsnaam`
`naam.voorletters`                                                      `voorletters`
`naam.voornamen`                                                        `voornamen`
`naam.voorvoegsel`                                                      `voorvoegselGeslachtsnaam`
`naam.inOnderzoek.geslachtsnaam`                                        *(`inOnderzoek.groepsnaam` == `Persoonsgegevens`)*                                 One of the multiple inOnderzoek occurrances matches
`naam.inOnderzoek.voornamen`                                            *(`inOnderzoek.groepsnaam` == `Persoonsgegevens`)*                                 One of the multiple inOnderzoek occurrances matches
`naam.inOnderzoek.voorvoegsel`                                          *(`inOnderzoek.groepsnaam` == `Persoonsgegevens`)*                                 One of the multiple inOnderzoek occurrances matches
`naam.inOnderzoek.datumIngangOnderzoek.dag`                             1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`naam.inOnderzoek.datumIngangOnderzoek.datum`                           "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`naam.inOnderzoek.datumIngangOnderzoek.jaar`                            1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
`naam.inOnderzoek.datumIngangOnderzoek.maand`                           1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`naam.aanhef`                                                           *(calculated)*                                                                     See `features`_ (TODO)
`naam.aanschrijfwijze`                                                  *(calculated)*                                                                     See `features`_ (TODO)
`naam.gebruikInLopendeTekst`                                            *(calculated)*                                                                     See `features`_ (TODO)
`naam.aanduidingNaamgebruik`                                            `aanduidingNaamgebruik`
`geboorte.datum.dag`                                                    DAY(`geboortedatum`)
`geboorte.datum.datum`                                                  `geboortedatum`
`geboorte.datum.jaar`                                                   YEAR(`geboortedatum`)
`geboorte.datum.maand`                                                  MONTH(`geboortedatum`)
`geboorte.land.code`                                                    COUNTRY_CODE(`inp.geboorteLand`)                                                   TODO
`geboorte.land.omschrijving`                                            `inp.geboorteLand`
`geboorte.plaats.code`                                                  CITY_CODE(`inp.geboorteplaats`)                                                    TODO
`geboorte.plaats.omschrijving`                                          `inp.geboorteplaats`
`geboorte.inOnderzoek.datum`                                            *(`inOnderzoek.groepsnaam` == `Persoonsgegevens`)*                                 One of the multiple inOnderzoek occurrances matches
`geboorte.inOnderzoek.land`                                             *(`inOnderzoek.groepsnaam` == `Persoonsgegevens`)*                                 One of the multiple inOnderzoek occurrances matches
`geboorte.inOnderzoek.plaats`                                           *(`inOnderzoek.groepsnaam` == `Persoonsgegevens`)*                                 One of the multiple inOnderzoek occurrances matches
`geboorte.inOnderzoek.datumIngangOnderzoek.dag`                         1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`geboorte.inOnderzoek.datumIngangOnderzoek.datum`                       "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`geboorte.inOnderzoek.datumIngangOnderzoek.jaar`                        1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
`geboorte.inOnderzoek.datumIngangOnderzoek.maand`                       1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`geslachtsaanduiding`                                                   `geslachtsaanduiding`
`leeftijd`                                                              *(calculated)*                                                                     See `features`_
`datumEersteInschrijvingGBA.dag`                                        DAY(`inp.datumInschrijving`)
`datumEersteInschrijvingGBA.datum`                                      `inp.datumInschrijving`
`datumEersteInschrijvingGBA.jaar`                                       YEAR(`inp.datumInschrijving`)
`datumEersteInschrijvingGBA.maand`                                      MONTH(`inp.datumInschrijving`)
`kiesrecht.europeesKiesrecht`                                           *(`ing.aanduidingEuropeesKiesrecht` == `2`)*                                       StUF-BG value "2" evaluates to "true".
`kiesrecht.uitgeslotenVanKiesrecht`                                     *(`ing.aanduidingUitgeslotenKiesrecht` == `A`)*                                    StUF-BG value "A" evaluates to "true".
`kiesrecht.einddatumUitsluitingEuropeesKiesrecht.dag`                   1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`kiesrecht.einddatumUitsluitingEuropeesKiesrecht.datum`                 "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`kiesrecht.einddatumUitsluitingEuropeesKiesrecht.jaar`                  1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
`kiesrecht.einddatumUitsluitingEuropeesKiesrecht.maand`                 1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`kiesrecht.einddatumUitsluitingKiesrecht.dag`                           1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`kiesrecht.einddatumUitsluitingKiesrecht.datum`                         "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`kiesrecht.einddatumUitsluitingKiesrecht.jaar`                          1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
`kiesrecht.einddatumUitsluitingKiesrecht.maand`                         1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`inOnderzoek.burgerservicenummer`                                       *(`inOnderzoek.groepsnaam` == `Persoonsgegevens`)*                                 One of the multiple inOnderzoek occurrances matches
`inOnderzoek.geslachtsaanduiding`                                       *(`inOnderzoek.groepsnaam` == `Persoonsgegevens`)*                                 One of the multiple inOnderzoek occurrances matches
`inOnderzoek.datumIngangOnderzoek.dag`                                  1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`inOnderzoek.datumIngangOnderzoek.datum`                                "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`inOnderzoek.datumIngangOnderzoek.jaar`                                 1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
`inOnderzoek.datumIngangOnderzoek.maand`                                1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`nationaliteit.aanduidingBijzonderNederlanderschap`                     `inp.aanduidingBijzonderNederlanderschap`
`nationaliteit.datumIngangGeldigheid.dag`                               DAY(`inp.heeftAlsNationaliteit.inp.datumVerkrijging`)
`nationaliteit.datumIngangGeldigheid.datum`                             `inp.heeftAlsNationaliteit.inp.datumVerkrijging`
`nationaliteit.datumIngangGeldigheid.jaar`                              YEAR(`inp.heeftAlsNationaliteit.inp.datumVerkrijging`)
`nationaliteit.datumIngangGeldigheid.maand`                             MONTH(`inp.heeftAlsNationaliteit.inp.datumVerkrijging`)
`nationaliteit.nationaliteit.code`                                      `inp.heeftAlsNationaliteit.gerelateerde.code`
`nationaliteit.nationaliteit.omschrijving`                              `inp.heeftAlsNationaliteit.gerelateerde.omschrijving`
`nationaliteit.redenOpname.code`                                        REDEN_CODE(`inp.heeftAlsNationaliteit.inp.redenVerkrijging`)                       TODO
`nationaliteit.redenOpname.omschrijving`                                `inp.heeftAlsNationaliteit.inp.redenVerkrijging`
`nationaliteit.inOnderzoek.aanduidingBijzonderNederlanderschap`         *(`inOnderzoek.elementnaam` == `aanduidingBijzonderNederlanderschap`)*             One of the multiple inOnderzoek occurrances matches
`nationaliteit.inOnderzoek.nationaliteit`                               *(`inOnderzoek.groepsnaam` == `Nationaliteit`)*                                    One of the multiple inOnderzoek occurrances matches
`nationaliteit.inOnderzoek.redenOpname`                                 `True`                                                                             TODO
`nationaliteit.inOnderzoek.datumIngangOnderzoek.dag`                    1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`nationaliteit.inOnderzoek.datumIngangOnderzoek.datum`                  "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`nationaliteit.inOnderzoek.datumIngangOnderzoek.jaar`                   1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
`nationaliteit.inOnderzoek.datumIngangOnderzoek.maand`                  1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`opschortingBijhouding.reden`                                           `inp.redenOpschortingBijhouding`
`opschortingBijhouding.datum.dag`                                       DAY(`inp.datumOpschortingBijhouding`)
`opschortingBijhouding.datum.datum`                                     `inp.datumOpschortingBijhouding`
`opschortingBijhouding.datum.jaar`                                      YEAR(`inp.datumOpschortingBijhouding`)
`opschortingBijhouding.datum.maand`                                     MONTH(`inp.datumOpschortingBijhouding`)
`overlijden.indicatieOverleden`                                         *(`inp.redenOpschortingBijhouding` == `O`)*
`overlijden.datum.dag`                                                  DAY(`overlijdensdatum`)
`overlijden.datum.datum`                                                `overlijdensdatum`
`overlijden.datum.jaar`                                                 YEAR(`overlijdensdatum`)
`overlijden.datum.maand`                                                MONTH(`overlijdensdatum`)
`overlijden.land.code`                                                  COUNTRY_CODE(`inp.overlijdenLand`)                                                 TODO
`overlijden.land.omschrijving`                                          `inp.overlijdenLand`
`overlijden.plaats.code`                                                CITY_CODE(`inp.overlijdenplaats`)                                                  TODO
`overlijden.plaats.omschrijving`                                        `inp.overlijdenplaats`
`overlijden.inOnderzoek.datum`                                          *(`inOnderzoek.groepsnaam` == `Overlijden`)*                                       One of the multiple inOnderzoek occurrances matches
`overlijden.inOnderzoek.land`                                           *(`inOnderzoek.groepsnaam` == `Overlijden`)*                                       One of the multiple inOnderzoek occurrances matches
`overlijden.inOnderzoek.plaats`                                         *(`inOnderzoek.groepsnaam` == `Overlijden`)*                                       One of the multiple inOnderzoek occurrances matches
`overlijden.inOnderzoek.datumIngangOnderzoek.dag`                       1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`overlijden.inOnderzoek.datumIngangOnderzoek.datum`                     "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`overlijden.inOnderzoek.datumIngangOnderzoek.jaar`                      1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
`overlijden.inOnderzoek.datumIngangOnderzoek.maand`                     1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.functieAdres`                                           `woonadres`                                                                        TODO
`verblijfplaats.huisletter`                                             `verblijfsadres.aoa.huisletter`
`verblijfplaats.huisnummer`                                             `verblijfsadres.aoa.huisnummer`
`verblijfplaats.huisnummertoevoeging`                                   `verblijfsadres.aoa.huisnummertoevoeging`
`verblijfplaats.aanduidingBijHuisnummer`                                null                                                                           TODO
`verblijfplaats.identificatiecodeNummeraanduiding`                      `verblijfsadres.aoa.identificatie`
`verblijfplaats.naamOpenbareRuimte`                                     `verblijfsadres.gor.openbareRuimteNaam`
`verblijfplaats.postcode`                                               `verblijfsadres.aoa.postcode`
`verblijfplaats.woonplaatsnaam`                                         `verblijfsadres.wpl.woonplaatsNaam`
`verblijfplaats.identificatiecodeAdresseerbaarObject`                   `verblijfsadres.wpl.identificatie`
`verblijfplaats.indicatieVestigingVanuitBuitenland`                     `True`                                                                             TODO
`verblijfplaats.locatiebeschrijving`                                    `verblijfsadres.inp.locatiebeschrijving`
`verblijfplaats.straatnaam`                                             `verblijfsadres.gor.straatnaam`
`verblijfplaats.vanuitVertrokkenOnbekendWaarheen`                       `True`                                                                             TODO
`verblijfplaats.datumAanvangAdreshouding.dag`                           DAY(`verblijfsadres.begindatumVerblijf`)
`verblijfplaats.datumAanvangAdreshouding.datum`                         `verblijfsadres.begindatumVerblijf`
`verblijfplaats.datumAanvangAdreshouding.jaar`                          YEAR(`verblijfsadres.begindatumVerblijf`)
`verblijfplaats.datumAanvangAdreshouding.maand`                         MONTH(`verblijfsadres.begindatumVerblijf`)
`verblijfplaats.datumIngangGeldigheid.dag`                              DAY(`inp.verblijftIn.gerelateerde.ingangsdatumObject`)
`verblijfplaats.datumIngangGeldigheid.datum`                            `inp.verblijftIn.gerelateerde.ingangsdatumObject`
`verblijfplaats.datumIngangGeldigheid.jaar`                             YEAR(`inp.verblijftIn.gerelateerde.ingangsdatumObject`)
`verblijfplaats.datumIngangGeldigheid.maand`                            MONTH(`inp.verblijftIn.gerelateerde.ingangsdatumObject`)
`verblijfplaats.datumInschrijvingInGemeente.dag`                        1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.datumInschrijvingInGemeente.datum`                      "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.datumInschrijvingInGemeente.jaar`                       1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.datumInschrijvingInGemeente.maand`                      1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.datumVestigingInNederland.dag`                          1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.datumVestigingInNederland.datum`                        "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.datumVestigingInNederland.jaar`                         1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.datumVestigingInNederland.maand`                        1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.gemeenteVanInschrijving.code`                           `inp.verblijftIn.gerelateerde.gemeenteCode`
`verblijfplaats.gemeenteVanInschrijving.omschrijving`                   `inp.verblijftIn.gerelateerde.gemeenteNaam`
`verblijfplaats.landVanwaarIngeschreven.code`                           ""                                                                                 TODO
`verblijfplaats.landVanwaarIngeschreven.omschrijving`                   ""                                                                                 TODO
`verblijfplaats.verblijfBuitenland.adresRegel1`                         `sub.verblijfBuitenland.sub.adresBuitenland1`
`verblijfplaats.verblijfBuitenland.adresRegel2`                         `sub.verblijfBuitenland.sub.adresBuitenland2`
`verblijfplaats.verblijfBuitenland.adresRegel3`                         `sub.verblijfBuitenland.sub.adresBuitenland3`
`verblijfplaats.verblijfBuitenland.vertrokkenOnbekendWaarheen`          `True`                                                                             TODO
`verblijfplaats.verblijfBuitenland.land.code`                           COUNTRY_CODE(sub.verblijfBuitenland.lnd.landcode)                                  TODO
`verblijfplaats.verblijfBuitenland.land.omschrijving`                   `sub.verblijfBuitenland.lnd.landcode`
`verblijfplaats.datumAanvangAdreshouding`                               `True`                                                                             TODO
`verblijfplaats.datumIngangGeldigheid`                                  `True`                                                                             TODO
`verblijfplaats.datumInschrijvingInGemeente`                            `True`                                                                             TODO
`verblijfplaats.datumVestigingInNederland`                              `True`                                                                             TODO
`verblijfplaats.gemeenteVanInschrijving`                                `True`                                                                             TODO
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
`verblijfplaats.inOnderzoek.datumIngangOnderzoek.dag`                   1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.inOnderzoek.datumIngangOnderzoek.datum`                 "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.inOnderzoek.datumIngangOnderzoek.jaar`                  1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
`verblijfplaats.inOnderzoek.datumIngangOnderzoek.maand`                 1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`gezagsverhouding.indicatieCurateleRegister`                            `ing.indicatieCurateleRegister`
`gezagsverhouding.indicatieGezagMinderjarige`                           `ing.indicatieGezagMinderjarige`
`gezagsverhouding.inOnderzoek.indicatieCurateleRegister`                *(`inOnderzoek.groepsnaam` == `Gezagsverhouding`)*
`gezagsverhouding.inOnderzoek.indicatieGezagMinderjarige`               *(`inOnderzoek.groepsnaam` == `Gezagsverhouding`)*
`gezagsverhouding.inOnderzoek.datumIngangOnderzoek.dag`                 *(`inOnderzoek.groepsnaam` == `Gezagsverhouding`)*
`gezagsverhouding.inOnderzoek.datumIngangOnderzoek.datum`               *(`inOnderzoek.groepsnaam` == `Gezagsverhouding`)*
`gezagsverhouding.inOnderzoek.datumIngangOnderzoek.jaar`                *(`inOnderzoek.groepsnaam` == `Gezagsverhouding`)*
`gezagsverhouding.inOnderzoek.datumIngangOnderzoek.maand`               *(`inOnderzoek.groepsnaam` == `Gezagsverhouding`)*
`verblijfstitel.aanduiding.code`                                        `vbt.aanduidingVerblijfstitel`
`verblijfstitel.aanduiding.omschrijving`                                *(calculated)*                                                                     Obtained from mapping https://publicaties.rvig.nl/dsresource?objectid=4801&type=org
`verblijfstitel.datumEinde.dag`                                         DAY(`ing.datumVerliesVerblijfstitel`)
`verblijfstitel.datumEinde.datum`                                       `ing.datumVerliesVerblijfstitel`
`verblijfstitel.datumEinde.jaar`                                        YEAR(`ing.datumVerliesVerblijfstitel`)
`verblijfstitel.datumEinde.maand`                                       MONTH(`ing.datumVerliesVerblijfstitel`)
`verblijfstitel.datumIngang.dag`                                        DAY(`ing.datumVerkrijgingVerblijfstitel`)
`verblijfstitel.datumIngang.datum`                                      `ing.datumVerkrijgingVerblijfstitel`
`verblijfstitel.datumIngang.jaar`                                       YEAR(`ing.datumVerkrijgingVerblijfstitel`)
`verblijfstitel.datumIngang.maand`                                      MONTH(`ing.datumVerkrijgingVerblijfstitel`)
`verblijfstitel.inOnderzoek.aanduiding`                                 *(`inOnderzoek.elementnaam` == `aanduidingVerblijfstitel`)*                        One of the multiple inOnderzoek occurrances matches
`verblijfstitel.inOnderzoek.datumEinde`                                 "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`verblijfstitel.inOnderzoek.datumIngang`                                "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`verblijfstitel.inOnderzoek.datumIngangOnderzoek.dag`                   1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
`verblijfstitel.inOnderzoek.datumIngangOnderzoek.datum`                 "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
`verblijfstitel.inOnderzoek.datumIngangOnderzoek.jaar`                  1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
`verblijfstitel.inOnderzoek.datumIngangOnderzoek.maand`                 1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
=====================================================================   ================================================================================   =====================================================================


Kind
--------------------

=====================================================================   ================================================================================   =====================================================================
API attribute                                                           StUF-BG attribute                                                                  Design decision  remarks
=====================================================================   ================================================================================   =====================================================================
burgerservicenummer                                                     `inp.heeftAlsKinderen.inp.bsn`
geheimhoudingPersoonsgegevens                                           `inp.heeftAlsKinderen.inp.indicatieGeheim`
naam.geslachtsnaam                                                      `inp.heeftAlsKinderen.geslachtsnaam`
naam.voorletters                                                        `inp.heeftAlsKinderen.voorletters`
naam.voornamen                                                          `inp.heeftAlsKinderen.voornamen`
naam.voorvoegsel                                                        `inp.heeftAlsKinderen.voorvoegselGeslachtsnaam`
naam.inOnderzoek.geslachtsnaam                                          *(`inp.heeftAlsKinderen.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*            One of the multiple inOnderzoek occurrances matches
naam.inOnderzoek.voornamen                                              *(`inp.heeftAlsKinderen.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*            One of the multiple inOnderzoek occurrances matches
naam.inOnderzoek.voorvoegsel                                            *(`inp.heeftAlsKinderen.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*            One of the multiple inOnderzoek occurrances matches
naam.inOnderzoek.datumIngangOnderzoek.dag                               1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
naam.inOnderzoek.datumIngangOnderzoek.datum                             "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
naam.inOnderzoek.datumIngangOnderzoek.jaar                              1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
naam.inOnderzoek.datumIngangOnderzoek.maand                             1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
geboorte.datum.dag                                                      DAY(`inp.heeftAlsKinderen.geboortedatum`)
geboorte.datum.datum                                                    `inp.heeftAlsKinderen.geboortedatum`
geboorte.datum.jaar                                                     YEAR(`inp.heeftAlsKinderen.geboortedatum`)
geboorte.datum.maand                                                    MONTH(`inp.heeftAlsKinderen.geboortedatum`)
geboorte.land.code                                                      COUNTRY_CODE(`inp.heeftAlsKinderen.inp.geboorteLand`)                              TODO
geboorte.land.omschrijving                                              `inp.heeftAlsKinderen.inp.geboorteLand`
geboorte.plaats.code                                                    CITY_CODE(`inp.heeftAlsKinderen.inp.geboorteplaats`)                               TODO
geboorte.plaats.omschrijving                                            `inp.heeftAlsKinderen.inp.geboorteplaats`
geboorte.inOnderzoek.datum                                              *(`inp.heeftAlsKinderen.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*            One of the multiple inOnderzoek occurrances matches
geboorte.inOnderzoek.land                                               *(`inp.heeftAlsKinderen.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*            One of the multiple inOnderzoek occurrances matches
geboorte.inOnderzoek.plaats                                             *(`inp.heeftAlsKinderen.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*            One of the multiple inOnderzoek occurrances matches
geboorte.inOnderzoek.datumIngangOnderzoek.dag                           1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
geboorte.inOnderzoek.datumIngangOnderzoek.datum                         "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
geboorte.inOnderzoek.datumIngangOnderzoek.jaar                          1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
geboorte.inOnderzoek.datumIngangOnderzoek.maand                         1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
leeftijd                                                                *(calculated)*                                                                     See `features`_
inOnderzoek.burgerservicenummer                                         *(`inp.heeftAlsKinderen.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*            One of the multiple inOnderzoek occurrances matches
inOnderzoek.datumIngangOnderzoek.dag                                    1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
inOnderzoek.datumIngangOnderzoek.datum                                  "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
inOnderzoek.datumIngangOnderzoek.jaar                                   1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
inOnderzoek.datumIngangOnderzoek.maand                                  1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
=====================================================================   ================================================================================   =====================================================================


Ouder
--------------------

=====================================================================   ================================================================================   =====================================================================
API attribute                                                           StUF-BG attribute                                                                  Design decision  remarks
=====================================================================   ================================================================================   =====================================================================
burgerservicenummer                                                     `inp.heeftAlsOuders.inp.bsn`
geslachtsaanduiding                                                     `inp.heeftAlsOuders.inp.indicatieGeheim`
ouderAanduiding                                                         `inp.heeftAlsOuders.ouderAanduiding`
datumIngangFamilierechtelijkeBetrekking.dag                             DAY(`inp.heeftAlsOuders.datumIngangFamilierechtelijkeBetrekking`)
datumIngangFamilierechtelijkeBetrekking.datum                           inp.heeftAlsOuders.datumIngangFamilierechtelijkeBetrekking
datumIngangFamilierechtelijkeBetrekking.jaar                            YEAR(`inp.heeftAlsOuders.datumIngangFamilierechtelijkeBetrekking`)
datumIngangFamilierechtelijkeBetrekking.maand                           MONTH(`inp.heeftAlsOuders.datumIngangFamilierechtelijkeBetrekking`)
naam.geslachtsnaam                                                      `inp.heeftAlsOuders.gerelateerde.geslachtsnaam`
naam.voorletters                                                        `inp.heeftAlsOuders.gerelateerde.voorletters`
naam.voornamen                                                          `inp.heeftAlsOuders.gerelateerde.voornamen`
naam.voorvoegsel                                                        `inp.heeftAlsOuders.gerelateerde.voorvoegselGeslachtsnaam`
naam.inOnderzoek.geslachtsnaam                                          *(`inp.heeftAlsOuders.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*              One of the multiple inOnderzoek occurrances matches
naam.inOnderzoek.voornamen                                              *(`inp.heeftAlsOuders.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*              One of the multiple inOnderzoek occurrances matches
naam.inOnderzoek.voorvoegsel                                            *(`inp.heeftAlsOuders.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*              One of the multiple inOnderzoek occurrances matches
naam.inOnderzoek.datumIngangOnderzoek.dag                               1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
naam.inOnderzoek.datumIngangOnderzoek.datum                             "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
naam.inOnderzoek.datumIngangOnderzoek.jaar                              1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
naam.inOnderzoek.datumIngangOnderzoek.maand                             1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
inOnderzoek.burgerservicenummer                                         *(`inp.heeftAlsOuders.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*              One of the multiple inOnderzoek occurrances matches
inOnderzoek.datumIngangFamilierechtelijkeBetrekking                     "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
inOnderzoek.geslachtsaanduiding                                         *(`inOnderzoek.groepsnaam` == `Persoonsgegevens`)*                                 One of the multiple inOnderzoek occurrances matches
inOnderzoek.datumIngangOnderzoek.dag                                    1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
inOnderzoek.datumIngangOnderzoek.datum                                  "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
inOnderzoek.datumIngangOnderzoek.jaar                                   1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
inOnderzoek.datumIngangOnderzoek.maand                                  1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
geboorte.datum.dag                                                      DAY(`inp.heeftAlsOuders.geboortedatum`)
geboorte.datum.datum                                                    `inp.heeftAlsOuders.geboortedatum`
geboorte.datum.jaar                                                     YEAR(`inp.heeftAlsOuders.geboortedatum`)
geboorte.datum.maand                                                    MONTH(`inp.heeftAlsOuders.geboortedatum`)
geboorte.land.code                                                      COUNTRY_CODE(`inp.heeftAlsOuders.inp.geboorteLand`)                                TODO
geboorte.land.omschrijving                                              `inp.heeftAlsOuders.inp.geboorteLand`
geboorte.plaats.code                                                    CITY_CODE(`inp.heeftAlsOuders.inp.geboorteplaats`)                                 TODO
geboorte.plaats.omschrijving                                            `inp.heeftAlsOuders.inp.geboorteplaats`
geboorte.inOnderzoek.datum                                              *(`inp.heeftAlsOuders.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*              One of the multiple inOnderzoek occurrances matches
geboorte.inOnderzoek.land                                               *(`inp.heeftAlsOuders.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*              One of the multiple inOnderzoek occurrances matches
geboorte.inOnderzoek.plaats                                             *(`inp.heeftAlsOuders.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*              One of the multiple inOnderzoek occurrances matches
geboorte.inOnderzoek.datumIngangOnderzoek.dag                           1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
geboorte.inOnderzoek.datumIngangOnderzoek.datum                         "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
geboorte.inOnderzoek.datumIngangOnderzoek.jaar                          1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
geboorte.inOnderzoek.datumIngangOnderzoek.maand                         1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
geheimhoudingPersoonsgegevens                                           `inp.heeftAlsOuders.inp.indicatieGeheim`
=====================================================================   ================================================================================   =====================================================================


Partner
--------------------

=====================================================================   ================================================================================   =====================================================================
API attribute                                                           StUF-BG attribute                                                                  Design decision  remarks
=====================================================================   ================================================================================   =====================================================================
burgerservicenummer                                                     `inp.heeftAlsEchtgenootPartner.inp.bsn`
geslachtsaanduiding                                                     `inp.heeftAlsEchtgenootPartner.inp.indicatieGeheim`
soortVerbintenis                                                        `inp.heeftAlsEchtgenootPartner.inp.soortVerbintenis`
naam.geslachtsnaam                                                      `inp.heeftAlsEchtgenootPartner.gerelateerde.geslachtsnaam`
naam.voorletters                                                        `inp.heeftAlsEchtgenootPartner.gerelateerde.voorletters`
naam.voornamen                                                          `inp.heeftAlsEchtgenootPartner.gerelateerde.voornamen`
naam.voorvoegsel                                                        `inp.heeftAlsEchtgenootPartner.gerelateerde.voorvoegselGeslachtsnaam`
naam.inOnderzoek.geslachtsnaam                                          *(`inp.heeftAlsEchtgenootPartner.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*   One of the multiple inOnderzoek occurrances matches
naam.inOnderzoek.voornamen                                              *(`inp.heeftAlsEchtgenootPartner.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*   One of the multiple inOnderzoek occurrances matches
naam.inOnderzoek.voorvoegsel                                            *(`inp.heeftAlsEchtgenootPartner.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*   One of the multiple inOnderzoek occurrances matches
naam.inOnderzoek.datumIngangOnderzoek.dag                               1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
naam.inOnderzoek.datumIngangOnderzoek.datum                             "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
naam.inOnderzoek.datumIngangOnderzoek.jaar                              1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
naam.inOnderzoek.datumIngangOnderzoek.maand                             1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
geboorte.datum.dag                                                      DAY(`inp.heeftAlsEchtgenootPartner.geboortedatum`)
geboorte.datum.datum                                                    `inp.heeftAlsEchtgenootPartner.geboortedatum`
geboorte.datum.jaar                                                     YEAR(`inp.heeftAlsEchtgenootPartner.geboortedatum`)
geboorte.datum.maand                                                    MONTH(`inp.heeftAlsEchtgenootPartner.geboortedatum`)
geboorte.land.code                                                      COUNTRY_CODE(`inp.heeftAlsEchtgenootPartner.inp.geboorteLand`)                     TODO
geboorte.land.omschrijving                                              `inp.heeftAlsEchtgenootPartner.inp.geboorteLand`
geboorte.plaats.code                                                    CITY_CODE(`inp.heeftAlsEchtgenootPartner.inp.geboorteplaats`)                      TODO
geboorte.plaats.omschrijving                                            `inp.heeftAlsEchtgenootPartner.inp.geboorteplaats`
geboorte.inOnderzoek.datum                                              *(`inp.heeftAlsEchtgenootPartner.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*   One of the multiple inOnderzoek occurrances matches
geboorte.inOnderzoek.land                                               *(`inp.heeftAlsEchtgenootPartner.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*   One of the multiple inOnderzoek occurrances matches
geboorte.inOnderzoek.plaats                                             *(`inp.heeftAlsEchtgenootPartner.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*   One of the multiple inOnderzoek occurrances matches
geboorte.inOnderzoek.datumIngangOnderzoek.dag                           1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
geboorte.inOnderzoek.datumIngangOnderzoek.datum                         "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
geboorte.inOnderzoek.datumIngangOnderzoek.jaar                          1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
geboorte.inOnderzoek.datumIngangOnderzoek.maand                         1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
inOnderzoek.burgerservicenummer                                         *(`inp.heeftAlsEchtgenootPartner.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*   One of the multiple inOnderzoek occurrances matches
inOnderzoek.geslachtsaanduiding                                         *(`inOnderzoek.groepsnaam` == `Persoonsgegevens`)*                                 One of the multiple inOnderzoek occurrances matches
inOnderzoek.datumIngangOnderzoek.dag                                    1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
inOnderzoek.datumIngangOnderzoek.datum                                  "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
inOnderzoek.datumIngangOnderzoek.jaar                                   1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
inOnderzoek.datumIngangOnderzoek.maand                                  1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
aangaanHuwelijkPartnerschap.datum.dag                                   DAY(`inp.heeftAlsEchtgenootPartner.datumSluiting`)
aangaanHuwelijkPartnerschap.datum.datum                                 `inp.heeftAlsEchtgenootPartner.datumSluiting`
aangaanHuwelijkPartnerschap.datum.jaar                                  YEAR(`inp.heeftAlsEchtgenootPartner.datumSluiting`)
aangaanHuwelijkPartnerschap.datum.maand                                 MONTH(`inp.heeftAlsEchtgenootPartner.datumSluiting`)
aangaanHuwelijkPartnerschap.land.code                                   COUNTRY_CODE(`inp.heeftAlsEchtgenootPartner.landSluiting`)                         TODO
aangaanHuwelijkPartnerschap.land.omschrijving                           `inp.heeftAlsEchtgenootPartner.landSluiting`
aangaanHuwelijkPartnerschap.plaats.code                                 CITY_CODE(`inp.heeftAlsEchtgenootPartner.plaatsSluiting`)                          TODO
aangaanHuwelijkPartnerschap.plaats.omschrijving                         `inp.heeftAlsEchtgenootPartner.plaatsSluiting`
aangaanHuwelijkPartnerschap.inOnderzoek.datum                           *(`inp.heeftAlsEchtgenootPartner.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*   One of the multiple inOnderzoek occurrances matches
aangaanHuwelijkPartnerschap.inOnderzoek.land                            *(`inp.heeftAlsEchtgenootPartner.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*   One of the multiple inOnderzoek occurrances matches
aangaanHuwelijkPartnerschap.inOnderzoek.plaats                          *(`inp.heeftAlsEchtgenootPartner.inOnderzoek.groepsnaam` == `Persoonsgegevens`)*   One of the multiple inOnderzoek occurrances matches
aangaanHuwelijkPartnerschap.inOnderzoek.datumIngangOnderzoek.dag        1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
aangaanHuwelijkPartnerschap.inOnderzoek.datumIngangOnderzoek.datum      "01-01-1900"                                                                       Fixed value since not in StUF-BG and cannot be `null`.
aangaanHuwelijkPartnerschap.inOnderzoek.datumIngangOnderzoek.jaar       1900                                                                               Fixed value since not in StUF-BG and cannot be `null`.
aangaanHuwelijkPartnerschap.inOnderzoek.datumIngangOnderzoek.maand      1                                                                                  Fixed value since not in StUF-BG and cannot be `null`.
geheimhoudingPersoonsgegevens                                           `inp.heeftAlsEchtgenootPartner.inp.indicatieGeheim`
=====================================================================   ================================================================================   =====================================================================


.. _features: https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/blob/v1.0.0/features/
