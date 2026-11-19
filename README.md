# BuildSignals

BuildSignals is an early-stage FastAPI project for blog posts about AI,
agentic AI, software testing, and other technology topics.

## Current functionality

- `GET /` and `GET /posts` render an HTML page listing the sample blog posts.
- The post page uses a shared, responsive Jinja2 layout with navigation,
  a sidebar, and a footer. Each post is displayed as a card with its profile
  image, title, author, content, and date posted.
- The layout includes a light, dark, and automatic theme selector that saves
  the selected mode in the browser.
- Static assets, including the stylesheet, profile image, icons, and web app
  manifest, are served from `/static`.
- `GET /api/posts` returns two sample posts stored in memory.
- `GET /posts/{post_id}` renders an individual post page, linked from the post
  titles on the home page. Unknown post IDs return a 404 response.
- `GET /api/post/{post_id}` returns an individual post as JSON. Unknown post
  IDs return a 404 response.
- Error responses for browser pages use a shared HTML error template and keep
  the original HTTP status code. API errors return JSON with a `detail` field;
  API validation errors use status 422 and include validation details, while
  browser validation errors show a friendly message.
- Interactive API documentation is available at `/docs`.

The sample posts are stored in memory and are not persisted. User accounts and
blog management are not yet implemented.

## Planned functionality

- Register and log in to a user account.
- Create, edit, and delete blog posts.

## Getting started

Requirements: Python 3.12 or newer and [uv](https://docs.astral.sh/uv/).

Install dependencies from the lockfile:

```powershell
uv sync --locked
```

Start the development server from the project root:

```powershell
uv run fastapi dev main.py
```

Visit `http://127.0.0.1:8000/docs` to explore the API, or
`http://127.0.0.1:8000/api/posts` to see the sample posts.

## Project layout

- `main.py` — FastAPI application and sample posts.
- `templates/` — Jinja2 templates for the shared page layout, post listing,
  individual posts, and error pages.
- `static/` — Stylesheets, profile images, icons, and web app manifest.
- `src/buidsignals/` — Python package scaffold.
- `pyproject.toml` — project metadata and dependencies.
- `uv.lock` — locked dependency versions.

This project is under development; its API and structure may change.