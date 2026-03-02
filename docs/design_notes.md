# Design Notes

## Goal
Build a lightweight Python tool that extracts common indicators of compromise from unstructured text and transforms them into useful analyst artifacts.

## Design Choices

### CLI first
A command line interface was chosen for speed, simplicity, and portability. This keeps the project focused on security workflow automation rather than UI development.

### Regex based extraction
Version 1 uses regex based pattern matching for IOC extraction. This is practical, fast to implement, and sufficient for a first working MVP.

### Modular structure
The tool separates extraction, normalization, reporting, and hunt pack generation into different modules. This makes the code easier to maintain and extend.

## Output Strategy
The tool produces:
- JSON for structured machine readable output
- Markdown for human readable reporting
- Hunt pack markdown for investigation support

## Known Limitation
Some domains may also appear inside extracted emails or URLs. This overlap is acceptable for version 1 and can be improved in later iterations.