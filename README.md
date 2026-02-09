# Static Site Generator

A small static site generator that turns a tree of Markdown files into a matching tree of HTML files using a shared HTML template.

## Demo

Live site: https://kunalr22.github.io/static-site-generator/

## Features

- Markdown to HTML conversion
- Shared HTML template injection (title + content)
- Recursive content directory traversal
- Static asset copying (CSS, images)
- Base path support for subdirectory deployments (e.g., GitHub Pages)

## How it works

The generator:

1. Cleans the output directory.
2. Copies the static assets into the output directory.
3. Converts Markdown blocks and inline nodes to HTML.
4. Injects the title and content into the HTML template.
5. Writes the result to the output path, preserving the directory structure.

## Usage

Run the build script from the project root:

```
./build.sh
```

The generated site is written to the `docs/` directory.

## Content authoring

Use a directory-per-page structure under `content/`:

```
content/
  index.md
  usage/
    index.md
  how-it-works/
    index.md
  usage/
    example/
      index.md
```

Each `dirname/index.md` becomes `dirname/index.html` in the output.

## Supported Markdown

### Blocks

- Paragraphs
- Headings (`#` through `######`)
- Code blocks (triple backticks, no blank lines)
- Blockquotes (`>`)
- Unordered lists (`-` or `*`)
- Ordered lists (`1.`, `2.`, ...)

### Inline

- Bold (double asterisks)
- Italic (underscores)
- Inline code (backticks)
- Links (brackets + parentheses)
- Images (exclamation mark + brackets + parentheses)

Nested inline styles are not supported.
