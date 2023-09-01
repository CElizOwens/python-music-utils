#!usr/bin/env python
from sys import argv
import requests
import get_cookies
import part_name_formatter as formatter

# Directory to test the downloading of pdfs
DEFAULT_DIR = "/Users/owens/music-projects/python-music-utils/test-directory/test-dir1/"
# Use any instrumental pdf url from the parts section of a given work
# - example pdf below is clarinets from Beethoven Eroica, Breitkopf and Härtel
# TEST_PDF_URL = "https://imslp.org/wiki/Special:ImagefromIndex/23762/hffp"
# Use a currently active cookie for user opusoakland
# cookie = "imslp_wikiLanguageSelectorLanguage=en; imslpdisclaimeraccepted=yes; __stripe_mid=fd2da1ce-268e-4232-960d-8d804184d71862a8af; imslp_wikiUserID=181393; imslp_wikiUserName=Opusoakland; _pbjs_userid_consent_data=6683316680106290; _sharedID=7cecd741-883e-4875-887e-de56a91d7b30; _lr_env_src_ats=false; _cc_id=a33ae3433a33fa89d9da031131775ef4; panoramaId_expiry=1691869160469; panoramaId=29895a2c1645802eea7b04aef13c16d53938c35ce559d8df2c39090804813713; panoramaIdType=panoIndiv; imslp_wikiUserName=Opusoakland; _clck=14e1sfl|2|fe3|0|1301; _gid=GA1.2.1976540689.1691803122; _ga_8370FT5CWW=GS1.2.1691803122.17.0.1691803122.0.0.0; _ga=GA1.1.1613048454.1689623535; imslp_wikiLoggedOut=20230812025049; _sharedID_last=Sat%2C%2012%20Aug%202023%2002%3A50%3A50%20GMT; _lr_retry_request=true; cto_bidid=8PHy7F9abnVLbnVBZmgzV25DY1hFV1MxVTVIRGFYU1VyTlJCVDM2VHh3Rlk4UFBZakg4V2xwODBBJTJGNERKcE1yWHBiSUxocDV5MDlYcjZqbzhEWXRxcVlJZHUyZ083QVFkVlBISWs0TDJ3ZW1hWjRNJTNE; __gads=ID=8c04675bd25a3a6a:T=1691264360:RT=1691808652:S=ALNI_MZ_SZkjh25KEYA1lxha8ZRaTtVPLA; __gpi=UID=000009b0ef095ddf:T=1691264360:RT=1691808652:S=ALNI_MZcw0oJJQogeh-BcpxoRFVoHrHvwQ; cto_bundle=RP-iGV8xJTJCT3NnMWtXOWY4ZHM0cjloOXJJVGplZjZLVnNvZTJTTzVHR004TDN5a2lDTmNNb0txcE9lMFlJVmN5QzhndlRsb0clMkJpaWdWV3pabTlZYzdIRyUyRkZHRDlTc2Y4b1lxMDZmYzVCR09qQ1ZlY0ZFUmFrdVoxUXkwWVFpSjVxREZoREIxdjlNdHhuMmd3YThoU1h4MWJCU0pTa0J5VnIzTyUyQkFlbG1OWlN5dTNHQ0NkaWRGQ0JoZDQxUSUyQmhaaE5BMm5z; __qca=I0-1515529160-1691808653121; __stripe_sid=d42a27a3-c768-4dd4-a5e6-d27b05cf3ed1e3e639; _clsk=g7flx6|1691808859481|7|0|u.clarity.ms/collect; _ga_4QW4VCTZ4E=GS1.1.1691808644.20.1.1691808864.0.0.0; imslp_wikiUserID=181393; imslp_wiki_session=2d51e1492cc35e0bef60227c21292e1a"  # noqa: E501
# cookie = "imslp_wikiLanguageSelectorLanguage=en; __stripe_mid=fd2da1ce-268e-4232-960d-8d804184d71862a8af; imslp_wikiUserID=181393; imslp_wikiUserName=Opusoakland; _pbjs_userid_consent_data=6683316680106290; _sharedID=7cecd741-883e-4875-887e-de56a91d7b30; _lr_env_src_ats=false; _cc_id=a33ae3433a33fa89d9da031131775ef4; panoramaId_expiry=1693594060003; panoramaId=a62a5fce0051e9d621742cfc5c7716d539385f6cba28b65a71981203df718654; panoramaIdType=panoIndiv; imslp_wikiUserName=Opusoakland; _clck=14e1sfl|2|fej|0|1301; _gid=GA1.2.578205444.1693240375; _ga_8370FT5CWW=GS1.2.1693240376.23.1.1693240773.0.0.0; _ga=GA1.1.1613048454.1689623535; imslp_wikiLoggedOut=20230828164921; _sharedID_last=Mon%2C%2028%20Aug%202023%2016%3A32%3A51%20GMT; _lr_retry_request=true; cto_bidid=f5S4KV9abnVLbnVBZmgzV25DY1hFV1MxVTVIRGFYU1VyTlJCVDM2VHh3Rlk4UFBZakg4V2xwODBBJTJGNERKcE1yWHBiSUxhWFlqaEFvNE1ObzM1ZVljVjNyRkl1T3FQZHZtd1olMkJZYlVsJTJCc3NYWDhjZ0pjbGE5ZUFhbFhXdWZ1OEthVVl6ZGgzTVFoeG5YdTVnNk1Vb3NmTGRIOUElM0QlM0Q; __gads=ID=8c04675bd25a3a6a:T=1691264360:RT=1693241092:S=ALNI_MZ_SZkjh25KEYA1lxha8ZRaTtVPLA; __gpi=UID=000009b0ef095ddf:T=1691264360:RT=1693241092:S=ALNI_MZcw0oJJQogeh-BcpxoRFVoHrHvwQ; cto_bundle=5pKQ3F8xJTJCT3NnMWtXOWY4ZHM0cjloOXJJVHNQcnd1bWV3VmlnNVd1ZUJMdUVsS0pmdDVPU1RNJTJCbVZ2ZTdlVGFYRUJEWnN6YlNqYmZlZkFZQkpiUTNmUVhUcWQ4ZVB4UGN0YzJrJTJGVFNZaVZCTDVlRkpaVmxpdGFXcEs4VFRpMVBVMUJVcm5zOGt3WG9BNGs2MldzWUJrZXJFQ3dla0kzVVAlMkYzJTJCOUFta00lMkJveGRTZHlxSVI2QW9oNXVSYVdxZDY2dWZESWE; _clsk=f6p50a|1693243040513|13|1|o.clarity.ms/collect; _ga_4QW4VCTZ4E=GS1.1.1693240369.25.1.1693243039.0.0.0; imslp_wikiUserID=181393; imslp_wiki_session=5224dd23b8dba1ecfec3d21797b7f20e; imslpdisclaimeraccepted=yes"  # noqa: E501
cookie = get_cookies.getCookiesFromDomain("imslp")

# TODO
# Have user manually login to imslp before running program
# pass in url associated with part's hyperlink
# Have program execute...
# -- retrieval imslp cookie
# -- downloading of part to local machine
# -- rename of part's filename


def download_pdf(part_url):
    try:
        part_url = args[1]
        # pass dict of cookie value paired with imslp's key of 'cookie' to get method's cookies parameter
        response = requests.get(part_url, cookies={"cookie": cookie})
        if response.status_code != 200:
            raise RuntimeError(
                f"Response status code is not 200. Received: {response.status_code}"
            )

        pdf_url = response.url
        pdf_filename = formatter.convert(pdf_url)
        content_type = response.headers["content-type"]

        print(f"\nResponse content-type: {content_type}")

        # prepare to write the downloaded pdf (binary) to a file
        pdf = open(f"{DEFAULT_DIR}{pdf_filename}", "wb+")
        pdf.write(response.content)
        # get first line of file (should be '%PDF'...)
        pdf.seek(0)
        line = pdf.readline()
        pdf.close()

        # check first line of file to see if a pdf has been downloaded as opposed to some other file format
        first_text = line.decode("ascii")
        if first_text[:4] != "%PDF":
            raise ValueError(
                f"ValueError: Expected file format 'pdf' to be specified on first line.\nReceived: '{first_text[:-1]}'"
            )

        print(f"\n{pdf_filename} downloaded!\n")

    except Exception as e:
        print(f"\n -- Error in 'download_part.py' --\n{e}\n")


# download_pdf(TEST_PDF_URL)

if __name__ == "__main__":
    assert (
        len(argv) == 2
    ), "Must provide part_url argument: python download_part.py <part_url>"
    download_pdf(argv[1])
