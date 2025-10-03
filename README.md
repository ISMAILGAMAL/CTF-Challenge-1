

# CTf Small Template — Quickstart

Minimal CTF web challenge template (Flask) ready to build locally and deploy.

## Files included
- `Dockerfile` — builds a small production image with Gunicorn.
- `app.py` — minimal Flask app and the starting point to the backend.
- `requirements.txt` — dependencies.
- `.dockerignore` — keep images small.

---

## 1) Build & run locally with Docker (quick test)

```bash
# build (tag the image)
docker build -t ctf-template:latest .

# run (map host 8000 -> container 8000)
docker run --rm -p 8000:8000 ctf-template:latest
````

Open: [http://localhost:8000](http://localhost:8000) — you should see the flag.

---

## 2) Prepare GitHub repo & push (one-time per student)

```bash
# local steps (run inside repo folder)
git init
git add .
git commit -m "Initial CTF template"
# create a GitHub repo on github.com (name: cyberus-ctf-xx) then:
git remote add origin https://github.com/<username>/<repo>.git
git branch -M main
git push -u origin main
```
---

## 3) Deploy to Railway

1. Sign up / sign in to Railway: [https://railway.app](https://railway.app)
2. Create a new project → choose *Deploy from GitHub* and select your repo.
3. Railway will detect the `Dockerfile` and build the image. Default port `8000` should be detected; if not, set the service port to `8000` in Railway service settings.
4. After build, Railway gives you a public URL (e.g., `https://<project>.railway.app`).



> **Note:** For private repos, make sure to authorize Railway to access them otherwise they won't appear in the search:
>
> 1. Go to [Railway Account Integrations](https://railway.com/account) → GitHub → Install & configure repository access.
> 2. This ensures Railway can see your private repo during deployment.

---

## 4) Add your challenge to the main CTFd scoreboard

* On CTFd, create a new challenge that links to the Railway URL.

---

Happy (and hopefully error-free) CTF setting! 🙂
