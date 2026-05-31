from fastmcp import FastMCP
import json

mcp = FastMCP("Simple Calculator Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool
def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b

@mcp.tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

@mcp.tool
def divide(a: int, b: int) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

@mcp.resource("info://server")
def server_info():
    "Return server information."
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0",
        "description": "A simple calculator server that supports basic arithmetic operations.",
        "tools": ["add", "subtract", "multiply", "divide"],
        "Author": "EnergyAI"
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)