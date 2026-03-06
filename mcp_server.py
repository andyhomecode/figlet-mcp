import pyfiglet
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "figlet",
    host=os.getenv("HOST", "0.0.0.0"),
    port=int(os.getenv("PORT", "8000")),
    streamable_http_path="/mcp",
    stateless_http=True,
    json_response=True,
)


@mcp.tool()
def figlet(text: str = "MCP", font: str = "slant", comment: bool = False) -> str:
    """Render text as ASCII art using a pyfiglet font."""
    try:
        output = pyfiglet.figlet_format(text, font=font)
    except pyfiglet.FontNotFound:
        fonts = ", ".join(pyfiglet.FigletFont.getFonts())
        raise ValueError(f"Unknown font '{font}'. Available fonts: {fonts}")

    if comment:
        output = "\n".join(f"#   {line}" for line in output.splitlines())

    return output


@mcp.tool()
def list_fonts() -> list[str]:
    """List all available pyfiglet fonts."""
    return pyfiglet.FigletFont.getFonts()


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
