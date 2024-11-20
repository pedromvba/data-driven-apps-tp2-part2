# FastAPI Translation and Chatbot Service

Este projeto implementa um serviço de tradução e chatbot utilizando FastAPI. Ele inclui endpoints para tradução de texto de inglês para francês e alemão, além de um chatbot simples para testes.


## Endpoints

### Chatbot Simples

- **Rota:** `/fakebot/`
- **Método:** `POST`
- **Descrição:** Retorna uma resposta simulada de um chatbot.
- **Modelo de Entrada:** [`SimpleChatInputModel`](models/simpleChatModel.py)
- **Modelo de Saída:** [`SimpleChatOutputModel`](models/simpleChatModel.py)

### Tradutor Inglês para Alemão

- **Rota:** `/en-de-translator/`
- **Método:** `POST`
- **Descrição:** Traduz texto de inglês para alemão utilizando o modelo `Helsinki-NLP/opus-mt-en-de`.
- **Modelo de Entrada:** [`EnDeTranlationInputModel`](models/enDeTranslatorModel.py)
- **Modelo de Saída:** [`EnDeTranlationOutputModel`](models/enDeTranslatorModel.py)

### Tradutor Inglês para Francês

- **Rota:** `/en-fr-translator/`
- **Método:** `POST`
- **Descrição:** Traduz texto de inglês para francês utilizando o modelo `gemini-1.5-pro`.
- **Modelo de Entrada:** [`EnFrTranlationInputModel`](models/enFrTranslatorModel.py)
- **Modelo de Saída:** [`EnFrTranlationOutputModel`](models/enFrTranslatorModel.py)

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/pedromvba/data-driven-apps-tp2-part2.git
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # No Windows, use .venv\Scripts\activate
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure as variáveis de ambiente no arquivo `.env`:
    ```env
    GEMINI_API_KEY=<SUA_CHAVE_API_GEMINI>
    HUGGING_FACE_API_KEY=<SUA_CHAVE_API_HUGGING_FACE>
    ```

## Execução

Para iniciar o servidor FastAPI, execute:
```sh
uvicorn main:app --reload