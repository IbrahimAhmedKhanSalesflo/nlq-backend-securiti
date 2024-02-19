from http.client import HTTPException
from fastapi import APIRouter
import httpx
import asyncio
from openai import OpenAI

router = APIRouter()


openai_client = OpenAI(
    # This is the default and can be omitted
    api_key="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"
)



@router.get("/generate-sql")
async def generate_sql(text_input: str):
    # Assume this function calls an external API to generate SQL from the text input
    async with httpx.AsyncClient() as client:
        # await asyncio.sleep(3)  # Wait for 3 seconds, simulating a lag
        try:    
            chat_completion = openai_client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"Given the following prompt, return a synctactically correct SQL query, to retrieve the data required to answer the question from the db :{text_input} ",
                    }
                ],
                model="gpt-3.5-turbo",
            )
            # generated_text = chat_completion.choices[0].text.strip()
            generated_text = chat_completion.choices[0].message.content

            return {"generated_text": generated_text}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    # Here, you could also add calls to your database using the generated SQL, etc.
    return {"generated_sql": "Select something"}
