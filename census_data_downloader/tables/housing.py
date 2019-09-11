#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class MedianMonthlyHousingCostsDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "medianmonthlyhousingcosts"
    UNIVERSE = "occupied housing units with monthly housing costs"
    RAW_TABLE_NAME = "B25105"
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001": "median"
    })


@register
class MedianHousingValueDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "medianhousingvalue"
    UNIVERSE = "owner-occupied housing units"
    RAW_TABLE_NAME = 'B25077'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001": "median"
    })


@register
class MedianGrossRentDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "mediangrossrent"
    UNIVERSE = "renter-occupied housing units paying cash rent"
    RAW_TABLE_NAME = 'B25064'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001": "median"
    })


@register
class AgeHouseholderByYearBuiltDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "agehouseholderbyyearbuilt"
    UNIVERSE = "occupied housing units"
    RAW_TABLE_NAME = 'B25126'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': 'estimate',
        '002': 'total_owner',
        '003': 'owner_15to34yrsold',
        '004': 'owner_15to34yrsoldbuilt2014orlater',
        '005': 'owner_15to34yrsoldbuilt2010to2013',
        '006': 'owner_15to34yrsoldbuilt2000to2009',
        '007': 'owner_15to34yrsoldbuilt1990to1999',
        '008': 'owner_15to34yrsoldbuilt1980to1989',
        '009': 'owner_15to34yrsoldbuilt1970to1979',
        '010': 'owner_15to34yrsoldbuilt1960to1969',
        '011': 'owner_15to34yrsoldbuilt1950to1959',
        '012': 'owner_15to34yrsoldbuilt1940to1949',
        '013': 'owner_15to34yrsoldbuilt1939orearlier',
        '014': 'owner_35to64yrsold',
        '015': 'owner_35to64yrsoldbuilt2014orlater',
        '016': 'owner_35to64yrsoldbuilt2010to2013',
        '017': 'owner_35to64yrsoldbuilt2000to2009',
        '018': 'owner_35to64yrsoldbuilt1990to1999',
        '019': 'owner_35to64yrsoldbuilt1980to1989',
        '020': 'owner_35to64yrsoldbuilt1970to1979',
        '021': 'owner_35to64yrsoldbuilt1960to1969',
        '022': 'owner_35to64yrsoldbuilt1950to1959',
        '023': 'owner_35to64yrsoldbuilt1940to1949',
        '024': 'owner_35to64yrsoldbuilt1939orearlier',
        '025': 'owner_65older',
        '026': 'owner_65older2014orlater',
        '027': 'owner_65olderbuilt2010to2013',
        '028': 'owner_65olderbuilt2000to2009',
        '029': 'owner_65olderbuilt1990to1999',
        '030': 'owner_65olderbuilt1980to1989',
        '031': 'owner_65olderbuilt1970to1979',
        '032': 'owner_65olderbuilt1960to1969',
        '033': 'owner_65olderbuilt1950to1959',
        '034': 'owner_65olderbuilt1940to1949',
        '035': 'owner_65olderbuilt1939orearlier',
        '036': 'total_renter',
        '037': 'renter_15to34yrsold',
        '038': 'renter_15to34yrsoldbuilt2014orlater',
        '039': 'renter_15to34yrsoldbuilt2010to2013',
        '040': 'renter_15to34yrsoldbuilt2000to2009',
        '041': 'renter_15to34yrsoldbuilt1990to1999',
        '042': 'renter_15to34yrsoldbuilt1980to1989',
        '043': 'renter_15to34yrsoldbuilt1970to1979',
        '044': 'renter_15to34yrsoldbuilt1960to1969',
        '045': 'renter_15to34yrsoldbuilt1950to1959',
        '046': 'renter_15to34yrsoldbuilt1940to1949',
        '047': 'renter_15to34yrsoldbuilt1939orearlier',
        '048': 'renter_35to64yrsold',
        '049': 'renter_35to64yrsold2014orlater',
        '050': 'renter_35to64yrsold2010to2013',
        '051': 'renter_35to64yrsold2000to2009',
        '052': 'renter_35to64yrsold1990to1999',
        '053': 'renter_35to64yrsold1980to1989',
        '054': 'renter_35to64yrsold1970to1979',
        '055': 'renter_35to64yrsoldbuilt1960to1969',
        '056': 'renter_35to64yrsoldbuilt1950to1959',
        '057': 'renter_35to64yrsoldbuilt1940to1949',
        '058': 'renter_35to64yrsoldbuilt1939orearlier',
        '059': 'renter_65older',
        '060': 'renter_65olderbuilt2014orlater',
        '061': 'renter_65olderbuilt2010to2013',
        '062': 'renter_65olderbuilt2000to2009',
        '063': 'renter_65olderbuilt1990to1999',
        '064': 'renter_65olderbuilt1980to1989',
        '065': 'renter_65olderbuilt1970to1979',
        '066': 'renter_65olderbuilt1960to1969',
        '067': 'renter_65olderbuilt1950to1959',
        '068': 'renter_65olderbuilt1940to1949',
        '069': 'renter_65olderbuilt1939orearlier'
    })


@register
class TenureByYearStructureBuiltDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "tenurebyyearbuilt"
    UNIVERSE = "occupied housing units"
    RAW_TABLE_NAME = 'B25036'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': 'estimate',
        '02': 'owner',
        '03': 'owner_built2014orlater',
        '04': 'owner_built2010to2013',
        '05': 'owner_built2000to2009',
        '06': 'owner_built1990to1999',
        '07': 'owner_built1980to1989',
        '08': 'owner_built1970to1979',
        '09': 'owner_built1960to1969',
        '10': 'owner_built1950to1959',
        '11': 'owner_built1940to1949',
        '12': 'owner_built1939orearlier',
        '13': 'renter',
        '14': 'renter_built2014orlater',
        '15': 'renter_built2010to2013',
        '16': 'renter_built2000to2009',
        '17': 'renter_built1990to1999',
        '18': 'renter_built1980to1989',
        '19': 'renter_built1970to1979',
        '20': 'renter_built1960to1969',
        '21': 'renter_built1950to1959',
        '22': 'renter_built1940to1949',
        '23': 'renter_built1939orearlier'
    })


@register
class TenureDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "tenure"
    UNIVERSE = "occupied housing units"
    RAW_TABLE_NAME = 'B25003'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': 'universe',
        '002': 'owner_occupied',
        '003': 'renter_occupied'
    })


@register
class TenureLatinoDownloader(TenureDownloader):
    PROCESSED_TABLE_NAME = "tenurelatino"
    RAW_TABLE_NAME = 'B25003I'


@register
class TenureWhiteDownloader(TenureDownloader):
    PROCESSED_TABLE_NAME = "tenurewhite"
    RAW_TABLE_NAME = 'B25003H'


@register
class TenureBlackDownloader(TenureDownloader):
    PROCESSED_TABLE_NAME = "tenureblack"
    RAW_TABLE_NAME = 'B25003B'


@register
class TenureAsianDownloader(TenureDownloader):
    PROCESSED_TABLE_NAME = "tenureasian"
    RAW_TABLE_NAME = 'B25003D'
