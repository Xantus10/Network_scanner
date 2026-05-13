# YAML configuration schema

## Sections

### `scanner`

Define the properties of the scanner.

| Key | Values | Description |
|-----|--------|-------------|
| `mode` | `auto` | Move through the network automatically |
| | `list` | Investigate only the specified nodes |
| `targets` | `string[]` | List of IP addresses to scan (For `mode: auto`, you may specify only the first IP)
| `adjacency` | `cdp` (Default) | Look for adjacent devices using cdp
| | `subnet` | Look for adjacency between routers based on networks on interfaces (only available for `mode: list`)


#### Examples

Example `mode: auto` configuration

```yaml
scanner:
  mode: auto
  targets:
    - 192.168.2.1
```

Example `mode: list` configuration

```yaml
scanner:
  mode: list
  targets:
    - 192.168.2.1
    - 192.168.2.2
    - 192.168.4.1
  adjacency: subnet
```
