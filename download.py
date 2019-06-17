"""
Download all the data.
"""
import logging
import census_data_downloader
from census_data_downloader import InternetDownloader


def main():
    # Configure logging
    logger = logging.getLogger('census_data_downloader')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s|%(name)s|%(levelname)s|%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    # Download em all
    # census_data_downloader.download_usa(data_dir="./data")
    internet = InternetDownloader(force=True)
    internet.download_everything()


if __name__ == '__main__':
    main()
