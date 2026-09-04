# Gráfico MP10 — Plotly + GitHub Pages

Este pacote contém uma página HTML autocontida, gerada com **Python + Plotly**, para publicação no GitHub Pages.

## Arquivos

- `index.html` — página pronta para o GitHub Pages.
- `gerar_grafico.py` — script Python utilizado para gerar o gráfico.
- `.github/workflows/pages.yml` — workflow para publicação automática no GitHub Pages.
- `.nojekyll` — arquivo auxiliar para publicação.
- `README.md` — instruções.

## Observação sobre os dados

Os valores foram **digitalizados visualmente a partir da imagem fornecida**. Portanto, podem existir pequenas diferenças em relação aos valores numéricos originais usados no gráfico fonte.

A série representa:
- Média Móvel (3 anos)
- Percentis 10/90
- MP10 em µg/m³
- Períodos de 2000–2002 a 2023–2025

Se os valores originais estiverem disponíveis em uma tabela/CSV, recomenda-se substituí-los no `gerar_grafico.py` para obter reprodução numérica exata.

---

# Publicação no GitHub Pages

## Opção recomendada — GitHub Actions

1. Crie um repositório no GitHub.
2. Extraia este ZIP.
3. Abra um terminal dentro da pasta extraída.
4. Inicialize o Git:

```bash
git init
git add .
git commit -m "Adicionar gráfico MP10 em Plotly"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
git push -u origin main
```

Substitua:

`SEU_USUARIO/SEU_REPOSITORIO`

pelo endereço do seu repositório.

### Configurar o GitHub Pages

No GitHub:

**Settings → Pages → Build and deployment → Source → GitHub Actions**

Depois do `git push`, o workflow:

`.github/workflows/pages.yml`

publicará automaticamente o `index.html`.

A página ficará disponível em:

`https://SEU_USUARIO.github.io/SEU_REPOSITORIO/`

---

# Publicação usando GitHub CLI

Se você utiliza o GitHub CLI:

```bash
gh repo create SEU_REPOSITORIO --public --source=. --remote=origin
git add .
git commit -m "Publicar gráfico MP10"
git push -u origin main
```

Depois, habilite o GitHub Pages usando **Settings → Pages → GitHub Actions**.

---

# Atualizar o gráfico

Se alterar os dados no `gerar_grafico.py`:

```bash
python gerar_grafico.py
```

Depois:

```bash
git add index.html gerar_grafico.py
git commit -m "Atualizar dados do gráfico MP10"
git push
```

O GitHub Actions fará a nova publicação automaticamente.

## Dependência Python

Para regenerar o HTML localmente:

```bash
pip install plotly
```

O `index.html` gerado neste pacote já contém o Plotly incorporado, portanto a página publicada não depende de um CDN externo.
