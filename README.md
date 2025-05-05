# AI Agent Memory Demo

A streamlit application to experiment with memory within AI Agent.

### Cloud Environments
- Prod: https://ai-agent-memory-demo.streamlit.app/
- Dev: https://ai-agent-memory-demo-dev.streamlit.app/

### Run locally

Follow the Streamlit Google Auth guide: https://docs.streamlit.io/develop/tutorials/authentication/google

Go to OpenAI and get API Key

So that we create a file `.streamlit/secrets.toml` with content:
```toml
OPENAI_MODEL = "openai:o3-mini"
OPENAI_API_KEY = "xxx"

[auth]
redirect_uri = "http://localhost:8502/oauth2callback"
cookie_secret = "xxx"
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
```

### Deploy feature branch onto Dev Environment

1. Go to GitHub repo's [Actions page > Deploy to Dev Branch](https://github.com/iamfranco/ai-agent-memory-demo/actions/workflows/deploy_dev.yml)
2. Open the `Run workflow` dropdown menu
3. Then select your feature branch under the `Use workflow from` dropdown menu
4. Then click the green `Run workflow` button

This will then run a new workflow to force push your feature branch's commits into the `dev` branch. 

Since https://ai-agent-memory-demo-dev.streamlit.app/ is setup to listen to changes in the `dev` branch, so those force push into the `dev` branch will get auto-deployed onto https://ai-agent-memory-demo-dev.streamlit.app/