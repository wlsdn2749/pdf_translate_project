from transformers import pipeline

from huggingface_hub import login

# ! Need
# login("your-huggingface-login-read-token")

class Translator:
    def __init__(self):
        # Load model
        self.model = pipeline('translation', model='NHNDQ/nllb-finetuned-en2ko', device=0, src_lang='eng_Latn', tgt_lang='kor_Hang', max_length=512)
        
    async def translate(self, text: str) -> str:
        # Run inference
        model_output = self.model(text, max_length=512)

        # Post-process output to return only the translation text
        translation = model_output[0]["translation_text"]

        return translation

    