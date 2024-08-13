import langchain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

def classifiedQuestion(question:str): 
    langchain.debug = True
    llm =ChatOpenAI()
    prompt_template  = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant"),
        ("human","Please tell me if the following question is asking for precedent or provision. If the question is closed to precedent, answer 'precedent'. If the question is closed to legal provision, answer 'provision'. If you don't know, just answer 'none'."),
        ("{question}")
    ])
    chain = prompt_template | llm | StrOutputParser()
    answer =  chain.invoke({"question":question})
    print(answer)
    
    return answer