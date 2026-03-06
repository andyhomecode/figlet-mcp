# figlet-mcp

```
    _______       __     __ 
   / ____(_)___ _/ /__  / /_
  / /_  / / __ `/ / _ \/ __/
 / __/ / / /_/ / /  __/ /_  
/_/   /_/\__, /_/\___/\__/  
        /____/

```

Remote HTTP MCP server (`/mcp`) for figlet tools.

## Run Container On Caddy Network

```bash
docker compose up -d --build
```

This starts `figlet-mcp` on Docker network `workday-mcp-net` as `figlet-mcp:8000`.

## Caddy Route

`../infra/caddy/Caddyfile` should proxy:

```caddy
handle @figlet_key {
    uri strip_prefix /figlet
    reverse_proxy figlet-mcp:8000
}
```

## Public MCP URL

`https://whatever.com/figlet/mcp`
