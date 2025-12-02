
# Dinastia Borges — Dashboard Mestre (Deploy package)

Este repositório contém o **Dashboard Mestre** (index.html) pronto para publicação no **GitHub Pages** e um template de backend para subir Runners em serviços como **Render**.

## Conteúdo
- `index.html` — dashboard pronto (edite `ENDPOINTS` dentro do arquivo para apontar para seus Runners no Render)
- `.gitignore` — recomendado
- `backend/` — template Flask para um Runner (ex.: EnergyRunner) com endpoints `/bills`, `/alerts`, `/forecasts`
- `README.md` — este arquivo

---

## Deploy rápido

### 1) GitHub Pages (frontend)
1. Crie um repositório no GitHub e faça push deste código (`index.html` no root).
2. Vá em **Settings → Pages** e selecione `main` branch `/ (root)` como fonte.
3. Aguarde alguns segundos; sua página estará em:
   `https://<SEU_USUARIO>.github.io/<REPO_NAME>/`

> IMPORTANTE: antes de publicar, edite `index.html` e atualize o bloco `ENDPOINTS` com as URLs dos seus Runners hospedados (ex.: `https://energy-runner.onrender.com/bills`).

### 2) Render (backend - Runner)
Dentro da pasta `backend/` tem um micro-template Flask que expõe:
- `GET /bills`
- `GET /alerts`
- `GET /forecasts`

Deploy no Render:
1. Crie um novo Web Service no Render e conecte ao seu repo.
2. Build command: `pip install -r requirements.txt`
3. Start command: `gunicorn app:app --bind 0.0.0.0:$PORT`
4. Configure CORS (o exemplo já retorna `Access-Control-Allow-Origin: *`).

Repita para cada Runner (Energy, Robotics, Finance, Security, Audit, Health).

---

## Observações de segurança
- Não exponha chaves ou credenciais no frontend.
- Proteja endpoints que fazem ações (POST) com autenticação.
- Para produção, use HTTPS e dominios customizados.

--- 

Se quiser, eu já gerencio o push automático via `gh` CLI ou gero o repositório pronto no seu GitHub. Diga `push-gh` para eu gerar o comando `gh repo create` e uma sequência pronta de git push.
