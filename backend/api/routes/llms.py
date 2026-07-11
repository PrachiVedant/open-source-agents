from fastapi import APIRouter

router=APIRouter()

@router.get("/")
def get_llms():
    return [
         {
            "provider": "openai",
            "models": [
                "gpt-4o-mini"
            ]
        },
        {
            "provider": "groq",
            "models": [
                "llama-3.3-70b-versatile"
            ]
        },
        {
            "provider": "ollama",
            "models": [
                "llama3.1"
            ]
        }
    ]