from llama_index import SimpleDirectoryReader, GPTListIndex, LLMPredictor, \
    GPTVectorStoreIndex, PromptHelper, ServiceContext, StorageContext, load_index_from_storage
from langchain import OpenAI
import gradio
from dotenv import load_dotenv
import os

os.environ['OPENAI_API_KEY'] = "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"
load_dotenv()

problem_data_dir, index_name = "problemData", "problems_index"
storage_context_directory = 'storage'


def initialize_index(directory_path, index_id="problems_index"):
    storage_context_exist = False
    try:
        storage_context = StorageContext.from_defaults(persist_dir=storage_context_directory)
        storage_context_exist = True
    except FileNotFoundError as e:
        print("Storage directory doesn't seem to exist, need to construct the index")

    if (not storage_context_exist) or (storage_context.index_store.get_index_struct(index_id) is None):
        print("Constructing index with name: " + index_id)
        max_input_size = 4096
        num_outputs = 100
        max_chunk_overlap = 0.2
        chunk_size_limit = 600

        prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
        llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="text-ada-001", max_tokens=num_outputs))

        documents = SimpleDirectoryReader(directory_path).load_data()
        service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
        index = GPTVectorStoreIndex.from_documents(documents=documents, service_context=service_context)

        index.set_index_id(index_id)
        index.storage_context.persist('./'+storage_context_directory)
    else:
        print("Index already present in storage index. No need to reconstruct it index: " + index_id)


def problem_solution_bot(query, chatHistory=[]):
    storage_context = StorageContext.from_defaults(persist_dir=storage_context_directory)
    index = load_index_from_storage(storage_context, index_id=index_name)
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    chatHistory.append((query, response.__str__()))
    return chatHistory


initialize_index(problem_data_dir, index_name)

iface = gradio.Interface(
    fn=problem_solution_bot,
    inputs=gradio.components.Textbox(lines=7, label='Enter your query'),
    outputs=gradio.components.Chatbot(label="Chat history"),
    title="ServiceNow Chatbot")

iface.launch(debug=True)
