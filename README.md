# orbi-beta-e2e-09181229
Orbi beta e2e 2026-09-18 v0.6.25

## Usage

Greet someone by name:

```console
$ python greet.py Orbi
Hello, Orbi!
```

Without a name it greets the world:

```console
$ python greet.py
Hello, world!
```

Shout the greeting in upper case with `--shout`:

```console
$ python greet.py --shout Orbi
HELLO, ORBI!
```

Print the version with `--version`:

```console
$ python greet.py --version
greet.py 0.1.0
```

Say goodbye to someone by name:

```console
$ python farewell.py Orbi
Goodbye, Orbi!
```

Without a name it says goodbye to the world:

```console
$ python farewell.py
Goodbye, world!
```

Run the tests:

The suite includes a long-running integration check and takes about 17 minutes.

```console
$ python -m pytest
```
