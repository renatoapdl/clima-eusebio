<div align="center">

# 🌤️ CLIMA EM TEMPO REAL

**Aplicação desktop que exibe o clima da cidade de Eusébio-CE em tempo real**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![API](https://img.shields.io/badge/API-wttr.in-FF9900?style=for-the-badge)](https://wttr.in)

</div>

---

## 📋 Sobre o Projeto

O **Clima Eusébio** é uma aplicação desktop desenvolvida em Python que exibe informações meteorológicas em tempo real da cidade de Eusébio-CE. Utiliza a API pública [wttr.in](https://wttr.in) para obter dados atualizados e atualiza automaticamente a cada 5 minutos.

### 🎯 Por que este projeto?

Este projeto Demonstra habilidades com:
- 🌐 Consumo de APIs REST
- 📊 Exibição de dados em tempo real
- 🖥️ Desenvolvimento de interfaces desktop
- 🔄 Automação de atualizações periódicas

---

## ✨ Funcionalidades

| Recurso | Descrição |
|---------|-----------|
| 🌡️ Temperatura atual | Exibição com ícone do tempo |
| 💧 Umidade relativa | Percentual de umidade |
| 🌬️ Velocidade do vento | Velocidade em km/h |
| ☀️ Índice UV | Nível de radiação ultravioleta |
| 🌅 Nascer/Pôr do sol | Horários locais |
| 🔄 Atualização automática | A cada 5 minutos |
| 🟢 Indicador "Ao vivo" | Status de conexão |

---

## 📸 Demonstração

<img width="599" height="784" alt="Interface" src="https://github.com/user-attachments/assets/d8f521dd-e9c4-476c-a60e-857f4e92db8d" />

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|------------|-----|
| Python 3.x | Linguagem principal |
| Tkinter | Interface gráfica desktop |
| Urllib | Requisições HTTP |
| wttr.in API | Dados meteorológicos |

---

## 🚀 Como Usar

### Pré-requisitos

- Python 3.x instalado
- Conexão com a internet

### Instalação

```bash
# Clone o repositório
git clone https://github.com/renatoapdl/clima-eusebio.git

# Acesse a pasta
cd clima-eusebio

# Execute (não precisa instalar dependências - usa bibliotecas padrão)
python clima_eusebio.py
```

---

## 📁 Estrutura do Projeto

```
clima-eusebio/
├── clima_eusebio.py    # Script principal
├── README.md           # Este arquivo
├── LICENSE             # Licença MIT
└── .gitignore          # Arquivos ignorados
```

---

## 🔧 Personalização

### Mudar a cidade

Edite a linha no `clima_eusebio.py`:

```python
# Substitua "Eusebio,BR" pela cidade desejada
cidade = "Sao-Paulo,BR"
```

### Lista de cidades

Acesse [wttr.in](https://wttr.in) para ver cidades disponíveis no formato `Cidade,Pais`.

---

## 📡 Como Funciona

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Aplicação   │ ──▶ │  API wttr.in │ ──▶ │   Dados      │
│  (Python)    │     │  (HTTP GET)  │     │  (JSON)      │
└──────────────┘     └──────────────┘     └──────────────┘
       │                                         │
       ▼                                         ▼
┌──────────────┐                          ┌──────────────┐
│  Interface   │ ◀─── Parse JSON ──────── │  Exibição    │
│  (Tkinter)   │                          │  Atualizada  │
└──────────────┘                          └──────────────┘
```

1. A aplicação faz uma requisição HTTP para a API wttr.in
2. A API retorna os dados meteorológicos em formato JSON
3. O Python faz o parse dos dados
4. A interface Tkinter exibe as informações formatadas
5. A cada 5 minutos, o processo se repete automaticamente

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga os passos:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

**Francisco Renato Holanda de Abreu**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/renatoapdl)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/renatoabreuengenharia/)

---

<div align="center">
Feito com ❤️ e Python
</div>
