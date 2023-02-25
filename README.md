# Yun.ir Python Client

A Python client for the [Yun.ir](https://yun.ir/) URL shortener API.

## Installation

Install with `pip`:

```sh
pip install yun-ir
```

## Usage

```python
from yun import Yun

api    = Yun('YOUR tOKEN')
result = api.short('title', 'url')

print(result)
```
## API

`yun_ir.Yun(token: str)`
Create a new Yun.ir client instance.

- Parameters
`token`: Your Yun.ir API token.

`yun_ir.Yun.short(title: str, url: str) -> dict`
Shorten a URL using Yun.ir API.

- Parameters
`title`: Title for the URL.
`url`: URL to shorten.
- Returns
A dictionary containing the shortened URL, or an error message if the request fails.
