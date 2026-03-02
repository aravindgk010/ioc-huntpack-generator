def build_hunt_pack(ioc_data: dict, source_file: str) -> str:
    """
    Build a markdown hunt pack with template Splunk and Elastic queries
    based on extracted IOCs.
    """

    lines = [
        "# Hunt Pack",
        "",
        f"**Source File:** `{source_file}`",
        "",
        "## Purpose",
        "",
        "This hunt pack was automatically generated from extracted IOCs.",
        "These queries are starting points and should be adjusted to match the field names in your SIEM.",
        "",
    ]

    # Splunk section
    lines.extend([
        "## Splunk Queries",
        "",
    ])

    for ip in ioc_data.get("ipv4", []):
        lines.extend([
            f"### IP: `{ip}`",
            "```spl",
            f'index=* ("{ip}")',
            "```",
            "",
        ])

    for domain in ioc_data.get("domains", []):
        lines.extend([
            f"### Domain: `{domain}`",
            "```spl",
            f'index=* ("{domain}")',
            "```",
            "",
        ])

    for url in ioc_data.get("urls", []):
        lines.extend([
            f"### URL: `{url}`",
            "```spl",
            f'index=* ("{url}")',
            "```",
            "",
        ])

    for email in ioc_data.get("emails", []):
        lines.extend([
            f"### Email: `{email}`",
            "```spl",
            f'index=* ("{email}")',
            "```",
            "",
        ])

    for file_hash in ioc_data.get("md5", []) + ioc_data.get("sha1", []) + ioc_data.get("sha256", []):
        lines.extend([
            f"### Hash: `{file_hash}`",
            "```spl",
            f'index=* ("{file_hash}")',
            "```",
            "",
        ])

    # Elastic section
    lines.extend([
        "## Elastic KQL Queries",
        "",
    ])

    for ip in ioc_data.get("ipv4", []):
        lines.extend([
            f"### IP: `{ip}`",
            "```kql",
            f'source.ip: "{ip}" or destination.ip: "{ip}"',
            "```",
            "",
        ])

    for domain in ioc_data.get("domains", []):
        lines.extend([
            f"### Domain: `{domain}`",
            "```kql",
            f'url.domain: "{domain}" or dns.question.name: "{domain}" or host.name: "{domain}"',
            "```",
            "",
        ])

    for url in ioc_data.get("urls", []):
        lines.extend([
            f"### URL: `{url}`",
            "```kql",
            f'url.full: "{url}"',
            "```",
            "",
        ])

    for email in ioc_data.get("emails", []):
        lines.extend([
            f"### Email: `{email}`",
            "```kql",
            f'email.from.address: "{email}" or email.sender.address: "{email}"',
            "```",
            "",
        ])

    for file_hash in ioc_data.get("md5", []):
        lines.extend([
            f"### MD5: `{file_hash}`",
            "```kql",
            f'file.hash.md5: "{file_hash}"',
            "```",
            "",
        ])

    for file_hash in ioc_data.get("sha1", []):
        lines.extend([
            f"### SHA1: `{file_hash}`",
            "```kql",
            f'file.hash.sha1: "{file_hash}"',
            "```",
            "",
        ])

    for file_hash in ioc_data.get("sha256", []):
        lines.extend([
            f"### SHA256: `{file_hash}`",
            "```kql",
            f'file.hash.sha256: "{file_hash}"',
            "```",
            "",
        ])

    return "\n".join(lines)