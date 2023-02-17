# Charm for a Python Temporal worker

This folder contains the Charm recipe to build a Charm that deploys
a Temporal worker.

The Worker code and "Hello World" workflow definitions are in `src/`.

The `/src/charm.py` will execute the worker, connecting then the Juju machine
to the Temporal cluster.

## How to build and deploy

NOTE: you'll need to change the Temporal cluster endpoint in `src/app.py`.

From this directory, run:

```bash
charmcraft pack

juju deploy mini_ubuntu-20.04-amd64.charm
```
