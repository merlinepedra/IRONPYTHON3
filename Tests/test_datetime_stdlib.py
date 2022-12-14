# Licensed to the .NET Foundation under one or more agreements.
# The .NET Foundation licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information.

##
## Run selected tests from test_datetime from StdLib
##

import unittest
import sys

from iptest import run_test

import test.datetimetester

def load_tests(loader, standard_tests, pattern):
    if sys.implementation.name == 'ironpython':
        suite = unittest.TestSuite()
        suite.addTest(unittest.expectedFailure(test.datetimetester.Oddballs('test_bug_1028306')))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDate('test_backdoor_resistance')))
        suite.addTest(test.datetimetester.TestDate('test_bad_constructor_arguments'))
        suite.addTest(test.datetimetester.TestDate('test_basic_attributes'))
        suite.addTest(test.datetimetester.TestDate('test_bool'))
        suite.addTest(test.datetimetester.TestDate('test_compare'))
        suite.addTest(test.datetimetester.TestDate('test_computations'))
        suite.addTest(test.datetimetester.TestDate('test_ctime'))
        suite.addTest(test.datetimetester.TestDate('test_extreme_ordinals'))
        suite.addTest(test.datetimetester.TestDate('test_extreme_timedelta'))
        suite.addTest(test.datetimetester.TestDate('test_format'))
        suite.addTest(test.datetimetester.TestDate('test_fromtimestamp'))
        suite.addTest(test.datetimetester.TestDate('test_harmful_mixed_comparison'))
        suite.addTest(test.datetimetester.TestDate('test_harmless_mixed_comparison'))
        suite.addTest(test.datetimetester.TestDate('test_hash_equality'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDate('test_insane_fromtimestamp')))
        suite.addTest(test.datetimetester.TestDate('test_iso_long_years'))
        suite.addTest(test.datetimetester.TestDate('test_isocalendar'))
        suite.addTest(test.datetimetester.TestDate('test_isoformat'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDate('test_mixed_compare')))
        suite.addTest(test.datetimetester.TestDate('test_ordinal_conversions'))
        suite.addTest(test.datetimetester.TestDate('test_overflow'))
        suite.addTest(test.datetimetester.TestDate('test_pickling'))
        suite.addTest(test.datetimetester.TestDate('test_pickling_subclass_date'))
        suite.addTest(test.datetimetester.TestDate('test_replace'))
        suite.addTest(test.datetimetester.TestDate('test_resolution_info'))
        suite.addTest(test.datetimetester.TestDate('test_roundtrip'))
        suite.addTest(test.datetimetester.TestDate('test_strftime'))
        suite.addTest(test.datetimetester.TestDate('test_strftime_y2k'))
        suite.addTest(test.datetimetester.TestDate('test_subclass_date'))
        suite.addTest(test.datetimetester.TestDate('test_timetuple'))
        suite.addTest(test.datetimetester.TestDate('test_today'))
        suite.addTest(test.datetimetester.TestDate('test_weekday'))
        suite.addTest(test.datetimetester.TestDateOnly('test_delta_non_days_ignored'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTime('test_astimezone'))) # https://github.com/IronLanguages/ironpython3/issues/1136
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTime('test_backdoor_resistance')))
        suite.addTest(test.datetimetester.TestDateTime('test_bad_constructor_arguments'))
        suite.addTest(test.datetimetester.TestDateTime('test_basic_attributes'))
        suite.addTest(test.datetimetester.TestDateTime('test_basic_attributes_nonzero'))
        suite.addTest(test.datetimetester.TestDateTime('test_bool'))
        suite.addTest(test.datetimetester.TestDateTime('test_combine'))
        suite.addTest(test.datetimetester.TestDateTime('test_compare'))
        suite.addTest(test.datetimetester.TestDateTime('test_computations'))
        suite.addTest(test.datetimetester.TestDateTime('test_ctime'))
        suite.addTest(test.datetimetester.TestDateTime('test_extract'))
        suite.addTest(test.datetimetester.TestDateTime('test_extreme_ordinals'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTime('test_extreme_timedelta')))
        suite.addTest(test.datetimetester.TestDateTime('test_format'))
        suite.addTest(test.datetimetester.TestDateTime('test_fromtimestamp'))
        suite.addTest(test.datetimetester.TestDateTime('test_harmful_mixed_comparison'))
        suite.addTest(test.datetimetester.TestDateTime('test_harmless_mixed_comparison'))
        suite.addTest(test.datetimetester.TestDateTime('test_hash_equality'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTime('test_insane_fromtimestamp')))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTime('test_insane_utcfromtimestamp')))
        suite.addTest(test.datetimetester.TestDateTime('test_iso_long_years'))
        suite.addTest(test.datetimetester.TestDateTime('test_isocalendar'))
        suite.addTest(test.datetimetester.TestDateTime('test_isoformat'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTime('test_microsecond_rounding')))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTime('test_mixed_compare')))
        suite.addTest(test.datetimetester.TestDateTime('test_more_compare'))
        suite.addTest(test.datetimetester.TestDateTime('test_more_ctime'))
        suite.addTest(test.datetimetester.TestDateTime('test_more_pickling'))
        suite.addTest(test.datetimetester.TestDateTime('test_more_strftime'))
        suite.addTest(test.datetimetester.TestDateTime('test_more_timetuple'))
        suite.addTest(test.datetimetester.TestDateTime('test_negative_float_fromtimestamp'))
        suite.addTest(test.datetimetester.TestDateTime('test_negative_float_utcfromtimestamp'))
        suite.addTest(test.datetimetester.TestDateTime('test_ordinal_conversions'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTime('test_overflow')))
        suite.addTest(test.datetimetester.TestDateTime('test_pickling'))
        suite.addTest(test.datetimetester.TestDateTime('test_pickling_subclass_date'))
        suite.addTest(test.datetimetester.TestDateTime('test_pickling_subclass_datetime'))
        suite.addTest(test.datetimetester.TestDateTime('test_replace'))
        suite.addTest(test.datetimetester.TestDateTime('test_resolution_info'))
        suite.addTest(test.datetimetester.TestDateTime('test_roundtrip'))
        suite.addTest(test.datetimetester.TestDateTime('test_strftime'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTime('test_strftime_with_bad_tzname_replace')))
        suite.addTest(test.datetimetester.TestDateTime('test_strftime_y2k'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTime('test_strptime')))
        suite.addTest(test.datetimetester.TestDateTime('test_subclass_date'))
        suite.addTest(test.datetimetester.TestDateTime('test_subclass_datetime'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTime('test_timestamp_aware'))) # AttributeError: 'datetime' object has no attribute 'timestamp'
        suite.addTest(test.datetimetester.TestDateTime('test_timestamp_naive'))
        suite.addTest(test.datetimetester.TestDateTime('test_timetuple'))
        suite.addTest(test.datetimetester.TestDateTime('test_today'))
        suite.addTest(test.datetimetester.TestDateTime('test_tz_independent_comparing'))
        suite.addTest(test.datetimetester.TestDateTime('test_utcfromtimestamp'))
        suite.addTest(test.datetimetester.TestDateTime('test_utcnow'))
        suite.addTest(test.datetimetester.TestDateTime('test_weekday'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_argument_passing'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTimeTZ('test_astimezone'))) # https://github.com/IronLanguages/ironpython3/issues/1136
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_astimezone_default_eastern'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_astimezone_default_utc'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_aware_compare'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_aware_subtract'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTimeTZ('test_backdoor_resistance')))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_bad_constructor_arguments'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_bad_tzinfo_classes'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_basic_attributes'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_basic_attributes_nonzero'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_bool'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_combine'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_compare'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_computations'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_ctime'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTimeTZ('test_even_more_compare')))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_extract'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTimeTZ('test_extreme_hashes')))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_extreme_ordinals'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTimeTZ('test_extreme_timedelta')))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_format'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_fromtimestamp'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_harmful_mixed_comparison'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_harmless_mixed_comparison'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_hash_equality'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTimeTZ('test_insane_fromtimestamp')))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTimeTZ('test_insane_utcfromtimestamp')))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_iso_long_years'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_isocalendar'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_isoformat'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTimeTZ('test_microsecond_rounding')))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTimeTZ('test_mixed_compare')))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_more_astimezone'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_more_compare'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_more_ctime'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_more_pickling'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_more_strftime'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_more_timetuple'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_negative_float_fromtimestamp'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_negative_float_utcfromtimestamp'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_ordinal_conversions'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTimeTZ('test_overflow')))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_pickling'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_pickling_subclass_date'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_pickling_subclass_datetime'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_replace'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_resolution_info'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_roundtrip'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_strftime'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTimeTZ('test_strftime_with_bad_tzname_replace')))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_strftime_y2k'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTimeTZ('test_strptime')))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_subclass_date'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_subclass_datetime'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_subclass_datetimetz'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTimeTZ('test_timestamp_aware'))) # AttributeError: 'datetime' object has no attribute 'timestamp'
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_timestamp_naive'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_timetuple'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_today'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_trivial'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTimeTZ('test_tz_aware_arithmetic')))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_tz_independent_comparing'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_tzinfo_classes'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_tzinfo_fromtimestamp'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_tzinfo_isoformat'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_tzinfo_now'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_tzinfo_timetuple'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_tzinfo_utcfromtimestamp'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_tzinfo_utcnow'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_utc_offset_out_of_bounds'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_utcfromtimestamp'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_utcnow'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestDateTimeTZ('test_utctimetuple'))) # SystemError: Object reference not set to an instance of an object.
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_weekday'))
        suite.addTest(test.datetimetester.TestDateTimeTZ('test_zones'))
        suite.addTest(test.datetimetester.TestModule('test_constants'))
        suite.addTest(test.datetimetester.TestModule('test_divide_and_round'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestSubclassDateTime('test_astimezone'))) # https://github.com/IronLanguages/ironpython3/issues/1136
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestSubclassDateTime('test_backdoor_resistance')))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_bad_constructor_arguments'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_basic_attributes'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_basic_attributes_nonzero'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_bool'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_combine'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_compare'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_computations'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_ctime'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_extract'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_extreme_ordinals'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestSubclassDateTime('test_extreme_timedelta')))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_format'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_fromtimestamp'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_harmful_mixed_comparison'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_harmless_mixed_comparison'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_hash_equality'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestSubclassDateTime('test_insane_fromtimestamp')))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestSubclassDateTime('test_insane_utcfromtimestamp')))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_iso_long_years'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_isocalendar'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_isoformat'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestSubclassDateTime('test_microsecond_rounding')))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestSubclassDateTime('test_mixed_compare')))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_more_compare'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_more_ctime'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_more_pickling'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_more_strftime'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_more_timetuple'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_negative_float_fromtimestamp'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_negative_float_utcfromtimestamp'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_ordinal_conversions'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestSubclassDateTime('test_overflow')))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_pickling'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_pickling_subclass_date'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_pickling_subclass_datetime'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestSubclassDateTime('test_replace'))) # TODO
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_resolution_info'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_roundtrip'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_strftime'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestSubclassDateTime('test_strftime_with_bad_tzname_replace')))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_strftime_y2k'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestSubclassDateTime('test_strptime')))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_subclass_date'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_subclass_datetime'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestSubclassDateTime('test_timestamp_aware')))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_timestamp_naive'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_timetuple'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_today'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestSubclassDateTime('test_tz_independent_comparing')))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_utcfromtimestamp'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_utcnow'))
        suite.addTest(test.datetimetester.TestSubclassDateTime('test_weekday'))
        suite.addTest(test.datetimetester.TestTZInfo('test_issue23600'))
        suite.addTest(test.datetimetester.TestTZInfo('test_non_abstractness'))
        suite.addTest(test.datetimetester.TestTZInfo('test_normal'))
        suite.addTest(test.datetimetester.TestTZInfo('test_pickling_base'))
        suite.addTest(test.datetimetester.TestTZInfo('test_pickling_subclass'))
        suite.addTest(test.datetimetester.TestTZInfo('test_refcnt_crash_bug_22044'))
        suite.addTest(test.datetimetester.TestTZInfo('test_subclass_must_override'))
        suite.addTest(test.datetimetester.TestTime('test_1653736'))
        suite.addTest(test.datetimetester.TestTime('test_backdoor_resistance'))
        suite.addTest(test.datetimetester.TestTime('test_bad_constructor_arguments'))
        suite.addTest(test.datetimetester.TestTime('test_basic_attributes'))
        suite.addTest(test.datetimetester.TestTime('test_basic_attributes_nonzero'))
        suite.addTest(test.datetimetester.TestTime('test_bool'))
        suite.addTest(test.datetimetester.TestTime('test_comparing'))
        suite.addTest(test.datetimetester.TestTime('test_format'))
        suite.addTest(test.datetimetester.TestTime('test_harmful_mixed_comparison'))
        suite.addTest(test.datetimetester.TestTime('test_harmless_mixed_comparison'))
        suite.addTest(test.datetimetester.TestTime('test_hash_equality'))
        suite.addTest(test.datetimetester.TestTime('test_isoformat'))
        suite.addTest(test.datetimetester.TestTime('test_pickling'))
        suite.addTest(test.datetimetester.TestTime('test_pickling_subclass_time'))
        suite.addTest(test.datetimetester.TestTime('test_replace'))
        suite.addTest(test.datetimetester.TestTime('test_repr'))
        suite.addTest(test.datetimetester.TestTime('test_resolution_info'))
        suite.addTest(test.datetimetester.TestTime('test_roundtrip'))
        suite.addTest(test.datetimetester.TestTime('test_str'))
        suite.addTest(test.datetimetester.TestTime('test_strftime'))
        suite.addTest(test.datetimetester.TestTime('test_subclass_time'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_basic_attributes'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_bool'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_carries'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_compare'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestTimeDelta('test_computations'))) # rounding differences
        suite.addTest(test.datetimetester.TestTimeDelta('test_constructor'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_disallowed_computations'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_disallowed_special'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_division'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_divmod'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_harmful_mixed_comparison'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_harmless_mixed_comparison'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_hash_equality'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_massive_normalization'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_microsecond_rounding'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_overflow'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_pickling'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_remainder'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_repr'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_resolution_info'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_roundtrip'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_str'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_subclass_timedelta'))
        suite.addTest(test.datetimetester.TestTimeDelta('test_total_seconds'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_1653736'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_argument_passing'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_aware_compare'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_backdoor_resistance'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_bad_constructor_arguments'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_bad_tzinfo_classes'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_basic_attributes'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_basic_attributes_nonzero'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_bool'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_comparing'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_empty'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_format'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_harmful_mixed_comparison'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_harmless_mixed_comparison'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_hash_edge_cases'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_hash_equality'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_isoformat'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestTimeTZ('test_mixed_compare')))
        suite.addTest(test.datetimetester.TestTimeTZ('test_more_bool'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_pickling'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_pickling_subclass_time'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_replace'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_repr'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_resolution_info'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_roundtrip'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_str'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_strftime'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_subclass_time'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_subclass_timetz'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_tzinfo_classes'))
        suite.addTest(test.datetimetester.TestTimeTZ('test_utc_offset_out_of_bounds'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestTimeTZ('test_zones')))
        suite.addTest(test.datetimetester.TestTimeZone('test_aware_datetime'))
        suite.addTest(test.datetimetester.TestTimeZone('test_class_members'))
        suite.addTest(  test.datetimetester.TestTimeZone('test_comparison'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestTimeZone('test_constructor')))
        suite.addTest(test.datetimetester.TestTimeZone('test_copy'))
        suite.addTest(test.datetimetester.TestTimeZone('test_deepcopy'))
        suite.addTest(test.datetimetester.TestTimeZone('test_dst'))
        suite.addTest(test.datetimetester.TestTimeZone('test_fromutc'))
        suite.addTest(test.datetimetester.TestTimeZone('test_inheritance'))
        suite.addTest(test.datetimetester.TestTimeZone('test_pickle'))
        suite.addTest(test.datetimetester.TestTimeZone('test_repr'))
        suite.addTest(test.datetimetester.TestTimeZone('test_str'))
        suite.addTest(test.datetimetester.TestTimeZone('test_tzname'))
        suite.addTest(test.datetimetester.TestTimeZone('test_utcoffset'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestTimezoneConversions('test_bogus_dst'))) # SystemError: Object reference not set to an instance of an object.
        suite.addTest(test.datetimetester.TestTimezoneConversions('test_easy'))
        suite.addTest(unittest.expectedFailure(test.datetimetester.TestTimezoneConversions('test_fromutc')))
        suite.addTest(test.datetimetester.TestTimezoneConversions('test_tricky'))
        return suite

    else:
        return loader.loadTestsFromModule(test.datetimetester, pattern)

run_test(__name__)
