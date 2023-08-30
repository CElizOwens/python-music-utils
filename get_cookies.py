#!usr/bin/env python

import browser_cookie3


def getCookiesFromDomain(domain):
    Cookies = ""
    chromeCookies = list(browser_cookie3.chrome(cookie_file=None, domain_name="imslp"))
    # return chromeCookies[0].name

    # get each cookie's name and value and store in dict
    cookieDict = {cookie.name: cookie.value for cookie in chromeCookies}
    # print(cookieDict)

    cookieNameList = [
        "imslp_wikiLanguageSelectorLanguage",
        "__stripe_mid",
        "imslp_wikiUserID",
        "imslp_wikiUserName",
        "_pbjs_userid_consent_data",
        "_sharedID",
        "_lr_env_src_ats",
        "_cc_id",
        "panoramaId_expiry",
        "panoramaId",
        "panoramaIdType",
        "imslp_wikiUserName",
        "_clck",
        "_gid",
        "_ga_8370FT5CWW",
        "_ga",
        "imslp_wikiLoggedOut",
        "_sharedID_last",
        "_lr_retry_request",
        "cto_bidid",
        "__gads",
        "__gpi",
        "cto_bundle",
        "_clsk",
        "_ga_4QW4VCTZ4E",
        "imslp_wikiUserID",
        "imslp_wiki_session",
    ]

    # This cookie needs to be added with a value of 'yes'
    # -> "imslpdisclaimeraccepted"
    # These cookies are not needed (and there may be others):
    # -> "__qca", "__stripe_sid"

    try:
        for cookieName in cookieNameList:
            if len(Cookies):
                Cookies += "; "
            # print ('name=value; '...)
            Cookies += f"{cookieName}={cookieDict[cookieName]}"
        Cookies += "; imslpdisclaimeraccepted=yes"
        return Cookies
    except KeyError:
        return f"Cookie '{cookieName}' could not be found."


# print(getCookiesFromDomain("imslp"))
