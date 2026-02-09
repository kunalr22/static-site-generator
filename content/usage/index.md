# Usage

Run the build from the project root using the helper script.

## Build

```
./build.sh
```

## Output

The generated site is written to the `docs/` directory so GitHub Pages can serve it by default.

## Content authoring

Create pages under `content/` using a directory-per-page layout:

```
content/
	index.md
	usage/
		index.md
	how-it-works/
		index.md
	blog/
		first-post/
			index.md
```

You can nest as deeply as you want. Each `dirname/index.md` becomes `dirname/index.html` in the output.

- Use headings (`#`, `##`) for structure.
- Use absolute root links like `/usage/` and `/images/logo.png`.
- Each file needs at least one main heading (`# `) so the title can be extracted.

## Supported blocks

The Markdown parser supports these block types:

- Paragraphs
- Headings (`#` through `######`)
- Code blocks (triple backticks)
- Blockquotes (`>`)
- Unordered lists (`-` or `*`)
- Ordered lists (`1.`, `2.`, ...)

Note: Code blocks can’t contain blank lines. The parser splits blocks on double newlines, which breaks fenced code blocks.

## Supported inline text

Inline text types include:

- Bold (use **double asterisks**)
- Italic (use _underscores_)
- Code (use backticks around code)
- Links (use square brackets + parentheses)
- Images (use an exclamation mark + brackets + parentheses)

Nested inline styles aren’t supported (for example, bold inside italics).

## Example

Note: This example avoids blank lines inside the code block.

```
# Hello Site
![Static Site Generator logo](/images/logo.png)
Here is **bold**, _italic_, and `code`.
> A small quote.
- Item one
- Item two
[Back home](/)
```

[Here’s this example visualized](/usage/example/)
