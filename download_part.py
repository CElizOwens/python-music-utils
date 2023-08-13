#!usr/bin/python3
import requests

# Directory to test the downloading of pdfs
DEFAULT_DIR = "/Users/owens/music-projects/test-directory/test-dir1/"
# Use any instrumental pdf url from the parts section of a given work
# - example pdf below is clarinets from Beethoven Eroica, Breitkopf and Härtel
TEST_PDF_URL = "https://imslp.org/wiki/Special:ImagefromIndex/23762/hffp"
# Use a currently active cookie for user opusoakland
cookie = "imslp_wikiLanguageSelectorLanguage=en; imslpdisclaimeraccepted=yes; __stripe_mid=fd2da1ce-268e-4232-960d-8d804184d71862a8af; imslp_wikiUserID=181393; imslp_wikiUserName=Opusoakland; _pbjs_userid_consent_data=6683316680106290; _sharedID=7cecd741-883e-4875-887e-de56a91d7b30; _lr_env_src_ats=false; _cc_id=a33ae3433a33fa89d9da031131775ef4; panoramaId_expiry=1691869160469; panoramaId=29895a2c1645802eea7b04aef13c16d53938c35ce559d8df2c39090804813713; panoramaIdType=panoIndiv; imslp_wikiUserName=Opusoakland; _clck=14e1sfl|2|fe3|0|1301; _gid=GA1.2.1976540689.1691803122; _ga_8370FT5CWW=GS1.2.1691803122.17.0.1691803122.0.0.0; _ga=GA1.1.1613048454.1689623535; imslp_wikiLoggedOut=20230812025049; _sharedID_last=Sat%2C%2012%20Aug%202023%2002%3A50%3A50%20GMT; _lr_retry_request=true; cto_bidid=8PHy7F9abnVLbnVBZmgzV25DY1hFV1MxVTVIRGFYU1VyTlJCVDM2VHh3Rlk4UFBZakg4V2xwODBBJTJGNERKcE1yWHBiSUxocDV5MDlYcjZqbzhEWXRxcVlJZHUyZ083QVFkVlBISWs0TDJ3ZW1hWjRNJTNE; __gads=ID=8c04675bd25a3a6a:T=1691264360:RT=1691808652:S=ALNI_MZ_SZkjh25KEYA1lxha8ZRaTtVPLA; __gpi=UID=000009b0ef095ddf:T=1691264360:RT=1691808652:S=ALNI_MZcw0oJJQogeh-BcpxoRFVoHrHvwQ; cto_bundle=RP-iGV8xJTJCT3NnMWtXOWY4ZHM0cjloOXJJVGplZjZLVnNvZTJTTzVHR004TDN5a2lDTmNNb0txcE9lMFlJVmN5QzhndlRsb0clMkJpaWdWV3pabTlZYzdIRyUyRkZHRDlTc2Y4b1lxMDZmYzVCR09qQ1ZlY0ZFUmFrdVoxUXkwWVFpSjVxREZoREIxdjlNdHhuMmd3YThoU1h4MWJCU0pTa0J5VnIzTyUyQkFlbG1OWlN5dTNHQ0NkaWRGQ0JoZDQxUSUyQmhaaE5BMm5z; __qca=I0-1515529160-1691808653121; __stripe_sid=d42a27a3-c768-4dd4-a5e6-d27b05cf3ed1e3e639; _clsk=g7flx6|1691808859481|7|0|u.clarity.ms/collect; _ga_4QW4VCTZ4E=GS1.1.1691808644.20.1.1691808864.0.0.0; imslp_wikiUserID=181393; imslp_wiki_session=2d51e1492cc35e0bef60227c21292e1a"  # noqa: E501


def download_pdf():
    try:
        # pass dict of cookie value paired with imslp's key of 'cookie' to get method's cookies parameter
        response = requests.get(TEST_PDF_URL, cookies={"cookie": cookie})
        content_type = response.headers["content-type"]
        print("\n")
        print(f"Response content-type: {content_type}")
        pdf = open(f"{DEFAULT_DIR}clarinets.pdf", "wb")
        pdf.write(response.content)
        pdf.close()
        print("\nclarinets.pdf downloaded!")
        print("\nResponse content printed.\n")
    except Exception as e:
        print(f"\n -- Error => {e}\n")


download_pdf()
