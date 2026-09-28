# AEGIS — Next-Gen Security

Landing page de vendas/apresentação do antivírus AEGIS. Site estático (HTML + CSS puro, sem build).

## Estrutura

```
aegis-site/
├── index.html          # página principal
├── assets/
│   ├── css/
│   │   └── style.css   # todo o estilo do site
│   └── img/
│       └── logo.jpg    # logo AEGIS
└── README.md
```

## Como abrir no VS Code

1. Extraia esta pasta em algum lugar do seu computador.
2. No VS Code: **File → Open Folder...** e selecione a pasta `aegis-site`.

## Como lançar (visualizar no navegador)

Por ser um site 100% estático, não precisa de `npm install` nem servidor de verdade. Duas formas:

**Opção 1 — Live Server (recomendado)**
1. Instale a extensão **Live Server** (de Ritwick Dey) pelo marketplace de extensões do VS Code.
2. Clique com o botão direito em `index.html` → **Open with Live Server**.
3. O site abre automaticamente no navegador em `http://127.0.0.1:5500` e recarrega sozinho a cada alteração salva.

**Opção 2 — Abrir direto**
1. Clique com o botão direito em `index.html` → **Reveal in File Explorer** (ou equivalente) e dê duplo clique nele.
2. O navegador abre o arquivo direto do disco (`file:///...`). Funciona, mas sem live-reload.

## Editar o conteúdo

- Textos e estrutura das seções: `index.html`
- Cores, fontes e espaçamentos: `assets/css/style.css` (as cores principais estão nas variáveis `:root` no topo do arquivo)
- Trocar a logo: substitua `assets/img/logo.jpg` por outro arquivo de mesmo nome (ou ajuste o caminho no `index.html`)
