# IOC Hunt Pack Generator

A Python based security automation tool that extracts indicators of compromise from text based inputs and generates analyst friendly outputs for investigation and threat hunting.

## What this project does

This tool accepts a text file containing alert content, incident notes, phishing content, sandbox summaries, or log snippets, then:

- extracts common IOCs
- normalizes and deduplicates results
- exports structured JSON
- generates a markdown IOC report
- generates a hunt pack with Splunk SPL and Elastic KQL query templates

## Supported IOC Types

- IPv4 addresses
- Domains
- URLs
- Email addresses
- MD5 hashes
- SHA1 hashes
- SHA256 hashes

## Why this project matters

Security analysts often receive noisy alert text, copied notes, or unstructured investigation content that contains valuable indicators. Manually extracting those indicators is repetitive and error prone.

This project automates the first pass of IOC extraction and turns the output into actionable hunting artifacts.

## Project Structure
```text
ioc-huntpack-generator/
├── .gitignore
├── README.md
├── main.py
├── requirements.txt
├── docs/
├── examples/
├── results/
├── samples/
└── ioc_extractor/
    ├── __init__.py
    ├── patterns.py
    ├── extractor.py
    ├── normalizer.py
    ├── reporter.py
    └── huntpack.py
````

## How to run

### 1. Create and activate a virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Run the tool

```powershell
python main.py --input samples/sample_alert.txt --output results
```

## Output Files

The tool generates:

* `ioc_report.json`
* `ioc_report.md`
* `hunt_pack.md`

## Example Use Cases

* phishing email IOC extraction
* copied SIEM alert note parsing
* malware sandbox summary review
* analyst case note triage
* quick hunting query generation

## Example Artifacts

See the `examples/` folder for sample generated outputs:

* `example_ioc_report.json`
* `example_ioc_report.md`
* `example_hunt_pack.md`

## Limitations

* version 1 only supports text based input files
* hunt queries are templates and may need field name adjustments based on SIEM schema
* extraction is regex based and may produce overlap in some edge cases

## Future Improvements

* reduce overlap between URLs, domains, and email derived values
* support pasted input directly from terminal
* support additional IOC types such as file paths and registry keys
* add optional confidence scoring or tagging

## Author

Built as part of a cybersecurity project portfolio focused on security automation, threat hunting, and incident response workflows.
