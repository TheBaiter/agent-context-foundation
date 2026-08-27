# Project Map Module

Read only when repository orientation is repeatedly expensive or ownership is non-obvious.

## Purpose

A project map localizes work. It is not a copied directory tree.

Capture only high-value anchors:

- behavior entrypoints,
- canonical owners,
- important boundaries,
- dependencies that affect change location,
- verification surfaces,
- areas that should not be changed for a class of task.

Prefer paths and symbols over prose.

## Create When

Create or refresh a project map when agents repeatedly scan broad parts of the repository to answer where a change belongs.

Do not create it for small or obvious repositories.

Use `references/templates/project-map.md`.

## Freshness

When anchored architecture changes materially, reverify the affected map entry. Remove stale paths instead of preserving historical layouts.
