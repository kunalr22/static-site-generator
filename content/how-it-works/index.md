# How it works

This generator turns a tree of Markdown files into a matching tree of HTML files.

## Build pipeline

1. **Clean output**: remove the previous build output.
2. **Copy static assets**: copy CSS and images into the output folder.
3. **Parse Markdown**: convert blocks and inline nodes into HTML.
4. **Apply template**: inject title and content into template placeholders.
5. **Write output**: save HTML files to the matching output paths.

## Directory mapping

```
content/            -> docs/
content/index.md    -> docs/index.html
content/blog/a.md   -> docs/blog/a.html
```

## Base path support

When deploying to a subdirectory (like GitHub Pages), the generator rewrites:

- `href="/` to `href="{basepath}`
- `src="/` to `src="{basepath}`

So links and images resolve correctly from a subpath.
