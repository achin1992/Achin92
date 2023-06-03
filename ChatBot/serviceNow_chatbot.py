from llama_index import SimpleDirectoryReader, GPTListIndex, LLMPredictor, \
    GPTVectorStoreIndex, PromptHelper, ServiceContext, StorageContext, load_index_from_storage
from langchain import OpenAI
import gradio
from dotenv import load_dotenv
import os

os.environ['OPENAI_API_KEY'] = "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"
load_dotenv()

def initialize_index(directory_path):
    max_input_size = 4096
    num_outputs = 100
    max_chunk_overlap = 0.2
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="text-ada-001", max_tokens=num_outputs))

    documents = SimpleDirectoryReader(directory_path).load_data()
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    index = GPTVectorStoreIndex.from_documents(documents=documents, service_context=service_context)

    index.set_index_id("problems_index")
    index.storage_context.persist('./storage')

def problem_solution_bot(query):
    storage_context = StorageContext.from_defaults(persist_dir='storage')
    index = load_index_from_storage(storage_context, index_id="problems_index")
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return response

initialize_index('problemData')

iface = gradio.Interface(fn=problem_solution_bot,
    inputs=gradio.inputs.Textbox(lines=7, label='Enter your query'),
    outputs="text", title="ServiceNow Chatbot")

iface.launch(debug=True)