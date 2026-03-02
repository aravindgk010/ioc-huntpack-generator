# Hunt Pack

**Source File:** `sample_alert.txt`

## Purpose

This hunt pack was automatically generated from extracted IOCs.
These queries are starting points and should be adjusted to match the field names in your SIEM.

## Splunk Queries

### IP: `185.199.110.153`
```spl
index=* ("185.199.110.153")
```

### Domain: `evil-login-support.com`
```spl
index=* ("evil-login-support.com")
```

### URL: `http://evil-login-support.com/update`
```spl
index=* ("http://evil-login-support.com/update")
```

### Email: `attacker@evil-login-support.com`
```spl
index=* ("attacker@evil-login-support.com")
```

### Hash: `44d88612fea8a8f36de82e1278abb02f`
```spl
index=* ("44d88612fea8a8f36de82e1278abb02f")
```

### Hash: `da39a3ee5e6b4b0d3255bfef95601890afd80709`
```spl
index=* ("da39a3ee5e6b4b0d3255bfef95601890afd80709")
```

### Hash: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
```spl
index=* ("e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
```

## Elastic KQL Queries

### IP: `185.199.110.153`
```kql
source.ip: "185.199.110.153" or destination.ip: "185.199.110.153"
```

### Domain: `evil-login-support.com`
```kql
url.domain: "evil-login-support.com" or dns.question.name: "evil-login-support.com" or host.name: "evil-login-support.com"
```

### URL: `http://evil-login-support.com/update`
```kql
url.full: "http://evil-login-support.com/update"
```

### Email: `attacker@evil-login-support.com`
```kql
email.from.address: "attacker@evil-login-support.com" or email.sender.address: "attacker@evil-login-support.com"
```

### MD5: `44d88612fea8a8f36de82e1278abb02f`
```kql
file.hash.md5: "44d88612fea8a8f36de82e1278abb02f"
```

### SHA1: `da39a3ee5e6b4b0d3255bfef95601890afd80709`
```kql
file.hash.sha1: "da39a3ee5e6b4b0d3255bfef95601890afd80709"
```

### SHA256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
```kql
file.hash.sha256: "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
```
