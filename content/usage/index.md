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
