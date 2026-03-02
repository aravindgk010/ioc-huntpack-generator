import re
from ioc_extractor.patterns import (
    IPV4_PATTERN,
    DOMAIN_PATTERN,
    URL_PATTERN,
    EMAIL_PATTERN,
    MD5_PATTERN,
    SHA1_PATTERN,
    SHA256_PATTERN,
)


def extract_iocs(text: str) -> dict:
    """
    Extract basic IOC types from input text and return them as a dictionary.
    """

    return {
        "ipv4": re.findall(IPV4_PATTERN, text),
        "domains": re.findall(DOMAIN_PATTERN, text),
        "urls": re.findall(URL_PATTERN, text),
        "emails": re.findall(EMAIL_PATTERN, text),
        "md5": re.findall(MD5_PATTERN, text),
        "sha1": re.findall(SHA1_PATTERN, text),
        "sha256": re.findall(SHA256_PATTERN, text),
    }