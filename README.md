# JWT CLI Editor

A lightweight CLI tool for **JWT inspection, verification, and modification**.

Built for security testing, CTFs, labs, and authorized penetration testing where quickly manipulating JWTs from the terminal is useful.

## Purpose

JWT CLI Editor provides a simple workflow to:

* Decode JWTs and inspect their contents.
* Verify JWTs using a specified algorithm and secret.
* Modify Header and Payload fields.
* Modify tokens **without the signing secret** while preserving the original signature.
* Modify and **re-sign tokens when the secret is available**.

## Installation

```bash
git clone <repository-url>
cd <repository>
pip install -r requirements.txt
```

Run:

```bash
python cli.py --help
```

## Usage

### Decode

```bash
python cli.py decode "<JWT>"
```

### Verify

```bash
python cli.py verify "<JWT>" \
    --algorithm HS256 \
    --secret "my-secret"
```

### Modify

Modify the JWT without a secret:

```bash
python cli.py modify "<JWT>" \
    --payload '{"admin":true}'
```

Modify the Header:

```bash
python cli.py modify "<JWT>" \
    --header '{"kid":"test-key"}'
```

Modify and re-sign using a secret:

```bash
python cli.py modify "<JWT>" \
    --payload '{"admin":true}' \
    --secret "my-secret"
```

Header and Payload can also be modified together:

```bash
python cli.py modify "<JWT>" \
    --header '{"kid":"test-key"}' \
    --payload '{"admin":true}' \
    --secret "my-secret"
```

## Options

| Command       | Purpose                                    |
| ------------- | ------------------------------------------ |
| `decode`      | Decode and inspect a JWT                   |
| `verify`      | Verify a JWT using an algorithm and secret |
| `modify`      | Modify JWT Header/Payload                  |
| `--no-banner` | Disable the startup banner                 |

### `modify` options

| Option      | Description                               |
| ----------- | ----------------------------------------- |
| `--header`  | Header fields to modify as a JSON object  |
| `--payload` | Payload fields to modify as a JSON object |
| `--secret`  | Secret used to re-sign the modified token |

## Tech Stack

* Python
* Typer
* PyJWT
* Rich