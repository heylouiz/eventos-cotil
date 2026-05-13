# Eventos COTIL

Spider Scrapy para coletar eventos publicados no site do [Colégio Técnico de Limeira (COTIL)](https://www.cotil.unicamp.br/eventos).

## Dados coletados

Para cada evento são extraídos:

| Campo | Descrição |
|---|---|
| `title` | Nome do evento |
| `url` | Link da página do evento |
| `date_start` | Data de início |
| `date_end` | Data de término |
| `time_start` | Horário de início |
| `time_end` | Horário de término |
| `categories` | Categorias do evento |
| `page` | Página da listagem de onde o evento foi extraído |

## Requisitos

- Python 3.8+

## Instalação

**1. Clone o repositório:**

```bash
git clone git@github.com:heylouiz/eventos-cotil.git
cd eventos-cotil
```

**2. Crie e ative um ambiente virtual:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

## Uso

**Coletar todos os eventos:**

```bash
scrapy crawl cotil
```

**Limitar o número de páginas percorridas:**

```bash
scrapy crawl cotil -a max_pages=2
```

O resultado é salvo automaticamente em `eventos.json` no diretório atual.
