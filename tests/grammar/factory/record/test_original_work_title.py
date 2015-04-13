# -*- coding: utf-8 -*-
import unittest

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


"""
CWR Original Work Title for Versions grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestOriginalWorkTitleGrammar(unittest.TestCase):
    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('original_work_title')

    def test_valid_full(self):
        record = 'VER0000123400000023THE TITLE                                                   T0123456789ESLAST NAME 1                                  FIRST NAME 1                  THE SOURCE                                                  00014107338I-000000229-7LAST NAME 2                                  FIRST NAME 2                  00014107339I-000000230-7ABCD0123456789'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('VER', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('THE TITLE', result.title)
        self.assertEqual(12345678, result.iswc.id_code)
        self.assertEqual(9, result.iswc.check_digit)
        self.assertEqual('ES', result.language_code)
        self.assertEqual('LAST NAME 1', result.writer_1_last_name)
        self.assertEqual('FIRST NAME 1', result.writer_1_first_name)
        self.assertEqual('THE SOURCE', result.source)
        self.assertEqual(14107338, result.writer_1_ipi_name_n)
        self.assertEqual('I', result.writer_1_ipi_base_n.header)
        self.assertEqual(229, result.writer_1_ipi_base_n.id_code)
        self.assertEqual(7, result.writer_1_ipi_base_n.check_digit)
        self.assertEqual('LAST NAME 2', result.writer_2_last_name)
        self.assertEqual('FIRST NAME 2', result.writer_2_first_name)
        self.assertEqual(14107339, result.writer_2_ipi_name_n)
        self.assertEqual('I', result.writer_2_ipi_base_n.header)
        self.assertEqual(230, result.writer_2_ipi_base_n.id_code)
        self.assertEqual(7, result.writer_2_ipi_base_n.check_digit)
        self.assertEqual('ABCD0123456789', result.submitter_work_n)
