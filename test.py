import pathlib
import unittest
import census_data_downloader


class CensusDataDownloaderTest(unittest.TestCase):
    THIS_DIR = pathlib.Path(__file__).parent

    def test_nothing(self):
        self.assertEqual(census_data_downloader, census_data_downloader)


if __name__ == '__main__':
    unittest.main()
