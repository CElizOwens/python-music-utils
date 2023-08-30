#!usr/bin/env python

import re

# url6 = "https://vmirror.imslp.org/files/imglnks/usimg/4/4e/IMSLP700257-PMLP116371-01._."

# url5 = "https://vmirror.imslp.org/files/imglnks/usimg/d/d4/IMSLP740006-PMLP4197-Bach_Mass_in_B_minor,_BWV_232_(Critical)_-_Trumpet_1-3_(D).pdf"   # noqa: E501

# url4 = "https://vmirror.imslp.org/files/imglnks/usimg/b/bf/IMSLP740003-PMLP4197-Bach_Mass_in_B_minor,_BWV_232_(Critical)_-_Oboe-Oboe_d'amore_1-3.pdf"     # noqa: E501

# url3 = "https://vmirror.imslp.org/files/imglnks/usimg/8/89/IMSLP41763-PMLP02751-Mozart-K626.Clarinet.pdf"

# url2 = "https://vmirror.imslp.org/files/imglnks/usimg/e/e9/IMSLP19966-PMLP06266-RimskyKorsakov_CapEsp_Perc.pdf"

# url1 = "https://vmirror.imslp.org/files/imglnks/usimg/4/4e/IMSLP700257-PMLP116371-01._BERLIOZ_-_WAVERLY_OVERTURE_-_Flute_1-2.pdf"     # noqa: E501

# urls = [url1, url2, url3, url4, url5]


def convert(url):
    if type(url) is not str:
        raise TypeError(f"url is not of type string, got '{type(url).__name__}'")
    try:
        pmlp_index = url.rindex("PMLP") + 4
        subURL = url[pmlp_index:]
        match_obj = re.search(r"[a-zA-Z]", subURL)
        i = match_obj.start() if match_obj else 0
        title = subURL[i:].lower()

        REPLACEMENTS = [
            ("_-_", "-"),
            (",", ""),
            ("(", ""),
            (")", ""),
        ]

        # print(f"\n'PMLP': {i}")

        for old, new in REPLACEMENTS:
            title = title.replace(old, new)

        if title[-4:] != ".pdf":
            title += ".pdf"
        # print(f"-> {title}")
        return title

    except Exception as e:
        return f"Error occured in 'part_name_formatter.convert' function: {e}"


# print(convert(url6))

# for url in urls:
#     convert(url)
