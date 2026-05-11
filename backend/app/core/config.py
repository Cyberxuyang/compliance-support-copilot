from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "development"
    llm_provider: str = "ollama"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "gemma4:e2b"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")



settings = Settings()
