import re
from urllib.parse import urlparse

from ioc_extractor.patterns import (
    IPV4_PATTERN,
    DOMAIN_PATTERN,
    URL_PATTERN,
    EMAIL_PATTERN,
    MD5_PATTERN,
    SHA1_PATTERN,
    SHA256_PATTERN,
)


def extract_domains_from_urls(urls: list[str]) -> set[str]:
    domains = set()

    for url in urls:
        try:
            parsed = urlparse(url)
            if parsed.netloc:
                domains.add(parsed.netloc.lower())
        except Exception:
            continue

    return domains


def extract_domains_from_emails(emails: list[str]) -> set[str]:
    domains = set()

    for email in emails:
        parts = email.split("@")
        if len(parts) == 2:
            domains.add(parts[1].lower())

    return domains


def extract_iocs(text: str) -> dict:
    """
    Extract IOC types from input text and reduce redundant domain overlap
    from URLs and email addresses.
    """

    ipv4_matches = re.findall(IPV4_PATTERN, text)
    domain_matches = re.findall(DOMAIN_PATTERN, text)
    url_matches = re.findall(URL_PATTERN, text)
    email_matches = re.findall(EMAIL_PATTERN, text)
    md5_matches = re.findall(MD5_PATTERN, text)
    sha1_matches = re.findall(SHA1_PATTERN, text)
    sha256_matches = re.findall(SHA256_PATTERN, text)

    url_domains = extract_domains_from_urls(url_matches)
    email_domains = extract_domains_from_emails(email_matches)

    filtered_domains = [
        domain for domain in domain_matches
        if domain.lower() not in url_domains and domain.lower() not in email_domains
    ]

    return {
        "ipv4": ipv4_matches,
        "domains": filtered_domains,
        "urls": url_matches,
        "emails": email_matches,
        "md5": md5_matches,
        "sha1": sha1_matches,
        "sha256": sha256_matches,
    }