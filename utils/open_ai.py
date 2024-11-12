from openai import OpenAI
import json


def CallOpenAI(model, input_text, max_tokens=256, temperature=0,n=1):
    # api_key= os.getenv("OPENAI_API_KEY")
    api_key = "sk-eSvitYqDHwPUKyyE30B699641eD243258e76E70aE490D1E4"
    api_base = "https://api.gptai.cc/v1"
    client = OpenAI(api_key=api_key, base_url=api_base)

    res = client.chat.completions.create(
        # model="gpt-3.5-turbo",
        model=model,
        messages=[
            # 设置行为
            {"role": "system", "content": "You are a helpful assistant."},
            # 有user和assistant两类交替进行，填入question
            {"role": "user", "content": input_text}
        ],
        max_tokens=max_tokens,
        temperature=temperature,
        n=1,
    )
    return res.choices[0].message.content
