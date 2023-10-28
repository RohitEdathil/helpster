# Helpster

Helpster one of the entries that won **Inquiry Bot Challange** by IEEE CS KS. It is an LLM-based chat bot that can answer questions related to AICSSYC 23, previous AICSSYC's, IEEE CS KS,  IEEE CS, IEEE, and other related questions.

Built using:

- [Python](https://www.python.org/)
- [LangChain](https://www.langchain.com/)
- [OpenAI](https://openai.com/)
- [ChainLit](https://github.com/Chainlit/chainlit)
- [Pinecone](https://www.pinecone.io/)

<img src="https://github.com/RohitEdathil/helpster/blob/main/img/ss1.jpg?raw=true" width="700px">
<img src="https://github.com/RohitEdathil/helpster/blob/main/img/ss2.jpg?raw=true" width="700px">

## Setup

Clone the repository

```bash
git clone https://github.com/RohitEdathil/helpster
```

Install dependencies

```bash
pip install -r requirements.txt
```

Setup environment variables

| Variable           | Description               |
| ------------------ | ------------------------- |
| `OPENAI_API_KEY`   | OpenAI API Key            |
| `PINECONE_API_KEY` | Pinecone API Key          |
| `PINECONE_ENV`     | Pinecone Environment Name |

If you want to enable LangChain tracing (Optional)

| Variable               | Description      |
| ---------------------- | ---------------- |
| `LANGCHAIN_TRACING_V2` | Enable version 2 |
| `LANGCHAIN_ENDPOINT`   | API endpoint     |
| `LANGCHAIN_API_KEY`    | API key          |
| `LANGCHAIN_PROJECT`    | Project name     |

Create an index in Pinecone with the name `helpster` and dimension `1536`

## Usage

### Load

```bash
python3 load.py
```

Running this command will load documents from `data` folder to Pinecone index. All files must be plain text files with `.txt` extension. One file is considered as one document in the index.

**Note:** The index `helpster` must be created in Pinecone before running this command.

### Run

```bash
chainlit run main.py
```

This will start the server at `http://localhost:8000` where you can ask questions similar to ChatGPT.

## Working

### RAG

This bot uses RAG(Retrieval Augmented Queries). It uses a Pinecone index to retrieve the most similar document to the question. Then it uses the retrieved document as a context to the GPT-3 model to generate the answer.

### ConversationBufferWindowMemory

The bot uses a memory buffer to store the last 3 questions and answers. You can thus ask follow up questions to the bot. It was limited to 3 because of the token consumption limitations.

### Information Constraints

The bot is explicitly instructed to not answer questions which it is not trained to answer. This prevents hallucination and makes the bot more robust. Also the bot will stay close to its purpose.

## Data Sources

Here are the data sources used to train the bot:

- Official website of AICSSYC 23
- Official instagram page of AISSYC 23
- Instagram pages of previous AICSSYC's
- Facebook page of AICSSYC 23
- Archived website of previous AICSSYC's
- IEEE CS KS website
- IEEE CS website
- Wikipedia

## Data Handling

### Training Data (Public)

The data obtained to train the data is publically available. It was obtained mostly manually and a tool called `instaloader` was used to download the instagram posts. The data was then cleaned and formatted to be used for training. Even though the data is publically available, it is still securely stored only in the development system and secure Pinecone servers.

### Chat Logs

All the **chat information is monitored** through `LangSmith`, a sister project of `LangChain`. It is a tool to diagnose and monitor LLM apps. The chat information is stored in a secure database and is only **used for debugging purposes**. Developers may look into the chat information to improve the bot. The chat information is **not shared with any third party**.

### LLM

The LLM used by the app is provided by OpenAI. Hence, data is visible to OpenAI.

Read more about OpenAI's API privacy policy [here](https://openai.com/enterprise-privacy).

From OpenAI's privacy policy we can see that data from API Platform is **not used to train** the models. Also, the data is not shared with any third party and is SOC 2 Type 2 compliant.

Read more about SOC 2 Type 2 [here](https://us.aicpa.org/interestareas/frc/assuranceadvisoryservices/aicpasoc2report).

Hence we can conclude there **won't be any data leaks** (user information presented to other users).
