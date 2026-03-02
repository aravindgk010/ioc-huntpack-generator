def normalize_iocs(ioc_data: dict) -> dict:
    """
    Normalize extracted IOCs:
    - strip whitespace
    - lowercase domains, urls, emails
    - deduplicate and sort results
    """

    normalized = {}

    for ioc_type, values in ioc_data.items():
        cleaned = []

        for value in values:
            item = value.strip()

            if ioc_type in {"domains", "urls", "emails"}:
                item = item.lower()

            cleaned.append(item)

        normalized[ioc_type] = sorted(set(cleaned))

    return normalized