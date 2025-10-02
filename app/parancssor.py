import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Környezeti változók betöltése (.env-ből is)
load_dotenv()

# Azure OpenAI kliens (OpenAI hivatalos SDK-jával)
client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],   # pl. https://<resource>.openai.azure.com/
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-08-01-preview")
)

DEPLOYMENT = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # pl. gpt-4o

SYSTEM_PROMPT = "Te egy segítőkész, tömören válaszoló asszisztens vagy. Válaszolj magyarul."

def main():
    print("Azure OpenAI – Parancssoros Chat")
    print("Kilépéshez Ctrl+C\n")

    history = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    while True:
        try:
            user_msg = input("Te: ")
            history.append({"role": "user", "content": user_msg})

            # Modern Responses API (ajánlott)
            resp = client.responses.create(
                model=DEPLOYMENT,
                input=history
            )

            # Kényelmes szöveg-kivonat (új SDK-kban elérhető)
            reply = getattr(resp, "output_text", None)
            if not reply:
                # kompatibilitás, ha nincs output_text mező
                # resp.output[0].content[0].text szerkezetben is lehet
                try:
                    reply = resp.output[0].content[0].text
                except Exception:
                    # fallback chat.completions-re (régebbi mintára)
                    cc = client.chat.completions.create(
                        model=DEPLOYMENT,
                        messages=history
                    )
                    reply = cc.choices[0].message.content

            print(f"Bot: {reply}\n")
            history.append({"role": "assistant", "content": reply})

        except KeyboardInterrupt:
            print("\nKilépés.")
            break

if __name__ == "__main__":
    main()
