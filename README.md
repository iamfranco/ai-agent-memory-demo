# AI Agent Memory Demo

A streamlit application to experiment with memory within AI Agent.

### Run locally

Follow the Streamlit Google Auth guide: https://docs.streamlit.io/develop/tutorials/authentication/google

So that we create a file `.streamlit/secrets.toml` with content:
```toml
[auth]
redirect_uri = "http://localhost:8502/oauth2callback"
cookie_secret = "xxx"
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
```