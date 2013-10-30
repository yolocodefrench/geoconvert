#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for Geoconvert."""

import unittest

from geoconvert.convert import zipcode_to_dept_name
from geoconvert.convert import address_to_zipcode
from geoconvert.convert import dept_name_to_zipcode
from geoconvert.convert import country_name_to_id
from geoconvert.address import AddressParser


class GeoconvertTestCase(unittest.TestCase):
    def test_zipcode_to_dept_name(self):
        self.assertEqual(zipcode_to_dept_name('121'), None)
        self.assertEqual(zipcode_to_dept_name('44000'), 'loire-atlantique')
        self.assertEqual(zipcode_to_dept_name('2a'), 'corse-du-sud')
        self.assertEqual(zipcode_to_dept_name('2A'), 'corse-du-sud')
        self.assertEqual(zipcode_to_dept_name('20A'), 'corse-du-sud')

    def test_address_to_zipcode(self):
        data = [
            (u"Chemin du Solarium\\n Le Haut Vigneau\\n 33175 GRADIGNAN CEDEX", '33'),
            ("Chemin du Solarium 061256784589 Le Haut Vigneau 33175 GRADIGNAN CEDEX ", '33'),
            ("Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX 061256784589", '33'),
            ("Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX", '33'),
            ('7 cours Grandval\\nBP 414 - 20183 AJACCIO - CEDEX', '20A'),
            ('20212   Erbajolo', '20B'),
            ('20223   Solenzara Air', '20A'),
            ('BP 55342 20223   Solenzara Air', '20A'),
            ('Chemin du Solarium Le Haut Vigneau 33 175 GRADIGNAN CEDEX', '33'),
            ('20 223   Solenzara Air', '20A'),
            ('97821 Le Port Cedex', '971'),
            ('27006 Évreux Cedex', '27'),
            ('  27006 Évreux Cedex', '27'),
            ('27006', '27'),
            ('Roissy-en-France95700', '95'),
            (' 44200 BP 10720 Nantes cedex', '44'),
            ('a l attention de M. Bon Jean, Avenue des clients BP 72152, F - 31020 Toulouse', '31'),
            ('a l attention de M. Bon Jean, Avenue des clients BP72152, F - 31020 Toulouse', '31'),
            ('a l attention de M. Bon Jean, Avenue des clients bp72152, F - 31020 Toulouse', '31'),
            ('Avenue des clients CS 72152, F - 31020 Toulouse', '31'),
            ('BP 1330, 6503 TARBES Cedex 9, tel. 05.62.54.58.63', '06'),
            ('Ville de Blanquefort, 12 rue Dupaty B.P. 20117, à l attention de fernanda Edant-33294 Blanquefort.', '33'),
            ('conseil général du Haut-Rhin, 100 avenue d alsace B.P.20351, conseil général du Haut-Rhin-68006 Colmar Cedex', '68'),
            ('Avenue des clients CS 72152, F - 31020 Toulouse', '31'),
            ('Avenue des clients CS72152, F - 31020 Toulouse', '31'),
            ('6503 TARBES Cedex 9, tel. 05.62.54.58.63', '06'),
            ('97700 Saint-Barthelemy', '974'),
            ('a l attention de M. Bon Jean, Avenue des client', None)
        ]

        for test in data:
            self.assertEqual(address_to_zipcode(test[0]), test[1])

    def test_dept_name_to_zipcode(self):
        data = [
            ('Martinique', '972'),
            ("cotes d'armr", None),
            ("cotes d'armor", '22'),
            (u'Hauts-de-Seine ', '92'),
            (u'H\xe9rault', '34'),
            (u'Seine-Saint-Denis ', '93'),
            (u'Loire', '42'),
            (u'Corse-du-Sud', '20A'),
            (u'', None),
            (u'Yonne', '89'),
            (u'Saint Pierre et Miquelon', '975')]
        for test in data:
            self.assertEqual(dept_name_to_zipcode(test[0]), test[1])

    def test_region_id_to_name(self):
        pass

    def test_region_name_to_id(self):
        pass

    def test_region_info_from_id(self):
        pass

    def test_region_info_from_name(self):
        pass

    def test_country_name_to_id_fr(self):
        data = [
            ('france', 'FR'),
            ('Comores', 'KM'),
            ('Madagascar', 'MG'),
            (u'S\xe9n\xe9gal', 'SN'),
            ('République démocratique du Congo', 'CD'),
            ('Mali', 'ML'),
            ('Sri Lanka ', 'LK'),
            (u'\xa0V\xe9n\xe9zuela\xa0', 'VE'),
            (u'Vi\xeatnam', 'VN'),
            ('Nigeria', 'NG'),
            (u'Niger', 'NE'),
            (u'aaa ( bbb', None),
            (u" Le  nigéria c'est trop   sympa", 'NG'),
            (u"Pays d'exécution : Niger", 'NE'),
            ("  Côte d'Ivoire ", 'CI'),
            ("U.S. Mission Iraq\n\nIraq", 'IQ'),
            ("Pays:France ?".encode('ascii', 'ignore'), 'FR'),
            (",royaume-uni,", 'GB'),
            ("PAYS-BRÉSIL", 'BR')]
        for test in data:
            self.assertEqual(country_name_to_id(test[0]), test[1])

    def test_country_name_to_id_en(self):
        data = [
            ('Mongolia', 'MN'),
            ('Marocco', 'MA'),
            ('Georgia', 'GE'),
            ('Namibia', 'NA'),
            ('Venezuela', 'VE'),
            ('Armenia', 'AM'),
            ('sweden', 'SE'),
            (u"Knotts Island, NC 27950\n\n27950-0039\nUnited States", 'US'),
            ("721 APS BLDG 3334\nUNIT 3295 \nRamstein Air Base, Non-U.S. 66877 \nGermany ", 'DE'),
            ("Saudi Arabia", 'SA'),
            ("Country execution:nigeria.", 'NG')]
        for test in data:
            self.assertEqual(country_name_to_id(test[0], lang='EN'), test[1])


class AddressParserTestCase(unittest.TestCase):
    """
    AddressParser test case
    """
    def setUp(self):
        self.address_parser = AddressParser()
        self.data = [
            (u"Chemin du Solarium\n Le Haut Vigneau\n 33175 GRADIGNAN CEDEX", '33175', '33'),
            ("Chemin du Solarium 061256784589 Le Haut Vigneau 33175 GRADIGNAN CEDEX ", '33175', '33'),
            ("Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX 061256784589", '33175', '33'),
            ("Chemin du Solarium Le Haut Vigneau 33175 GRADIGNAN CEDEX", '33175', '33'),
            ('7 cours Grandval\nBP 414 - 20183 AJACCIO - CEDEX', '20183', '2A'),
            ('20212   Erbajolo', '20212', '2B'),
            ('20223   Solenzara Air', '20223', '2B'),
            ('BP 55342 20223   Solenzara Air', '20223', '2B'),
            ('Chemin du Solarium Le Haut Vigneau 33 175 GRADIGNAN CEDEX', '33175', '33'),
            ('20 223   Solenzara Air', '20223', '2B'),
            ('97821 Le Port Cedex', '97821', '978'),
            ('27006 Évreux Cedex', '27006', '27'),
            ('  27006 Évreux Cedex', '27006', '27'),
            ('27006', '27006', '27'),
            ('Roissy-en-France95700', '95700', '95'),
            (' 44200 BP 10720 Nantes cedex', '44200', '44'),
            ('a l attention de M. Bon Jean, Avenue des clients BP 72152, F - 31020 Toulouse', '31020', '31'),
            ('a l attention de M. Bon Jean, Avenue des clients BP72152, F - 31020 Toulouse', '31020', '31'),
            ('a l attention de M. Bon Jean, Avenue des clients bp72152, F - 31020 Toulouse', '31020', '31'),
            ('Avenue des clients CS 72152, F - 31020 Toulouse', '31020', '31'),
            ('BP 1330, 6503 TARBES Cedex 9, tel. 05.62.54.58.63', '06503', '06'),
            ('Ville de Blanquefort, 12 rue Dupaty B.P. 20117, à l attention de fernanda Edant-33294 Blanquefort.', '33294', '33'),
            ('conseil général du Haut-Rhin, 100 avenue d alsace B.P.20351, conseil général du Haut-Rhin-68006 Colmar Cedex', '68006', '68'),
            ('Avenue des clients CS 72152, F - 31020 Toulouse', '31020', '31'),
            ('Avenue des clients CS72152, F - 31020 Toulouse', '31020', '31'),
            ('6503 TARBES Cedex 9, tel. 05.62.54.58.63', '06503', '06'),
            ('97700 Saint-Barthelemy', '97700', '977'),
            ('Mme Cindy DUMAS, 1500 Bd Lepic - B.P. 348 73103 Aix-les-Bains', '73103', '73'),
            ('Mme Cindy DUMAS, 15000 Bd Lepic - B.P. 348 73103 Aix-les-Bains', '73103', '73'),
            ('Mme Cindy DUMAS, 15000 Bd Lepic - 73103 B.P. 89348 Aix-les-Bains', '73103', '73'),
            ('Mme Cindy DUMAS, 15000 Bd Lepic - 73103 b.p. 89348 Aix-les-Bains', '73103', '73'),
            ('Mme Cindy DUMAS, 15000 Bd Lepic - 73103 bp 89348 Aix-les-Bains', '73103', '73'),
            (u"M. le président Du Conseil Général Du Lot, avenue de l'europe - regourd Cedex 9 46005 Cahors", '46005', '46'),
            (u"M. le maire, place Dr Pierre Esquirol Cedex 9 47916 Agen.", '47916', '47'),
            ("M. Claude Lopez, 44 avenue Saint Lazare Cedex 2 34965 Montpellier", '34965', '34'),
            (u"M. le président, le Forum 3, rue Malakoff Cedex 01 38031 Grenoble", '38031', '38'),
            (u"Samop - mandataire du cg38, les jardins d'entreprises \r\nbâtiment b4 \r\n213 rue de gerland 69007 Lyon", '69007', '69'),
            (u"M. le président, 9, rue Saint Pierre Lentin cs 94117 Cedex 1 45041 Orléans Cedex", '45041', '45'),
            (u"M. le président Du Conseil Général Du Lot, avenue de l'europe - regourd Cedex 9 46005 Cahors", '46005', '46'),
            (u"M. le président, hôtel du Département , rue Gaston Manent B.P. 1324 Cedex 9 65013 Tarbes", '65013', '65'),
            ('a l attention de M. Bon Jean, Avenue des client', None, None),
            (u"SICTOM du Guiers\n27 avenue Pravaz BP66\n38480 - Pont de Beauvoisin ", '38480', '38'),
            (u"SICTOM du Guiers\n27\n avenue Pravaz BP\n\n 66\n38480\n - Pont de Beauvoisin ", '38480', '38'),
        ]

    def test_zipcode(self):
        """
        Test zipcode detection
        """
        for address_string, zipcode, dept_number in self.data:
            address = self.address_parser.parse(address_string)
            self.assertEqual(address.zipcode, zipcode)

    def test_department(self):
        """
        Test department detection
        """
        for address_string, zipcode, dept_number in self.data:
            address = self.address_parser.parse(address_string)
            self.assertEqual(address.get_department(), dept_number)


if __name__ == '__main__':
    unittest.main()
