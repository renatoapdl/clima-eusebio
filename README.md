# Clima em Tempo Real - Eusébio/CE

Aplicação desktop em Python que exibe as informações do clima da cidade de Eusébio (CE) em tempo real, utilizando a API pública [wttr.in](https://wttr.in).

## Funcionalidades

- Temperatura atual com ícone do tempo
- Descrição do clima em português
- Sensação térmica, umidade relativa, vento, pressão atmosférica
- Visibilidade e índice UV
- Nascer e pôr do sol
- Atualização automática a cada 5 minutos
- Indicador de status "Ao vivo"

## Pré-requisitos

- Conexão com a internet

### 1. Instalar Python

1. Acesse https://www.python.org/downloads/
2. Clique em **Download Python 3.x.x**
3. Na instalação, marque a opção **"Add Python to PATH"**
4. Clique em **Install Now**

### 2. Instalar Git

1. Acesse https://git-scm.com/download/win
2. Baixe o instalador (64-bit)
3. Rode o `.exe` e siga o assistente (pode deixar tudo no padrão)

### 3. Baixar o projeto

Abra o PowerShell e execute:

```bash
git clone https://github.com/renatoapdl/clima-eusebio.git
cd clima-eusebio
```

## Execução

```bash
python clima_eusebio.py
```

## Tecnologias

- Python 3
- tkinter (interface gráfica)
- urllib (requisições HTTP)
- API wttr.in (dados meteorológicos)

## Licença

MIT
