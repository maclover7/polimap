import clarify
import os
from pathlib import Path
import requests
from zipfile import ZipFile


class ResultsDownloader:
    def __init__(self, election_owner, election_id, contest_name, downloaded):
        self.base_url = 'https://results.enr.clarityelections.com/%s/%s' % (
            election_owner, election_id)
        self.election_id = election_id
        self.contest_name = contest_name
        self.downloaded = downloaded

    def fetch_and_parse_results(self):
        results_filename = 'downloads/detailxml-%s' % self.election_id

        if not self.downloaded:
            current_ver_response = requests.get(
                self.base_url + '/current_ver.txt')
            current_ver_response.raise_for_status()

            Path("downloads").mkdir(exist_ok=True)

            results_response = requests.get(
                self.base_url + '/' + current_ver_response.text + '/reports/detailxml.zip',
                headers={'Accept-Encoding': 'gzip'},
                stream=True)
            results_response.raise_for_status()

            with open('%s.zip' % results_filename, 'wb') as file:
                for chunk in results_response.iter_content(chunk_size=128):
                    file.write(chunk)

            with ZipFile('%s.zip' % results_filename, 'r') as zip:
                path = os.path.splitext(results_filename)[0]
                zip.extractall(path=path)

        clarity_parser = clarify.Parser()
        clarity_parser.parse('%s/detail.xml' % results_filename)

        self.contest_results = [
            r for r in clarity_parser.results if r.choice and r.jurisdiction and r.contest.text == self.contest_name]

    def run(self):
        self.fetch_and_parse_results()
