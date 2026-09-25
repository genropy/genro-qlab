<p align="center"><img src="docs/logo/qlab-logo.svg" alt="qlab" width="360"></p>

# genro-qlab

Laboratory project for new [GenroPy](https://github.com/genropy/genropy)
components: the `qlab` package holds the components under test, their test
pages and their tests. See [packages/qlab/README.md](packages/qlab/README.md)
for what the lab is for.

## Layout

```
packages/qlab/        the package: resources/<component>/, webpages/components/
instances/qlab/       test instance: sys, adm, glbl, qlab on PostgreSQL
tests/                Python and JavaScript tests
docs/                 component documentation
```

## Setup

Clone it under a projects folder registered in your `environment.xml`, then:

```bash
gnr db setup qlab
python -c "from gnr.app.gnrapp import GnrApp; app = GnrApp('qlab'); app.db.package('glbl').loadStartupData(); app.db.commit()"
gnr web serve qlab
```

The second line loads the `glbl` startup data (regions, provinces), which the
test pages use; the setup alone leaves those tables empty. The same load is
available from the startup data manager in the `sys` package.

## Tests

```bash
pytest tests
GNRHOME=/path/to/genropy node --test tests/*.test.js
```

The Python tests run on a temporary SQLite database built from the `qlab`
instance and need a source checkout of `genropy` (they reuse its test
helpers). `GNRHOME` defaults to a `genropy` checkout next to the projects
folder.
