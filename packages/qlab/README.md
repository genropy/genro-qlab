# qlab

`qlab` is the laboratory package for new GenroPy components.

A component starts here while it is still being tested, instead of landing
directly in the framework. The lab keeps each experiment self-contained and
usable on a real instance, so its API and behaviour can be tried, changed or
dropped without touching `genropy`.

## Intents

- **Incubate new components.** Every component in the lab lives under
  `resources/<component>/` and is loaded like any package resource, e.g.
  `py_requires = 'recordpicker/recordpicker:RecordPicker'`.
- **Test them on real data.** Each component has a `testhandler` page under
  `webpages/components/`, served by the `qlab` instance, which carries the
  packages the examples need (`sys`, `adm`, `glbl`).
- **Keep their tests next to them.** Python tests run against the `qlab`
  instance on a temporary database, JavaScript tests with `node --test`; both
  live in the repository's `tests/` folder.
- **Leave the lab deliberately.** A component that proves itself is proposed
  to the framework as its own change, or its best ideas are folded into an
  existing framework component. Until then, nothing in `genropy` depends on
  `qlab`.

## Components

| Component | Resource | Test page |
|---|---|---|
| Record picker | `recordpicker/recordpicker:RecordPicker` | `/qlab/components/recordpicker` |

The record picker's API is documented in `docs/recordpicker.rst`.
